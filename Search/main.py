from __future__ import print_function
from __future__ import division

import torch.optim as optim

import torchvision.transforms as transforms
import cPickle as pickle
import os
import argparse

from models import *
from utils import progress_bar
import importer.TinyImageNet as tiny
import importer.cifar as cifar
import importer.svhn as svhn
from utils import find_gpu
import numpy as np

parser = argparse.ArgumentParser(description='Searching')
parser.add_argument('--data', default='/common/users/an499/Datasets/', type=str, help='data root directory')
parser.add_argument('--lr', default=0.1, type=float, help='learning rate')
parser.add_argument('--network', default=3, type=int,help='Which network to use, 0-11')
parser.add_argument('--last_layer', default=200, type=int,help='The size of the last layer, 0-11')
parser.add_argument('--dataset', default='tiny', type=str,help='The dataset being used')
parser.add_argument('--pickle_path', default='saved_pickle', type=str,help='Directory to save all of the policies with pickle.')

args = parser.parse_args()


best_gpu = find_gpu()
cuda_device = 'cuda:'+str(best_gpu)

device = cuda_device if torch.cuda.is_available() else 'cpu'
best_acc = 0  # best test accuracy
start_epoch = 0  # start from epoch 0 or last checkpoint epoch
ll = args.last_layer

networks_names = ('DenseNet121', 'DPN92', 'GoogLeNet', 'MobileNet', 'MobileNetV2', 'PreActResNet18', 'ResNet18', 'ResNeXt29_2x64d', 'SENet18', 'ShuffleNetG2', 'VGG', 'ShuffleNetV2')

root = args.data

print('==> Building model..')

if args.network==0:
    net = DenseNet121(ll)
elif args.network==1:
    net = DPN92(ll)
elif args.network==2:
    net = GoogLeNet(ll)
elif args.network==3:
    net = MobileNet(ll)
elif args.network==4:
    net = MobileNetV2(ll)
elif args.network==5:
    net = PreActResNet18(ll)
elif args.network==6:
    net = ResNet18(num_classes=ll)
elif args.network==7:
    net = ResNeXt29_2x64d(ll)
elif args.network==8:
    net = SENet18(ll)
elif args.network==9:
    net = ShuffleNetG2(ll)
elif args.network==10:
    net = VGG('VGG19', ll)
elif args.network==11:
    net = ShuffleNetV2(1, ll)
else:
    "Network numbers is not correct"

net = net.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=args.lr, momentum=0.9, weight_decay=5e-4)

# Training
def train(epoch, trainloader):
    print('\nEpoch: %d' % epoch)
    net.train()
    train_loss = 0
    correct = 0
    total = 0
    for batch_idx, (inputs, targets) in enumerate(trainloader):
        inputs, targets = inputs.to(device), targets.to(device)
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

        train_loss += loss.item()
        _, predicted = outputs.max(1)
        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()

        progress_bar(batch_idx, len(trainloader), 'Loss: %.3f | Acc: %.3f%% (%d/%d)'
            % (train_loss/(batch_idx+1), 100.*correct/total, correct, total))
        return correct

def test(testloader):
    global best_acc
    net.eval()
    test_loss = 0
    correct = 0
    total = 0
    with torch.no_grad():
        for batch_idx, (inputs, targets) in enumerate(testloader):
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = net(inputs)
            loss = criterion(outputs, targets)

            test_loss += loss.item()
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()

            progress_bar(batch_idx, len(testloader), 'Loss: %.3f | Acc: %.3f%% (%d/%d)'
                % (test_loss/(batch_idx+1), 100.*correct/total, correct, total))

    acc = 100.*correct/total
    if acc > best_acc:
        best_acc = acc
    return acc, best_acc

def SepTrainPart1():
    from PIL import Image
    print("Reading tiny imagenet started...")
    # now load the picked numpy arrays
    train_data = []
    train_labels = []
    train_names = []

    base_folder = 'tiny-imagenet-200'
    base_dir = os.path.join(root, base_folder)
    image_dir = os.path.join(root, base_folder, 'train/')

    with open(base_dir + '/folder2labels-py2', "rb") as f:
        folder2labels = pickle.load(f)

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

                train_data.append(image_data)
                train_labels.append(folder2labels[folder_name])
                train_names.append(image)
    train_data = np.array(train_data)
    train_labels = np.array(train_labels)
    print("Reading Data for Part1 Finished.")
    return train_data, train_labels

