from fpdf import FPDF
import pandas as pd

# orientation= pirtrate, ...
pdf = FPDF(orientation="P", unit="mm", format="A4")
#to have correct footer, stop auto breaking of page
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

# pages
for index, row in df.iterrows():
    ## master page
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=14)
    # pdf.set_text_color(100,100,100)
    pdf.set_text_color(0, 0, 254)
    pdf.cell(w=0, h=12, txt=row["Topic"],align="L", ln=1)
    # pdf.line(x1 y1, x2 y2) # size of line from lest x and y in mm
    pdf.line(10, 21, 200, 21)

    #footer lines and text for master page
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(0,0,254)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


    # other pages for this topic!
    for i in range(row["Pages"] -1):
        pdf.add_page()
        # footer lines and text for other pages
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(0, 0, 254)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


pdf.output("big-pdffile.pdf")
