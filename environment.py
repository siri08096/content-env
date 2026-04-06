import random

class ContentEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = {
            "followers": 1000,
            "engagement": 2.0,
            "fatigue": 0,
            "day": 1,
            "platform": random.choice(["instagram", "twitter"]),
            "trend": random.choice(["reel", "carousel", "none"]),
            "trend_days": random.randint(2, 4)
        }
        return self.state

    def step(self, action):
        reward = 0

        trend = self.state["trend"]

        #  Action logic
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

        #  Algorithm randomness
        if random.random() < 0.1:
            reward -= 0.2

        #  Platform logic
        if self.state["platform"] == "instagram":
            if action == "post_reel":
                reward += 0.2

        elif self.state["platform"] == "twitter":
            if action == "post_carousel":
                reward += 0.2

        #  Fatigue penalty
        if self.state["fatigue"] > 50:
            reward -= 0.3

        #  Clean values
        self.state["fatigue"] = max(0, self.state["fatigue"])
        self.state["engagement"] = max(0, self.state["engagement"])

        #  Update day
        self.state["day"] += 1

        #  Trend persistence system
        self.state["trend_days"] -= 1
        if self.state["trend_days"] <= 0:
            self.state["trend"] = random.choice(["reel", "carousel", "none"])
            self.state["trend_days"] = random.randint(2, 4)

        done = self.state["day"] > 10

        return self.state, round(reward, 2), done