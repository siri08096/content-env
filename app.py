from flask import Flask, request, jsonify
from environment import ContentEnv
import gradio as gr

app = Flask(__name__)
env = ContentEnv()

@app.route("/")
def home():
    return "API is running"

@app.route("/reset", methods=["GET", "POST"])
def reset():
    state = env.reset()
    return jsonify(state)

@app.route("/step", methods=["POST"])
def step():
    data = request.get_json()
    action = data.get("action")
    state, reward, done = env.step(action)
    return jsonify({
        "state": state,
        "reward": reward,
        "done": done
    })

def ui_reset():
    return env.reset()

def ui_step(action):
    state, reward, done = env.step(action)
    return state

with gr.Blocks() as demo:
    output = gr.JSON()
    with gr.Row():
        reset_btn = gr.Button("Reset")
        reel_btn = gr.Button("Post Reel")
        carousel_btn = gr.Button("Post Carousel")
        break_btn = gr.Button("Take Break")

    reset_btn.click(fn=ui_reset, outputs=output)
    reel_btn.click(fn=lambda: ui_step("post_reel"), outputs=output)
    carousel_btn.click(fn=lambda: ui_step("post_carousel"), outputs=output)
    break_btn.click(fn=lambda: ui_step("take_break"), outputs=output)

app = gr.mount_gradio_app(app, demo, path="/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)