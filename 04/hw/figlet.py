from pyfiglet import Figlet
import sys

figlet = Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
    figlet.setFont(font=sys.argv[2])
    t = input("Txt: ")
    print(figlet.renderText(t))
else:
    print("Invalid usage")
    sys.exit()

