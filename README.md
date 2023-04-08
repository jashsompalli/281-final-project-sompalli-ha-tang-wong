# W281 Final TrashNet

## Getting Started

To get started, download dataset from [here](https://github.com/garythung/trashnet/blob/master/data/dataset-resized.zip) and put the class files (i.e. 'paper', 'metal', 'cardboard', 'trash', 'glass', and 'plastic') into the data-resized directory.

### Create the necessary folders

Run the python script to set up your directories, which creates the folders `combined` and `outputs`

```
python3 setup_folder.py
```

### Run the edge detection script to generate edge detected images

```
cd feature_extraction
python3 edge_detect.py
```

## Features Implemented

- Shape Features:

  - Image Segmentation

- Color Features
  - Color Historgram
