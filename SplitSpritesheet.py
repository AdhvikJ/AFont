# <  A Note to the wonderful people seeing the code! :]  >
# If you attempt to dissect this code, then please know what you are doing.
# Not even I have the slightest idea of what is happening here.
# Still, I hope this makes your work easier! :D
# <  - Curious Adhvik  >

def launch2():

    import os
    from PIL import Image
    import cv2
    import svgwrite
    import string

    # === SAFE FILENAME HANDLER ===
    def safe_filename_char(c):
        # Allowed characters for filenames
        allowed = string.ascii_letters + string.digits + "_-"

        if c in allowed:
            return c

        # Special readable names
        special_names = {
            " ": "SPACE",
            "\t": "TAB",
            "\n": "NEWLINE"
        }
        if c in special_names:
            return special_names[c]

        # Fallback: Unicode codepoint
        return f"U{ord(c):04X}"

    print("""________________________________\n|                              |\n|  AFont Spritesheet Splitter  |\n|                              |\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾""")
    print("Made by Curious Adhvik\nv1.0\n")

    def tguh3():

        choice = input("Type 'ready' to start.\nType 'help' for help.\nType 'exit' to exit.\nEnter: ")
            
        if choice.lower() == "ready":

            print("We will now split your already created spritesheet.")

            # === CONFIGURATION ===
            sheet = Image.open(input("What is your file named? e.g.: 'MySpritesheet.png' (must be PNG)\nEnter: "))
            sheet_w, sheet_h = sheet.size

            cols = int(input("How many characters per row?\nEnter: "))
            rows = int(input("How many rows?\nEnter: "))

            cell_w = int(input("Cell width? (it is recommended to put 256)\nEnter: "))
            cell_h = int(input("Cell height? (it is recommended to put 256)\nEnter: "))

            chars = input("What are the characters in the sheet?\nEnter: ")

            if len(chars) != cols * rows:
                print(f"Error: expected {cols*rows} characters, got {len(chars)}")
                exit()

            output_dir = input("Finally, since the svgs are stored in a folder, what should the folder be named?\nEnter: ")
            os.makedirs(output_dir, exist_ok=True)

            # === MAIN LOOP ===
            index = 0
            for row in range(rows):
                for col in range(cols):
                    if index >= len(chars):
                        break

                    # Crop cell
                    x = col * cell_w
                    y = row * cell_h
                    box = (x, y, x + cell_w, y + cell_h)
                    glyph = sheet.crop(box).convert("RGBA")

                    # Force resize to exact cell size
                    glyph = glyph.resize((cell_w, cell_h), Image.NEAREST)

                    # Remove white background
                    datas = glyph.getdata()
                    newData = []
                    for item in datas:
                        if item[0] > 230 and item[1] > 230 and item[2] > 230:
                            newData.append((255, 255, 255, 0))  # transparent
                        else:
                            newData.append(item)
                    glyph.putdata(newData)

                    # === Safe filename handling ===
                    char = chars[index]
                    safe_char = safe_filename_char(char)

                    filename_png = f"{safe_char}_U{ord(char):04X}.png"
                    filepath_png = os.path.join(output_dir, filename_png)
                    glyph.save(filepath_png)
                    print("Saved", filename_png)

                    # === Convert PNG → SVG using alpha channel + hierarchy ===
                    img = cv2.imread(filepath_png, cv2.IMREAD_UNCHANGED)
                    alpha = img[:, :, 3]  # transparency mask
                    _, thresh = cv2.threshold(alpha, 127, 255, cv2.THRESH_BINARY)

                    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                    filename_svg = f"{safe_char}_U{ord(char):04X}.svg"
                    filepath_svg = os.path.join(output_dir, filename_svg)

                    # Scale factor to normalize to ~1000 units
                    scale = 5.6  # 256 * 4 = 1024 units

                    dwg = svgwrite.Drawing(filepath_svg, size=("1000", "1000"))
                    dwg.viewbox(0, 0, cell_w * scale, cell_h * scale)

                    # Build one path with evenodd fill rule
                    path_data = ""

                    for cnt in contours:
                        # Skip empty or tiny contours
                        if len(cnt) < 3:
                            continue

                        points = [(int(x * scale), int(y * scale)) for x, y in cnt[:, 0]]

                        if len(points) < 3:
                            continue

                        path_data += f"M {points[0][0]} {points[0][1]} "
                        for x, y in points[1:]:
                            path_data += f"L {x} {y} "
                        path_data += "Z "

                    # Prevent invalid SVGs
                    if path_data.strip() == "":
                        print(f"⚠ Warning: No valid contours for {filename_svg} (glyph may be blank)")
                        index += 1
                        continue

                    dwg.add(dwg.path(d=path_data, fill="black", stroke="black", fill_rule="evenodd"))
                    dwg.save()
                    print("Converted to", filename_svg)

                    index += 1

            print("All glyphs saved as ~1000-unit SVGs in", output_dir)

            # === DELETE PNGs ===
            for filename in os.listdir(output_dir):
                if filename.endswith(".png"):
                    filepath = os.path.join(output_dir, filename)
                    try:
                        os.remove(filepath)
                        print("Deleted:", filepath)
                    except Exception as e:
                        print("Error deleting", filepath, ":", e)

            print("Success! All PNGs destroyed, only SVG vectors remain! :D")
            print("Complete. Import these into Glyphr Studio, like the video said! :)")

        elif choice == "help":
            
            print("\nIf there is any doubts about anything, then check the GitHub page, or the video.\nAny bugs? Report it on GitHub! I, the creator, will eventually get to fixing it.\n\nLaunch the program again to come back.\nThanks!")

        elif choice == "exit":

            print("Exiting...")
            exit()

        else:

            print("\nInvalid! Please try again.\n")
            tguh3()

    
    tguh3()
