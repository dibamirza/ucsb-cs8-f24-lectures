from PIL import Image

# Function to hide n most significant bits of one number into the least significant bits of another
def hide_bits(hat_value, bunny_value, n=4):
    """
    Embeds the n most significant bits of small_value into the least significant bits of large_value.
    hat_value = 0xAB , bunny_value= 0xC3 , output = 0xAC
    """
    n = (hat_value >> 4) << 4 # n = 0xA0
    m = bunny_value >> 4  # 0x0C
    
    return n | m

# Function to extract hidden bits from a number
def extract_hidden_value(combined_value, n):
    """
    Extracts the small_value hidden in the least significant n bits of combined_value.
    """
    return 42

# Function to encode a single pixel
def encode_pixel(hat_pixel, bunny_pixel, n=4):
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
# Function to encode an entire image
def encode_image(hat_image_path, bunny_image_path, output_image_path, n=4):
    """
    Loops through all pixels to encode the small image into the large image.
    returns the size of the small image
    """
    # Load the large and small images
    hat_image = Image.open(hat_image_path)
    bunny_image = Image.open(bunny_image_path)

    if bunny_image.size[0] > hat_image.size[0] or bunny_image.size[1] > hat_image.size[1]:
        print("Hidden image is larger than Cover Image")
        return
    
    encoded_image = Image.new('RGB', hat_image.size, (0, 0, 0))
    for x in range(hat_image.size[0]):
        for y in range(hat_image.size[1]):
            color_hat = hat_image.getpixel((x, y))
            # TO DO: write code to create the output(encoded) image
            # Clear out the last four bits of color_hat

            # new_color = []
            # for hat_channel_value in color_hat:
            #     new_value = hat_channel_value & 0xf0 
            #     new_color.append(new_value) 
            # list of three values 
            encoded_image.putpixel((x,y), tuple(color_hat))
    
    # Save the encoded image
    encoded_image.save(output_image_path, 'PNG')
    print(f"Encoded image saved as {output_image_path}")
    return bunny_image.size

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
            hidden_pixel = []
            for encoded_value in encoded_pixel:
                hidden_value = encoded_value & 0x0f
                hidden_value = hidden_value << 4
                hidden_pixel.append(hidden_value)
           
            hidden_image.putpixel((x, y), tuple(hidden_pixel))

    # Save the hidden image
    hidden_image.save("hidden_image.png", 'PNG')
    print("Hidden image saved as 'hidden_image.png'")

param_n = 4
small_image_size = encode_image('hat.jpg', 'bunny.jpg', 'encoded_hat')

# Decode the hidden image from the encoded image
decode_image('encoded_hat', small_image_size)
