# shirtificate.py

"""
Suppose that you’d like to implement a CS50 "shirtificate",
a PDF with an image of an I took CS50 t-shirt, shirtificate.png,
customized with a user’s own name.

Implement a program that prompts the user for their name and outputs,
using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf,
with these specifications:

- The orientation of the PDF should be Portrait.
- The format of the PDF should be A4, which is 210mm wide by 297mm tall.
- The top of the PDF should say “CS50 Shirtificate” as text,
  centered horizontally.
- The shirt's image should be centered horizontally.
- The user's name should be on top of the shirt, in white text.
"""


from PIL import Image
from fpdf import FPDF


def main():
    # set workspace path and open image
    img_path = "/home/alex-anast/workspace/cs50p_2023/8_oop/shirtificate/"
    image = Image.open(img_path + "shirtificate.png")
    image_width, image_height = image.size

    # Set the dimensions of the image on the PDF page
    image_width /= 3  # Adjust as needed
    image_height /= 3  # Adjust as needed

    # create pdf from scratch
    pdf = FPDF(
        orientation="portrait",
        unit="mm",
        format="A4",
    )
    pdf.add_page()
    pdf.set_font("Arial", "B", 64)

    # override header method
    def header(self):
        page_width = self.w
        header_text = "CS50 Shirtificate"
        text_width = self.get_string_width(header_text)
        text_height = 10  # Set the height of the header text
        x_coord = (page_width - text_width) / 2
        self.set_xy(x_coord, 20)
        self.cell(0, text_height, header_text, 0, 0, "C")

    FPDF.header = header
    pdf.header()

    # set the image in the center
    x_centered = (pdf.w - image_width) / 2
    pdf.image(
        img_path + "shirtificate.png",
        x=x_centered,
        y=80,  # custom to fit the page
        w=image_width,
        h=image_height,
    )

    name = input("Name: ")

    # write text on top of the image
    text_box_x = 50  # X-coordinate of the text box
    text_box_y = 135  # Y-coordinate of the text box
    text_box_width = 110  # Width of the text box
    pdf.set_xy(text_box_x, text_box_y)
    pdf.set_font("Arial", size=24)
    pdf.set_text_color(255, 255, 255)  # Set text color
    # MultiCell method allows the text to wrap within the specified width
    pdf.multi_cell(
        text_box_width,
        10,
        name + " took CS50",
    )

    # export pdf
    pdf.output(img_path + "shirtificate.pdf")


if __name__ == "__main__":
    main()
