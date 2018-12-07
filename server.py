from flask import Flask, jsonify, request
import pandas as pd


app = Flask(__name__, static_url_path='/static')
database = pd.DataFrame(columns=['uid', 'cid', 'score'])


@app.route('/')
def main():
    return app.send_static_file('index.html')


@app.route('/users/<uid>/recommendations')
def rec_for_user(uid):
    recs = [
        {'name': n, 'score': s} for n, s in zip(
            ['BWL I', 'BWL II', 'VWL I'],
            [0.95, 0.93, 0.8]
        )
    ]
    return jsonify(recs)


@app.route('/users/<uid>/votes')
def votes_for_user(uid):
    recs = [
        {'name': n, 'score': s} for n, s in zip(
            ['Buchhaltung', 'Huynya'], [5, 2]
        )
    ]
    return jsonify(recs)


@app.route('/users/<int:uid>/vote', methods=['POST'])
def do_vote(uid):
    database.append(
        [int(request.post['uid']),
         int(request.post['cid']),
         float(request.post['score'])]
    )
    return 'Vote sucksassful'


if __name__ == '__main__':
    app.run(debug=True)
