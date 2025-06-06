import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

from ml_model.svm import svm_train_predict


data = pd.read_csv('./data/fitness_recommendation_dataset.csv')
df = pd.DataFrame(data)

def evaluate(model , Y_test , Y_pred):
    pass


features = ['BFSI',
             'ABSI',
             'ABSI_zscore',
             'Mortality_Risk',
             'BMI',
             'Weight_Status',
             'Current_Weight',
             'Ideal_Weight']
target = 'Recommendation'

