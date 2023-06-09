import os
import cv2
import numpy as np
from pathlib import Path
import skimage

# Define the static things that we need

DATA = Path('/home/jash/CV_final/dataset-resized')
DATA_CATEGORIES = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# Edge detection class.


class FeatureExtract:

    '''
    Class that extracts the edges of the things in the image. This just
    considers the edges of the object, and does no segmentation
    '''

    def __init__(self, image_path, kernel, DATA_DIR=None):

        self.filename = str(image_path.split('/')[-1])
        self.category = str(image_path.split('/')[-2])
        self.unedited = cv2.imread(image_path)
        self.img = cv2.imread(image_path)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.kernel = kernel
        self.save_path = Path(
                f'../outputs/{self.category}/{self.kernel}/{self.filename}'
                )
        if DATA_DIR:
            DATA = DATA_DIR

    def blur_image(self):

        # Do gaussian blurring if gaussian is passed into object
        if self.kernel == 'gaussian':

            blur_kernel = cv2.GaussianBlur(self.img, (5, 5), 0)
            feature = cv2.Canny(blur_kernel, 100, 200)
            ret, mask = cv2.threshold(feature, 50, 255, cv2.THRESH_BINARY)

        # Do median blurring if median is passed into object
        if self.kernel == 'median':

            blur_kernel = cv2.medianBlur(self.img, 5)
            feature = cv2.Canny(blur_kernel, 100, 100)
            ret, mask = cv2.threshold(feature, 50, 255, cv2.THRESH_BINARY)

        # Do mean blurring if mean is passed into object
        if self.kernel == 'mean':

            blur_kernel = cv2.blur(self.img, (5, 5))
            feature = cv2.Canny(blur_kernel, 100, 100)
            ret, mask = cv2.threshold(feature, 50, 255, cv2.THRESH_BINARY)

        if self.kernel == 'lbp':
            '''
            finds the local binary pattern of the image with the given Pand R.
            P is Number of circularly symmetric neighbour set points.
            R is Radius of circle.
            '''
            p = 10
            r = 40
            feature = skimage.feature.local_binary_pattern(self.img, p, r)
        # Save edges to the correct location with the correct filename
        # OpenCV doesnt understand PosixPath objects - ugly str casting to fix
        cv2.imwrite(str(self.save_path.resolve()), feature)

def executor(category):

    '''
    Function to make the object and execute the blur_image() method for
    all the images inside the category
    '''

    blur_methods = ['gaussian', 'median', 'mean', 'lbp']
    image_paths = DATA / category
    images = [str(image_paths / i) for i in os.listdir(image_paths)]

    for i in images:
        for method in blur_methods:
            extractor = FeatureExtract(i, method)
            extractor.blur_image()

def combiner(category, blur_type):

    '''
    Function to take the edges detected and overlay them onto the original
    images. Kinda messy, but does what needs to be done
    '''

    combined_loc = Path(f'../combined/{category}/{blur_type}')

    original_loc = DATA / category
    original_files = [str(original_loc / i) for i in os.listdir(original_loc)]
    blur_loc = Path(f'../outputs/{category}/{blur_type}')
    blur_files = [str(blur_loc / i) for i in os.listdir(blur_loc)]

    for i, v in enumerate(original_files):

        original_img = cv2.imread(v)
        edges = cv2.imread(blur_files[i])
        filename = v.split('/')[-1]

        output = cv2.addWeighted(original_img, 0.5, edges, 0.5, 0.0)

        cv2.imwrite(str(combined_loc / filename), output)


if __name__ == '__main__':

    # Main routine to get the edges for all images using
    # gaussian, median, and mean blurring

    blur_methods = ['gaussian', 'mean', 'median', 'lbp']

    for category in DATA_CATEGORIES:
        executor(category)
        for method in blur_methods:
            combiner(category, method)
