import glob
import os
import sys

from PIL import Image


def get_image_names(path):
    assert os.path.isdir(path), 'Source is not a valid folder'
    path_wildcard = "*.png"
    full_path_wildcard = os.path.join(path, path_wildcard)
    return glob.iglob(full_path_wildcard)


def convertToPdf(name, path_src, path_dst):
    file_names = get_image_names(path_src)
    images = [Image.open(file_path) for file_path in file_names]
    assert len(images) > 0, 'No image to be converted to PDF.'
    first_image = images[0]
    assert os.path.isdir(path_dst), 'Dest is not a valid Folder.'
    save_destination = os.path.join(path_dst, name)
    first_image.save(
        save_destination,
        "PDF",
        resolution=100.0,
        save_all=True,
        append_images=images[1:]
    )


if __name__ == '__main__':
    assert len(sys.argv) >= 2, 'Name might be defined to continue.'
    assert len(sys.argv) >= 3, 'Source might be defined to continue.'
    assert len(sys.argv) >= 4, 'Destination might be defined to continue.'
    convertToPdf(sys.argv[1], sys.argv[2], sys.argv[3])
