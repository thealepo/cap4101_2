import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder

def svm_train_predict(x_train , y_train , x_test):
    # encode target layers
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y_train)

    # scaling input layers
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    # define the SVM model
    param_grid = {
        'kernel': ['linear' , 'rbf'],
        'C': [1 , 10],
        'gamma': ['scale']
    }

    grid_search = GridSearchCV(
        estimator=SVC(),
        param_grid=param_grid,
        cv=5
    )

    # fitting model
    grid_search.fit(x_train_scaled , y_encoded)
    model = grid_search.best_estimator_

    # predict
    predictions_encoded = model.predict(x_test_scaled)
    predictions = label_encoder.inverse_transform(predictions)

    return predictions