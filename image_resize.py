from PIL import Image

# Opening an image file (.bmp,.jpg,.png,.gif) present in the working folder.
# (change name of image from img.jpg to the respective image name followed by the extension)
img = Image.open("img.jpg")

# Initializing parameters for resized image.
new_width = 0
new_height = 0

# Get parameter values of input image
width, height = img.size

# Get parameter values of resized image.
if width >= 500 or height >= 500:
    new_width = int(width/2)
    new_height = new_width
elif width < 500 or height < 500:
    new_width = int(width*2)
    new_height = new_width

# Resize input image using obtained parameter values using LANCZOS filter.
img1 = img.resize((new_width, new_height), Image.LANCZOS)
ext = ".jpg"

# Save the new image on the working folder.
img1.save("new_img" + ext)

# Output parrameters of both images for comparison.
print("Parameters of original image:- Width: " + str(width) + ", Height: " + str(height))
print("Parameters of resized image:- New_Width: " + str(new_width) + ", New_Height: " + str(new_height))

# Display resized image
img1.show()
