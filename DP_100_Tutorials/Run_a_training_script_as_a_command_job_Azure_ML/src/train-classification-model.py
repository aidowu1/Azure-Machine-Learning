#!/usr/bin/env python
# coding: utf-8

# # Train diabetes classification model
# 
# This notebook reads a CSV file and trains a model to predict diabetes in patients. The data is already preprocessed and requires no feature engineering.
# 
# The evaluation methods were used during experimentation to decide whether the model was accurate enough. Moving forward, there's a preference to use the autolog feature of MLflow to more easily deploy the model later on.

# ## Read data from local file
# 
# 

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
import argparse

def readData(train_data_path: str):
    """
    Reads data
    """
    #print("Reading data...")
    df = pd.read_csv(train_data_path)
    return df


def splitData(df):
    """
    Splits data
    """
    #print("Splitting data...")
    X, y = df[['Pregnancies','PlasmaGlucose','DiastolicBloodPressure','TricepsThickness','SerumInsulin','BMI','DiabetesPedigree','Age']].values, df['Diabetic'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
    return X_train, X_test, y_train, y_test

def trainModel(X_train, y_train):
    """
    Train model
    """
    print("Training model...")
    model = LogisticRegression(C=1/0.1, solver="liblinear").fit(X_train, y_train)
    return model

def evaluateModel(model, X_test, y_test):
    """
    Evaluate model
    """
    y_hat = model.predict(X_test)
    acc = np.average(y_hat == y_test)
    #print('Accuracy:', acc)
    y_scores = model.predict_proba(X_test)
    auc = roc_auc_score(y_test,y_scores[:,1])
    #print('AUC: ' + str(auc))
    # plot ROC curve
    fpr, tpr, thresholds = roc_curve(y_test, y_scores[:,1])
    fig = plt.figure(figsize=(6, 4))
    # Plot the diagonal 50% line
    plt.plot([0, 1], [0, 1], 'k--')
    # Plot the FPR and TPR achieved by our model
    plt.plot(fpr, tpr)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')

def parseArgs():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument(
        "--train_data_path",
        dest='train_data_path',
        type=str
    )

    # parse args
    args = parser.parse_args()

    return args


def main():
    args = parseArgs()
    df = readData(args.train_data_path)
    X_train, X_test, y_train, y_test = splitData(df)
    model = trainModel(X_train, y_train)
    evaluateModel(model, X_test, y_test)



if __name__ == "__main__":
    main()

