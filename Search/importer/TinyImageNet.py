from __future__ import print_function
from __future__ import division
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
import copy

class TinyIN(data.Dataset):

    base_folder = 'tiny-imagenet-200'

    class_number = 200

    def __init__(self, root, train=True, transform=None, target_transform=None,
                 current_policy = None, train_data_finding_part2=None, train_labels_finding_part2=None):
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

        self.current_policy = current_policy
        self.train_data_finding_part2 = train_data_finding_part2
        self.train_labels_finding_part2 = train_labels_finding_part2
        self.Original()




    def Original(self):
        if self.train:
            self.train_data = copy.deepcopy(self.train_data_finding_part2)
            self.train_labels = copy.deepcopy(self.train_labels_finding_part2)
            self.train_data, self.train_labels = self.divide_train(self.train_data, self.train_labels)
            self.train_data, self.train_labels = self.OriginalGAutoAug(self.train_data, self.train_labels)

        else:
            train_data = copy.deepcopy(self.train_data_finding_part2)
            train_labels = copy.deepcopy(self.train_labels_finding_part2)
            self.test_data, self.test_labels = self.divide_train(train_data, train_labels)

    def divide_train(self,batch_xs,batch_ys):
        import random
        random.seed(10000)
        s = set()
        while len(s)<5000:
            r = random.randint(0, 99999)
            s.add(r)
        test_idx = list(s)

        x = []
        y = []
        for idx, label in enumerate(batch_ys):
            data = batch_xs[idx]
            if self.train == True:
                if idx in test_idx:
                    continue
                x.append(data)
                y.append(label)
            else:
                if idx in test_idx:
                    x.append(data)
                    y.append(label)
        print(len(y))
        #print("Data finished")
        return np.array(x), np.array(y)

    def OriginalGAutoAug(self,batch_xs,batch_ys):
        import augmentation_transforms

        gp = self.current_policy

        x = []
        y = []
        for idx, label in enumerate(batch_ys):
            data = batch_xs[idx]
            data2 = augmentation_transforms.apply_policy(gp, data)
            data2 = np.array(data2)
            x.append(data2)
            y.append(label)
        return np.array(x), np.array(y)

    def divide_train2(self,batch_xs,batch_ys, mode):
        import random
        random.seed(10000)
        s = set()
        while len(s)<5000:
            r = random.randint(0, 99999)
            s.add(r)
        test_idx = list(s)

        #print(test_idx)

        import my_augmentation_transforms as augmentation_transforms

        gp = self.current_policy

        x = []
        y = []
        for idx, label in enumerate(batch_ys):
            data = batch_xs[idx]
            if mode == "train":
                data2 = data
                data2 = augmentation_transforms.apply_policy(gp, data)
                # data2 = np.array(data2.getdata(),dtype='uint8')

                # data2 = Image.fromarray(data)

                data2 = np.array(data2)
                if idx in test_idx:

                    continue
                x.append(data2)
                y.append(label)
            else:
                if idx in test_idx:
                    x.append(data)
                    y.append(label)
        print(len(y))
        print("Data finished")
        return np.array(x), np.array(y)



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



