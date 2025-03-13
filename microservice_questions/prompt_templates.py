GENERAL_QUESTIONS_PROMPT = """
You are a helpful assistant. The user has provided some text chunks from a PDF.

Context:
{context}

Please generate a list of broad, general questions that someone might have about this content.
Return the questions in a JSON array format, like:
[
  "Question 1",
  "Question 2",
  ...
]
Please only return valid JSON, no extra commentary.
"""
