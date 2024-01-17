from fpdf import FPDF

#orientation= pirtrate, ...
pdf = FPDF(orientation="P", unit="mm", format="A4" )

#page1
pdf.add_page()
#pdf.set_font(family="Times", style="B", size=14)
pdf.set_font(family="Times", size=14)
#pdf.cell(w=0, h=20, txt="Hello there!", align="L",ln=1, border=1)
pdf.cell(w=0, h=12, txt="Hi there!", align="L", ln=1)

#page2
pdf.add_page()
pdf.set_font(family="Times", style="B", size=14)
#pdf.cell(w=0, h=20, txt="Hello there!", align="L",ln=1, border=1)
pdf.cell(w=0, h=12, txt="Hi there!", align="L", ln=1)
pdf.output("mypdffile.pdf")
