import pandas as pd
import numpy as np
import glob

def pipeline():
    path = r'./Data-out' 
    all_files = glob.glob(path + "/hda_dataset_uniform_random_[0-7].csv")
    all_files.sort()

    #dataset = pd.read_csv("./Data-out/hda_dataset_uniform_random_0.csv")
    df = (pd.read_csv(f) for f in all_files)
    concat_df = pd.concat(df).drop_duplicates().reset_index(drop=True)
    concat_df = concat_df.sort_values(by=['case', 'ts'])
    #concat_df.to_csv('test1.csv')
    return concat_df

def test():
    a = 5
    return a