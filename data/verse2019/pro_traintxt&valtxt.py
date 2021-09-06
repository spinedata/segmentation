import numpy as np
import os
import os.path as osp
import random

def gen_txt(input_path, train_path, val_path):

    assert osp.exists(input_path) and osp.isdir(input_path)

    print(os.listdir(input_path))
    filenames = os.listdir(input_path) #返回是一个np的数组ndarray, 这是文件夹下面所有文件名列表
    random.shuffle(filenames)

    count = int(len(filenames) * 0.8)
    train = filenames[:count]
    val = filenames[count:]

    with open(train_path, 'w', encoding='utf-8') as f:
        for name in train:
            f.write(name[:-4] + '\n')
    with open(val_path, 'w', encoding='utf-8') as f:
        for name in val:
            f.write(name[:-4] + '\n')


def main():
    input_path = "images/"
    train_path = "train.txt"
    val_path = "val.txt"
    gen_txt(input_path, train_path, val_path)

if __name__ == '__main__':
    main()
