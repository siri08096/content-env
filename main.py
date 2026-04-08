from flask import Flask, request, jsonify
from environment import ContentEnv

app = Flask(__name__)
env = ContentEnv()

@app.route("/")
def home():
    return "API running"

@app.route("/reset", methods=["GET"])
def reset():
    return jsonify(env.reset())

@app.route("/step", methods=["POST"])
def step():
    action = request.json.get("action")
    state, reward, done = env.step(action)
    return jsonify({
        "state": state,
        "reward": reward,
        "done": done
    })