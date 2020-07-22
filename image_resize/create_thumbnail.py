from PIL import Image

# The input image must be .png or .jpeg(jpg) however, the output image can be .gif, .tif or other
image_name = "image2.png"
path = "./original_images/"
image_path = path + image_name
output_path = "./resized_images/"
thumbnail_size = (48, 48)

# Resize according the aspect relation between height and width
"""
new_width  = 680
new_height = new_width * height / width

new_height = 680
new_width  = new_height * width / height
"""
base_width = 300
img = Image.open(image_path)
width_percent = (base_width / float(img.size[0]))
height_size = int((float(img.size[1]) * float(width_percent)))
img = img.resize((base_width, height_size), Image.ANTIALIAS)
img.save(output_path + 'resized_' + image_name)

# Use the thumbnail method
img = Image.open(image_path)
img.thumbnail(thumbnail_size, Image.ANTIALIAS)
img.save(output_path + "thumbnail_" + image_name)

"""
half = 0.5
out = im.resize( [int(half * s) for s in im.size] )

img = ImageOps.fit(img, size, Image.ANTIALIAS)
"""
