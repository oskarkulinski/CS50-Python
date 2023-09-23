from fpdf import FPDF

def main():
    name = input("Name: ")
    make_shirt()


def make_shirt():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("ZapfDingbats", "", 16)
    pdf.cell(60, 10, 'CS50 Shirtificate!', 1)


if __name__ == "__main__":
    main()