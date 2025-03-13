from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

from config import settings
from pdf_parser import PdfParser
from text_chunker import TextChunker

app = FastAPI(title="PDF to Text Service")

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Receives a PDF file, extracts text, chunks it, returns chunked data in JSON.
    """
    try:
        pdf_bytes = await file.read()

        # Parse PDF
        parser = PdfParser()
        full_text = parser.parse(pdf_bytes)

        # Create chunker from config values
        text_chunker = TextChunker(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap
        )

        # Split into chunks
        chunks = text_chunker.chunk_text(full_text)

        return JSONResponse(content={"chunks": chunks})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
