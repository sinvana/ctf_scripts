from PIL import Image,ImageFilter

f = open(r"E:\1\1.txt","r")
print(len(f.read()))
'''
im = Image.open(r"e:\1\2.jpg")
im2 = im.filter(ImageFilter.BLUR)
#im2.save("blur.jpg",'jpeg')
im.show()
'''
def foo():
    im1 = Image.open(r"e:\1\2.jpg")
    im = im1.copy()
    wen = open(r"e:\1\1.txt").read()
    pix=im.load()
    height=256
    width=256
    for x in range(0,width):
        for y in range(0,height):
            if wen[x+y*256]=="0":
                pix[x,y]=255
            else:
                pix[x,y]=0

    im.show()

    pass

foo()
print("done")
