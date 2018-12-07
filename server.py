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
name_to_id = {}


@app.route('/')
def main():
    return app.send_static_file('index.html')


@app.route('/users/<uid>/recommendations')
def rec_for_user(uid):
    global model

    # Get dummy predictions
    predictions = model.predict([5., 6., 7., 0., 7., 8., 7., 0., 8., 5.],
                                top_courses=3)

    recs = [
        {'name': n, 'score': s, 'id': i} for n, s, i in
        zip(['BWL I', 'BWL II', 'VWL I'],
            [predictions[0] + 1, predictions[1] + 1, predictions[2] + 1],
            ['IN0001', 'IN0002', 'IN0003'])
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
    return 'Vote sucksassful'


if __name__ == '__main__':
    # Load and prepare ML Model
    global model
    model = MLModel()
    predictions = model.predict([5., 6., 7., 0., 7., 8., 7., 0., 8., 5.],
                                top_courses=3)
    ###

    app.run(debug=True)
