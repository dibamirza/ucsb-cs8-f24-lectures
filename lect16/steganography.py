from PIL import Image

# Function to hide n most significant bits of one number into the least significant bits of another
def hide_bits(large_value, small_value, n=4):
    """
    Embeds the n most significant bits of small_value into the least significant bits of large_value.
    """
    return 42

# Function to extract hidden bits from a number
def extract_hidden_value(combined_value, n):
    """
    Extracts the small_value hidden in the least significant n bits of combined_value.
    """
    return 42

# Function to encode a single pixel
def encode_pixel(large_pixel, small_pixel, n=4):
    """
    Encodes a single pixel as a tuple from the hidden image into a pixel from the cover image.
    """
    return (1, 1, 1)

# Function to decode a single pixel
def decode_pixel(encoded_pixel, n=4):
    """
    Decodes a single pixel to retrieve the hidden image pixel.
    """
    return (1, 1, 1)

# Function to encode an entire image
def encode_image(large_image_path, small_image_path, output_image_path, n=4):
    """
    Loops through all pixels to encode the small image into the large image.
    returns the size of the small image
    """
    # Load the large and small images
    large_image = Image.open(large_image_path)
    small_image = Image.open(small_image_path)

    if small_image.size[0] > large_image.size[0] or small_image.size[1] > large_image.size[1]:
        print("Hidden image is larger than Cover Image")
        return
    
    encoded_image = Image.new('RGB', large_image.size, (0, 0, 0))
    for x in range(large_image.size[0]):
        for y in range(large_image.size[1]):
            large_pixel = large_image.getpixel((x, y))
            # TO DO: write code to create the output image

            encoded_image.putpixel((x,y), large_pixel )
    
    # Save the encoded image
    encoded_image.save(output_image_path, 'PNG')
    print(f"Encoded image saved as {output_image_path}")
    return small_image.size

# Function to decode a hidden image
def decode_image(encoded_image_path, hidden_image_size, n=4):
    # Load the encoded image
    encoded_image = Image.open(encoded_image_path)

    # Create a new image to store the hidden pixels
    hidden_image = Image.new('RGB', hidden_image_size)

    for x in range(hidden_image_size[0]):
        for y in range(hidden_image_size[1]):
            encoded_pixel = encoded_image.getpixel((x, y))
            # TO DO: Decode the hidden pixel
           
            hidden_image.putpixel((x, y), encoded_pixel)

    # Save the hidden image
    hidden_image.save("hidden_image.png", 'PNG')
    hidden_image.show()
    print("Hidden image saved as 'hidden_image.png'")

param_n = 4
small_image_size = encode_image('hat.jpg', 'bunny.jpg', 'encoded_hat')

# Decode the hidden image from the encoded image
decode_image('encoded_hat', small_image_size)
