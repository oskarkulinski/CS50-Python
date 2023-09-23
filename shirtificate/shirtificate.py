from fpdf import FPDF

def main():
    name = input("Name: ")
    make_shirt(name)


def make_shirt(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", "B", 30)
    #pdf.cell(75)
    pdf.cell(200, 20, "CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png", 10, 40, 190)
    pdf.ln(100)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Times", "I", 30)
    pdf.cell(200, 20, f"{name.lower().title()} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()