from environment import ContentEnv
from graders import grade_followers, grade_engagement, grade_balance

env = ContentEnv()

task_name = "content_strategy"
env_name = "content-env"
model_name = "rule-based"

state = env.reset()

print(f"[START] task={task_name} env={env_name} model={model_name}", flush=True)

rewards = []
steps = 0
done = False

for step in range(1, 11):
    if state["fatigue"] > 40:
        action = "take_break"
    elif state["engagement"] < 2:
        action = "post_carousel"
    else:
        action = "post_reel"

    state, reward, done = env.step(action)

    reward = reward or 0.0
    rewards.append(reward)
    steps = step

    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null",
        flush=True
    )

    if done:
        break

# Calculate final score
score = (
    grade_followers(state) +
    grade_engagement(state) +
    grade_balance(state)
) / 3.0

score = min(max(score, 0.0), 1.0)
success = score > 0.3

rewards_str = ",".join(f"{r:.2f}" for r in rewards)

print(
    f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}",
    flush=True
)