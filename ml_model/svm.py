import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

def svm_train_predict(x_train , y_train , x_test):
    # scaling data
    scaler_X = StandardScaler()
    scaler_Y = StandardScaler()

    X_train_scaled = scaler_X.fit_transform(x_train)
    x_test_scaled = scaler_X.transform(x_test)

    Y_train_scaled = scaler_Y.fit_transform(y_train.values.reshape(-1,1))

    # model
    model = SVC()

    # define hyperparameters
    param_grid = {
        'kernel': ['linear' , 'rbf' , 'tanh'],
        'C': [1 , 10],
        'gamma': ['scale']
    }

    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
    )

    # model fitting
    model = grid_search.best_estimator_

    # predictions
    predictions_scaled = model.predict(x_test_scaled)
    predictions = scaler_Y.inverse_transform(predictions_scaled.reshape(-1,1))

    return predictions