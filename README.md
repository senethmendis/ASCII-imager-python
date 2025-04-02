# Image to ASCII Converter

This Python script converts an image into an ASCII representation using grayscale pixel intensity mapping.

## Features

-   Converts any image into ASCII art.
-   Allows customization of output width for better clarity.
-   Saves ASCII output to a text file.

## Requirements

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

Run the script with an image file:

```python
from image_to_ascii import image_to_ascii

image_to_ascii('input.jpg', 'ascii_output.txt', width=100)
```

Replace `'input.jpg'` with the path to your image file.

## Example Output

```
@@@@@%%%%###*****===---....
@@@%%%###*****===---....
...
```

## License

This project is open-source and free to use.
