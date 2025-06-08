import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report , confusion_matrix , accuracy_score
from sklearn.preprocessing import LabelEncoder

from ml_model.svm import svm_train_predict


data = pd.read_csv('./data/fitness_recommendation_dataset.csv')
df = pd.DataFrame(data)

features = ['BFSI',
             'ABSI',
             'ABSI_zscore',
             'Mortality_Risk',
             'BMI',
             'Weight_Status',
             'Current_Weight',
             'Ideal_Weight']
target = 'Recommendation'

# encoding any categorical features
categorical = ['Mortality_Risk' , 'Weight_Status']
data_encoded = data.copy()
for col in categorical:
    le = LabelEncoder()
    data_encoded[col] = le.fit_transform(data[col])

# encoding target
le_target = LabelEncoder()
data_encoded[target] = le_target.fit_transform(data[target])

# train/test split
X = data_encoded[features]
y = data[target]
X_train , X_test , y_train , y_test = train_test_split(
    X , y , test_size=0.2 , stratify=y , random_state=42
)

# pred
y_pred = svm_train_predict(X_train , y_train , X_test)

def evaluate(y_true , y_pred):
    print("Classification Report:" , classification_report(y_true,y_pred))
    print("\nConfusion Matrix:\n" , confusion_matrix(y_true,y_pred))
    print("\nAccuracy Score:\n" , accuracy_score(y_true,y_pred))
evaluate(y_test , y_pred)