def data_prepare(current_policy,train_data,train_labels):
    # Data
    print('==> Preparing data..')
    if args.dataset == "tiny":
        transform_train = transforms.Compose([
        transforms.Resize(32),
        transforms.ToTensor(),])

        trainset = tiny.TinyIN(root=root, train=True, transform=transform_train, current_policy=current_policy,
                                   train_data_finding_part2=train_data, train_labels_finding_part2=train_labels)
        testset = tiny.TinyIN(root=root, train=False, transform=transform_train, current_policy=current_policy,
                                  train_data_finding_part2=train_data, train_labels_finding_part2=train_labels)

    elif args.dataset == "cifar10":
        transform_train = transforms.Compose([
        transforms.Resize(32),
        transforms.ToTensor(),])

        trainset = cifar.CIFAR10(root=root, train=True, download=True, transform=transform_train, current_policy=current_policy)
        testset = cifar.CIFAR10(root=root, train=False, download=True, transform=transform_train, current_policy=current_policy)

    elif args.dataset == "cifar100":
        transform_train = transforms.Compose([
        transforms.Resize(32),
        transforms.ToTensor(),])

        trainset = cifar.CIFAR100(root=root, train=True, download=True, transform=transform_train, current_policy=current_policy)
        testset = cifar.CIFAR100(root=root, train=False, download=True, transform=transform_train, current_policy=current_policy)

    elif args.dataset == "SVHN":
        transform_train = transforms.Compose([
        transforms.Resize(32),
        transforms.ToTensor(),])

        trainset = svhn.SVHN(root=root, split='train', split2='train',download=True, transform=transform_train, current_policy=current_policy)
        testset = svhn.SVHN(root=root, split='train', split2='test',download=True, transform=transform_train, current_policy=current_policy)

    else:
        print("you dataset name is not correct")



    trainloader = torch.utils.data.DataLoader(trainset, batch_size=128, shuffle=True, num_workers=2)
    testloader = torch.utils.data.DataLoader(testset, batch_size=100, shuffle=False, num_workers=2)

    return trainloader, testloader

global randomseed
randomseed = 2097
def getresults():
    global randomseed
    randomseed += 1000
    import random
    random.seed(randomseed)
    res = random.uniform(0, 1)
    return res

def get_max_idx(indeces, all_policies, s):
    max_idx = -1
    for i in indeces:
        if all_policies[i] not in s:
            s.add(all_policies[i])
            max_idx = i
            break
    return max_idx, s

def grouper(lst, k =3):
    return [lst[n:n + k] for n, i in enumerate(lst) if n % k == 0]

def save_variables(path = "", policies = None):
    if policies != None:
        pickle.dump(policies, open(path, 'wb'))

def doSearch():
    policies = ['FlipLR', 'FlipUD', 'AutoContrast', 'Equalize', 'Invert', 'Rotate', 'Posterize', 'CropBilinear',
                'Solarize',
                'Color', 'Contrast', 'Brightness', 'Sharpness', 'ShearX', 'ShearY', 'TranslateX', 'TranslateY',
                'Cutout', 'Blur',
                'Smooth']

    if args.dataset=="tiny":#this is a special command only for tiny imagenet to make reading images much faster (only once from hard disk)
        train_data, train_labels = SepTrainPart1()
    else:
        train_data, train_labels = None,None

    all_epochs = 0
    all_trainings = 0
    all_results = []
    all_policies = []
    s = set()
    for t in range(20):
        for m in range(10):
            all_trainings += 1
            all_epochs += 5
            sub_policy = (policies[t], 1, m)
            current_policy = sub_policy
            grouped_policy = grouper(current_policy)
            trainloader, testloader = data_prepare(grouped_policy,train_data, train_labels)            
            for epoch in range(5):
                train(epoch, trainloader)
            res, _ = test(testloader)
            """res = getresults()"""
            all_policies.append(current_policy)
            all_results.append(res)
            print("Training: ", all_trainings, " res:", res)
    indeces = np.argsort(all_results)[::-1][:len(all_results)]
    max_idx, s = get_max_idx(indeces, all_policies, s)

    for i in range(4):
        pre_policy = all_policies[max_idx]
        for t in range(20):
            for m in range(10):
                all_trainings += 1
                all_epochs += 5
                sub_policy = (policies[t], 1, m)
                current_policy = pre_policy + sub_policy
                grouped_policy = grouper(current_policy)
                trainloader, testloader = data_prepare(grouped_policy,train_data, train_labels)                
                for epoch in range(5):
                    train(epoch, trainloader)
                res, _ = test(testloader)
                """res = getresults()"""
                all_policies.append(current_policy)
                all_results.append(res)
                print("Training: ", all_trainings, " res:", res)
        indeces = np.argsort(all_results)[::-1][:len(all_results)]
        max_idx, s = get_max_idx(indeces, all_policies, s)

    saved_policies =  []
    for i in range(len(all_policies)):
        idx = indeces[i]
        policy = all_policies[idx]
        grouped_policy = grouper(policy)
        saved_policies.append(grouped_policy)

    for i in range(100):
        print(saved_policies[i])

    print("All epochs:" + str(all_epochs) + " All trainings:" + str(all_trainings))
    return saved_policies

policies = doSearch()
save_variables(args.pickle_path, policies = policies)
