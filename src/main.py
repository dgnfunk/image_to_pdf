from PIL import Image
import glob
import os
import sys

def get_image_names(path):
    isDirectory = os.path.isdir(path)
    if isDirectory is False:
        return []
    # This is my path
    path_wildcard = "\\*.png"
    return glob.iglob(path + path_wildcard)

def convertToPdf(name, path_src, path_dst):
    file_names = get_image_names(path_src)
    images = [Image.open(file_path) for file_path in file_names]
    first_image = images[0]
    first_image.save(path_dst + '\\' + name, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])

if __name__ == '__main__':
    convertToPdf(sys.argv[1], sys.argv[2], sys.argv[3])