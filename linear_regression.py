from flask import Flask
from flask import render_template
import tensorflow
import keras
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    data = pd.read_csv("student-mat.csv", sep=";")
    data = data[["G1","G2","G3","studytime","failures","absences"]]

    predict = "G3"

    x = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

    '''

    TRAINING FOR LOOP TO GET HIGHEST ACCURACY
    best = 0
    for _ in range(30):
    #splits test data into chunks of ten percent of the original test data amount
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

        linear = linear_model.LinearRegression()

        linear.fit(x_train, y_train)
        acc = linear.score(x_test,y_test)
        print(acc)

        if acc > best:
            best = acc
            with open("studentmodel.pickle", "wb") as f:
                pickle.dump(linear, f)
    '''

    pickle_in = open("studentmodel.pickle", "rb")
    linear = pickle.load(pickle_in)

    print("Coefficient: \n", linear.coef_)
    print("intercept: \n", linear.intercept_)

    predictions = linear.predict(x_test)

    for x in range(len(predictions)):
        print(predictions[x], x_test[x], y_test[x])


    '''CREATES SCATERPLOT FOR DATA'''
    p = "G1"
    style.use("ggplot")
    pyplot.scatter(data[p], data["G3"])
    pyplot.xlabel(p)
    pyplot.ylabel("final grade")
    pyplot.show()

    app.run()