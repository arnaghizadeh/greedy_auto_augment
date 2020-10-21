import pickle
import numpy as np
randomseed = 2097


def save_variables(path="", policies=None):
    if policies != None:
        pickle.dump(policies, open(path, 'wb'))

def test():
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

def grouper(lst, k=3):
    return [lst[n:n + k] for n, i in enumerate(lst) if n % k == 0]

def management():
    policies = ['FlipLR', 'FlipUD', 'AutoContrast', 'Equalize', 'Invert', 'Rotate', 'Posterize', 'CropBilinear',
                'Solarize', 'Color', 'Contrast', 'Brightness', 'Sharpness', 'ShearX', 'ShearY', 'TranslateX',
                'TranslateY',
                'Cutout', 'Blur', 'Smooth']

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
            print(grouped_policy)
            res = test()
            all_policies.append(current_policy)
            all_results.append(res)

    indeces = np.argsort(all_results)[::-1][:len(all_results)]
    max_idx, s = get_max_idx(indeces, all_policies, s)

    for k in range(4):
        pre_policy = all_policies[max_idx]
        for t in range(20):
            for m in range(10):
                all_trainings += 1
                all_epochs += 5
                sub_policy = (policies[t], 1, m)
                current_policy = pre_policy + sub_policy
                grouped_policy = grouper(current_policy)
                print(grouped_policy)
                res = test()
                all_policies.append(current_policy)
                all_results.append(res)
        indeces = np.argsort(all_results)[::-1][:len(all_results)]
        max_idx, s = get_max_idx(indeces, all_policies, s)

    saved_policies = []
    for i in range(len(all_policies)):
        idx = indeces[i]
        policy = all_policies[idx]
        grouped_policy = grouper(policy)
        saved_policies.append(grouped_policy)
    for i in range(100):
        print(saved_policies[i])

    print("All epochs:" + str(all_epochs) + " All trainings:" + str(all_trainings))
    return saved_policies


policies = management()
save_variables("saved_policies", policies=policies)
