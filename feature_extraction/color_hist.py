import cv2
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

# Define the static things that we need

DATA = Path('../dataset-resized')
DATA_CATEGORIES = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
EDGES = Path('../outputs')

# Color histogram extraction class.


class ColorHist:

    '''
    Class that extracts the color histograms for each channel of the image.
    This does not rely on segmentation
    '''

    def __init__(self, image_path):

        self.filename = str(image_path.split('/')[-1])
        self.category = str(image_path.split('/')[-2])
        self.img = cv2.imread(image_path)

    def get_color_hist(self):

        self.red_channel = cv2.calcHist(self.img, [0], None, [512], [0, 256])
        self.green_channel = cv2.calcHist(self.img, [1], None, [512], [0, 256])
        self.blue_channel = cv2.calcHist(self.img, [2], None, [512], [0, 256])

    def get_corresponding_edge(self):

        self.corresponding_edge = EDGES / self.category / 'gaussian' / self.filename
        self.corresponding_edge = str(self.corresponding_edge.resolve())
        self.corresponding_edge = cv2.imread(self.corresponding_edge)

    def get_edge_map(self):

        self.edges = cv2.cvtColor(self.corresponding_edge, cv2.COLOR_BGR2GRAY)
        self.edges = np.transpose(self.edges)
        self.edges = [np.mean(i) for i in self.edges]
        self.edges = np.asarray(self.edges)
        self.edges = np.reshape(self.edges, (512, 1))

    def merge_hists(self):

        self.merged = np.array([
            [self.edges],
            [self.red_channel],
            [self.green_channel],
            [self.blue_channel]
            ])

    def show_plots(self):

        plt.plot(self.edges, label='edge')
        plt.show()
        plt.plot(self.red_channel, label='red')
        plt.show()
        plt.plot(self.green_channel, label='green')
        plt.show()
        plt.plot(self.blue_channel, label='blue')
        plt.show()
