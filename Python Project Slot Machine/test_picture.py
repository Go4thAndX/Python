from PIL import Image, ImageOps

# # Open the .jpg file
# img = Image.open("pinup_A.jpg")

# # Show the image in the web page
# img.show()

image1 = Image.open("pinup_A.jpg")
image2 = Image.open("pinup_B.jpg")

# assuming both images have the same size
width, height = image1.size

# horizontal concatenation
# result_image = Image.new(image1.mode, (2*width, height))
# result_image.paste(image1, (0, 0))
# result_image.paste(image2, (width, 0))

# vertical concatenation
result_image = Image.new(image1.mode, (width, 2*height))
result_image.paste(image1, (0, 0))
result_image.paste(image2, (0, height))

result_image.show()
