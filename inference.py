from environment import ContentEnv
from graders import grade_followers, grade_engagement, grade_balance

env = ContentEnv()

print("[START]")

state = env.reset()

for step in range(10):

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

print("Followers Score:", grade_followers(state))
print("Engagement Score:", grade_engagement(state))
print("Balance Score:", grade_balance(state))