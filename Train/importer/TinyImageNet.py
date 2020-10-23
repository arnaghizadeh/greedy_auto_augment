from __future__ import print_function
from PIL import Image
import os
import os.path
import numpy as np
import sys
if sys.version_info[0] == 2:
    import cPickle as pickle
else:
    import pickle

import torch.utils.data as data
import pandas as pd


class TinyIN(data.Dataset):

    base_folder = 'tiny-imagenet-200'

    class_number = 200

    def __init__(self, root, train=True,
                 transform=None, target_transform=None,
                 download=False):
        self.root = os.path.expanduser(root)
        self.transform = transform
        self.target_transform = target_transform
        self.train = train  # training set or test set
        self.train_data = []
        self.train_labels = []
        self.train_names = []

        self.test_data = []
        self.test_labels = []
        self.test_names = []
        self.Original()

    def Original(self):
        # now load the picked numpy arrays
        if self.train:
            self.train_data = []
            self.train_labels = []
            self.train_names = []
            base_dir = os.path.join(self.root, self.base_folder)
            image_dir = os.path.join(self.root, self.base_folder,'train/')

            with open(base_dir+'/folder2labels-py2', "rb") as f:
                folder2labels= pickle.load(f)

            for folder_name in os.listdir(image_dir):
                if os.path.isdir(image_dir + folder_name + '/images/'):
                    type_images = os.listdir(image_dir + folder_name + '/images/')
                    # Loop through all the images of a type directory
                    batch_index = 0;
                    # print ("Loading Class ", type)
                    for image in type_images:
                        image_file = os.path.join(image_dir, folder_name + '/images/', image)

                        # reading the images as they are; no normalization, no color editing
                        image_data = Image.open(image_file)
                        image_data = np.array(image_data)
                        if (image_data.shape != (64, 64, 3)):
                            # there are images that are not three channels, in this case we have to convert them.
                            image_data = Image.open(image_file).convert("RGB")
                            image_data = np.array(image_data)

                        self.train_data.append(image_data)
                        self.train_labels.append(folder2labels[folder_name])
                        self.train_names.append(image)
            self.train_data = np.array(self.train_data)
            self.train_labels = np.array(self.train_labels)
            self.train_names = np.array(self.train_names)
        else:
            self.test_data = []
            self.test_labels = []
            self.test_names = []
            base_dir = os.path.join(self.root, self.base_folder)
            val_dir = os.path.join(self.root, self.base_folder,'val/')
            val_images = os.listdir(val_dir + 'images/')

            validation_data = pd.read_csv(val_dir + 'val_annotations.txt', sep='\t', header=None, names=['File', 'Class', 'X', 'Y', 'H', 'W'])
            tempdict = {}
            for idx, row in validation_data.iterrows():
                tempdict.update({row['File']:row['Class']})
            validation_data = tempdict

            with open(base_dir+'/folder2labels-py2', "rb") as f:
                folder2labels= pickle.load(f)

            # Loop through all the images of a val directory
            for i in range(len(val_images)):
                image = val_images[i]
                image_file = os.path.join(val_dir, 'images/', image)

                image_data = Image.open(image_file)
                image_data = np.array(image_data)
                if (image_data.shape != (64, 64, 3)):
                    #there are images that are not three channels, in this case we have to convert them.
                    image_data = Image.open(image_file).convert("RGB")
                    image_data = np.array(image_data)

                self.test_data.append(image_data)
                folder_name = validation_data[image]
                self.test_labels.append(folder2labels[folder_name])
                self.test_names.append(image)

            self.test_data = np.array(self.test_data)
            self.test_labels = np.array(self.test_labels)
            self.test_names = np.array(self.test_names)

    def __getitem__(self, index):
        """
        Args:
            index (int): Index

        Returns:
            tuple: (image, target) where target is index of the target class.
        """

        if self.train:
            img, target = self.train_data[index], self.train_labels[index]
        else:
            #print(index, len(self.test_data),len(self.test_labels))
            img, target = self.test_data[index], self.test_labels[index]

        # doing this so that it is consistent with all other datasets
        # to return a PIL Image
        img = Image.fromarray(img)

        if self.transform is not None:
            img = self.transform(img)

        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target

    def __len__(self):
        if self.train:
            return len(self.train_data)
        else:
            return len(self.test_data)


    def __repr__(self):
        fmt_str = 'Dataset ' + self.__class__.__name__ + '\n'
        fmt_str += '    Number of datapoints: {}\n'.format(self.__len__())
        tmp = 'train' if self.train is True else 'test'
        fmt_str += '    Split: {}\n'.format(tmp)
        fmt_str += '    Root Location: {}\n'.format(self.root)
        tmp = '    Transforms (if any): '
        fmt_str += '{0}{1}\n'.format(tmp, self.transform.__repr__().replace('\n', '\n' + ' ' * len(tmp)))
        tmp = '    Target Transforms (if any): '
        fmt_str += '{0}{1}'.format(tmp, self.target_transform.__repr__().replace('\n', '\n' + ' ' * len(tmp)))
        return fmt_str





