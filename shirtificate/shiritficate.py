from fpdf import FPDF

def main():
    name = input("Name: ")
    make_shirt()


def make_shirt():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font()


if __name__ == "__main__":
    main()