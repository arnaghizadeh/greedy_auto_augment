def tiny_AutoAug():
    p0 = [[('Posterize', 0.4, 8), ('Rotate', 0.6, 9)]]
    p1 = [[('Solarize', 0.6, 5), ('AutoContrast', 0.6, 5)]]
    p2 = [[('Equalize', 0.8, 8), ('Equalize', 0.6, 3)]]
    p3 = [[('Posterize', 0.6, 7), ('Posterize', 0.6, 6)]]
    p4 = [[('Equalize', 0.4, 7), ('Solarize', 0.2, 4)]]
    p5 = [[('Equalize', 0.4, 4), ('Rotate', 0.8, 8)]]
    p6 = [[('Solarize', 0.6, 3), ('Equalize', 0.6, 7)]]
    p7 = [[('Posterize', 0.8, 5), ('Equalize', 1.0, 2)]]
    p8 = [[('Rotate', 0.2, 3), ('Solarize', 0.6, 8)]]
    p9 = [[('Equalize', 0.6, 8), ('Posterize', 0.4, 6)]]
    p10 = [[('Rotate', 0.8, 8), ('Color', 0.4, 0)]]
    p11 = [[('Rotate', 0.4, 9), ('Equalize', 0.6, 2)]]
    p12 = [[('Equalize', 0.0, 7), ('Equalize', 0.8, 8)]]
    p13 = [[('Invert', 0.6, 4), ('Equalize', 1.0, 8)]]
    p14 = [[('Color', 0.6, 4), ('Contrast', 1.0, 8)]]
    p15 = [[('Rotate', 0.8, 8), ('Color', 1.0, 2)]]
    p16 = [[('Color', 0.8, 8), ('Solarize', 0.8, 7)]]
    p17 = [[('Sharpness', 0.4, 7), ('Invert', 0.6, 8)]]
    p18 = [[('ShearX', 0.6, 5), ('Equalize', 1.0, 9)]]
    p19 = [[('Color', 0.4, 0), ('Equalize', 0.6, 3)]]
    p20 = [[('Equalize', 0.4, 7), ('Solarize', 0.2, 4)]]
    p21 = [[('Solarize', 0.6, 5), ('AutoContrast', 0.6, 5)]]
    p22 = [[('Invert', 0.6, 4), ('Equalize', 1.0, 8)]]
    p23 = [[('Color', 0.6, 4), ('Contrast', 1.0, 8)]]
    p24 = [[('Equalize', 0.8, 8), ('Equalize', 0.6, 3)]]
    return p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24


def cifar_AutoAug():
    """AutoAugment policies found on Cifar."""
    exp0_0 = [
        [('Invert', 0.1, 7), ('Contrast', 0.2, 6)],
        [('Rotate', 0.7, 2), ('TranslateX', 0.3, 9)],
        [('Sharpness', 0.8, 1), ('Sharpness', 0.9, 3)],
        [('ShearY', 0.5, 8), ('TranslateY', 0.7, 9)],
        [('AutoContrast', 0.5, 8), ('Equalize', 0.9, 2)]]
    exp0_1 = [
        [('Solarize', 0.4, 5), ('AutoContrast', 0.9, 3)],
        [('TranslateY', 0.9, 9), ('TranslateY', 0.7, 9)],
        [('AutoContrast', 0.9, 2), ('Solarize', 0.8, 3)],
        [('Equalize', 0.8, 8), ('Invert', 0.1, 3)],
        [('TranslateY', 0.7, 9), ('AutoContrast', 0.9, 1)]]
    exp0_2 = [
        [('Solarize', 0.4, 5), ('AutoContrast', 0.0, 2)],
        [('TranslateY', 0.7, 9), ('TranslateY', 0.7, 9)],
        [('AutoContrast', 0.9, 0), ('Solarize', 0.4, 3)],
        [('Equalize', 0.7, 5), ('Invert', 0.1, 3)],
        [('TranslateY', 0.7, 9), ('TranslateY', 0.7, 9)]]
    exp0_3 = [
        [('Solarize', 0.4, 5), ('AutoContrast', 0.9, 1)],
        [('TranslateY', 0.8, 9), ('TranslateY', 0.9, 9)],
        [('AutoContrast', 0.8, 0), ('TranslateY', 0.7, 9)],
        [('TranslateY', 0.2, 7), ('Color', 0.9, 6)],
        [('Equalize', 0.7, 6), ('Color', 0.4, 9)]]
    exp1_0 = [
        [('ShearY', 0.2, 7), ('Posterize', 0.3, 7)],
        [('Color', 0.4, 3), ('Brightness', 0.6, 7)],
        [('Sharpness', 0.3, 9), ('Brightness', 0.7, 9)],
        [('Equalize', 0.6, 5), ('Equalize', 0.5, 1)],
        [('Contrast', 0.6, 7), ('Sharpness', 0.6, 5)]]
    exp1_1 = [
        [('Brightness', 0.3, 7), ('AutoContrast', 0.5, 8)],
        [('AutoContrast', 0.9, 4), ('AutoContrast', 0.5, 6)],
        [('Solarize', 0.3, 5), ('Equalize', 0.6, 5)],
        [('TranslateY', 0.2, 4), ('Sharpness', 0.3, 3)],
        [('Brightness', 0.0, 8), ('Color', 0.8, 8)]]
    exp1_2 = [
        [('Solarize', 0.2, 6), ('Color', 0.8, 6)],
        [('Solarize', 0.2, 6), ('AutoContrast', 0.8, 1)],
        [('Solarize', 0.4, 1), ('Equalize', 0.6, 5)],
        [('Brightness', 0.0, 0), ('Solarize', 0.5, 2)],
        [('AutoContrast', 0.9, 5), ('Brightness', 0.5, 3)]]
    exp1_3 = [
        [('Contrast', 0.7, 5), ('Brightness', 0.0, 2)],
        [('Solarize', 0.2, 8), ('Solarize', 0.1, 5)],
        [('Contrast', 0.5, 1), ('TranslateY', 0.2, 9)],
        [('AutoContrast', 0.6, 5), ('TranslateY', 0.0, 9)],
        [('AutoContrast', 0.9, 4), ('Equalize', 0.8, 4)]]
    exp1_4 = [
        [('Brightness', 0.0, 7), ('Equalize', 0.4, 7)],
        [('Solarize', 0.2, 5), ('Equalize', 0.7, 5)],
        [('Equalize', 0.6, 8), ('Color', 0.6, 2)],
        [('Color', 0.3, 7), ('Color', 0.2, 4)],
        [('AutoContrast', 0.5, 2), ('Solarize', 0.7, 2)]]
    exp1_5 = [
        [('AutoContrast', 0.2, 0), ('Equalize', 0.1, 0)],
        [('ShearY', 0.6, 5), ('Equalize', 0.6, 5)],
        [('Brightness', 0.9, 3), ('AutoContrast', 0.4, 1)],
        [('Equalize', 0.8, 8), ('Equalize', 0.7, 7)],
        [('Equalize', 0.7, 7), ('Solarize', 0.5, 0)]]
    exp1_6 = [
        [('Equalize', 0.8, 4), ('TranslateY', 0.8, 9)],
        [('TranslateY', 0.8, 9), ('TranslateY', 0.6, 9)],
        [('TranslateY', 0.9, 0), ('TranslateY', 0.5, 9)],
        [('AutoContrast', 0.5, 3), ('Solarize', 0.3, 4)],
        [('Solarize', 0.5, 3), ('Equalize', 0.4, 4)]]
    exp2_0 = [
        [('Color', 0.7, 7), ('TranslateX', 0.5, 8)],
        [('Equalize', 0.3, 7), ('AutoContrast', 0.4, 8)],
        [('TranslateY', 0.4, 3), ('Sharpness', 0.2, 6)],
        [('Brightness', 0.9, 6), ('Color', 0.2, 8)],
        [('Solarize', 0.5, 2), ('Invert', 0.0, 3)]]
    exp2_1 = [
        [('AutoContrast', 0.1, 5), ('Brightness', 0.0, 0)],
        [('Cutout', 0.2, 4), ('Equalize', 0.1, 1)],
        [('Equalize', 0.7, 7), ('AutoContrast', 0.6, 4)],
        [('Color', 0.1, 8), ('ShearY', 0.2, 3)],
        [('ShearY', 0.4, 2), ('Rotate', 0.7, 0)]]
    exp2_2 = [
        [('ShearY', 0.1, 3), ('AutoContrast', 0.9, 5)],
        [('TranslateY', 0.3, 6), ('Cutout', 0.3, 3)],
        [('Equalize', 0.5, 0), ('Solarize', 0.6, 6)],
        [('AutoContrast', 0.3, 5), ('Rotate', 0.2, 7)],
        [('Equalize', 0.8, 2), ('Invert', 0.4, 0)]]
    exp2_3 = [
        [('Equalize', 0.9, 5), ('Color', 0.7, 0)],
        [('Equalize', 0.1, 1), ('ShearY', 0.1, 3)],
        [('AutoContrast', 0.7, 3), ('Equalize', 0.7, 0)],
        [('Brightness', 0.5, 1), ('Contrast', 0.1, 7)],
        [('Contrast', 0.1, 4), ('Solarize', 0.6, 5)]]
    exp2_4 = [
        [('Solarize', 0.2, 3), ('ShearX', 0.0, 0)],
        [('TranslateX', 0.3, 0), ('TranslateX', 0.6, 0)],
        [('Equalize', 0.5, 9), ('TranslateY', 0.6, 7)],
        [('ShearX', 0.1, 0), ('Sharpness', 0.5, 1)],
        [('Equalize', 0.8, 6), ('Invert', 0.3, 6)]]
    exp2_5 = [
        [('AutoContrast', 0.3, 9), ('Cutout', 0.5, 3)],
        [('ShearX', 0.4, 4), ('AutoContrast', 0.9, 2)],
        [('ShearX', 0.0, 3), ('Posterize', 0.0, 3)],
        [('Solarize', 0.4, 3), ('Color', 0.2, 4)],
        [('Equalize', 0.1, 4), ('Equalize', 0.7, 6)]]
    exp2_6 = [
        [('Equalize', 0.3, 8), ('AutoContrast', 0.4, 3)],
        [('Solarize', 0.6, 4), ('AutoContrast', 0.7, 6)],
        [('AutoContrast', 0.2, 9), ('Brightness', 0.4, 8)],
        [('Equalize', 0.1, 0), ('Equalize', 0.0, 6)],
        [('Equalize', 0.8, 4), ('Equalize', 0.0, 4)]]
    exp2_7 = [
        [('Equalize', 0.5, 5), ('AutoContrast', 0.1, 2)],
        [('Solarize', 0.5, 5), ('AutoContrast', 0.9, 5)],
        [('AutoContrast', 0.6, 1), ('AutoContrast', 0.7, 8)],
        [('Equalize', 0.2, 0), ('AutoContrast', 0.1, 2)],
        [('Equalize', 0.6, 9), ('Equalize', 0.4, 4)]]

    exp0s = exp0_0 + exp0_1 + exp0_2 + exp0_3
    exp1s = exp1_0 + exp1_1 + exp1_2 + exp1_3 + exp1_4 + exp1_5 + exp1_6
    exp2s = exp2_0 + exp2_1 + exp2_2 + exp2_3 + exp2_4 + exp2_5 + exp2_6 + exp2_7
    ps = exp0s + exp1s + exp2s
    # print(ps)
    return exp0s + exp1s + exp2s


