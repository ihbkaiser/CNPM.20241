import os
import random

def select_random_image(folder):
    """Select a random image filename from a specified folder."""
    image_files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    if not image_files:
        raise ValueError("No images found in the folder")
    return random.choice(image_files)

# Example usage
folder_path = 'samples'
random_image = select_random_image(folder_path)
print(os.path.join(folder_path,'d.png')