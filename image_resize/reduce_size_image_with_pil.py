import math
from PIL import Image

# My image is a 1280x1072 jpeg that is 191kb large
image_name = "image2"
image_ext = ".png"
reduction_factor = 10
foo = Image.open("./original_images/" + image_name + image_ext)
height, width = foo.size
print([height, width])

# If you like reduce specified value
"""x2, y2 = math.floor(height - 50), math.floor(width - 20)
foo = foo.resize((x2, y2), Image.ANTIALIAS)"""

# I downsize the image with a ANTIALIAS filter (gives the heighest quality)
# ANTIALIAS allows to preserve the highest possible quality
foo = foo.resize((int(height / reduction_factor), int(width / reduction_factor)), Image.ANTIALIAS)
# The saved downsized image size is 107kb
foo.save("./resized_images/scales_middle_" + image_name + image_ext, quality = 75)
# The saved downsized image size is 102kb
# optimize parameter only work with .png and .jpeg extensions files
foo.save("./resized_images/opt_scales_middle_" + image_name + image_ext, optimize = True, quality = 75)


