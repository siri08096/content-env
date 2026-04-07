import gradio as gr
from environment import ContentEnv

env = ContentEnv()
state = env.reset()

def reset_env():
    global state
    state = env.reset()
    return state

def take_action(action):
    global state
    state, reward, done = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }

with gr.Blocks() as demo:
    gr.Markdown("## 🚀 Content Strategy AI Simulator")

    output = gr.JSON()

    with gr.Row():
        reset_btn = gr.Button("🔄 Reset")
        reel_btn = gr.Button("🎬 Post Reel")
        carousel_btn = gr.Button("📸 Post Carousel")
        break_btn = gr.Button("☕ Take Break")

    reset_btn.click(fn=reset_env, outputs=output)
    reel_btn.click(fn=lambda: take_action("post_reel"), outputs=output)
    carousel_btn.click(fn=lambda: take_action("post_carousel"), outputs=output)
    break_btn.click(fn=lambda: take_action("take_break"), outputs=output)

demo.launch()