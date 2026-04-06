def grade_followers(state):
    return min(state["followers"] / 1500, 1.0)


def grade_engagement(state):
    return min(state["engagement"] / 5.0, 1.0)


def grade_balance(state):
    score = (state["followers"] / 1500) * 0.6 + (1 - state["fatigue"] / 100) * 0.4
    return min(max(score, 0), 1.0)