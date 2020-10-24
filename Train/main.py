'''Train CIFAR10 with PyTorch.'''
from __future__ import print_function

import torch.optim as optim

import torchvision.transforms as transforms

import platform
import os
import argparse

from models import *
from utils import progress_bar
import importer.TinyImageNet as tiny
import importer.cifar as cifar
import importer.svhn as svhn
import importer.custom_augment as CA
import numpy as np
import torch.utils.data as utils
from utils import find_gpu

networks_names = (
'DenseNet121', 'DPN92', 'GoogLeNet', 'MobileNet', 'MobileNetV2', 'PreActResNet18', 'ResNet18', 'ResNeXt29_2x64d',
'SENet18', 'ShuffleNetG2', 'ShuffleNetV2', 'VGG')

# for server, files comment out, smallprint=1, nodeletion=0
parser = argparse.ArgumentParser(description='Training')
parser.add_argument('--data', default='/common/users/an499/Datasets/', type=str, help='data root directory')
parser.add_argument('--lr', default=0.1, type=float, help='learning rate')
parser.add_argument('--network', default=7, type=int, help='Which network to use, 0-11')
parser.add_argument('--last_layer', default=200, type=int, help='The size of the last layer, 0-11')
parser.add_argument('--dataset', default="cifar10", type=str, help='The dataset being used, cifar10, cifar100, tiny, SVHN')
parser.add_argument('--mode', default="GAutoAug", type=str, help='The training mode, Manual, AutoAug, GAutoAug.')
parser.add_argument('--resume', default=1, type=int, help='resume from checkpoint')
parser.add_argument('--smallprint', default=0, type=int, help='Produce detailed output (0) or small output (1).')
parser.add_argument('--ckptfolder', default="ckptfolder/", type=str, help='The location of the checkpoint folder.')
parser.add_argument('--ckptname', default="test", type=str, help='The checkpoint name.')
parser.add_argument('--end_epoch', default=200, type=int, help='The number of epochs')

args = parser.parse_args()

root = args.data
checkpoint_folder = args.ckptfolder
checkpoint_primary = checkpoint_folder + 'checkpoint/' + args.ckptname

# print(checkpoint_file)
best_gpu = find_gpu()
cuda_device = 'cuda:'+str(best_gpu)
device = cuda_device if torch.cuda.is_available() else 'cpu'
best_acc = 0  # best test accuracy
start_epoch = 0  # start from epoch 0 or last checkpoint epoch
ll = args.last_layer
# Data
print('==> Preparing data..')

augmentation = CA.Original()

if args.dataset == "tiny":
    if args.mode == "Manual":
        augmentation = CA.Manual()
    elif args.mode == "AutoAug":
        augmentation = CA.tiny_AutoAug()
    elif args.mode == "GAutoAug":
        augmentation = CA.tiny_GAutoAug(network=args.network)
    else:
        print("Mode is not correct!!")

elif args.dataset == "cifar10":
    if args.mode == "Manual":
        augmentation = CA.Manual()
    elif args.mode == "AutoAug":
        augmentation = CA.cifar_AutoAug()
    elif args.mode == "GAutoAug":
        augmentation = CA.cifar_GAutoAug(mode="CIFAR10", network=args.network)
    else:
        print("Mode is not correct!!")

elif args.dataset == "cifar100":
    if args.mode == "Manual":
        augmentation = CA.Manual()
    elif args.mode == "AutoAug":
        augmentation = CA.cifar_AutoAug()
    elif args.mode == "GAutoAug":
        augmentation = CA.cifar_GAutoAug(mode="CIFAR100", network=args.network)
    else:
        print("Mode is not correct!!")

elif args.dataset == "SVHN":
    if args.mode == "Manual":
        augmentation = CA.Manual()
    elif args.mode == "AutoAug":
        augmentation = CA.svhn_AutoAug()
    elif args.mode == "GAutoAug":
        augmentation = CA.svhn_GAutoAug(network=args.network)
    else:
        print("Mode is not correct!!")
else:
    print("you dataset name is not correct")

transform_train = transforms.Compose([
    transforms.Resize(32),
    augmentation,
    transforms.ToTensor(),])

transform_test = transforms.Compose([
    transforms.Resize(32),
    transforms.ToTensor(),
])

if args.dataset == "tiny":
    trainset = tiny.TinyIN(root=root, train=True, download=True, transform=transform_train)
    testset = tiny.TinyIN(root=root, train=False, download=True, transform=transform_test)


