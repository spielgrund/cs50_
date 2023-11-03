from fpdf import FPDF
import os

pdf = FPDF(orientation="P",unit="mm")
x = 210
y = 297
py = 297/10*2
pw = 210/10*9

pdf.add_page(orientation="portrait", format=[x,y]) #format="A4"
pdf.set_font('helvetica', size=48)
pdf.cell(w=0,text="CS50 Shirtificate", align="C")
pdf.set_text_color(255,255,255)


pdf.image((os.path.join(os.path.dirname(__file__), "shirtificate.png")),x="c",y=py, w=pw)
name = input("Name: ")
name = name + " took CS50"
pdf.set_y(150)
pdf.cell(w=0, text=name, align="C")
#pdf.text(x=50,y=150, text=name)

pdf.output(os.path.join(os.path.dirname(__file__),"hello_world.pdf"))


#Image(string file [, float x [, float y [, float w [, float h [, string type [, mixed link]]]]]])

#image_1 = Image.open(r'C:\Users\Ron\Desktop\Test\view_1.png')