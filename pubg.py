import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


DATA_PATH = 'data/'


def save_validation():
    data = pd.read_csv(DATA_PATH + 'train_C2.csv')
    validation_data = data.sample(frac=0.5, replace=True, random_state=1)
    validation_data.to_csv(DATA_PATH + 'validation_data.csv')
    data.to_csv(DATA_PATH + 'new_train.csv')


if __name__ == '__main__':
    # split to validation
    save_validation()
    pass
