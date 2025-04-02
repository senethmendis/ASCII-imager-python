from PIL import Image
import numpy as np

def image_to_ascii(image_path, output_path="ascii_output.txt", width=100):
    # Load image and convert to grayscale
    image = Image.open(image_path).convert("L")
    
    # Calculate new height to maintain aspect ratio
    aspect_ratio = image.height / image.width
    new_height = int(aspect_ratio * width * 0.55)  
    
    # Resize the image
    image = image.resize((width, new_height))
    
    # ASCII character set from dark to light
    ascii_chars = "@%#*+=-:. "
    
    # Convert pixels to ASCII
    pixels = np.array(image)
    ascii_image = "\n".join(
        "".join(ascii_chars[pixel // 32] for pixel in row) for row in pixels
    )
    
    # Save to file
    with open(output_path, "w") as f:
        f.write(ascii_image)
    
    print(f"ASCII image saved to {output_path}")
