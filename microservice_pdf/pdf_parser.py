import io
import PyPDF2

class PdfParser:
    """Handles PDF file reading and text extraction using PyPDF2."""

    @staticmethod
    def parse(pdf_bytes: bytes) -> str:
        """Extracts text from a PDF file in memory and returns the full text."""
        pdf_filelike = io.BytesIO(pdf_bytes)
        pdf_reader = PyPDF2.PdfReader(pdf_filelike)

        full_text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if text:
                full_text += text + "\n"
        return full_text