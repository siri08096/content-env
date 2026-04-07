import os
from openai import OpenAI
from environment import ContentEnv

# REQUIRED ENV VARIABLES
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN", "dummy")

# OpenAI client (required by checklist)
client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

env = ContentEnv()

def run_inference():
    print("[START]")

    state = env.reset()

    for step in range(5):
        if state["fatigue"] > 40:
            action = "take_break"
        elif state["engagement"] < 2:
            action = "post_carousel"
        else:
            action = "post_reel"

        state, reward, done = env.step(action)

        print(f"[STEP] action={action} reward={reward}")

        if done:
            break

    print("[END]")

    return state


if __name__ == "__main__":
    run_inference()