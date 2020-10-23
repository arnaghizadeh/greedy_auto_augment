from __future__ import division
import numpy as np
import random
import augmentation_transforms as AT
import found_policies as FP

class Original(object):
    def __call__(self,img):
        return  img

class Manual(object):
    def __call__(self,img):
        img = self.func_manual(img)
        return  img

    def func_manual(self, img):
        img = np.array(img)
        img = AT.random_flip(AT.zero_pad_and_crop(img, 4))
        img = AT.cutout_numpy(img)
        return img

###################################################
def func_autoaug(img,selected_policies):
    epoch_policy = selected_policies[np.random.choice(len(selected_policies))]
    img = np.array(img)
    img = AT.apply_policy(epoch_policy, img)
    img = np.array(img)
    img = AT.random_flip(AT.zero_pad_and_crop(img, 4))
    img = AT.cutout_numpy(img)
    return img

class tiny_AutoAug(object):
    def __call__(self,img):
        selected_policies = FP.tiny_AutoAug()
        img = func_autoaug(img,selected_policies)
        return  img

class cifar_AutoAug(object):
    def __call__(self,img):
        selected_policies = FP.cifar_AutoAug()
        img = func_autoaug(img,selected_policies)
        return  img

class svhn_AutoAug(object):
    def __call__(self,img):
        selected_policies = FP.svhn_AutoAug()
        img = func_autoaug(img,selected_policies)
        return  img

###################################################
def func_gautoaug(img, selected_policies):
    alpha = 2
    p1 = 1
    p_list = []
    p_list.append(p1)
    for i in range(2, 16):
        tmp = pow((p1 / i), alpha)
        p_list.append(tmp)

    r = random.uniform(0, 1)

    for gdx in reversed(range(len(selected_policies))):
        if r <= p_list[gdx]:
            gp = selected_policies[gdx]
            img = np.array(img)
            img = AT.apply_policy(gp, img)  # good_policies[20]
            return img

class svhn_GAutoAug(object):
    def __init__(self, network):#it should be either CIFAR10 or CIFAR100
        self.network = network

    def __call__(self,img):
        network = self.network

        if network==0:
            selected_policies = FP.svhn_GAutoAug_DenseNet121()
        elif network==1:
            selected_policies = FP.svhn_GAutoAug_DPN92()
        elif network==2:
            selected_policies = FP.svhn_GAutoAug_GoogLeNet()
        elif network==3:
            selected_policies = FP.svhn_GAutoAug_MobileNet()
        elif network==4:
            selected_policies = FP.svhn_GAutoAug_MobileNetV2()
        elif network==5:
            selected_policies = FP.svhn_GAutoAug_PreActResNet18()
        elif network==6:
            selected_policies = FP.svhn_GAutoAug_ResNet18()
        elif network==7:
            selected_policies = FP.svhn_GAutoAug_ResNeXt29_2x64d()
        elif network==8:
            selected_policies = FP.svhn_GAutoAug_SENet18()
        elif network==9:
            selected_policies = FP.svhn_GAutoAug_ShuffleNetG2(onex=True)
        elif network==10:
            selected_policies = FP.svhn_GAutoAug_ShuffleNetV2(onex=True)
        elif network==11:
            selected_policies = FP.svhn_GAutoAug_VGG(onex=True)
        else:
            print("Network numbers is not correct")

        img = func_gautoaug(img, selected_policies)
        return img

class tiny_GAutoAug(object):
    def __init__(self, network):#it should be either CIFAR10 or CIFAR100
        self.network = network

    def __call__(self,img):
        network = self.network

        if network == 0:
            selected_policies = FP.tiny_GAutoAug_DenseNet121()
        elif network == 1:
            selected_policies = FP.tiny_GAutoAug_DPN92()
        elif network == 2:
            selected_policies = FP.tiny_GAutoAug_GoogLeNet()
        elif network == 3:
            selected_policies = FP.tiny_GAutoAug_MobileNet()
        elif network == 4:
            selected_policies = FP.tiny_GAutoAug_MobileNetV2()
        elif network == 5:
            selected_policies = FP.tiny_GAutoAug_PreActResNet18()
        elif network == 6:
            selected_policies = FP.tiny_GAutoAug_ResNet18()
        elif network == 7:
            selected_policies = FP.tiny_GAutoAug_ResNeXt29_2x64d()
        elif network == 8:
            selected_policies = FP.tiny_GAutoAug_SENet18()
        elif network == 9:
            selected_policies = FP.tiny_GAutoAug_ShuffleNetG2()
        elif network == 10:
            selected_policies = FP.tiny_GAutoAug_ShuffleNetV2()
        elif network == 11:
            selected_policies = FP.tiny_GAutoAug_VGG(onex=True)
        else:
            print("Network numbers is not correct")

        img = func_gautoaug(img, selected_policies)
        return img

