#  Indian Meal Planner Frontend

### Streamlit • FastAPI Client • Neo4j Aura • Llama-3.1

<p align="center">
  <img src="https://via.placeholder.com/900x250.png?text=Indian+Meal+Planner+%7C+Streamlit+Frontend" />
</p>

<p align="center">
The interactive user interface for the Meal Planner project — powered by FastAPI and a Neo4j Knowledge Graph.
</p>

---

##  Features

*  City + month selector
*  Weekly meal plan display
*  Breakfast/Lunch/Dinner cards
*  Ingredient chips
*  Market availability
*  Fully grouped weekly shopping list
*  Calls backend via HTTP

---

##  Tech Stack

![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![Neo4j](https://img.shields.io/badge/Neo4j-KnowledgeGraph-blue?logo=neo4j)

---

##  Folder Structure

```
meal-planner-frontend/
│── streamlit_app.py
│── requirements.txt
└── README.md
```

---

##  Setup

```
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

##  Connect Backend

Edit `streamlit_app.py`:

```python
BACKEND_URL = "https://your-backend.onrender.com/mealplan"
```

---

##  Deployment (Streamlit Cloud)

1. Go to [https://share.streamlit.io](https://share.streamlit.io)
2. Connect GitHub repo
3. Select `streamlit_app.py`
4. Deploy!

Final URL looks like:

```
https://mealplanner-frontend.streamlit.app
```

---
