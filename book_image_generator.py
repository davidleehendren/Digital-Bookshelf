from PIL import Image, ImageDraw, ImageFont

def main():
    # Parameters
    text = "The Great Escape"
    font_path = 'C:/Users/jbro2554/OneDrive - J.B. Hunt Transport/Python Sandbox/DigitalBookshelf/ALGER.ttf'
    font_size = 60 #need to parameterize this to take up X or Y % of width or height of image. 
    background_path = 'C:/Users/jbro2554/OneDrive - J.B. Hunt Transport/Python Sandbox/DigitalBookshelf/TaleOfTwoCitiesSpine.jpeg'
    #Need to get these figured out, not sure how they behave...
    #text_box_height_percent = 50  # Set the text box height as a percentage of the background image height
    #text_box_width_percent = 50  # Set the text box width as a percentage of the background image width
    #position_x_percent = 20  # Set the x-coordinate position as a percentage of the background image width
    #position_y_percent = 20  # Set the y-coordinate position as a percentage of the background image height

    # Calculate the position coordinates based on percentages
    background_img = Image.open(background_path)
    background_width, background_height = background_img.size
    
    # Calculate the position coordinates to center the text box
    #position_x = int((background_width - text_box_width_percent * background_width / 100) / 2)
    #position_y = int((background_height - text_box_height_percent * background_height / 100) / 2)

    # position = (
    #     (background_width * position_x_percent) // 100,
    #     (background_height * position_y_percent) // 100
    # )

    # Create text box and superimpose
    text_box = create_text_box(text, font_path, font_size, background_path) #, text_box_width_percent, text_box_height_percent)
    left, top, right, bottom = text_box.getbbox()
    text_height = bottom - top
    text_width = right - left
    
    # Calculate the position coordinates to center the text box
    position_x = int(background_width / 2) - int(text_height/2)
    position_y = int(background_height / 2) - int(text_width/2)

    result_img = superimpose_text(background_path, text_box, (position_x, position_y))

    # Display or save the result
    result_img.show()
    # result_img.save("path/to/save/result.jpg")

# Function to create transparent text box with adjustable dimensions
def create_text_box(text, font_path, font_size, background_path): #, text_box_width_percent, text_box_height_percent):
    # Load font
    font = ImageFont.truetype(font_path, font_size)

    # Open background image to get its dimensions
    background_img = Image.open(background_path)
    background_width, background_height = background_img.size

    # Calculate text box dimensions as percentages of the background image size
    text_box_width = (background_width)# * text_box_width_percent) // 100
    text_box_height = (background_height)# * text_box_height_percent) // 100

    # Calculate the height needed to fit the text within the text box
    #text_size_width, text_size_height = font.getlength(text)
    #text_size = font.getsize(text)
    left, top, right, bottom = font.getbbox(text)
    text_size_width_required = right - left
    text_height_required = bottom - top

    # Ensure the text box height is at least as tall as the required text height
    text_box_height = max(text_box_height, text_height_required)
    text_box_width = max(text_box_width, text_size_width_required)

    # Create transparent image for text
    text_img = Image.new('RGBA', (text_box_width, text_box_height), (255, 255, 255, 0))

    # Create drawing context
    draw = ImageDraw.Draw(text_img)

    # Draw text
    font_color = (184, 134, 11, 255) #Dark Gold
    #font_color = (255, 215, 0, 255) #Light Gold
    #font_color = (255,255,255,255)
    draw.text((0, 0), text, font=font, fill=font_color)

    return text_img

# Function to superimpose text box on background image
def superimpose_text(background_path, text_img, position):
    # Open background image
    background = Image.open(background_path)

    # Rotate text image 90 degrees
    rotated_text = text_img.rotate(90, expand=True)

    # Paste text on background at the specified position
    background.paste(rotated_text, position, rotated_text)

    return background

if __name__ == "__main__":
    main()
