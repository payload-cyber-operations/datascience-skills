#!/usr/bin/env python3

import numpy as np
import pandas as pd
from pprint import pprint

def loading_dataset(filename: str):

    dataset = pd.read_csv(filename)
    pprint(dataset)



def main():
    filename = "heart.csv"
    loading_dataset(filename)


if __name__ == "__main__":
    main()
