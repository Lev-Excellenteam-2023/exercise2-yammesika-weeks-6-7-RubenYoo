from PIL import Image
PATH = 'code.png'

s = ''
with Image.open(PATH) as img:
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if img.getpixel((i, j)) == 1:
                s += chr(j)
                
print(s)







