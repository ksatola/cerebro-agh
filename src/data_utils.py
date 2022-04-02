
import pandas as pd
from sklearn.model_selection import train_test_split

from config import *

def get_train_test_split_for_stock(data_file):
    """
    Takes... csv file
    Outputs... X_train, X_test, y_train, y_test split
    """
    
    data = pd.read_csv(data_file)
    
    #X = data.loc[:, data.columns != 'target']
    #Y = data.loc[:, data.columns == 'target']
    
    X = data.iloc[:, :-1]
    Y = data.iloc[:, -1]
    
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=SPLIT_RATIO, random_state=RANDOM_STATE, stratify=Y)
    
    return X_train, X_test, y_train, y_test
