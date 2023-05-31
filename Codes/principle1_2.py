# Ask for structured output
from aihelper import get_completion

prompt = """
Generate a list of three made-up book titles along \
with their authors and genres. 
Provide them in JSON format with the following keys: 
book_id, title, author, genre.
"""
response = get_completion(prompt)
print(response)
