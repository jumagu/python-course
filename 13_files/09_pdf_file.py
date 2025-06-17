# Third party library for creating pdf files
from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial", size=14)
# Width, Height, Text, Line break, Text alignment C = Center
pdf.cell(200, 10, txt="Hello world in PDF!!", ln=True, align="C")
pdf.cell(
    200,
    10,
    txt="Culpa et ea culpa amet ea proident quis commodo deserunt mollit dolore.",
    ln=True,
    align="C",
)

pdf.output("test_files/my_pdf_test.pdf")
