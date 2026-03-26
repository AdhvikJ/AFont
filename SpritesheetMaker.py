from PIL import Image, ImageDraw

print("""_______________________________
|                             |
|  AFont Spritesheet Creator  |
|                             |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾""")
print("Made by Curious Adhvik\nv1.0\n")

choice = input("Type 'ready' to start.\nType 'help' for help.\nType anything else to exit.\nEnter: ")

if choice.lower() == "ready":
    print("We will now create a spritesheet template.\n")

    # === CONFIGURATION ===
    cols = int(input("How many columns (characters per row)?\nEnter: "))
    rows = int(input("How many rows?\nEnter: "))

    cell_w = int(input("Cell width? (recommended: 256)\nEnter: "))
    cell_h = int(input("Cell height? (recommended: 256)\nEnter: "))

    # === CANVAS SIZE ===
    sheet_w = cols * cell_w
    sheet_h = rows * cell_h

    # Transparent background
    sheet = Image.new("RGBA", (sheet_w, sheet_h), (255, 255, 255, 255))
    draw = ImageDraw.Draw(sheet)

    # === GRID SETTINGS ===
    grid_color = (0, 0, 0, 128)  # semi-transparent black
    line_width = 1

    # Vertical lines
    for c in range(cols + 1):
        x = c * cell_w
        draw.line([(x, 0), (x, sheet_h)], fill=grid_color, width=line_width)

    # Horizontal lines
    for r in range(rows + 1):
        y = r * cell_h
        draw.line([(0, y), (sheet_w, y)], fill=grid_color, width=line_width)

    output = "spritesheet_template.png"
    sheet.save(output)
    print(f"Spritesheet template with grid saved as {output}")

elif choice.lower() == "help":
    print("This program creates a blank spritesheet PNG with a visible grid.\n"
          "- You choose rows, columns, and cell size.\n"
          "- Output is 'spritesheet_template.png'.\n"
          "You can then draw or paste glyphs into each cell.")
    print("Any bugs? Report it on GitHub! I, the creator, will eventually get to fixing it.\n\nLaunch the program again to come back.\nThanks!")
