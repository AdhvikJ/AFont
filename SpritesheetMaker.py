# <  A Note to the wonderful people seeing the code! :]  >
# If you attempt to dissect this code, then please know what you are doing.
# Not even I have the slightest idea of what is happening here.
# Still, I hope this makes your work easier! :D
# <  - Curious Adhvik  >

def launch1():

    from PIL import Image, ImageDraw

    print("_______________________________\n|                             |\n|  AFont Spritesheet Creator  |\n|                             |\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("Made by Curious Adhvik\nv1.0\n")

    def tguhtwo():

        choice = input("Type 'ready' to start.\nType 'help' for help.\nType 'exit' to exit.\nEnter: ")

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

            # WHITE background
            sheet = Image.new("RGBA", (sheet_w, sheet_h), (255, 255, 255, 255))
            draw = ImageDraw.Draw(sheet)

            # === GRID SETTINGS ===
            # === GRID SETTINGS ===
            value_100 = max(0, min(100, float(input("Enter 0-100 (black-white) for how bright the grid lines should be: "))))
            color = int(round(value_100 * 2.55))
            grid_color = (color, color, color, 255)

            choice2 = float(input("Enter how thick the lines should be (min: 0.1): "))
            line_width = max(0.1, choice2)
            line_width_int = int(round(line_width))




            # Vertical lines
            for c in range(cols + 1):
                x = c * cell_w
                draw.line([(x, 0), (x, sheet_h)], fill=grid_color, width=line_width_int)

            # Horizontal lines
            for r in range(rows + 1):
                y = r * cell_h
                draw.line([(0, y), (sheet_w, y)], fill=grid_color, width=line_width_int)

            output1 = f"{input("Alright, we made the spritesheet, and now you need to give it a name! What shall it be called?\nDo not type the suffix of the file.\nEnter: ")}.png"
            output = output1.replace(" ", "_")
            sheet.save(output)
            if " " in output1:
                print(f"Spritesheet template with grid saved as {output}\n(the spaces were replaced w/ underscores)")
            else:
                print(f"Spritesheet template with grid saved as {output}")

        elif choice.lower() == "help":
            print("This program creates a blank spritesheet PNG with a visible grid.\n"
                "- You choose rows, columns, and cell size.\n"
                "- Output will be a .png.\n"
                "You can then draw or paste glyphs into each cell.")
            print("Any bugs? Report it on GitHub! I, the creator, will eventually get to fixing it.\n\nLaunch the program again to come back.\nThanks!")

        elif choice.lower() == "exit":

            print("Exiting...")
            exit()

        else:

            print("\nInvalid! Please try again.\n")
            tguhtwo()


    tguhtwo()
