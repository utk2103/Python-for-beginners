##pip install pdf2docx
# Try installing this using pip install pdf2docx --user if you have any issues

# Why: Convert PDF to DOCX for easier editing
from pdf2docx import Convertor  # Why: Handles PDF to Word conversion
pdf_file ='ListsOfInbuiltMethods.pdf'
docx_file = 'ListsOfInbuiltMethods.docx'
cv = Convertor(pdf_file)
cv.convertor(docx_file)  # Why: Actually does the conversion
cv.close  # Why: Clean up resources