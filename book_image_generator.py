from PIL import Image, ImageDraw, ImageFont

def main():

    # Parameters
    text = "The Great Escape"
    font_path = "/Users/mturner/Downloads/arial.ttf"  # Replace with your font file path
    font_size = 20
    background_path = '/Users/mturner/Downloads/books.jpg'  # Replace with your background image path
    position = (40, 40)  # Replace with desired position

    # Create text box and superimpose
    text_box = create_text_box(text, font_path, font_size)
    result_img = superimpose_text(background_path, text_box, position)

    # Display or save the result
    result_img.show()
    # result_img.save("path/to/save/result.jpg")

# Function to create transparent text box
def create_text_box(text, font_path, font_size):
    # Load font
    font = ImageFont.truetype(font_path, font_size)

    # Create transparent image for text
    text_img = Image.new('RGBA', (280, 40), (255, 255, 255, 0))

    # Create drawing context
    draw = ImageDraw.Draw(text_img)

    # Draw text
    draw.text((0, 0), text, font=font, fill=(0, 0, 0, 255))

    return text_img

# Function to superimpose text box on background image
def superimpose_text(background_path, text_img, position):
    # Open background image
    background = Image.open(background_path)

    # Rotate text image 90 degrees
    rotated_text = text_img.rotate(90, expand=True)

    # Paste text on background
    background.paste(rotated_text, position, rotated_text)

    return background




if __name__ == "__main__":
    main()