from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_image = img.convert('L')
box = (100, 100, 400, 400)
region = filtered_image.crop(box)

region.save('grey.png', 'png')

img = Image.open('./astro.jpg')
img.thumbnail((400, 400))
img.save('thumbnail.jpg')