### Greedy AutoAugment
Official implementation of the Greedy AutoAugment. The code is written with Python. With this code, you will get an overall structure of the algorithm for search, doing actual searching and training on many network architectures. This process includes reading on four different datasets and applying custom augmentation on them based on Torch library guideline.

 ### Overall search structure
The Greedy AutoAugment is a very flexible algorithm and the underlying structure can be changed easily. The only thing that is needed is to have a score from different augmentations. To show the flexibility we provide `search_structure.py`. The `test()` provides random numbers as a fake score generator back to the `doSearch()`:
```
python search_structure.py
```

### Search
For the search simply enter the following code in a python 2 environment with torch library enabled. The `--last_layer` option should correspond to the number of classes in `--dataset`. For instance, cifar10 needs value 10, cifar100 needs value 100, Tiny Imagenet needs value 200, and SVHN needs value 10. The `--pickle_path` determines that where a pickle variable of the final search result should be saved. Next to saving a pickle file, the 100 best policies of the final search is printer after the search is finished.

```
cd Search
python main.py --data='Datasets' --lr=0.1 --network=1 --last_layer=10 --dataset=cifar10 --pickle_path='saved_pickle'
```
### Train
For the traing enter the following code in a python 2 environment with torch library enabled. There are multiple options added to the available options for the search. For the `--mode`, we can use `'Manual'`,`'AutoAug'`, and `'GAutoAug'`. The  `--resume=0`, `--smallprint=1` the values to be 0, 1.

```
cd Train
python main.py --data='Datasets' --lr=0.1  --network=1 --last_layer=10 --dataset='cifar10' --mode='GAutoAug' --resume=0 --smallprint=1 --ckptfolder='ckptfolder/' --ckptname='test' --end_epoch=200
```

#### Note for Tiny Imagenet
For Tiny Imagenet to be read by our importer `folder2labels-py2` which is a pickle variable should be copied into 'tiny-imagenet-200' folder. In case python 3 is used `folder2labels` should be copied. 

### Citation

If you used this code please consider citing the accompanying paper:

```
@article{naghizadeh2020greedy,
  title={Greedy autoaugment},
  author={Naghizadeh, Alireza and Abavisani, Mohammadsajad and Metaxas, Dimitris N},
  journal={Pattern Recognition Letters},
  volume={138},
  pages={624--630},
  year={2020},
  publisher={Elsevier}
}

```

### References
For the code we did get help from these two repositories: [AutoAugment](https://github.com/tensorflow/models/tree/master/research/autoaugment), [Train CIFAR10 with PyTorch](https://github.com/kuangliu/pytorch-cifar).



