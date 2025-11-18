# Indian Meal Planner Frontend

### Streamlit • FastAPI Client • Neo4j Aura • Llama-3.1

<p align="center">
  <img src="https://via.placeholder.com/900x250.png?text=Indian+Meal+Planner+%7C+Streamlit+Frontend" />
</p>

<p align="center">
The interactive user interface for the Meal Planner project — powered by FastAPI and a Neo4j Knowledge Graph.
</p>

---

## Features

* City and month selector
* 7-day meal plan visualization
* Breakfast, lunch, and dinner segmentation
* Ingredient badges
* Market-wise availability display
* Fully grouped weekly shopping list
* Communicates with backend via REST API

---

## Tech Stack

![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![Neo4j](https://img.shields.io/badge/Neo4j-KnowledgeGraph-blue?logo=neo4j)

---

## Folder Structure

```
meal-planner-frontend/
│── streamlit_app.py
│── requirements.txt
└── README.md
```

---

## Setup

```
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## Connect Backend

Update the backend URL inside `streamlit_app.py`:

```python
BACKEND_URL = "https://your-backend.onrender.com/mealplan"
```

Ensure that the backend is deployed and accessible publicly.

---

## Backend Repository (Required)

The frontend depends on the FastAPI backend for all meal-plan generation.
Refer to the backend repository for setup, environment variables, Neo4j configuration, and API details:

```
https://github.com/harsheeka/meal_planner_backend
```

The backend must be running locally or deployed before the frontend can function.

---

## Deployment (Streamlit Cloud)

1. Visit: [https://share.streamlit.io](https://share.streamlit.io)
2. Connect your GitHub repository
3. Select `streamlit_app.py` as the entry script
4. Deploy

Your final app URL will look like:

```
https://mealplanner-frontend.streamlit.app
```

---
