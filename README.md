# 🤖 Learning Agent AI System

An advanced **Learning Agent** built using Python.

This project demonstrates how AI systems:

* learn from feedback
* improve recommendations over time
* adapt behavior dynamically
* store learning memory persistently

---

# 🧠 What is a Learning Agent?

A Learning Agent is an AI system that improves its behavior using experience and feedback.

Unlike traditional agents that always behave the same way, a Learning Agent can:

✅ observe outcomes
✅ receive feedback
✅ update future decisions
✅ improve recommendations over time

---

# 🚀 Real-World Applications

Learning Agents are used in:

* 🎬 Netflix movie recommendations
* 🎵 Spotify music recommendations
* 📱 TikTok feed ranking
* 🛒 Amazon product suggestions
* 🚗 Self-driving cars
* 🤖 ChatGPT fine-tuning
* 📈 Stock trading systems

---

# 🏗️ Architecture

```text
                    +----------------------+
                    |      User Input      |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Preference Extraction|
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Utility Calculation  |
                    |  (Movie Scoring)     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Recommendation Agent |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   Recommended Movie  |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |    User Feedback     |
                    |  (like / dislike)    |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   Learning Engine    |
                    |  (Reward/Penalty)    |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Updated Future Scores|
                    +----------------------+
```

---

# 🧠 Learning Workflow

```text
User Preferences
      ↓
Extract Genres
      ↓
Calculate Scores
      ↓
Recommend Movie
      ↓
Receive Feedback
      ↓
Update Learning Memory
      ↓
Improve Future Recommendations
```

---

# 📂 Project Structure

```text
learning-agent/
│
├── agent/
│   ├── movies.py
│   ├── utility.py
│   ├── learner.py
│   ├── memory.py
│   ├── processor.py
│   └── agent.py
│
├── data/
│   └── learning.json
│
├── main.py
├── README.md
└── .gitignore
```

---

# 📁 File Responsibilities

| File            | Responsibility             |
| --------------- | -------------------------- |
| `movies.py`     | Stores movie dataset       |
| `processor.py`  | Extracts user preferences  |
| `utility.py`    | Calculates movie scores    |
| `memory.py`     | Stores last recommendation |
| `learner.py`    | Handles learning system    |
| `agent.py`      | Main recommendation engine |
| `learning.json` | Persistent learning memory |

---

# 🔥 Core Learning Concept

The agent learns using:

```text
Positive Feedback  → Increase Score
Negative Feedback  → Decrease Score
```

---

# 🧠 Example Learning Behavior

## Before Learning

```text
Avengers Score = 28
```

---

## User Feedback

```text
like
```

---

## After Learning

```text
Avengers Score = 33
```

The agent now prefers Avengers more strongly in future recommendations.

---

# 🧠 Learning Memory

The system stores learning data inside:

```text
data/learning.json
```

Example:

```json
{
    "Avengers": 10,
    "Titanic": -5
}
```

Meaning:

* User likes Avengers 👍
* User dislikes Titanic 👎

---

# ⚙️ Features

✅ Movie recommendation system
✅ Utility-based scoring
✅ Learning from feedback
✅ Reward and penalty system
✅ Persistent learning memory
✅ Adaptive recommendations
✅ Modular AI architecture
✅ Real-time score updates

---

# 🧪 Example Usage

## User Input

```text
I like action movies
```

## Agent Output

```text
🎬 Recommended: Avengers
⭐ Score: 28
```

---

## User Feedback

```text
like
```

## Agent Learning

```text
Learned that you like Avengers 👍
```

---

# 🧪 Example Learning Flow

```text
You: I like action movies

Agent:
🎬 Recommended: Avengers
⭐ Score: 28

You: like

Agent:
Learned that you like Avengers 👍

You: I like action movies

Agent:
🎬 Recommended: Avengers
⭐ Score: 33
```

---

# 🚀 How to Run

---

# 1️⃣ Create Virtual Environment

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 2️⃣ Run the Agent

```bash
python main.py
```

---

# 🧪 Supported Commands

| Command                | Description            |
| ---------------------- | ---------------------- |
| `I like action movies` | Request recommendation |
| `like`                 | Positive feedback      |
| `dislike`              | Negative feedback      |
| `exit`                 | Close program          |

---

# 🧠 Key AI Concepts Learned

This project teaches:

* Learning Agents
* Feedback Loops
* Reward Systems
* Adaptive Behavior
* Persistent Memory
* Recommendation Systems
* Utility Functions
* Reinforcement Learning Basics

---

# 🔥 Major AI Concepts

| Concept           | Description             |
| ----------------- | ----------------------- |
| Feedback Loop     | Learning from outcomes  |
| Reward            | Positive reinforcement  |
| Penalty           | Negative reinforcement  |
| Utility Function  | Scoring decisions       |
| Adaptive System   | Improves over time      |
| Persistent Memory | Stores learned behavior |

---

# ⚠️ Current Limitations

* Uses predefined movie dataset
* No real machine learning model yet
* Basic preference understanding
* No neural networks
* Limited recommendation logic

---

# 🚀 Future Improvements

Planned upgrades:

* 🤖 LLM-based recommendations
* 📊 Machine learning algorithms
* 🧠 Personalized recommendation engine
* 🌐 API integration
* 📈 Dynamic scoring models
* 🎯 Deep learning recommendation systems
* 👤 Multi-user support

---

# 🎯 Learning Outcome

By building this project, you understand how modern AI systems:

* learn from user behavior
* improve recommendations
* adapt using feedback
* build personalized experiences
* optimize future decisions

This is the foundation of:

* recommendation engines
* reinforcement learning systems
* adaptive AI
* self-improving agents

---

# 👨‍💻 Author

Built as part of a deep learning journey into AI Agent Architectures.

---
