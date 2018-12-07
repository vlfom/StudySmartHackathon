from flask import Flask, jsonify

class MLModel():
    def __init__(self):
        pass

    def predict(self, user_ratings, top_courses):
        return user_ratings


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def main():
    return app.send_static_file('index.html')


@app.route('/users/<uid>/recommendations')
def rec_for_user(uid):
    global model

    # Get dummy predictions
    predictions = model.predict([5., 6., 7., 0., 7., 8., 7., 0., 8., 5.], top_courses=3)

    recs = [
        {'name': n, 'score': s} for n, s in 
        zip(['BWL I', 'BWL II', 'VWL I'], [predictions[0], predictions[1], predictions[2]])
    ]
    ###

    return jsonify(recs)


@app.route('/users/<uid>/votes')
def votes_for_user(uid):
    recs = [
        {'name': n, 'score': s} for n, s in zip(
            ['Buchhaltung', 'Huynya'], [5, 2]
        )
    ]
    return jsonify(recs)


if __name__ == '__main__':
	# Load and prepare ML Model
    global model
    model = MLModel()
    predictions = model.predict([5., 6., 7., 0., 7., 8., 7., 0., 8., 5.], top_courses=3)
    ###

    app.run(debug=True)