def svhn_AutoAug():
    p0 = [[('ShearX', 0.9, 4), ('Invert', 0.2, 3)]]
    p1 = [[('ShearY', 0.9, 8), ('Invert', 0.7, 5)]]
    p2 = [[('Equalize', 0.6, 5), ('Solarize', 0.6, 6)]]
    p3 = [[('Invert', 0.9, 3), ('Equalize', 0.6, 3)]]
    p4 = [[('Equalize', 0.6, 1), ('Rotate', 0.9, 3)]]
    p5 = [[('ShearX', 0.9, 4), ('AutoContrast', 0.8, 3)]]
    p6 = [[('ShearY', 0.9, 8), ('Invert', 0.4, 5)]]
    p7 = [[('ShearY', 0.9, 5), ('Solarize', 0.2, 6)]]
    p8 = [[('Invert', 0.9, 6), ('AutoContrast', 0.8, 1)]]
    p9 = [[('Equalize', 0.6, 3), ('Rotate', 0.9, 3)]]
    p10 = [[('ShearX', 0.9, 4), ('Solarize', 0.3, 3)]]
    p11 = [[('ShearY', 0.8, 8), ('Invert', 0.7, 4)]]
    p12 = [[('Equalize', 0.9, 5), ('TranslateY', 0.6, 6)]]
    p13 = [[('Invert', 0.9, 4), ('Equalize', 0.6, 7)]]
    p14 = [[('Contrast', 0.3, 3), ('Rotate', 0.8, 4)]]
    p15 = [[('Invert', 0.8, 5), ('TranslateY', 0.0, 2)]]
    p16 = [[('ShearY', 0.7, 6), ('Solarize', 0.4, 8)]]
    p17 = [[('Invert', 0.6, 4), ('Rotate', 0.8, 4)]]
    p18 = [[('ShearY', 0.3, 7), ('TranslateX', 0.9, 3)]]
    p19 = [[('ShearX', 0.1, 6), ('Invert', 0.6, 5)]]
    p20 = [[('Solarize', 0.7, 2), ('TranslateY', 0.6, 7)]]
    p21 = [[('ShearY', 0.8, 4), ('Invert', 0.8, 8)]]
    p22 = [[('ShearX', 0.7, 9), ('TranslateY', 0.8, 3)]]
    p23 = [[('ShearY', 0.8, 5), ('AutoContrast', 0.7, 3)]]
    p24 = [[('ShearX', 0.7, 2), ('Invert', 0.1, 5)]]
    return p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24


