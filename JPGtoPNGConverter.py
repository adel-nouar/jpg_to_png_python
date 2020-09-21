import sys
import os
from PIL import Image

# 1- Grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# 2- Check if arg2 directory exist, if not create this directory
if not os.path.exists(output_folder):
    os.makedirs(f'{output_folder}')

# 3- Loop through arg1 directory
for filename in os.listdir(image_folder):
    if filename.split('.')[1] == 'jpg':
        img = Image.open(f'{image_folder}{filename}')
        clean_name = os.path.splitext(filename)[0]
        # 4- Convert images to png
        # 5 - Save to the new folder
        img.save(f'{output_folder}{clean_name}.png', 'png')
print('All done!')
