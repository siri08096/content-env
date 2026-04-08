from flask import Flask, request, jsonify
from environment import ContentEnv

app = Flask(__name__)

env = ContentEnv()

@app.route("/")
def home():
    return "API running"

@app.route("/reset", methods=["POST"])
def reset():
    state = env.reset()
    return jsonify(state)

@app.route("/step", methods=["POST"])
def step():
    data = request.get_json()
    action = data.get("action")

    state, reward, done, info = env.step(action)

    return jsonify({
        "state": state,
        "reward": reward,
        "done": done
    })