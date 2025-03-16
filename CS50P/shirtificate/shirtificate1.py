from fpdf import FPDF


pdf = FPDF(orientation="Portrait", format="A4")

pdf.add_page()
pdf.set_auto_page_break(0)

pdf.set_font("helvetica", size=35)
pdf.cell(80)
pdf.cell(30, 10, "CS50 Shirtificate", border=0, align="C")
pdf.ln(20)
pdf.image("/workspaces/184296233/shirtificate.png", 15, 50, 180, 0)
pdf.set_font("helvetica", size=20)
pdf.set_text_color(255)
pdf.cell(80)
name = f"{input("Name: ")} took CS50"
pdf.cell(30, 170, name, align="C")


pdf.output("shirtificate.pdf")
