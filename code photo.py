from PIL import Image
from PIL import ImageDraw

img= Image.open('C://Users//admin//Pictures//photo2.png')
I1=ImageDraw.Draw(img)
V1=float(input("entrez la valeur de vitesse 1 :"))
V2=float(input("entrez la valeur de vitesse 2 :"))
D1= float(input("entrez la valeur de dimétre :"))
mv= float(input("entrez la valeur de la masse volumique"))
import math
angle =math.tan(10*3.14/180)
print(angle)
try :
    L=D1/(2*angle)*(1-(V1/V2)**(1/2))
    print("la valeur de la longeur est :",L,"mm")
except :
    print("la valeur de V1 et/ou de V2 et/ou D1 que vous avez donnée est inorrect")
