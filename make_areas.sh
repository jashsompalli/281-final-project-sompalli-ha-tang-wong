#!/bin/bash

THIS_DIR=$( pwd )

if [ -e $THIS_DIR/dataset-resized.zip ]; then
	unzip $THIS_DIR/dataset-resized.zip
	rm -rf $THIS_DIR/__MACOSX
	rm -rf $THIS_DIR/.DS_Store
fi

create_class_dirs(){
	mkdir -p $THIS_DIR/$1/$2/gaussian
	mkdir -p $THIS_DIR/$1/$2/mean
	mkdir -p $THIS_DIR/$1/$2/median
}

create_class_dirs outputs glass
create_class_dirs outputs cardboard
create_class_dirs outputs paper
create_class_dirs outputs plastic
create_class_dirs outputs metal
create_class_dirs outputs trash

create_class_dirs combined glass
create_class_dirs combined cardboard
create_class_dirs combined paper
create_class_dirs combined plastic
create_class_dirs combined metal
create_class_dirs combined trash

cd $THIS_DIR/feature_extraction
python edge_detect.py

rm $THIS_DIR/dataset-resized.zip


