import cv2
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

# Define the static things that we need

DATA = Path('../dataset-resized')
DATA_CATEGORIES = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
# EDGES = Path('../outputs')

# Color histogram extraction class.


class ColorHist:

    '''
    Class that extracts the color histograms for each channel of the image.
    This does not rely on segmentation
    '''

    def __init__(self, image_path, relative_output_dir="../outputs"):

        self.filename = str(image_path.split('/')[-1])
        self.category = str(image_path.split('/')[-2])
        self.img = cv2.imread(image_path)
        self.EDGES = Path(relative_output_dir)

    def get_color_hist(self):

        '''
        This does NOT have an issue
        '''

        self.red_channel = cv2.calcHist(self.img, [0], None, [512], [0, 256])
        self.green_channel = cv2.calcHist(self.img, [1], None, [512], [0, 256])
        self.blue_channel = cv2.calcHist(self.img, [2], None, [512], [0, 256])


    def get_corresponding_edge(self):

        self.corresponding_edge = self.EDGES / self.category / 'gaussian' / self.filename
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


if __name__ == '__main__':

    obj = ColorHist(str(DATA / 'glass' / 'glass276.jpg'))
    obj.get_color_hist()
    obj.get_corresponding_edge()
    obj.get_edge_map()
    obj.show_plots()
    obj.merge_hists()
    obj.merged = obj.merged.flatten()

