from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextChunker:
    """Handles text splitting/chunking logic."""

    def __init__(self, chunk_size: int, chunk_overlap: int):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self._text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

    
