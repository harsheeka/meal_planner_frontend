# streamlit_app.py
import streamlit as st
import requests

BACKEND_URL = "https://meal-planner-backend-8hs4.onrender.com"

st.set_page_config(page_title="Weekly Meal Planner", layout="wide")
st.title("🍛 Weekly Meal Planner")

def chip(text):
    return f"`{text}`"

city = st.text_input("City:", "Amritsar")
month = st.selectbox("Month:", [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
])

if st.button("Generate Meal Plan"):
    url = f"{BACKEND_URL}?city={city}&month={month}&format=json"
    res = requests.get(url)

    if res.status_code != 200:
        st.error("Backend error")
        st.stop()

    data = res.json()

    if "week_plan" not in data:
        st.error("No structured plan returned")
        st.stop()

    week = data["week_plan"]
    shopping_grouped = data["weekly_shopping_grouped"]

    st.header(f"📅 Weekly Meal Plan for {city} ({month})")
    st.write("---")

    for day in week:
        st.subheader(f"Day {day['day']}")
        col1, col2, col3 = st.columns(3)

        # Breakfast
        with col1:
            st.markdown("### 🍽️ Breakfast")
            st.markdown(f"**Dish:** {day['breakfast']['name']}")
            st.write(", ".join([chip(i) for i in day['breakfast']['ingredients']]))
            st.markdown("**Markets:**")
            st.write(", ".join([chip(m) for m in day['breakfast']['markets']]))
        
        # Lunch
        with col2:
            st.markdown("### 🍱 Lunch")
            st.markdown(f"**Dish:** {day['lunch']['name']}")
            st.write(", ".join([chip(i) for i in day['lunch']['ingredients']]))
            st.markdown("**Markets:**")
            st.write(", ".join([chip(m) for m in day['lunch']['markets']]))

        # Dinner
        with col3:
            st.markdown("### 🍛 Dinner")
            st.markdown(f"**Dish:** {day['dinner']['name']}")
            st.write(", ".join([chip(i) for i in day['dinner']['ingredients']]))
            st.markdown("**Markets:**")
            st.write(", ".join([chip(m) for m in day['dinner']['markets']]))

        st.write("---")

    # Weekly Shopping List
    st.header("🛒 Weekly Shopping List")

    cols = st.columns(2)
    idx = 0

    for category, items in shopping_grouped.items():
        with cols[idx]:
            with st.expander(f"{category} ({len(items)})"):
                for item in items:
                    st.markdown(f"- {chip(item)}")
        idx = 1 - idx
