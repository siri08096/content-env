
from flask import Flask, request, jsonify
import gradio as gr
from environment import ContentEnv

app = Flask(__name__)
env = ContentEnv()

@app.route("/reset", methods=["GET", "POST"])
def reset():
    state = env.reset()
    return jsonify(state)

@app.route("/step", methods=["POST"])
def step():
    action = request.json.get("action")
    state, reward, done = env.step(action)
    return jsonify({
        "state": state,
        "reward": reward,
        "done": done
    })

ui_env = ContentEnv()
ui_state = ui_env.reset()

def ui_reset():
    global ui_state
    ui_state = ui_env.reset()
    return ui_state

def post_reel():
    global ui_state
    ui_state, _, _ = ui_env.step("post_reel")
    return ui_state

def post_carousel():
    global ui_state
    ui_state, _, _ = ui_env.step("post_carousel")
    return ui_state

def take_break():
    global ui_state
    ui_state, _, _ = ui_env.step("take_break")
    return ui_state

with gr.Blocks() as demo:
    gr.Markdown("## 🚀 Content Strategy AI Simulator")
    state_output = gr.JSON()

    with gr.Row():
        reset_btn = gr.Button("Reset")
        reel_btn = gr.Button("Post Reel")
        carousel_btn = gr.Button("Post Carousel")
        break_btn = gr.Button("Take Break")

    reset_btn.click(fn=ui_reset, outputs=state_output)
    reel_btn.click(fn=post_reel, outputs=state_output)
    carousel_btn.click(fn=post_carousel, outputs=state_output)
    break_btn.click(fn=take_break, outputs=state_output)

if __name__ == "__main__":
    import threading

    def run_flask():
        app.run(host="0.0.0.0", port=7860)

    threading.Thread(target=run_flask).start()
    demo.launch(server_name="0.0.0.0", server_port=7860)