elif args.dataset == "cifar10":
    trainset = cifar.CIFAR10(root=root, train=True, download=True, transform=transform_train)
    testset = cifar.CIFAR10(root=root, train=False, download=True, transform=transform_test)


elif args.dataset == "cifar100":
    trainset = cifar.CIFAR100(root=root, train=True, download=True, transform=transform_train)
    testset = cifar.CIFAR100(root=root, train=False, download=True, transform=transform_test)


elif args.dataset == "SVHN":
    trainset = svhn.SVHN(root=root, split="train", download=True, transform=transform_train)
    testset = svhn.SVHN(root=root, split="test", download=True, transform=transform_test)

else:
    print("you dataset name is not correct")

trainloader = torch.utils.data.DataLoader(trainset, batch_size=len(trainset), shuffle=False, num_workers=2)
testloader = torch.utils.data.DataLoader(testset, batch_size=100, shuffle=False, num_workers=2)

# Model
print('==> Building model..')

if args.network == 0:
    net = DenseNet121(ll)
elif args.network == 1:
    net = DPN92(ll)
elif args.network == 2:
    net = GoogLeNet(ll)
elif args.network == 3:
    net = MobileNet(ll)
elif args.network == 4:
    net = MobileNetV2(ll)
elif args.network == 5:
    net = PreActResNet18(ll)
elif args.network == 6:
    net = ResNet18(num_classes=ll)
elif args.network == 7:
    net = ResNeXt29_2x64d(ll)
elif args.network == 8:
    net = SENet18(ll)
elif args.network == 9:
    net = ShuffleNetG2(ll)
elif args.network == 10:
    net = ShuffleNetV2(1, ll)
elif args.network == 11:
    net = VGG('VGG19', ll)
else:
    "Network numbers is not correct"

net = net.to(device)

if os.path.isfile(checkpoint_primary) == True:
    args.resume = 1
    checkpoint_file = checkpoint_primary
else:
    print("No started file, this should only happen for testing")
if args.resume:
    # Load checkpoint.
    print('==> Resuming from checkpoint..')
    assert os.path.isdir(checkpoint_folder + 'checkpoint'), 'Error: no checkpoint directory found!'
    checkpoint = torch.load(checkpoint_file)
    net.load_state_dict(checkpoint['net'])
    best_acc = checkpoint['acc']
    start_epoch = checkpoint['epoch']

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=args.lr, momentum=0.9, weight_decay=5e-4)


# Training
def train(epoch):
    print('\nEpoch: %d' % epoch)
    net.train()
    train_loss = 0
    correct = 0
    total = 0
    # all_tensors = []
    tensor_x = []
    tensor_y = []

    for batch_idx, (inputs, targets) in enumerate(trainloader):
        if batch_idx == 0:
            tensor_x = inputs
            tensor_y = targets
        else:
            tensor_x = torch.cat([tensor_x, inputs])
            tensor_y = torch.cat([tensor_y, targets])
    my_dataset = utils.TensorDataset(tensor_x, tensor_y)  # create your datset
    my_dataloader = utils.DataLoader(my_dataset, batch_size=128, shuffle=True, num_workers=2)  # create your dataloader

    for batch_idx, (inputs, targets) in enumerate(my_dataloader):
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
        if args.smallprint == 0:
            progress_bar(batch_idx, len(trainloader), 'Loss: %.3f | Acc: %.3f%% (%d/%d)'
                         % (train_loss / (batch_idx + 1), 100. * correct / total, correct, total))


def test(epoch):
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

            if args.smallprint == 0:
                progress_bar(batch_idx, len(testloader), 'Loss: %.3f | Acc: %.3f%% (%d/%d)'
                             % (test_loss / (batch_idx + 1), 100. * correct / total, correct, total))

    # Save checkpoint.
    acc = 100. * correct / total
    if acc > best_acc:
        print('Saving..')
        state = {
            'net': net.state_dict(),
            'acc': acc,
            'epoch': epoch,
        }
        if not os.path.isdir(checkpoint_folder + 'checkpoint'):
            os.mkdir(checkpoint_folder + 'checkpoint')

        torch.save(state, checkpoint_primary)
        best_acc = acc
    print("Accuracy and best acc are:", acc, best_acc)
    return acc, best_acc


acc = 0
best_acc = 0
print("Start Epoch is:", start_epoch)
for epoch in range(start_epoch, args.end_epoch):
    train(epoch)
    acc, best_acc = test(epoch)
