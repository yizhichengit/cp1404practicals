# Dictionary of color names and codes
ALL_CAPS = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "AliceBlue": "#f0f8ff",
    "Alizarin crimson": "#e32636",
    "Amaranth": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "AntiqueWhite": "#faebd7",
    "AntiqueWhite1": "#ffefdb",
    "AntiqueWhite2": "#eedfcc"
}


# Function to get color code by name (case-insensitive)
def get_color_code(color_name):
    return ALL_CAPS.get(color_name.capitalize(), "Color not found")



# Main program loop
while True:
    color_name = input("Enter a color name (or blank to exit): ").strip()

    if color_name.lower() == "blank":
        break  # Exit the loop if the input is "blank"

    color_code = get_color_code(color_name)
    print(f"{color_name}: {color_code}")

