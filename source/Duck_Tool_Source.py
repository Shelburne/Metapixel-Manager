import sys
import csv
import os
from PIL import Image

# Hat Dimensions
WIDTH, HEIGHT = 97, 56
METAPIXEL_X = 96 
HAT_FOLDER = "Hats"

def png_to_csv(image_path, output_in_root=False):
    """Scans the 97th column of a hat and saves metapixels to a CSV."""
    try:
        with Image.open(image_path) as img:
            img = img.convert('RGBA')
            metapixels = []
            for y in range(HEIGHT):
                r, g, b, a = img.getpixel((METAPIXEL_X, y))
                if a > 0:
                    metapixels.append({'R': r, 'G': g, 'B': b})
            
            # Extract the filename without the folder path
            filename_only = os.path.basename(image_path)
            base_name = os.path.splitext(filename_only)[0]
            
            # Determine save location
            if output_in_root:
                output_csv = f"{base_name}_meta.csv"
            else:
                output_csv = os.path.join(os.path.dirname(image_path), f"{base_name}_meta.csv")

            with open(output_csv, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['R', 'G', 'B'])
                writer.writeheader()
                writer.writerows(metapixels)
            print(f"Extracted: {output_csv}")
    except Exception as e:
        print(f"Error reading {os.path.basename(image_path)}: {e}")

def csv_to_hats(csv_path):
    """Reads a CSV and applies it to all PNGs in the 'Hats' folder."""
    try:
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            metapixels = [(int(row['R']), int(row['G']), int(row['B']), 255) for row in reader]

        overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
        for i, color in enumerate(metapixels):
            if i < HEIGHT:
                overlay.putpixel((METAPIXEL_X, i), color)
        
        output_folder = "Output"
        os.makedirs(output_folder, exist_ok=True)

        if not os.path.exists(HAT_FOLDER):
            print(f"No '{HAT_FOLDER}' folder found!")
            return

        for filename in os.listdir(HAT_FOLDER):
            if filename.lower().endswith('.png'):
                with Image.open(os.path.join(HAT_FOLDER, filename)) as hat:
                    hat = hat.convert('RGBA')
                    combined = Image.alpha_composite(hat, overlay)
                    combined.save(os.path.join(output_folder, filename))
                    print(f"Applied metapixels to: {filename}")
    except Exception as e:
        print(f"Error processing CSV: {e}")

if __name__ == "__main__":
    # Case 1: File(s) dragged and dropped onto the EXE
    if len(sys.argv) > 1:
        for file_path in sys.argv[1:]:
            ext = os.path.splitext(file_path)[1].lower()
            if ext == '.png':
                png_to_csv(file_path)
            elif ext == '.csv':
                csv_to_hats(file_path)
    
    # Case 2: EXE run directly (Double-clicked)
    else:
        print(f"No file dropped. Checking '{HAT_FOLDER}' folder for batch extraction...")
        if os.path.exists(HAT_FOLDER):
            hat_files = [f for f in os.listdir(HAT_FOLDER) if f.lower().endswith('.png')]
            if not hat_files:
                print("No PNGs found in the Hats folder.")
            else:
                for hat in hat_files:
                    png_to_csv(os.path.join(HAT_FOLDER, hat),output_in_root=True)
        else:
            print(f"'{HAT_FOLDER}' folder not found. Create it and put hats inside!")

    input("\nProcess complete. Press Enter to exit...")