class cifar_GAutoAug(object):
    def __init__(self, mode, network):#it should be either CIFAR10 or CIFAR100
        self.mode = mode
        self.network = network

    def __call__(self,img):
        network = self.network
        class_name = self.mode

        if network==0:
            if class_name=="CIFAR10":
                selected_policies = FP.cifar10_GAutoAug_DenseNet121()
            elif class_name=="CIFAR100":
                selected_policies = FP.cifar100_GAutoAug_DenseNet121(onex=True)
            else:
                print("Class name is wrong!!")
        elif network==1:
            if class_name=="CIFAR10":
                selected_policies = FP.cifar10_GAutoAug_DPN92()
            elif class_name=="CIFAR100":
                selected_policies = FP.cifar100_GAutoAug_DPN92(onex=True)
            else:
                print("Class name is wrong!!")
        elif network==2:
            if class_name=="CIFAR10":
                selected_policies = FP.cifar10_GAutoAug_GoogLeNet()
            elif class_name=="CIFAR100":
                selected_policies = FP.cifar100_GAutoAug_GoogLeNet(onex=True)
            else:
                print("Class name is wrong!!")
        elif network==3:
            if class_name=="CIFAR10":
                selected_policies = FP.cifar10_GAutoAug_MobileNet()
            elif class_name=="CIFAR100":
                selected_policies = FP.cifar100_GAutoAug_MobileNet(onex=True)
            else:
                print("Class name is wrong!!")
        elif network==4:
            if class_name=="CIFAR10":
                selected_policies = FP.cifar10_GAutoAug_MobileNetV2()
            elif class_name=="CIFAR100":
                selected_policies = FP.cifar100_GAutoAug_MobileNetV2(onex=True)
            else:
                print("Class name is wrong!!")
        elif network==5:
            if class_name=="CIFAR10":
                selected_policies = FP.cifar10_GAutoAug_PreActResNet18()
            elif class_name=="CIFAR100":
                selected_policies = FP.cifar100_GAutoAug_PreActResNet18(onex=True)
            else:
                print("Class name is wrong!!")
        elif network==6:
            if class_name=="CIFAR10":
                selected_policies = FP.cifar10_GAutoAug_ResNet18()
            elif class_name=="CIFAR100":
                selected_policies = FP.cifar100_GAutoAug_ResNet18(onex=True)
            else:
                print("Class name is wrong!!")
        elif network==7:
            if class_name=="CIFAR10":
                selected_policies = FP.cifar10_GAutoAug_ResNeXt29_2x64d()
            elif class_name=="CIFAR100":
                selected_policies = FP.cifar100_GAutoAug_ResNeXt29_2x64d(onex=True)
            else:
                print("Class name is wrong!!")
        elif network==8:
            if class_name=="CIFAR10":
                selected_policies = FP.cifar10_GAutoAug_SENet18()
            elif class_name=="CIFAR100":
                selected_policies = FP.cifar100_GAutoAug_SENet18(onex=True)
            else:
                print("Class name is wrong!!")
        elif network==9:
            if class_name=="CIFAR10":
                selected_policies = FP.cifar10_GAutoAug_ShuffleNetG2()
            elif class_name=="CIFAR100":
                selected_policies = FP.cifar100_GAutoAug_ShuffleNetG2(onex=True)
            else:
                print("Class name is wrong!!")
        elif network==10:
            if class_name=="CIFAR10":
                selected_policies = FP.cifar10_GAutoAug_ShuffleNetV2()
            elif class_name=="CIFAR100":
                selected_policies = FP.cifar100_GAutoAug_ShuffleNetV2(onex=True)
            else:
                print("Class name is wrong!!")
        elif network==11:
            if class_name=="CIFAR10":
                selected_policies = FP.cifar_GAutoAug_VGG()
            elif class_name=="CIFAR100":
                selected_policies = FP.cifar100_GAutoAug_VGG(onex=True)
            else:
                print("Class name is wrong!!")

        else:
            print("Network numbers is not correct")

        img = func_gautoaug(img, selected_policies)
        return img