def svhn_GAutoAug_DenseNet121():
    p0 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('Brightness', 1, 7)]]
    p1 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('Brightness', 1, 6)]]
    p2 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('ShearX', 1, 4)]]
    p3 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('Brightness', 1, 8)]]
    p4 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('ShearX', 1, 5)]]
    p5 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('Sharpness', 1, 7)]]
    p6 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('Brightness', 1, 5)]]
    p7 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('Sharpness', 1, 6)]]
    p8 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('ShearX', 1, 6)]]
    p9 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('Sharpness', 1, 8)]]
    p10 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('Brightness', 1, 9)]]
    p11 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('Sharpness', 1, 5)]]
    p12 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0)]]
    p13 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('ShearY', 1, 9)]]
    p14 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 1)]]
    p15 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('ShearX', 1, 3)]]
    p16 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 3)]]
    p17 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('Sharpness', 1, 9)]]
    p18 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 2)]]
    p19 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('Brightness', 1, 4)]]
    p20 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('ShearX', 1, 2)]]
    p21 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('ShearX', 1, 7)]]
    p22 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('Sharpness', 1, 4)]]
    p23 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('Sharpness', 1, 0)]]
    p24 = [[('Smooth', 1, 6), ('Smooth', 1, 4), ('Sharpness', 1, 2), ('TranslateX', 1, 0), ('ShearX', 1, 0)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def svhn_GAutoAug_DPN92():
    p0 = [[('ShearY', 1, 4)]]
    p1 = [[('ShearY', 1, 5)]]
    p2 = [[('ShearY', 1, 2)]]
    p3 = [[('ShearY', 1, 5), ('FlipLR', 1, 5)]]
    p4 = [[('ShearY', 1, 5), ('Blur', 1, 2)]]
    p5 = [[('ShearY', 1, 7)]]
    p6 = [[('ShearY', 1, 5), ('FlipLR', 1, 6)]]
    p7 = [[('ShearY', 1, 5), ('Rotate', 1, 9)]]
    p8 = [[('ShearY', 1, 3)]]
    p9 = [[('ShearY', 1, 6)]]
    p10 = [[('ShearY', 1, 2), ('Blur', 1, 3)]]
    p11 = [[('Blur', 1, 8)]]
    p12 = [[('ShearY', 1, 4), ('Cutout', 1, 8)]]
    p13 = [[('ShearY', 1, 4), ('Cutout', 1, 7)]]
    p14 = [[('ShearY', 1, 4), ('Cutout', 1, 6)]]
    p15 = [[('ShearY', 1, 5), ('Rotate', 1, 7)]]
    p16 = [[('ShearY', 1, 4), ('FlipUD', 1, 3)]]
    p17 = [[('ShearY', 1, 4), ('FlipUD', 1, 2)]]
    p18 = [[('ShearY', 1, 4), ('FlipUD', 1, 1)]]
    p19 = [[('ShearY', 1, 5), ('Rotate', 1, 8)]]
    p20 = [[('ShearY', 1, 5), ('Posterize', 1, 0)]]
    p21 = [[('ShearY', 1, 5), ('Posterize', 1, 1)]]
    p22 = [[('Sharpness', 1, 6)]]
    p23 = [[('ShearY', 1, 4), ('TranslateY', 1, 8)]]
    p24 = [[('ShearY', 1, 2), ('Smooth', 1, 8)]]

    augmentations = []
    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def svhn_GAutoAug_GoogLeNet():
    p0 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('Blur', 1, 0)]]
    p1 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('Cutout', 1, 9)]]
    p2 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('ShearX', 1, 0)]]
    p3 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('Sharpness', 1, 9)]]
    p4 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('ShearX', 1, 1)]]
    p5 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('TranslateX', 1, 4)]]
    p6 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('Blur', 1, 1)]]
    p7 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('TranslateX', 1, 5)]]
    p8 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('Sharpness', 1, 7)]]
    p9 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('ShearX', 1, 2)]]
    p10 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('Sharpness', 1, 8)]]
    p11 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('TranslateX', 1, 6)]]
    p12 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('Cutout', 1, 8)]]
    p13 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('Sharpness', 1, 6)]]
    p14 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('TranslateX', 1, 3)]]
    p15 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('ShearX', 1, 3)]]
    p16 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('TranslateX', 1, 2)]]
    p17 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('Sharpness', 1, 5)]]
    p18 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('Blur', 1, 2)]]
    p19 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('TranslateX', 1, 7)]]
    p20 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6)]]
    p21 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('TranslateX', 1, 1)]]
    p22 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 7)]]
    p23 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('Smooth', 1, 8)]]
    p24 = [[('TranslateX', 1, 8), ('ShearX', 1, 8), ('TranslateX', 1, 5), ('Brightness', 1, 6), ('Sharpness', 1, 4)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5
    return augmentations


def svhn_GAutoAug_MobileNet():
    p0 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Brightness', 1, 8)]]
    p1 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Brightness', 1, 7)]]
    p2 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Brightness', 1, 8), ('ShearX', 1, 7)]]
    p3 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Brightness', 1, 9)]]
    p4 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Sharpness', 1, 0)]]
    p5 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Brightness', 1, 8), ('ShearX', 1, 8)]]
    p6 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Brightness', 1, 8), ('ShearX', 1, 6)]]
    p7 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Brightness', 1, 6)]]
    p8 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('ShearY', 1, 7)]]
    p9 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('ShearY', 1, 6)]]
    p10 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Sharpness', 1, 2)]]
    p11 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Brightness', 1, 8), ('FlipLR', 1, 1)]]
    p12 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Sharpness', 1, 1)]]
    p13 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('ShearX', 1, 2)]]
    p14 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('ShearX', 1, 8)]]
    p15 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('ShearX', 1, 7)]]
    p16 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('ShearX', 1, 3)]]
    p17 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Contrast', 1, 9)]]
    p18 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Contrast', 1, 8)]]
    p19 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('ShearX', 1, 1)]]
    p20 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Brightness', 1, 8), ('ShearX', 1, 5)]]
    p21 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('ShearY', 1, 8)]]
    p22 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Brightness', 1, 8), ('Sharpness', 1, 7)]]
    p23 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('Brightness', 1, 5)]]
    p24 = [[('Smooth', 1, 6), ('ShearX', 1, 5), ('Smooth', 1, 2), ('ShearY', 1, 5)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def svhn_GAutoAug_MobileNetV2():
    p0 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 8), ('ShearX', 1, 7)]]
    p1 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 8), ('ShearX', 1, 6)]]
    p2 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 8), ('ShearX', 1, 5)]]
    p3 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 8)]]
    p4 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 9)]]
    p5 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('ShearX', 1, 0)]]
    p6 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 7)]]
    p7 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 8), ('ShearX', 1, 8)]]
    p8 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 8), ('ShearY', 1, 1)]]
    p9 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 5)]]
    p10 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 8)]]
    p11 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('ShearX', 1, 1)]]
    p12 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 4)]]
    p13 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('ShearX', 1, 3)]]
    p14 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 8), ('ShearY', 1, 0)]]
    p15 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 6)]]
    p16 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 8), ('ShearX', 1, 9)]]
    p17 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Brightness', 1, 8)]]
    p18 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 8), ('ShearX', 1, 4)]]
    p19 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 9)]]
    p20 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 3)]]
    p21 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 7)]]
    p22 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('ShearX', 1, 2)]]
    p23 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 8), ('ShearX', 1, 0)]]
    p24 = [[('Smooth', 1, 8), ('Sharpness', 1, 8), ('Sharpness', 1, 8), ('ShearY', 1, 2)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def svhn_GAutoAug_PreActResNet18():
    p0 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('TranslateX', 1, 3)]]
    p1 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('TranslateX', 1, 4)]]
    p2 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('TranslateX', 1, 8)]]
    p3 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('TranslateX', 1, 9)]]
    p4 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('TranslateX', 1, 2)]]
    p5 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('Sharpness', 1, 4)]]
    p6 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('TranslateY', 1, 0)]]
    p7 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('ShearY', 1, 7)]]
    p8 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('TranslateX', 1, 7)]]
    p9 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('Sharpness', 1, 3)]]
    p10 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('ShearY', 1, 8)]]
    p11 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('TranslateX', 1, 5)]]
    p12 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('Cutout', 1, 6)]]
    p13 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6)]]
    p14 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 5)]]
    p15 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('ShearY', 1, 6)]]
    p16 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('TranslateX', 1, 6)]]
    p17 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('Cutout', 1, 5)]]
    p18 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('Cutout', 1, 7)]]
    p19 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('Brightness', 1, 5)]]
    p20 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('ShearY', 1, 9)]]
    p21 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('ShearY', 1, 5)]]
    p22 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('TranslateX', 1, 1)]]
    p23 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('Cutout', 1, 4)]]
    p24 = [[('Smooth', 1, 8), ('ShearX', 1, 7), ('ShearY', 1, 5), ('ShearX', 1, 6), ('Smooth', 1, 9)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def svhn_GAutoAug_ResNet18():
    p0 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('TranslateX', 1, 5)]]
    p1 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('TranslateX', 1, 6)]]
    p2 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('TranslateX', 1, 4)]]
    p3 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('TranslateX', 1, 3)]]
    p4 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('ShearX', 1, 6)]]
    p5 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('ShearX', 1, 5)]]
    p6 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('ShearX', 1, 7)]]
    p7 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('ShearX', 1, 4)]]
    p8 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('TranslateX', 1, 2)]]
    p9 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('TranslateX', 1, 7)]]
    p10 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('ShearX', 1, 3)]]
    p11 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('ShearX', 1, 8)]]
    p12 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('TranslateX', 1, 1)]]
    p13 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('ShearX', 1, 0)]]
    p14 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('ShearX', 1, 9)]]
    p15 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('ShearY', 1, 4)]]
    p16 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('Sharpness', 1, 9)]]
    p17 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('Sharpness', 1, 6)]]
    p18 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('ShearY', 1, 5)]]
    p19 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('Sharpness', 1, 8)]]
    p20 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('ShearX', 1, 2)]]
    p21 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('Sharpness', 1, 5)]]
    p22 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('Sharpness', 1, 4)]]
    p23 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('Sharpness', 1, 7)]]
    p24 = [[('Smooth', 1, 9), ('ShearX', 1, 2), ('ShearY', 1, 5), ('ShearX', 1, 1)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def svhn_GAutoAug_ResNeXt29_2x64d():
    p0 = [[('Brightness', 1, 1), ('ShearY', 1, 0)]]
    p1 = [[('Brightness', 1, 1), ('Sharpness', 1, 3)]]
    p2 = [[('Brightness', 1, 1), ('Sharpness', 1, 3), ('Cutout', 1, 9)]]
    p3 = [[('Brightness', 1, 1), ('Sharpness', 1, 3), ('Cutout', 1, 7)]]
    p4 = [[('Brightness', 1, 1), ('ShearY', 1, 4)]]
    p5 = [[('Brightness', 1, 1), ('Sharpness', 1, 3), ('Cutout', 1, 5)]]
    p6 = [[('Brightness', 1, 1), ('Sharpness', 1, 3), ('Cutout', 1, 9), ('Brightness', 1, 2)]]
    p7 = [[('Brightness', 1, 1), ('Sharpness', 1, 1)]]
    p8 = [[('Brightness', 1, 1), ('Sharpness', 1, 3), ('Cutout', 1, 8)]]
    p9 = [[('Brightness', 1, 1), ('Sharpness', 1, 3), ('Cutout', 1, 6)]]
    p10 = [[('Brightness', 1, 1), ('ShearY', 1, 6)]]
    p11 = [[('Brightness', 1, 1), ('Sharpness', 1, 3), ('Cutout', 1, 9), ('Brightness', 1, 4)]]
    p12 = [[('Brightness', 1, 1), ('ShearY', 1, 5)]]
    p13 = [[('Brightness', 1, 1), ('Sharpness', 1, 3), ('Cutout', 1, 9), ('Color', 1, 5)]]
    p14 = [[('Brightness', 1, 1), ('Sharpness', 1, 3), ('Cutout', 1, 9), ('Brightness', 1, 3)]]
    p15 = [[('Brightness', 1, 1), ('ShearY', 1, 3)]]
    p16 = [[('Brightness', 1, 1), ('Equalize', 1, 5)]]
    p17 = [[('Brightness', 1, 1), ('Sharpness', 1, 3), ('Cutout', 1, 9), ('Brightness', 1, 1)]]
    p18 = [[('Brightness', 1, 1), ('Sharpness', 1, 3), ('Cutout', 1, 9), ('FlipUD', 1, 5)]]
    p19 = [[('Brightness', 1, 1), ('Sharpness', 1, 3), ('Cutout', 1, 9), ('Contrast', 1, 9)]]
    p20 = [[('Brightness', 1, 1), ('Sharpness', 1, 2)]]
    p21 = [[('Brightness', 1, 1), ('Solarize', 1, 6)]]
    p22 = [[('Brightness', 1, 1), ('Equalize', 1, 4)]]
    p23 = [[('Brightness', 1, 1), ('Invert', 1, 0)]]
    p24 = [[('Brightness', 1, 1), ('Sharpness', 1, 3), ('Cutout', 1, 9), ('CropBilinear', 1, 8)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def svhn_GAutoAug_SENet18():
    p0 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('Sharpness', 1, 5)]]
    p1 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('Sharpness', 1, 6)]]
    p2 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('Sharpness', 1, 4)]]
    p3 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('Sharpness', 1, 7)]]
    p4 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('FlipLR', 1, 1)]]
    p5 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('Smooth', 1, 5)]]
    p6 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('ShearX', 1, 2)]]
    p7 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('ShearX', 1, 3)]]
    p8 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('Smooth', 1, 4)]]
    p9 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('TranslateX', 1, 4)]]
    p10 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('ShearX', 1, 4)]]
    p11 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('FlipLR', 1, 0)]]
    p12 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('Sharpness', 1, 3)]]
    p13 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('Sharpness', 1, 8)]]
    p14 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('Smooth', 1, 6)]]
    p15 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8)]]
    p16 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5)]]
    p17 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearY', 1, 3)]]
    p18 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 6)]]
    p19 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('ShearY', 1, 7)]]
    p20 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('Smooth', 1, 8)]]
    p21 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('Smooth', 1, 7)]]
    p22 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('Sharpness', 1, 9)]]
    p23 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 2)]]
    p24 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('ShearX', 1, 5), ('Sharpness', 1, 8), ('Smooth', 1, 3)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def svhn_GAutoAug_ShuffleNetG2():
    p0 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('ShearX', 1, 4)]]
    p1 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('ShearX', 1, 5)]]
    p2 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('TranslateX', 1, 9)]]
    p3 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('Cutout', 1, 8)]]
    p4 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('Cutout', 1, 9)]]
    p5 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('Smooth', 1, 9)]]
    p6 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('TranslateY', 1, 0)]]
    p7 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('Cutout', 1, 7)]]
    p8 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('TranslateX', 1, 8)]]
    p9 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('ShearX', 1, 3)]]
    p10 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('Smooth', 1, 8)]]
    p11 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('TranslateX', 1, 5)]]
    p12 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('Blur', 1, 0)]]
    p13 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('TranslateX', 1, 4)]]
    p14 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('Smooth', 1, 5)]]
    p15 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('TranslateX', 1, 7)]]
    p16 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('TranslateX', 1, 6)]]
    p17 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('Smooth', 1, 7)]]
    p18 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('TranslateY', 1, 1)]]
    p19 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('ShearX', 1, 6)]]
    p20 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('Sharpness', 1, 1)]]
    p21 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('Cutout', 1, 6)]]
    p22 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('Contrast', 1, 1)]]
    p23 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('Smooth', 1, 4)]]
    p24 = [[('Cutout', 1, 6), ('Blur', 1, 2), ('TranslateX', 1, 5), ('TranslateY', 1, 3), ('TranslateX', 1, 3)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def svhn_GAutoAug_ShuffleNetV2():
    p0 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Blur', 1, 4)]]
    p1 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Blur', 1, 5)]]
    p2 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Blur', 1, 3)]]
    p3 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 5)]]
    p4 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9)]]
    p5 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 4)]]
    p6 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Blur', 1, 6)]]
    p7 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Blur', 1, 2)]]
    p8 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 6)]]
    p9 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 7)]]
    p10 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 8)]]
    p11 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 3)]]
    p12 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 2)]]
    p13 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Blur', 1, 7)]]
    p14 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Blur', 1, 1)]]
    p15 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 1)]]
    p16 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Blur', 1, 8)]]
    p17 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 0)]]
    p18 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Blur', 1, 9)]]
    p19 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('ShearX', 1, 9)]]
    p20 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Cutout', 1, 9)]]
    p21 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('ShearY', 1, 0)]]
    p22 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('ShearX', 1, 3)]]
    p23 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Blur', 1, 0)]]
    p24 = [[('AutoContrast', 1, 1), ('Smooth', 1, 9), ('Smooth', 1, 9), ('Smooth', 1, 9), ('ShearX', 1, 8)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def svhn_GAutoAug_VGG():
    p0 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('ShearX', 1, 4)]]
    p1 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Brightness', 1, 9)]]
    p2 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Sharpness', 1, 0)]]
    p3 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('ShearX', 1, 3)]]
    p4 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Sharpness', 1, 1)]]
    p5 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('ShearX', 1, 5)]]
    p6 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Brightness', 1, 8)]]
    p7 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Sharpness', 1, 2)]]
    p8 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Blur', 1, 0)]]
    p9 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Blur', 1, 1)]]
    p10 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Cutout', 1, 9)]]
    p11 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Sharpness', 1, 4)]]
    p12 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Sharpness', 1, 3)]]
    p13 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Sharpness', 1, 5)]]
    p14 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('ShearX', 1, 2)]]
    p15 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Cutout', 1, 8)]]
    p16 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Sharpness', 1, 6)]]
    p17 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('TranslateX', 1, 5)]]
    p18 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Sharpness', 1, 7)]]
    p19 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('ShearX', 1, 1)]]
    p20 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Brightness', 1, 7)]]
    p21 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('TranslateX', 1, 6)]]
    p22 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Cutout', 1, 7)]]
    p23 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('Sharpness', 1, 8)]]
    p24 = [[('Smooth', 1, 8), ('Smooth', 1, 9), ('ShearX', 1, 0), ('Sharpness', 1, 5), ('ShearX', 1, 6)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def tiny_GAutoAug_DenseNet121():
    p0 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Sharpness', 1, 7)]]
    p1 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Sharpness', 1, 8)]]
    p2 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Sharpness', 1, 6)]]
    p3 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Sharpness', 1, 5)]]
    p4 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Smooth', 1, 6)]]
    p5 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Smooth', 1, 9)]]
    p6 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Smooth', 1, 7)]]
    p7 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Smooth', 1, 8)]]
    p8 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Sharpness', 1, 9)]]
    p9 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Smooth', 1, 5)]]
    p10 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Smooth', 1, 0)]]
    p11 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Sharpness', 1, 3)]]
    p12 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Sharpness', 1, 4)]]
    p13 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Smooth', 1, 4)]]
    p14 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Blur', 1, 8)]]
    p15 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Blur', 1, 9)]]
    p16 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('FlipUD', 1, 5)]]
    p17 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Blur', 1, 7)]]
    p18 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Smooth', 1, 3)]]
    p19 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Smooth', 1, 1)]]
    p20 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Sharpness', 1, 2)]]
    p21 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('FlipUD', 1, 2)]]
    p22 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('ShearX', 1, 0)]]
    p23 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('Smooth', 1, 2)]]
    p24 = [[('Blur', 1, 9), ('Blur', 1, 6), ('Smooth', 1, 1), ('Sharpness', 1, 9), ('FlipLR', 1, 1)]]
    augmentations = []
    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def tiny_GAutoAug_DPN92():
    p0 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Smooth', 1, 9)]]
    p1 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Smooth', 1, 8)]]
    p2 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Smooth', 1, 6)]]
    p3 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Smooth', 1, 7)]]
    p4 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Smooth', 1, 1)]]
    p5 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Smooth', 1, 5)]]
    p6 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Smooth', 1, 4)]]
    p7 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('AutoContrast', 1, 7)]]
    p8 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('AutoContrast', 1, 6)]]
    p9 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Smooth', 1, 0)]]
    p10 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Smooth', 1, 3)]]
    p11 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('AutoContrast', 1, 9)]]
    p12 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('AutoContrast', 1, 5)]]
    p13 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Blur', 1, 9)]]
    p14 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Blur', 1, 7)]]
    p15 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Smooth', 1, 2)]]
    p16 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Equalize', 1, 0)]]
    p17 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Blur', 1, 8)]]
    p18 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Blur', 1, 5)]]
    p19 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('AutoContrast', 1, 8)]]
    p20 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('AutoContrast', 1, 4)]]
    p21 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Blur', 1, 3)]]
    p22 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Blur', 1, 6)]]
    p23 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('AutoContrast', 1, 3)]]
    p24 = [[('Sharpness', 1, 3), ('Smooth', 1, 4), ('Blur', 1, 5), ('Cutout', 1, 9), ('Blur', 1, 1)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def tiny_GAutoAug_GoogLeNet():
    p0 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Blur', 1, 8)]]
    p1 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Blur', 1, 0)]]
    p2 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Blur', 1, 9)]]
    p3 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Cutout', 1, 6)]]
    p4 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2)]]
    p5 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Cutout', 1, 5)]]
    p6 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Cutout', 1, 9)]]
    p7 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Blur', 1, 1)]]
    p8 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Blur', 1, 2)]]
    p9 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Blur', 1, 7)]]
    p10 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Cutout', 1, 4)]]
    p11 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Cutout', 1, 3)]]
    p12 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 0)]]
    p13 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Blur', 1, 3)]]
    p14 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 1)]]
    p15 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Cutout', 1, 7)]]
    p16 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Blur', 1, 6)]]
    p17 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Blur', 1, 4)]]
    p18 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Cutout', 1, 8)]]
    p19 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Smooth', 1, 0)]]
    p20 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('Blur', 1, 5)]]
    p21 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearX', 1, 9)]]
    p22 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('ShearY', 1, 8)]]
    p23 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('ShearY', 1, 2), ('ShearY', 1, 7)]]
    p24 = [[('Cutout', 1, 8), ('ShearY', 1, 8), ('Smooth', 1, 6), ('TranslateX', 1, 4)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def tiny_GAutoAug_MobileNet():
    p0 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('FlipUD', 1, 3), ('Smooth', 1, 9)]]
    p1 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('FlipUD', 1, 3), ('ShearY', 1, 8)]]
    p2 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('FlipUD', 1, 3), ('ShearY', 1, 9)]]
    p3 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('FlipUD', 1, 3), ('FlipUD', 1, 0)]]
    p4 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('FlipUD', 1, 3)]]
    p5 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('Blur', 1, 2)]]
    p6 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('Blur', 1, 4)]]
    p7 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('AutoContrast', 1, 4)]]
    p8 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('FlipUD', 1, 3), ('Smooth', 1, 8)]]
    p9 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('Blur', 1, 1)]]
    p10 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('FlipUD', 1, 3), ('FlipLR', 1, 9)]]
    p11 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('TranslateX', 1, 1)]]
    p12 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('FlipUD', 1, 2)]]
    p13 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('FlipUD', 1, 3), ('ShearY', 1, 7)]]
    p14 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('AutoContrast', 1, 5)]]
    p15 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('FlipUD', 1, 3), ('ShearY', 1, 6)]]
    p16 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('Blur', 1, 3)]]
    p17 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('FlipUD', 1, 1)]]
    p18 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('FlipUD', 1, 3), ('TranslateX', 1, 1)]]
    p19 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('AutoContrast', 1, 3)]]
    p20 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('FlipUD', 1, 3), ('ShearY', 1, 5)]]
    p21 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8)]]
    p22 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('FlipUD', 1, 4)]]
    p23 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('Blur', 1, 0)]]
    p24 = [[('Smooth', 1, 1), ('TranslateY', 1, 8), ('TranslateX', 1, 8), ('FlipUD', 1, 3), ('Sharpness', 1, 7)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def tiny_GAutoAug_MobileNetV2():
    p0 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('Sharpness', 1, 8)]]
    p1 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('Sharpness', 1, 9)]]
    p2 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('Sharpness', 1, 7)]]
    p3 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('Sharpness', 1, 6)]]
    p4 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('FlipUD', 1, 8)]]
    p5 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('ShearX', 1, 0)]]
    p6 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('Sharpness', 1, 5)]]
    p7 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('FlipUD', 1, 9)]]
    p8 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('FlipUD', 1, 7)]]
    p9 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('Sharpness', 1, 3)]]
    p10 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('AutoContrast', 1, 0)]]
    p11 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('Sharpness', 1, 4)]]
    p12 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('FlipUD', 1, 6)]]
    p13 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('Sharpness', 1, 0)]]
    p14 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('FlipUD', 1, 2)]]
    p15 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('FlipUD', 1, 5)]]
    p16 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('FlipUD', 1, 0)]]
    p17 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('FlipUD', 1, 4)]]
    p18 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('Sharpness', 1, 2)]]
    p19 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('FlipLR', 1, 9)]]
    p20 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('FlipUD', 1, 1)]]
    p21 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('FlipUD', 1, 3)]]
    p22 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8)]]
    p23 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('AutoContrast', 1, 1)]]
    p24 = [[('Smooth', 1, 9), ('Sharpness', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 8), ('Sharpness', 1, 1)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def tiny_GAutoAug_PreActResNet18():
    p0 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('FlipLR', 1, 2)]]
    p1 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('Cutout', 1, 3)]]
    p2 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('Cutout', 1, 7)]]
    p3 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('Cutout', 1, 8)]]
    p4 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('Smooth', 1, 9)]]
    p5 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('Cutout', 1, 6)]]
    p6 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('ShearY', 1, 5)]]
    p7 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('Smooth', 1, 0)]]
    p8 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('FlipLR', 1, 3)]]
    p9 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5)]]
    p10 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('Cutout', 1, 5)]]
    p11 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('ShearY', 1, 6)]]
    p12 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('Cutout', 1, 2)]]
    p13 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('Cutout', 1, 4)]]
    p14 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('FlipLR', 1, 4)]]
    p15 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('FlipLR', 1, 6)]]
    p16 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('Smooth', 1, 8)]]
    p17 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('Blur', 1, 1)]]
    p18 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 6)]]
    p19 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('ShearY', 1, 7)]]
    p20 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('FlipLR', 1, 8)]]
    p21 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('ShearY', 1, 8)]]
    p22 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('Smooth', 1, 7)]]
    p23 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('Sharpness', 1, 7)]]
    p24 = [[('Blur', 1, 6), ('Smooth', 1, 6), ('Blur', 1, 9), ('Smooth', 1, 5), ('TranslateX', 1, 0)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def tiny_GAutoAug_ResNet18():
    p0 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 6)]]
    p1 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 5)]]
    p2 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 4)]]
    p3 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 7)]]
    p4 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 6), ('Cutout', 1, 2)]]
    p5 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 6), ('Cutout', 1, 3)]]
    p6 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1)]]
    p7 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 8)]]
    p8 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Smooth', 1, 0)]]
    p9 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 6), ('TranslateX', 1, 4)]]
    p10 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Smooth', 1, 1)]]
    p11 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 6), ('Cutout', 1, 1)]]
    p12 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 6), ('TranslateY', 1, 7)]]
    p13 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 6), ('AutoContrast', 1, 4)]]
    p14 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 6), ('Cutout', 1, 4)]]
    p15 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 0)]]
    p16 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 3)]]
    p17 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Smooth', 1, 2)]]
    p18 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 6), ('AutoContrast', 1, 5)]]
    p19 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 2)]]
    p20 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 6), ('AutoContrast', 1, 6)]]
    p21 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 6), ('Sharpness', 1, 9)]]
    p22 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 6), ('TranslateX', 1, 5)]]
    p23 = [[('Cutout', 1, 9), ('Equalize', 1, 0), ('FlipLR', 1, 1), ('Blur', 1, 6), ('AutoContrast', 1, 7)]]
    p24 = [[('Cutout', 1, 9), ('Equalize', 1, 0)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def tiny_GAutoAug_ResNeXt29_2x64d():
    p0 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('ShearX', 1, 0)]]
    p1 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('Equalize', 1, 2)]]
    p2 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('FlipUD', 1, 0)]]
    p3 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('Equalize', 1, 3)]]
    p4 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('FlipLR', 1, 9)]]
    p5 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('Sharpness', 1, 9)]]
    p6 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('Equalize', 1, 1)]]
    p7 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('Equalize', 1, 4)]]
    p8 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('Equalize', 1, 0)]]
    p9 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('FlipUD', 1, 1)]]
    p10 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('Smooth', 1, 5)]]
    p11 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('Smooth', 1, 6)]]
    p12 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('ShearX', 1, 1)]]
    p13 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('Sharpness', 1, 8)]]
    p14 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('FlipUD', 1, 2)]]
    p15 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('Sharpness', 1, 7)]]
    p16 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('Smooth', 1, 7)]]
    p17 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('ShearX', 1, 2)]]
    p18 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('AutoContrast', 1, 9)]]
    p19 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('FlipLR', 1, 8)]]
    p20 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('Smooth', 1, 3)]]
    p21 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('Smooth', 1, 8)]]
    p22 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('Cutout', 1, 2)]]
    p23 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('FlipUD', 1, 3)]]
    p24 = [[('Blur', 1, 7), ('Cutout', 1, 7), ('Smooth', 1, 9), ('Cutout', 1, 9), ('Smooth', 1, 4)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def tiny_GAutoAug_SENet18():
    p0 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Sharpness', 1, 5)]]
    p1 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Sharpness', 1, 6)]]
    p2 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Sharpness', 1, 7)]]
    p3 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Sharpness', 1, 4)]]
    p4 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Sharpness', 1, 8)]]
    p5 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('FlipUD', 1, 3)]]
    p6 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('FlipUD', 1, 2)]]
    p7 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Sharpness', 1, 3)]]
    p8 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Smooth', 1, 9)]]
    p9 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Sharpness', 1, 9)]]
    p10 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Blur', 1, 2)]]
    p11 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('ShearX', 1, 0)]]
    p12 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('FlipUD', 1, 4)]]
    p13 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('ShearX', 1, 1)]]
    p14 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('ShearX', 1, 2)]]
    p15 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Blur', 1, 1)]]
    p16 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Smooth', 1, 6)]]
    p17 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Sharpness', 1, 2)]]
    p18 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('FlipUD', 1, 1)]]
    p19 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Smooth', 1, 8)]]
    p20 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('ShearX', 1, 4)]]
    p21 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Blur', 1, 3)]]
    p22 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Smooth', 1, 7)]]
    p23 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Blur', 1, 4)]]
    p24 = [[('Blur', 1, 6), ('Cutout', 1, 4), ('Sharpness', 1, 6), ('FlipUD', 1, 9), ('Blur', 1, 0)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def tiny_GAutoAug_ShuffleNetG2():
    p0 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('Sharpness', 1, 3)]]
    p1 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('Sharpness', 1, 4)]]
    p2 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('Sharpness', 1, 2)]]
    p3 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('Sharpness', 1, 6)]]
    p4 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('Sharpness', 1, 5)]]
    p5 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('Sharpness', 1, 1)]]
    p6 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('Sharpness', 1, 7)]]
    p7 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('Sharpness', 1, 8)]]
    p8 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('Sharpness', 1, 9)]]
    p9 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('Sharpness', 1, 0)]]
    p10 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('FlipLR', 1, 1)]]
    p11 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('FlipLR', 1, 3)]]
    p12 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('FlipLR', 1, 0)]]
    p13 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('FlipLR', 1, 2)]]
    p14 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('FlipLR', 1, 7)]]
    p15 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('Smooth', 1, 9)]]
    p16 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('FlipLR', 1, 6)]]
    p17 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('FlipLR', 1, 4)]]
    p18 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('FlipLR', 1, 5)]]
    p19 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('FlipLR', 1, 8)]]
    p20 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('Smooth', 1, 4)]]
    p21 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('Brightness', 1, 9)]]
    p22 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('Smooth', 1, 3)]]
    p23 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('FlipUD', 1, 6)]]
    p24 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Smooth', 1, 2), ('Smooth', 1, 9), ('FlipUD', 1, 7)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def tiny_GAutoAug_ShuffleNetV2():
    p0 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Color', 1, 8)]]
    p1 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('CropBilinear', 1, 3)]]
    p2 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Color', 1, 8), ('Equalize', 1, 7)]]
    p3 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Contrast', 1, 2)]]
    p4 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Contrast', 1, 1)]]
    p5 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Contrast', 1, 0)]]
    p6 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Color', 1, 9)]]
    p7 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Solarize', 1, 3)]]
    p8 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Solarize', 1, 8)]]
    p9 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Color', 1, 8), ('Brightness', 1, 6)]]
    p10 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Color', 1, 8), ('Brightness', 1, 0)]]
    p11 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Color', 1, 8), ('Equalize', 1, 5)]]
    p12 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Contrast', 1, 3)]]
    p13 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Color', 1, 2)]]
    p14 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Color', 1, 6)]]
    p15 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Color', 1, 5)]]
    p16 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('CropBilinear', 1, 2)]]
    p17 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Color', 1, 8), ('Equalize', 1, 6)]]
    p18 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Color', 1, 8), ('Contrast', 1, 7)]]
    p19 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Solarize', 1, 5)]]
    p20 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Color', 1, 8), ('Contrast', 1, 9)]]
    p21 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Color', 1, 7)]]
    p22 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Contrast', 1, 4)]]
    p23 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Solarize', 1, 7)]]
    p24 = [[('AutoContrast', 1, 8), ('FlipUD', 1, 9), ('Color', 1, 7), ('Color', 1, 1)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def tiny_GAutoAug_VGG():
    p0 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Smooth', 1, 9)]]
    p1 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Smooth', 1, 8)]]
    p2 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Smooth', 1, 0)]]
    p3 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Blur', 1, 9)]]
    p4 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Smooth', 1, 1)]]
    p5 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Blur', 1, 8)]]
    p6 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Smooth', 1, 7)]]
    p7 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Smooth', 1, 2)]]
    p8 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Blur', 1, 7)]]
    p9 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Smooth', 1, 3)]]
    p10 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Smooth', 1, 6)]]
    p11 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Blur', 1, 6)]]
    p12 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Blur', 1, 0)]]
    p13 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Cutout', 1, 8)]]
    p14 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Blur', 1, 5)]]
    p15 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Cutout', 1, 9)]]
    p16 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Smooth', 1, 5)]]
    p17 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Sharpness', 1, 9)]]
    p18 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('AutoContrast', 1, 1)]]
    p19 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Blur', 1, 4)]]
    p20 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Sharpness', 1, 8)]]
    p21 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Smooth', 1, 4)]]
    p22 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Blur', 1, 3)]]
    p23 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Blur', 1, 1)]]
    p24 = [[('Blur', 1, 2), ('Smooth', 1, 6), ('Blur', 1, 4), ('FlipLR', 1, 6), ('Blur', 1, 2)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar10_GAutoAug_DenseNet121():
    p0 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('Blur', 1, 0)]]
    p1 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('Cutout', 1, 9)]]
    p2 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('ShearY', 1, 9)]]
    p3 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('TranslateX', 1, 0)]]
    p4 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('Brightness', 1, 7)]]
    p5 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('Brightness', 1, 6)]]
    p6 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('ShearY', 1, 8)]]
    p7 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('AutoContrast', 1, 7)]]
    p8 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('TranslateX', 1, 2)]]
    p9 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('Brightness', 1, 4)]]
    p10 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('Brightness', 1, 3)]]
    p11 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('TranslateX', 1, 1)]]
    p12 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('AutoContrast', 1, 6)]]
    p13 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('AutoContrast', 1, 8)]]
    p14 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('Cutout', 1, 0)]]
    p15 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('TranslateX', 1, 3)]]
    p16 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('Brightness', 1, 5)]]
    p17 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('Cutout', 1, 8)]]
    p18 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('ShearY', 1, 7)]]
    p19 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('Brightness', 1, 2)]]
    p20 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('Blur', 1, 1)]]
    p21 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('AutoContrast', 1, 5)]]
    p22 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('TranslateY', 1, 9)]]
    p23 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7)]]
    p24 = [[('Smooth', 1, 6), ('TranslateX', 1, 4), ('Brightness', 1, 7), ('AutoContrast', 1, 9)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar10_GAutoAug_DPN92():
    p0 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('AutoContrast', 1, 8)]]
    p1 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('Cutout', 1, 4)]]
    p2 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('AutoContrast', 1, 7)]]
    p3 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('Cutout', 1, 3)]]
    p4 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('AutoContrast', 1, 6)]]
    p5 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 4)]]
    p6 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('AutoContrast', 1, 9)]]
    p7 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5)]]
    p8 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('Cutout', 1, 5)]]
    p9 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('AutoContrast', 1, 5)]]
    p10 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 6)]]
    p11 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('Smooth', 1, 2)]]
    p12 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('Cutout', 1, 2)]]
    p13 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 3)]]
    p14 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 4), ('Blur', 1, 4)]]
    p15 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 2)]]
    p16 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('Smooth', 1, 3)]]
    p17 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('Equalize', 1, 0)]]
    p18 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('ShearX', 1, 6)]]
    p19 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('ShearX', 1, 7)]]
    p20 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('Blur', 1, 0)]]
    p21 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 4), ('Blur', 1, 3)]]
    p22 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('ShearX', 1, 8)]]
    p23 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 5), ('Smooth', 1, 6)]]
    p24 = [[('Blur', 1, 9), ('FlipUD', 1, 3), ('AutoContrast', 1, 4), ('Blur', 1, 1)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar10_GAutoAug_GoogLeNet():
    p0 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('Blur', 1, 4)]]
    p1 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('TranslateX', 1, 1)]]
    p2 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('TranslateX', 1, 2)]]
    p3 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('TranslateX', 1, 3)]]
    p4 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('Blur', 1, 3)]]
    p5 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('Blur', 1, 5)]]
    p6 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('ShearY', 1, 6)]]
    p7 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('ShearY', 1, 5)]]
    p8 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8)]]
    p9 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('ShearX', 1, 5)]]
    p10 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('ShearX', 1, 6)]]
    p11 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('TranslateX', 1, 4)]]
    p12 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('Blur', 1, 0)]]
    p13 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('Cutout', 1, 9)]]
    p14 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('Blur', 1, 0)]]
    p15 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('Cutout', 1, 8)]]
    p16 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('ShearX', 1, 4)]]
    p17 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateY', 1, 9)]]
    p18 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 3)]]
    p19 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('ShearY', 1, 4)]]
    p20 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('Blur', 1, 2)]]
    p21 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('TranslateX', 1, 0)]]
    p22 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('ShearY', 1, 3)]]
    p23 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('FlipUD', 1, 0)]]
    p24 = [[('TranslateX', 1, 6), ('TranslateY', 1, 1), ('TranslateX', 1, 8), ('ShearY', 1, 2)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar10_GAutoAugar10_MobileNet():
    p0 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7)]]
    p1 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('FlipUD', 1, 2)]]
    p2 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 8)]]
    p3 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('FlipUD', 1, 1)]]
    p4 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 5)]]
    p5 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 6)]]
    p6 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 9)]]
    p7 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('ShearY', 1, 2)]]
    p8 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('FlipUD', 1, 0)]]
    p9 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 3)]]
    p10 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 4)]]
    p11 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('ShearX', 1, 1)]]
    p12 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('ShearY', 1, 9)]]
    p13 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('ShearX', 1, 5)]]
    p14 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('FlipUD', 1, 3)]]
    p15 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 2)]]
    p16 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('ShearX', 1, 4)]]
    p17 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 1)]]
    p18 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('ShearY', 1, 1)]]
    p19 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('ShearX', 1, 6)]]
    p20 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('FlipLR', 1, 9)]]
    p21 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('ShearX', 1, 3)]]
    p22 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearY', 1, 0)]]
    p23 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 0)]]
    p24 = [[('Cutout', 1, 7), ('ShearY', 1, 2), ('ShearX', 1, 3)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar10_GAutoAug_MobileNetV2():
    p0 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('ShearY', 1, 4)]]
    p1 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('ShearY', 1, 3)]]
    p2 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('TranslateX', 1, 1)]]
    p3 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('ShearY', 1, 2)]]
    p4 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('TranslateX', 1, 2)]]
    p5 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('TranslateX', 1, 3)]]
    p6 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('ShearY', 1, 5)]]
    p7 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('TranslateY', 1, 3)]]
    p8 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('TranslateX', 1, 0)]]
    p9 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('TranslateY', 1, 1)]]
    p10 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('ShearX', 1, 2)]]
    p11 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('ShearY', 1, 6)]]
    p12 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('TranslateY', 1, 2)]]
    p13 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('ShearX', 1, 0)]]
    p14 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('ShearY', 1, 7)]]
    p15 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('ShearX', 1, 1)]]
    p16 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('TranslateY', 1, 6)]]
    p17 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('Brightness', 1, 6)]]
    p18 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('TranslateY', 1, 4)]]
    p19 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('ShearY', 1, 1)]]
    p20 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('ShearY', 1, 9)]]
    p21 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('TranslateY', 1, 5)]]
    p22 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('TranslateY', 1, 7)]]
    p23 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('TranslateY', 1, 0)]]
    p24 = [[('Smooth', 1, 9), ('ShearX', 1, 6), ('ShearY', 1, 4), ('Cutout', 1, 0), ('Brightness', 1, 5)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar10_GAutoAug_PreActResNet18():
    p0 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateX', 1, 7)]]
    p1 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateX', 1, 6)]]
    p2 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateX', 1, 5)]]
    p3 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateX', 1, 3)]]
    p4 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateX', 1, 4)]]
    p5 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateX', 1, 8)]]
    p6 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateY', 1, 5)]]
    p7 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateX', 1, 1)]]
    p8 = [[('Blur', 1, 1), ('Cutout', 1, 6)]]
    p9 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateY', 1, 4)]]
    p10 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateX', 1, 2)]]
    p11 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4)]]
    p12 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateX', 1, 9)]]
    p13 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateY', 1, 7)]]
    p14 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateY', 1, 6)]]
    p15 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateX', 1, 0)]]
    p16 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateY', 1, 3)]]
    p17 = [[('Blur', 1, 1), ('Cutout', 1, 7)]]
    p18 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 5)]]
    p19 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateY', 1, 1)]]
    p20 = [[('Blur', 1, 1), ('Cutout', 1, 5)]]
    p21 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateY', 1, 0)]]
    p22 = [[('Blur', 1, 1), ('Cutout', 1, 6), ('TranslateY', 1, 8)]]
    p23 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('TranslateY', 1, 2)]]
    p24 = [[('Blur', 1, 1), ('Cutout', 1, 7), ('TranslateX', 1, 4), ('ShearY', 1, 9)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar10_GAutoAug_ResNet18():
    p0 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Blur', 1, 0)]]
    p1 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Blur', 1, 1)]]
    p2 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Cutout', 1, 9)]]
    p3 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Cutout', 1, 8)]]
    p4 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Blur', 1, 2)]]
    p5 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('TranslateX', 1, 3)]]
    p6 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Blur', 1, 3)]]
    p7 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Blur', 1, 5)]]
    p8 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Contrast', 1, 7)]]
    p9 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Contrast', 1, 8)]]
    p10 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('TranslateX', 1, 2)]]
    p11 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7)]]
    p12 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Blur', 1, 4)]]
    p13 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('TranslateY', 1, 8)]]
    p14 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('ShearY', 1, 6)]]
    p15 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('TranslateY', 1, 9)]]
    p16 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Sharpness', 1, 6)]]
    p17 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('FlipLR', 1, 1)]]
    p18 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Sharpness', 1, 7)]]
    p19 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Blur', 1, 6)]]
    p20 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('TranslateY', 1, 7)]]
    p21 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('ShearY', 1, 5)]]
    p22 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Cutout', 1, 0)]]
    p23 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Sharpness', 1, 1)]]
    p24 = [[('ShearY', 1, 7), ('Cutout', 1, 5), ('TranslateX', 1, 0), ('TranslateY', 1, 7), ('Sharpness', 1, 0)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint

    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5
    return augmentations


def cifar10_GAutoAug_ResNeXt29_2x64d():
    p0 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('TranslateX', 1, 4)]]
    p1 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('TranslateX', 1, 5)]]
    p2 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('TranslateX', 1, 3)]]
    p3 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('TranslateY', 1, 1)]]
    p4 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('TranslateX', 1, 0)]]
    p5 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('TranslateX', 1, 6)]]
    p6 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('TranslateY', 1, 0)]]
    p7 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('TranslateX', 1, 2)]]
    p8 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('ShearY', 1, 9)]]
    p9 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('ShearY', 1, 8)]]
    p10 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('TranslateX', 1, 1)]]
    p11 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('TranslateX', 1, 7)]]
    p12 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('Blur', 1, 2)]]
    p13 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('TranslateX', 1, 8)]]
    p14 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('TranslateY', 1, 2)]]
    p15 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('Blur', 1, 3)]]
    p16 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('TranslateX', 1, 9)]]
    p17 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('TranslateY', 1, 3)]]
    p18 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('TranslateY', 1, 4)]]
    p19 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('ShearY', 1, 7)]]
    p20 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3)]]
    p21 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('FlipUD', 1, 7)]]
    p22 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 4)]]
    p23 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('Blur', 1, 1)]]
    p24 = [[('TranslateX', 1, 5), ('TranslateX', 1, 1), ('Cutout', 1, 6), ('TranslateX', 1, 3), ('Sharpness', 1, 6)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar10_GAutoAug_SENet18():
    p0 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('TranslateX', 1, 7), ('Cutout', 1, 2)]]
    p1 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('TranslateX', 1, 7), ('Cutout', 1, 3)]]
    p2 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('TranslateX', 1, 7), ('ShearX', 1, 6)]]
    p3 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('TranslateX', 1, 7), ('Contrast', 1, 9)]]
    p4 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('TranslateX', 1, 7)]]
    p5 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('TranslateX', 1, 7), ('Brightness', 1, 0)]]
    p6 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('TranslateX', 1, 7), ('Contrast', 1, 8)]]
    p7 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('TranslateX', 1, 7), ('ShearX', 1, 7)]]
    p8 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8)]]
    p9 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('TranslateX', 1, 6)]]
    p10 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('TranslateX', 1, 7), ('Cutout', 1, 1)]]
    p11 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('TranslateX', 1, 7)]]
    p12 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 9)]]
    p13 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('Sharpness', 1, 9)]]
    p14 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Blur', 1, 0)]]
    p15 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('TranslateX', 1, 0)]]
    p16 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('ShearY', 1, 7)]]
    p17 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('Sharpness', 1, 8)]]
    p18 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('TranslateX', 1, 7), ('Cutout', 1, 4)]]
    p19 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('TranslateX', 1, 7), ('Brightness', 1, 1)]]
    p20 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('TranslateX', 1, 8)]]
    p21 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 7)]]
    p22 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('TranslateX', 1, 7), ('TranslateX', 1, 9)]]
    p23 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('TranslateX', 1, 7), ('TranslateY', 1, 2)]]
    p24 = [[('TranslateY', 1, 2), ('TranslateX', 1, 3), ('Smooth', 1, 8), ('TranslateX', 1, 7), ('TranslateY', 1, 0)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar10_GAutoAug_ShuffleNetG2():
    p0 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('ShearY', 1, 3)]]
    p1 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('ShearY', 1, 2)]]
    p2 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('ShearY', 1, 4)]]
    p3 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('ShearY', 1, 5)]]
    p4 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('ShearY', 1, 7)]]
    p5 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('ShearY', 1, 1)]]
    p6 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('ShearY', 1, 6)]]
    p7 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('ShearY', 1, 8)]]
    p8 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('Solarize', 1, 4)]]
    p9 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('Solarize', 1, 3)]]
    p10 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('Solarize', 1, 0)]]
    p11 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('Solarize', 1, 5)]]
    p12 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('Cutout', 1, 2)]]
    p13 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4)]]
    p14 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('ShearY', 1, 0)]]
    p15 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('Cutout', 1, 4)]]
    p16 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('Cutout', 1, 5)]]
    p17 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('Solarize', 1, 2)]]
    p18 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('Solarize', 1, 1)]]
    p19 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('CropBilinear', 1, 9)]]
    p20 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('Cutout', 1, 1)]]
    p21 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('Cutout', 1, 3)]]
    p22 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('Cutout', 1, 6)]]
    p23 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 3)]]
    p24 = [[('Blur', 1, 3), ('TranslateY', 1, 8), ('TranslateX', 1, 0), ('Sharpness', 1, 4), ('ShearY', 1, 9)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar10_GAutoAug_ShuffleNetV2():
    p0 = [[('Invert', 1, 0), ('Rotate', 1, 1)]]
    p1 = [[('Invert', 1, 0), ('Rotate', 1, 3)]]
    p2 = [[('Invert', 1, 0), ('Rotate', 1, 0)]]
    p3 = [[('Invert', 1, 0), ('Rotate', 1, 2)]]
    p4 = [[('Invert', 1, 0), ('Rotate', 1, 1), ('Brightness', 1, 9)]]
    p5 = [[('Invert', 1, 0), ('Rotate', 1, 1), ('Color', 1, 9)]]
    p6 = [[('Invert', 1, 0), ('Rotate', 1, 1), ('Sharpness', 1, 2)]]
    p7 = [[('Invert', 1, 0), ('Invert', 1, 9)]]
    p8 = [[('Invert', 1, 0), ('Rotate', 1, 1), ('Contrast', 1, 8)]]
    p9 = [[('Invert', 1, 0), ('Posterize', 1, 9)]]
    p10 = [[('Invert', 1, 0), ('Rotate', 1, 1), ('Sharpness', 1, 1)]]
    p11 = [[('Invert', 1, 0), ('Rotate', 1, 1), ('Sharpness', 1, 0)]]
    p12 = [[('Invert', 1, 0), ('Invert', 1, 8)]]
    p13 = [[('Invert', 1, 0), ('Posterize', 1, 8)]]
    p14 = [[('Invert', 1, 0), ('Rotate', 1, 1), ('CropBilinear', 1, 0)]]
    p15 = [[('Invert', 1, 0), ('CropBilinear', 1, 0)]]
    p16 = [[('Invert', 1, 0), ('Invert', 1, 7)]]
    p17 = [[('Invert', 1, 0), ('Rotate', 1, 1), ('CropBilinear', 1, 2)]]
    p18 = [[('Invert', 1, 0), ('Rotate', 1, 1), ('Brightness', 1, 8)]]
    p19 = [[('Invert', 1, 0), ('Rotate', 1, 1), ('Contrast', 1, 7)]]
    p20 = [[('Invert', 1, 0), ('Invert', 1, 6)]]
    p21 = [[('Invert', 1, 0), ('Rotate', 1, 1), ('Contrast', 1, 6)]]
    p22 = [[('Invert', 1, 0), ('CropBilinear', 1, 1)]]
    p23 = [[('Invert', 1, 0), ('Invert', 1, 5)]]
    p24 = [[('Invert', 1, 0), ('Rotate', 1, 1), ('CropBilinear', 1, 1)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar10_GAutoAug_VGG():
    p0 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 3), ('TranslateY', 1, 2)]]
    p1 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 3), ('TranslateY', 1, 4)]]
    p2 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 3), ('TranslateY', 1, 3)]]
    p3 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 3), ('TranslateY', 1, 1)]]
    p4 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 3), ('TranslateY', 1, 0)]]
    p5 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 3), ('TranslateY', 1, 5)]]
    p6 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 3)]]
    p7 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 2)]]
    p8 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 3), ('TranslateX', 1, 9)]]
    p9 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 4)]]
    p10 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 3), ('TranslateX', 1, 7)]]
    p11 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 3), ('TranslateX', 1, 8)]]
    p12 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 5)]]
    p13 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 1)]]
    p14 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 6)]]
    p15 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 3), ('ShearY', 1, 1)]]
    p16 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('ShearY', 1, 2)]]
    p17 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 7)]]
    p18 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('ShearX', 1, 9)]]
    p19 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('ShearY', 1, 3)]]
    p20 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 3), ('TranslateX', 1, 6)]]
    p21 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('ShearX', 1, 8)]]
    p22 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 3), ('ShearX', 1, 9)]]
    p23 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 3), ('ShearY', 1, 0)]]
    p24 = [[('Smooth', 1, 3), ('TranslateX', 1, 6), ('ShearY', 1, 1), ('TranslateY', 1, 3), ('TranslateY', 1, 6)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar100_GAutoAug_DenseNet121():
    p0 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('TranslateX', 1, 1)]]
    p1 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('TranslateX', 1, 4)]]
    p2 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('TranslateX', 1, 3)]]
    p3 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('TranslateX', 1, 5)]]
    p4 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('TranslateX', 1, 2)]]
    p5 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('TranslateX', 1, 0)]]
    p6 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('Sharpness', 1, 6)]]
    p7 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('Cutout', 1, 5)]]
    p8 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('Cutout', 1, 4)]]
    p9 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('Cutout', 1, 7)]]
    p10 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('Sharpness', 1, 7)]]
    p11 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8)]]
    p12 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('Sharpness', 1, 3)]]
    p13 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 3)]]
    p14 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 4)]]
    p15 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('Sharpness', 1, 2)]]
    p16 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('Sharpness', 1, 4)]]
    p17 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('Sharpness', 1, 5)]]
    p18 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('Cutout', 1, 8)]]
    p19 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 9)]]
    p20 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('Cutout', 1, 6)]]
    p21 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('Cutout', 1, 3)]]
    p22 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 7)]]
    p23 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('TranslateX', 1, 8)]]
    p24 = [[('Smooth', 1, 2), ('ShearX', 1, 7), ('TranslateX', 1, 7), ('Cutout', 1, 8), ('ShearY', 1, 8)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar100_GAutoAug_DPN92():
    p0 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('TranslateY', 1, 3)]]
    p1 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 6)]]
    p2 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 4)]]
    p3 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2)]]
    p4 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 5)]]
    p5 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3)]]
    p6 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('TranslateY', 1, 4)]]
    p7 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 9)]]
    p8 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 7)]]
    p9 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('TranslateY', 1, 5)]]
    p10 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('TranslateY', 1, 2)]]
    p11 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('TranslateY', 1, 1)]]
    p12 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('ShearY', 1, 6)]]
    p13 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('TranslateX', 1, 8)]]
    p14 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('ShearY', 1, 9)]]
    p15 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Smooth', 1, 3)]]
    p16 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('Cutout', 1, 6)]]
    p17 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Smooth', 1, 2)]]
    p18 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('ShearY', 1, 7)]]
    p19 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('ShearY', 1, 4)]]
    p20 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('ShearY', 1, 3)]]
    p21 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('TranslateY', 1, 0)]]
    p22 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('TranslateX', 1, 9)]]
    p23 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('Cutout', 1, 5)]]
    p24 = [[('Smooth', 1, 9), ('Cutout', 1, 6), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 8)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar100_GAutoAug_GoogLeNet():
    p0 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('Cutout', 1, 9)]]
    p1 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('Blur', 1, 0)]]
    p2 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('Cutout', 1, 8)]]
    p3 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('TranslateY', 1, 1)]]
    p4 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('TranslateY', 1, 0)]]
    p5 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('Cutout', 1, 5)]]
    p6 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('Cutout', 1, 6)]]
    p7 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('Cutout', 1, 7)]]
    p8 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('ShearY', 1, 6)]]
    p9 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('ShearX', 1, 5)]]
    p10 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('ShearY', 1, 1)]]
    p11 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('ShearX', 1, 8)]]
    p12 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('Cutout', 1, 6)]]
    p13 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('ShearY', 1, 5)]]
    p14 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('ShearY', 1, 0)]]
    p15 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('Blur', 1, 1)]]
    p16 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('ShearY', 1, 2)]]
    p17 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('ShearX', 1, 7)]]
    p18 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('TranslateY', 1, 2)]]
    p19 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('ShearX', 1, 4)]]
    p20 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6)]]
    p21 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('ShearX', 1, 6)]]
    p22 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('TranslateY', 1, 5)]]
    p23 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('ShearX', 1, 6), ('ShearY', 1, 4)]]
    p24 = [[('Smooth', 1, 8), ('Cutout', 1, 8), ('Cutout', 1, 5)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar100_GAutoAug_MobileNet():
    p0 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('ShearY', 1, 8)]]
    p1 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('ShearY', 1, 5)]]
    p2 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('ShearY', 1, 6)]]
    p3 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('ShearY', 1, 9)]]
    p4 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('ShearY', 1, 4)]]
    p5 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('ShearY', 1, 7)]]
    p6 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('Blur', 1, 4)]]
    p7 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('Blur', 1, 3)]]
    p8 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('TranslateX', 1, 6)]]
    p9 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('TranslateX', 1, 4)]]
    p10 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('TranslateX', 1, 5)]]
    p11 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('TranslateX', 1, 7)]]
    p12 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('TranslateX', 1, 3)]]
    p13 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('ShearY', 1, 3)]]
    p14 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('TranslateX', 1, 0)]]
    p15 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('TranslateX', 1, 2)]]
    p16 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('ShearY', 1, 2)]]
    p17 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('Blur', 1, 5)]]
    p18 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('Blur', 1, 2)]]
    p19 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('TranslateX', 1, 1)]]
    p20 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('Smooth', 1, 3)]]
    p21 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('Blur', 1, 1)]]
    p22 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('Smooth', 1, 2)]]
    p23 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('ShearY', 1, 1)]]
    p24 = [[('Blur', 1, 3), ('FlipLR', 1, 4), ('Cutout', 1, 8), ('Smooth', 1, 5)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar100_GAutoAug_MobileNetV2():
    p0 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('ShearY', 1, 4)]]
    p1 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('ShearY', 1, 6)]]
    p2 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('TranslateY', 1, 1)]]
    p3 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('ShearY', 1, 7)]]
    p4 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('ShearY', 1, 5)]]
    p5 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('ShearY', 1, 8)]]
    p6 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('ShearY', 1, 9)]]
    p7 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('TranslateX', 1, 0)]]
    p8 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('ShearY', 1, 3)]]
    p9 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('TranslateY', 1, 2)]]
    p10 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('TranslateX', 1, 1)]]
    p11 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('ShearY', 1, 2)]]
    p12 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('TranslateX', 1, 4)]]
    p13 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('TranslateY', 1, 0)]]
    p14 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Blur', 1, 0)]]
    p15 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9)]]
    p16 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('TranslateX', 1, 3)]]
    p17 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('TranslateX', 1, 5)]]
    p18 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('TranslateX', 1, 2)]]
    p19 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 8)]]
    p20 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('ShearY', 1, 1)]]
    p21 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('Sharpness', 1, 6)]]
    p22 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('ShearY', 1, 0)]]
    p23 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('ShearX', 1, 9)]]
    p24 = [[('Smooth', 1, 9), ('Smooth', 1, 8), ('Cutout', 1, 9), ('Sharpness', 1, 5)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar100_GAutoAug_PreActResNet18():
    p0 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('Smooth', 1, 3)]]
    p1 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('Smooth', 1, 4)]]
    p2 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('Smooth', 1, 9)]]
    p3 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('Smooth', 1, 2)]]
    p4 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('Smooth', 1, 1)]]
    p5 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('Smooth', 1, 5)]]
    p6 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('Smooth', 1, 7)]]
    p7 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3)]]
    p8 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('Smooth', 1, 6)]]
    p9 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('TranslateY', 1, 5)]]
    p10 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('ShearY', 1, 7)]]
    p11 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('TranslateY', 1, 4)]]
    p12 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('Smooth', 1, 8)]]
    p13 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('TranslateX', 1, 3)]]
    p14 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('TranslateY', 1, 2)]]
    p15 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('FlipUD', 1, 1)]]
    p16 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('Blur', 1, 9)]]
    p17 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('ShearY', 1, 6)]]
    p18 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('Smooth', 1, 0)]]
    p19 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 4)]]
    p20 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('TranslateY', 1, 3)]]
    p21 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('TranslateY', 1, 6)]]
    p22 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('Blur', 1, 8)]]
    p23 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 2)]]
    p24 = [[('Smooth', 1, 7), ('Smooth', 1, 5), ('Blur', 1, 2), ('Smooth', 1, 3), ('TranslateY', 1, 1)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar100_GAutoAug_ResNet18():
    p0 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('Blur', 1, 6)]]
    p1 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('Blur', 1, 5)]]
    p2 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('Sharpness', 1, 3)]]
    p3 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('Blur', 1, 4)]]
    p4 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('Sharpness', 1, 2)]]
    p5 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('Blur', 1, 7)]]
    p6 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('TranslateX', 1, 1)]]
    p7 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('Blur', 1, 3)]]
    p8 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('TranslateX', 1, 0)]]
    p9 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('TranslateY', 1, 3)]]
    p10 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('TranslateY', 1, 4)]]
    p11 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('ShearY', 1, 6)]]
    p12 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('TranslateY', 1, 5)]]
    p13 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('TranslateX', 1, 2)]]
    p14 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('ShearY', 1, 9)]]
    p15 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('ShearY', 1, 7)]]
    p16 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('Sharpness', 1, 4)]]
    p17 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('TranslateY', 1, 6)]]
    p18 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('Sharpness', 1, 9)]]
    p19 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('Blur', 1, 8)]]
    p20 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('TranslateX', 1, 3)]]
    p21 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('ShearY', 1, 8)]]
    p22 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('ShearX', 1, 0)]]
    p23 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('Brightness', 1, 7)]]
    p24 = [[('Smooth', 1, 9), ('Smooth', 1, 9), ('TranslateX', 1, 0), ('Smooth', 1, 1), ('ShearX', 1, 1)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar100_GAutoAug_ResNeXt29_2x64d():
    p0 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('ShearY', 1, 2)]]
    p1 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('TranslateX', 1, 6)]]
    p2 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('ShearY', 1, 0)]]
    p3 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('FlipLR', 1, 6)]]
    p4 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('ShearY', 1, 1)]]
    p5 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('Smooth', 1, 6)]]
    p6 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('Blur', 1, 7)]]
    p7 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('TranslateY', 1, 1)]]
    p8 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('ShearY', 1, 3)]]
    p9 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('Smooth', 1, 9)]]
    p10 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('Smooth', 1, 5)]]
    p11 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('TranslateX', 1, 8)]]
    p12 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('TranslateY', 1, 2)]]
    p13 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('TranslateY', 1, 8)]]
    p14 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('Blur', 1, 6)]]
    p15 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('TranslateY', 1, 0)]]
    p16 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('TranslateX', 1, 7)]]
    p17 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('TranslateX', 1, 9)]]
    p18 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('Blur', 1, 5)]]
    p19 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('Blur', 1, 8)]]
    p20 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('Smooth', 1, 7)]]
    p21 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('TranslateX', 1, 5)]]
    p22 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6)]]
    p23 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('Smooth', 1, 8)]]
    p24 = [[('Smooth', 1, 8), ('Smooth', 1, 2), ('Blur', 1, 3), ('Blur', 1, 6), ('TranslateY', 1, 6)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar100_GAutoAug_SENet18():
    p0 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('Smooth', 1, 9)]]
    p1 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('TranslateX', 1, 3)]]
    p2 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('TranslateX', 1, 5)]]
    p3 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('TranslateX', 1, 4)]]
    p4 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('TranslateX', 1, 2)]]
    p5 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('ShearY', 1, 9)]]
    p6 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('Smooth', 1, 8)]]
    p7 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('ShearY', 1, 8)]]
    p8 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('TranslateX', 1, 6)]]
    p9 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('FlipUD', 1, 7)]]
    p10 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('ShearY', 1, 7)]]
    p11 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('TranslateX', 1, 0)]]
    p12 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('Smooth', 1, 7)]]
    p13 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('TranslateX', 1, 1)]]
    p14 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('Cutout', 1, 2)]]
    p15 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('FlipUD', 1, 6)]]
    p16 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('Cutout', 1, 3)]]
    p17 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7)]]
    p18 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 8)]]
    p19 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 8), ('Blur', 1, 1)]]
    p20 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 8), ('TranslateX', 1, 2)]]
    p21 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 8), ('Smooth', 1, 9)]]
    p22 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 8), ('TranslateX', 1, 3)]]
    p23 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 7), ('TranslateX', 1, 7)]]
    p24 = [[('Smooth', 1, 3), ('Cutout', 1, 2), ('Blur', 1, 8), ('Blur', 1, 3)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar100_GAutoAug_ShuffleNetG2():
    p0 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateY', 1, 9), ('TranslateX', 1, 6)]]
    p1 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateY', 1, 9), ('TranslateX', 1, 7)]]
    p2 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateY', 1, 9), ('TranslateX', 1, 5)]]
    p3 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateY', 1, 9), ('TranslateX', 1, 4)]]
    p4 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateY', 1, 9), ('TranslateX', 1, 8)]]
    p5 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateY', 1, 9)]]
    p6 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('Cutout', 1, 0)]]
    p7 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('Cutout', 1, 1)]]
    p8 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateY', 1, 8)]]
    p9 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('Cutout', 1, 2)]]
    p10 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateY', 1, 9), ('ShearY', 1, 3)]]
    p11 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('Cutout', 1, 3)]]
    p12 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateY', 1, 7)]]
    p13 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateX', 1, 7)]]
    p14 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateX', 1, 6)]]
    p15 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateX', 1, 5)]]
    p16 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateX', 1, 8)]]
    p17 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateY', 1, 6)]]
    p18 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateY', 1, 9), ('ShearY', 1, 2)]]
    p19 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('ShearX', 1, 0)]]
    p20 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateY', 1, 9), ('ShearY', 1, 6)]]
    p21 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateY', 1, 9), ('ShearX', 1, 2)]]
    p22 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateY', 1, 9), ('ShearY', 1, 4)]]
    p23 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('Sharpness', 1, 9)]]
    p24 = [[('Smooth', 1, 6), ('TranslateY', 1, 7), ('Cutout', 1, 2), ('TranslateY', 1, 9), ('TranslateX', 1, 3)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar100_GAutoAug_ShuffleNetV2():
    p0 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('TranslateY', 1, 1)]]
    p1 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('TranslateY', 1, 0)]]
    p2 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('TranslateY', 1, 2)]]
    p3 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('TranslateX', 1, 9)]]
    p4 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('FlipUD', 1, 2)]]
    p5 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Smooth', 1, 2)]]
    p6 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3)]]
    p7 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('Sharpness', 1, 1)]]
    p8 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('Blur', 1, 8)]]
    p9 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('Equalize', 1, 0)]]
    p10 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('Sharpness', 1, 0)]]
    p11 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('Brightness', 1, 7)]]
    p12 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('Brightness', 1, 8)]]
    p13 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('TranslateX', 1, 8)]]
    p14 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('Sharpness', 1, 2)]]
    p15 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Smooth', 1, 3)]]
    p16 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 4)]]
    p17 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('Sharpness', 1, 3)]]
    p18 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('FlipUD', 1, 1)]]
    p19 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Smooth', 1, 2), ('FlipLR', 1, 1)]]
    p20 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('FlipUD', 1, 3)]]
    p21 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('TranslateY', 1, 3)]]
    p22 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('Blur', 1, 9)]]
    p23 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Smooth', 1, 2), ('FlipLR', 1, 0)]]
    p24 = [[('FlipLR', 1, 8), ('Smooth', 1, 8), ('Blur', 1, 3), ('Sharpness', 1, 4)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations


def cifar100_GAutoAug_VGG():
    p0 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Blur', 1, 6)]]
    p1 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('ShearX', 1, 0)]]
    p2 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('ShearX', 1, 1)]]
    p3 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Sharpness', 1, 9)]]
    p4 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Blur', 1, 7)]]
    p5 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Blur', 1, 5)]]
    p6 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Blur', 1, 8)]]
    p7 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('ShearX', 1, 2)]]
    p8 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Blur', 1, 9)]]
    p9 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Blur', 1, 4)]]
    p10 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Sharpness', 1, 8)]]
    p11 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Blur', 1, 3)]]
    p12 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Smooth', 1, 0)]]
    p13 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Smooth', 1, 8)]]
    p14 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Smooth', 1, 9)]]
    p15 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Sharpness', 1, 7)]]
    p16 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('ShearX', 1, 3)]]
    p17 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('TranslateX', 1, 0)]]
    p18 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('ShearX', 1, 4)]]
    p19 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Sharpness', 1, 6)]]
    p20 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Sharpness', 1, 0)]]
    p21 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Smooth', 1, 7)]]
    p22 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('Brightness', 1, 9)]]
    p23 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('ShearY', 1, 9)]]
    p24 = [[('TranslateY', 1, 9), ('Smooth', 1, 6), ('Smooth', 1, 0), ('Cutout', 1, 7), ('ShearY', 1, 8)]]
    augmentations = []

    result = p0 + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15 + p16 + p17 + p18 + p19 + p20 + p21 + p22 + p23 + p24
    pnone = [('Smooth', 0, 10)]
    augmentations.append(pnone)
    i = int(len(result) / 5)
    counterS = 0
    counterE = 4
    from random import randint
    for j in range(i):
        rand = randint(counterS, counterE)
        augmentations.append(result[rand])
        counterS += 5
        counterE += 5

    return augmentations
