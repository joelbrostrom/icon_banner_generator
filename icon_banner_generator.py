import os

from PIL import Image, ImageDraw, ImageFont


def add_banner(input_image_path, output_image_path, banner_text, banner_color=(0, 128, 0), font_size_ratio=0.12):
    # Load the base icon
    base_icon = Image.open(input_image_path).convert("RGBA")
    width, height = base_icon.size

    # Calculate font size based on the image size
    font_size = int(height * font_size_ratio)

    # Define banner dimensions
    banner_height = int(height * 0.2)
    banner_width = int(width * 1.2)
    banner = Image.new("RGBA", (banner_width, banner_height), (0, 0, 0, 0))

    # Draw the banner background
    draw = ImageDraw.Draw(banner)
    draw.rectangle([0, 0, banner_width, banner_height], fill=banner_color)

    # Load font
    try:
        font = ImageFont.truetype("Arial Black.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Create a text image to center the text precisely
    text_img = Image.new("RGBA", (banner_width, banner_height), (0, 0, 0, 0))
    text_draw = ImageDraw.Draw(text_img)

    # Calculate text position to center it
    text_bbox = text_draw.textbbox((0, 0), banner_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = ((banner_width - text_width/2 ) // 2, (banner_height - text_height*2) // 2)
    text_draw.text(text_position, banner_text, fill="white", font=font)

    # Paste the centered text onto the banner before rotation
    banner.paste(text_img, (0, 0), text_img)

    # Rotate the banner to place it diagonally
    banner = banner.rotate(45, expand=True)

    # Create the combined image
    combined = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    combined.paste(base_icon, (0, 0))

    # Position the banner in the top-left corner, keeping the text centered
    banner_x_offset = -int(banner_width * 0.3)
    banner_y_offset = -int(banner_height * 1.3)
    combined.paste(banner, (banner_x_offset, banner_y_offset), banner)

    # Save the output
    combined.save(output_image_path, format="PNG")

def generate_all_icons(base_icon_path):
    # Define output paths and banner texts
    icons = [
        ("dev_icon.png", "DEV", (255, 0, 0)),
        ("stg_icon.png", "STG", (255, 165, 0)),
        ("prod_icon.png", "PROD", (0, 128, 0))
    ]

    # Generate each icon
    for output_name, text, color in icons:
        output_path = os.path.join("assets/icons/", output_name)
        add_banner(base_icon_path, output_path, text, banner_color=color)

if __name__ == "__main__":
    # Path to the base icon
    base_icon_path = "assets/icons/icon.png"
    generate_all_icons(base_icon_path)
