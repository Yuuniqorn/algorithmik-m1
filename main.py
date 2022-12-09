import os
from pathlib import Path
from PIL import Image
import imagehash
from AVLTree import AVLTree

path = "C:/Users/nico/Desktop/cats_vs_dogs_dataset/PetImages/Cat"
data_dir = Path(path)
mydict = {}

Tree = AVLTree()
Tree.root = None

for files in data_dir.glob('*jpg'):
    hash_of_image = str(imagehash.average_hash(Image.open(files)))
    mydict[hash_of_image] = files
    Tree.insert(hash_of_image, files)


def get_in_constant_runtime(image):
    hash_of_image_2 = str(imagehash.average_hash(Image.open(image)))

    if hash_of_image_2 in mydict:
        print(f"{mydict[hash_of_image_2]}")
        # os.startfile(mydict[hash_of_image_2], "open")

    else:
        'Nothing found'


def get_in_logarithmic_runtime(image):
    hash_of_image_3 = str(imagehash.average_hash(Image.open(image)))
    if Tree.search(hash_of_image_3):
        print(Tree.find(hash_of_image_3).getPaths())

    else:
        'Nothing found'


def get_most_similar_in_log_runtime(image):
    pass


def get_image_paths(self):
    """
    Path to the image files to be read based on the local location of this project.
    """

    # Project Location
    project_dir = os.path.dirname(os.path.realpath('__file__'))
    # Modul Location
    module_name = 'Cat_Images'

    path_to_file = os.path.join(project_dir, module_name)
    list_of_all_imagine_paths: list = []

    for path in Path(path_to_file).rglob('*.jpg'):
        list_of_all_imagine_paths.append(os.path.join(path_to_file, path))

        return list_of_all_imagine_paths


test_image_path = 'C:/Users/nico/Desktop/cats_vs_dogs_dataset/PetImages/Cat/2.jpg'

get_in_constant_runtime(test_image_path)
get_in_logarithmic_runtime(test_image_path)