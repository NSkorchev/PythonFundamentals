import pytesseract
from PIL import Image

# Open the image
image = Image.open('image.jpg')

# Convert the image to black and white
image = image.convert('L')

# Use pytesseract to recognize the action
text = pytesseract.image_to_string(image)

# Print the recognized action
print(text)
