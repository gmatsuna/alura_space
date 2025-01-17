from PIL import Image

# Load the image to be resized
image_path = 'setup/static/assets/ícones/1x/new.png'
image = Image.open(image_path)

# Set the new dimensions (replace with actual dimensions)
new_width = 32  # Replace with the width of Surpreenda-me - inativo.png
new_height = 32  # Replace with the height of Surpreenda-me - inativo.png

# Resize the image
resized_image = image.resize((new_width, new_height))

# Save the resized image
resized_image.save('setup/static/assets/ícones/1x/new_resized.png')

print("Image resized and saved as new_resized.png")
