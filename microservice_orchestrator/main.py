from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import requests

from config import settings

app = FastAPI(title="Orchestrator Service")

@app.post("/process-pdf")
async def process_pdf(file: UploadFile = File(...)):
    """
    1) Send the uploaded PDF to the PDF microservice -> get chunks
    2) Send chunks to Question microservice -> get questions
    3) Return questions to the user
    """
    try:
        # Step 1: Upload PDF to PDF microservice
        pdf_bytes = await file.read()
        # We'll do a multipart/form-data request
        files = {"file": (file.filename, pdf_bytes, file.content_type)}

        pdf_response = requests.post(settings.pdf_service_url, files=files)
        if pdf_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error from PDF service: " + pdf_response.text)

        pdf_data = pdf_response.json()
        if "chunks" not in pdf_data:
            raise HTTPException(status_code=500, detail="No chunks returned from PDF service")

        chunks = pdf_data["chunks"]

        # Step 2: Send chunks to Question microservice
        question_payload = {"chunks": chunks}
        question_response = requests.post(settings.question_service_url, json=question_payload)
        if question_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error from Question service: " + question_response.text)

        questions_data = question_response.json()

        # Step 3: Return combined result
        return JSONResponse(content={
            "questions": questions_data.get("questions"),
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
