import cv2
import numpy as np
import sys

# Read in the image

s = format (sys.argv[1])
	    
print(s)

image = cv2.imread(s)

# Make a copy of the image
image_copy = np.copy(image)

# Change color to RGB (from BGR)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)


# play around with these values until you isolate the blue background

lower_green = np.array([0, 100, 0])    
upper_green = np.array([120, 255, 100])


# Define the masked area
mask = cv2.inRange(image_copy, lower_green, upper_green)


# Mask the image to let the pizza show through
masked_image = np.copy(image_copy)
masked_image[mask != 0] = [0, 0, 0]

# Load in a background image, and convert it to RGB 
background_image = cv2.imread('3.jpg')
background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

# Crop it to the right size (514x816)
crop_background = background_image

# Mask the cropped background so that the pizza area is blocked
crop_background[mask == 0] = [0, 0, 0]

# Add the two images together to create a complete image!
final_image = crop_background + masked_image

final_image = cv2.cvtColor(final_image, cv2.COLOR_RGB2BGR)

cv2.imwrite('out.jpg', final_image)
