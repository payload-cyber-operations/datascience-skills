#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pprint import pprint

def loading_dataset(filename: str):

    dataset = pd.read_csv(filename)
    pprint(dataset)

    plt.figure(figsize=(12,12))
    plt.plot(dataset["age"])
    plt.show()



def main():
    filename = "heart.csv"
    loading_dataset(filename)


if __name__ == "__main__":
    main()
