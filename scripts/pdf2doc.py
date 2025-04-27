##pip install pdf2docx
# Try installing this using pip install pdf2docx --user if you have any issues

from pdf2docx import Convertor
pdf_file ='ListsOfInbuiltMethods.pdf'
docx_file = 'ListsOfInbuiltMethods.docx'
cv = Convertor(pdf_file)
cv.convertor(docx_file)
cv.close