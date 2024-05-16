from PIL import Image
import os

Image.MAX_IMAGE_PIXELS = 933120000


def reduce_image_size(input_folder, output_folder, max_size=(1200, 630)):
    """
    Reduces the size of all images in the input_folder and saves them to the output_folder without losing quality.

    Args:
    input_folder (str): Path to the folder containing input images.
    output_folder (str): Path to the folder where resized images will be saved.
    max_size (tuple): Maximum size (width, height) of the resized images.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    # Loop through each file in the input folder
    for file in files:
        # Check if the file is an image
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Open the image file
            with Image.open(os.path.join(input_folder, file)) as img:
                # Resize the image without losing quality
                img.thumbnail(max_size, Image.LANCZOS)

                # Save the resized image to the output folder
                img.save(os.path.join(output_folder, file))


reduce_image_size('C:/Users/DSi/Downloads/New glasses', 'C:/Users/DSi/Downloads/Optimized New glasses')
