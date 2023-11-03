from PIL import Image
from PIL import ImageOps
import sys
import os

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

filename1, file_extension1 = os.path.splitext(sys.argv[1])
filename1 = str(sys.argv[1]).lower()
file_extension1 = str(file_extension1).lower()

filename2, file_extension2 = os.path.splitext(sys.argv[2])
filename2 = str(sys.argv[2])
file_extension2 = str(file_extension2).lower()
#print(file_extension1)

if os.path.isfile(sys.argv[1]):         #check if arg1 is valid file
    pass
else:
    sys.exit("Input does not exist.")

if file_extension1 == ".jpg" or file_extension1 == ".jpeg" or file_extension1 == ".png":        #check if extension1 is correct
    try:
        image1 = Image.open(filename1)
    except FileNotFoundError:
        sys.exit("Invalid file.")

if file_extension2 == ".jpg" or file_extension2 == ".jpeg" or file_extension2 == ".png":        #check if extension1 is correct
    pass
else:
    sys.exit("Invalid output.")

if file_extension1 != file_extension2:
    sys.exit("Input and output have different extensions.")

shirt = Image.open("shirt.png")

image1 = ImageOps.fit(image1, shirt.size, method=0, bleed=0.0, centering=(0.5, 0.5))
#image2 = image2.resize((int(image1.size[0]),int(image1.size[0]*ar)), Image.Resampling.LANCZOS)

image1.paste(shirt, (0,0), mask = shirt) 
  
# Displaying the image 
image1.save(filename2)