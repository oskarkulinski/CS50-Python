from fpdf import FPDF

def main():
    name = input("Name: ")
    make_shirt(name)


def make_shirt(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("ZapfDingbats", "", 16)
    pdf.cell(60, 10, "CS50 Shirtificate!", align="C")
    pdf.image("shirtificate.png", 40, 50, 33)
    pdf.cell(60, 10, f"{name.capitalize()} took CS50", align="C")

if __name__ == "__main__":
    main()