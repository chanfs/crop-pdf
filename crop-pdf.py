#!//usr/bin/python3

from PyPDF2.generic import RectangleObject
from PyPDF2 import PdfReader, PdfWriter, Transformation
from PyPDF2.generic import RectangleObject
from decimal import Decimal
import sys

# usage: crop-pdf.py pdffile

# Read the input
reader = PdfReader(sys.argv[1])
numberOfPages = len(reader.pages)
print("Number of pages: ", numberOfPages)

writer = PdfWriter()

# for i in range(3):
#    print(i)
# 0
# 1
# 2
#page = reader.pages[0]
# scale
for x in range(len(reader.pages)):
    #print(x)
    page = reader.pages[x]
    MyRectangleObject = page.mediabox
    print("\nmedia left: ", MyRectangleObject.left)
    print("media bottom: ", MyRectangleObject.bottom)
    print("media right: ", MyRectangleObject.right)
    print("media top: ", MyRectangleObject.top)
    
    MyRectangleObject = page.cropbox
    print("\ncropbox left: ", MyRectangleObject.left)
    print("cropbox bottom: ", MyRectangleObject.bottom)
    print("cropbox right: ", MyRectangleObject.right)
    print("cropbox top: ", MyRectangleObject.top)
    cropLeft = MyRectangleObject.left
    cropBottom = MyRectangleObject.bottom
    cropRight = MyRectangleObject.right
    cropTop = MyRectangleObject.top
    cropLeftRight = MyRectangleObject.right - MyRectangleObject.left
    cropTopBottom = MyRectangleObject.top - MyRectangleObject.bottom
    
    MyRectangleObject = page.trimbox
    print("\ntrimbox left: ", MyRectangleObject.left)
    print("trimbox bottom: ", MyRectangleObject.bottom)
    print("trimbox right: ", MyRectangleObject.right)
    print("trimbox top: ", MyRectangleObject.top)
    
    MyRectangleObject = page.bleedbox
    print("\nbleedbox left: ", MyRectangleObject.left)
    print("bleedbox bottom: ", MyRectangleObject.bottom)
    print("bleedbox right: ", MyRectangleObject.right)
    print("bleedbox top: ", MyRectangleObject.top)
    
    MyRectangleObject = page.artbox
    print("\nartbox left: ", MyRectangleObject.left)
    print("artbox bottom: ", MyRectangleObject.bottom)
    print("artbox right: ", MyRectangleObject.right)
    print("artbox top: ", MyRectangleObject.top)
    
    
    mb = page.mediabox
    percentage = int(sys.argv[2])/100
    percentage = Decimal(percentage)# else you will get TypeError: unsupported operand type(s) for *: 'float' and 'decimal.Decimal'
    deltaLeftRight = percentage*cropLeftRight
    deltaTopBottom = percentage*cropTopBottom 
    print("DeltaLeftRight = ", deltaLeftRight)
    print("DeltaTopBottom = ", deltaTopBottom)

    NewCropLeft = cropLeft + (deltaLeftRight/2)
    NewCropBottom = cropBottom+deltaTopBottom/2
    NewCropRight = cropRight-deltaLeftRight/2
    NewCropTop = cropTop-deltaTopBottom/2
    
    print("New cropLeft: ", NewCropLeft)
    print("New cropBottom: ", NewCropBottom)
    print("New cropRight: ", NewCropRight)
    print("New cropTop: ", NewCropTop)
        
    page.cropbox = RectangleObject((NewCropLeft,NewCropBottom,NewCropRight,NewCropTop))
    #page.cropbox = RectangleObject((cropLeft-reducedLeftRight/2,cropBottom-reducedTopBottom/2,cropRight-reducedLeftRight/2,cropTop-reducedTopBottom/2))
    #page.trimbox = RectangleObject((50,50,500,700))
    
    #sx with value > 1 will shift content to right
    #op = Transformation().scale(sx=1.1, sy=1.1)
    #page.add_transformation(op)
    #page.scale_by(0.7)
    
    writer.add_page(page)

writer.write("out-pg-transform.pdf")





