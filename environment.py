import random

class ContentEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = {
            "followers": 1000,
            "engagement": 2.0,
            "fatigue": 0,
            "day": 1
        }
        return self.state

    def step(self, action):   # 👈 MUST be inside class
        reward = 0

        trend = random.choice(["reel", "carousel", "none"])

        if action == "post_reel":
            self.state["followers"] += 40
            self.state["engagement"] += 0.4
            self.state["fatigue"] += 10
            reward = 0.6

            if trend == "reel":
                reward = 1.0

        elif action == "post_carousel":
            self.state["followers"] += 25
            self.state["engagement"] += 0.6
            self.state["fatigue"] += 8
            reward = 0.5

            if trend == "carousel":
                reward = 0.9

        elif action == "take_break":
            self.state["fatigue"] -= 15
            reward = 0.4

        elif action == "skip":
            self.state["engagement"] -= 0.3
            reward = 0.2

        if self.state["fatigue"] > 50:
            reward -= 0.3

        self.state["fatigue"] = max(0, self.state["fatigue"])
        self.state["engagement"] = max(0, self.state["engagement"])

        self.state["day"] += 1

        done = self.state["day"] > 10

        return self.state, round(reward, 2), done