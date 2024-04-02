from PIL import Image
import os
import math

IMAGE_FOLDERS = ['.\\Pictures\\1369_12_Наклейки 3-D_3', '.\\Pictures\\1388_2_Наклейки 3-D_1']
OUTPUT_FILE = 'collage.tif'

def make_collage(collage_args):
    image_folders, output_file, thumbnail_size, padding_between, padding_edge, accepted_formats, images_per_row = collage_args.values()
    
    images = []

    for folder in image_folders:
        folder_images = [img for img in os.listdir(folder) if img.endswith(accepted_formats)]
        for img_name in folder_images:
            img_path = os.path.join(folder, img_name)
            img = Image.open(img_path)
            img.thumbnail(thumbnail_size)
            images.append(img)
    
    num_images = len(images)
    cols = min(num_images, images_per_row)
    rows = math.ceil(num_images / images_per_row)

    collage_width = cols * (thumbnail_size[0] + padding_between) - padding_between + 2 * padding_edge
    collage_height = rows * (thumbnail_size[1] + padding_between) - padding_between + 2 * padding_edge

    collage = Image.new('RGB', (collage_width, collage_height), 'white')

    for i, img in enumerate(images):
        col = i if i < cols else i % cols
        row = i // cols
        x = padding_edge + col * (thumbnail_size[0] + padding_between)
        y = padding_edge + row * (thumbnail_size[1] + padding_between)
        collage.paste(img, (x, y))

    collage.save(output_file, format='TIFF')

if __name__ == '__main__':
    collage_args = {
        'image_folders': IMAGE_FOLDERS,
        'output_file': OUTPUT_FILE,
        'thumbnail_size': (200, 200),
        'padding_between': 20,
        'padding_edge': 40,
        'accepted_formats': ('png', 'jpg', 'jpeg'),
        'images_per_row': 4
    }

    make_collage(collage_args)
