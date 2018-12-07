from flask import Flask, jsonify, request

import os
os.environ["KERAS_BACKEND"] = "tensorflow"
import tensorflow as tf
import keras
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE

course_names = ["Introduction to Informatics 1", "Fundamentals of Programming (Exercises & Laboratory)", "Introduction to Informatics 2", "Introduction to Computer Organization and Technology - Computer Architecture", "Laboratory: Computer Organization and Computer Architecture", "Introduction to Software Engineering", "Fundamentals of Algorithms and Data Structures", "Fundamentals of Databases", "Basic Principles: Operating Systems and System Software", "Introduction to Computer Networking and Distributed Systems", "Computer Systems Performance Analysis", "Cloud Computing", "Microprocessors", "Advanced Computer Architecture", "Foundations of program and system development", "IT-Consulting", "Algorithms and Data Structures", "User Modeling and Recommender Systems", "Networks for Monetary Transactions", "International Experience & Communication Skills", "Start-up financing", "Business Plan - Basic Course (Business Idea and Market)", "Patents and Trade Secrets", "Topics in Marketing, Strategy & Leadership (MSL) - (F&WM) I", "Introduction to Business Law", "Statistics for BWL", "Energy & Climate Policy", "High Performance Leadership", "Basic Principles and international Aspects of Corporate Management", "Project Management", "Law of Business Association 1", "Topics in General Management", "Investment and Financial Management", "Production and Logistics",]
course_ids = ["IN0001", "IN0002", "IN0003", "IN0004", "IN0005", "IN0006", "IN0007", "IN0008", "IN0009", "IN0010", "IN2072", "IN2073", "IN2075", "IN2076", "IN2078", "IN2079", "IN8009", "IN2119", "IN2161", "WI900004", "WI001163", "WI000159", "WI000810", "WIB21933", "WI001119", "MA9712", "WI001183", "WI000996", "WI001028", "WI000264", "WI100130", "WI001159", "WI000219", "WI001060",]

class MLModel():
    def __init__(self):
        #Wait forever for incoming htto requests
        n_nodes_inp = 10
        n_nodes_h = 10  
        n_nodes_out = 10

        inp = keras.layers.Input(shape=[n_nodes_inp], name='Item')
        embedding = keras.layers.Dense(n_nodes_h, activation='sigmoid')(inp)
        output = keras.layers.Dense(n_nodes_out, activation=None)(embedding)

        self.model = keras.Model(inp, output)
        self.model.compile('adam', 'mean_squared_error')
        self.model.load_weights("model.h5")

    def predict(self, user_ratings, top_courses):
        user_ratings = np.array(user_ratings)
        predictions = self.model.predict(user_ratings.reshape(1, -1))
        ix = np.argsort(-predictions[0])
        return np.array(list(zip(predictions[0][ix], ix))[:top_courses])[:, 1].astype(np.int).tolist()


app = Flask(__name__, static_url_path='/static')
database = {}
database_z = [0] * len(course_names)
name_to_id = dict(zip(course_names, course_ids))


@app.route('/')
def main():
    return app.send_static_file('index.html')


@app.route('/users/<uid>/recommendations')
def rec_for_user(uid):
    global model

    # Get dummy predictions
    predictions = model.predict([5., 6., 7., 0., 7., 8., 7., 0., 8., 5.],
                                top_courses=5)

    recs = [
        {'name': course_names[i], 'score': 1.0 - i*i * 0.1, 'id': name_to_id[course_names[i]]} for i in
        predictions
    ]
    ###
    return jsonify(recs)


@app.route('/users/<int:uid>/votes')
def votes_for_user(uid):
    recs = [
        {'name': e, 'score': database[e], 'id': name_to_id[e]} for e in database
    ]
    return jsonify(recs)


@app.route('/users/<int:uid>/vote', methods=['POST'])
def do_vote(uid):
    # print(dict(request.form))
    for cid in request.form:
        database[cid] = float(request.form[cid])
        i = course_names.index(cid)
        database_z[i] = float(request.form[cid])
    return 'Vote sucksassful'


if __name__ == '__main__':
    # Load and prepare ML Model
    global model
    model = MLModel()
    predictions = model.predict([5., 6., 7., 0., 7., 8., 7., 0., 8., 5.],
                                top_courses=3)
    ###

    app.run(debug=True, host='0.0.0.0')
