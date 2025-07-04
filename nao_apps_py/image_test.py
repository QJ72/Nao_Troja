from nao_classes.ImageCollector import ImageCollector
from PIL import Image

def main():

    image_collector = ImageCollector(None,None, None, "")
    image = Image.open("nao_screenshot.jpg")
    Image._show(image)
    Image._show(image_collector.mirror_image(image))


if __name__ == '__main__':
    main()