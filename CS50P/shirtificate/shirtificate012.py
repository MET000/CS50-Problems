from fpdf import FPDF, enums

def main():

    pdf = FPDF(orientation="Portrait", format="A4")
    pdf.set_auto_page_break(0)
    pdf.add_page()
    pdf.ln(15)
    pdf.set_font("helvetica", style='b', size=35)
    pdf.cell(text="CS50 Shirtificate", center=True)
    pdf.ln(50)

    pdf.image("/workspaces/184296233/shirtificate/shirtificate.png", x=enums.Align.C, w=190)

    pdf.ln(-120)
    pdf.set_font("helvetica", size=20)
    pdf.set_text_color(255)
    pdf.cell(text=f"{input("Name: ")} took CS50", center=True)


    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
