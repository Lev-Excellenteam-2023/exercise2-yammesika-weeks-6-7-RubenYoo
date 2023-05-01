from PIL import Image
PATH = 'code.png'


def decode_image(path):
    with Image.open(path) as img:
        width, height = img.size
        return ''.join(chr(column) for row in range(width) for column in range(height)
                       if img.getpixel((row, column)) == 1)


def main():
    print(decode_image(PATH))


if __name__ == "__main__":
    main()







