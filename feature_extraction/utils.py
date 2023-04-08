import os
from PIL import Image
import numpy as np

def create_image_paths(data_dir, load_images=False, vectorize_images=False):
    '''
    Creates a list of dictionaries from the data directory.
    This also loads and vectorizes the images as another key in the dictionary if the parameter is set.
    '''
    class_data = [f"{data_dir}/{name}" for name in os.listdir(data_dir) if os.path.isdir(f"{data_dir}/{name}")]
    constructed = []
    for c in class_data:
        images = os.listdir(c)
        for im_name in images:
            im_path = f"{c}/{im_name}"
            row = {"im_path": im_path,
                                "class": c.split('/')[1]}
            if load_images:
                loaded_image = image = Image.open(im_path)
                im_arr = np.asarray(image)
                im_size = im_arr.shape
                row["im_arr"] = im_arr
                row["im_shape"] = im_size
                if vectorize_images:
                    image_vector = im_arr.reshape(1, -1, 3)
                    row['vectorized_R'] = image_vector[0, :, 0]
                    row['vectorized_G'] = image_vector[0, :, 1]
                    row['vectorized_B'] = image_vector[0, :, 2]
            constructed.append(row)
    return constructed

def load_output_images(source_file_names, output_dir="outputs", load_images=False, vectorize_images=False):
    '''
    Example usage:

    data_dir = 'dataset-resized'
    data_list = []
    dfs = []
    for d in data_list:
        dfs.append(pd.DataFrame(load_output_images(source_file_names=data_dir, load_images=True, vectorize_images=True)))
    df = pd.concat(dfs)

    '''
    constructed = []
    for category in os.listdir(source_file_names):
        category_dir = f"{source_file_names}/{category}"
        if os.path.isdir(category_dir):
            for fn in os.listdir(category_dir):
                row = {"class": category}
                output_category_dir = f"{output_dir}/{category}"
                if os.path.isdir(output_category_dir):
                    for method in os.listdir(f"{output_dir}/{category}"):
                        target_im_path = f"{output_dir}/{category}/{method}/{fn}"
                        if os.path.isfile(target_im_path):
                            if load_images:
                                loaded_image = Image.open(target_im_path)
                                im_arr = np.asarray(loaded_image)
                                row["im_path"] = target_im_path
                                row["im_arr"] = im_arr
                                row["im_shape"] = im_arr.shape
                                if vectorize_images:
                                    image_vector = im_arr.reshape(1, -1, 3)
                                    row[f"vectorized_{method}_R"] = image_vector[0, :, 0]
                                    row[f"vectorized_{method}_G"] = image_vector[0, :, 1]
                                    row[f"vectorized_{method}_B"] = image_vector[0, :, 2]
                constructed.append(row)
    return constructed
