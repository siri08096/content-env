 Content Strategy AI Environment (OpenEnv)

 Overview

This project implements a real-world simulation environment where an AI agent learns to make content strategy decisions for a social media platform.

The agent must balance:

 Growth (followers)
 Engagement
 Content fatigue

The environment follows the OpenEnv specification with `step()`, `reset()`, and structured state representation.


 Environment Description

The environment simulates a content creator managing posts over multiple days.

 State

```json
{
  "followers": 1000,
  "engagement": 2.0,
  "fatigue": 0,
  "day": 1
}
```

 Actions

 `post_reel`
 `post_carousel`
 `take_break`
 `skip`


 Reward Logic

The reward system is designed to reflect real-world trade-offs:

Higher engagement → higher reward
Trending content → bonus reward
High fatigue → penalty
Random algorithm changes → occasional drop in reward

This ensures the agent learns **balanced strategies instead of greedy behavior.



 Tasks

Task 1 — Grow Followers

Increase followers to 1500.

 Task 2 — High Engagement

Maintain engagement above 5.0.

 Task 3 — Balanced Strategy

Grow followers while keeping fatigue low.

 Grading

Each task is evaluated using graders that return a score between **0.0 and 1.0**.

 API Endpoints

 Reset Environment

```
GET /reset
```

 Take Step

```
POST /step
```

Request body:

```json
{
  "action": "post_reel"
}
```

 Project Structure

```
content-env/
│
├── environment.py
├── inference.py
├── graders.py
├── tasks.py
├── openenv.yaml
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
```

 Setup Instructions

 1. Install dependencies

```
pip install -r requirements.txt
```

 2. Run locally

```
python app.py
```

 3. Run inference

```
python inference.py
```

 Deployment

The project is deployed using Hugging Face Spaces with Docker support.

 Key Highlights

 Real-world simulation (not a toy problem)
 Multi-objective optimization (growth vs fatigue)
 Dynamic reward system with randomness
 Fully OpenEnv compliant


 Conclusion

This environment demonstrates how AI agents can learn strategic decision-making in real-world scenarios like content creation and social media growth.
