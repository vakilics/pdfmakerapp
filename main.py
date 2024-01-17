from fpdf import FPDF
import pandas as pd

# orientation= pirtrate, ...
pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read_csv("topics.csv")

# pages
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=14)
    # pdf.set_text_color(100,100,100)
    pdf.set_text_color(0, 0, 254)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # pdf.line(x1 y1, x2 y2) # size of line from lest x and y in mm
    pdf.line(10, 21, 200, 21)

    for i in range(row["Pages"]):
        pdf.add_page()

pdf.output("big-pdffile.pdf")
