from fpdf import FPDF


class PDF(FPDF):

    def shirtificate(self, name):

        self.set_auto_page_break(0)
        self.add_page()
        self.ln(15)
        self.set_font("helvetica", style='b', size=35)
        self.cell(txt="CS50 Shirtificate", align='C', w=0)
        self.ln(50)
        self.image("shirtificate.png", w=190)
        self.ln(-120)
        self.set_font("helvetica", size=20)
        self.set_text_color(255)
        self.cell(txt=f"{name} took CS50", align='C', w=0)
        self.output("shirtificate.pdf")


pdf = PDF()
pdf.shirtificate(input("Name: "))
