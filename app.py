from flask import Flask, request, jsonify
from environment import ContentEnv
import gradio as gr
import threading

app = Flask(__name__)
env = ContentEnv()

@app.route("/")
def home():
    return "API running"

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

def run_gradio():
    with gr.Blocks() as demo:
        output = gr.JSON()
        with gr.Row():
            gr.Button("Reset").click(fn=ui_reset, outputs=output)
            gr.Button("Post Reel").click(fn=lambda: ui_step("post_reel"), outputs=output)
            gr.Button("Post Carousel").click(fn=lambda: ui_step("post_carousel"), outputs=output)
            gr.Button("Take Break").click(fn=lambda: ui_step("take_break"), outputs=output)
    demo.launch(server_name="0.0.0.0", server_port=7861, share=False)

if __name__ == "__main__":
    threading.Thread(target=run_gradio).start()
    app.run(host="0.0.0.0", port=7860)