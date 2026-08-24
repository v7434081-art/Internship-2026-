import pandas as pd
import streamlit as st

def all_option(values: pd.Series) -> list[str]:
    return ["All"] + values.unique().tolist()

st.title("Student Dashboard")

df = pd.read_csv("students.csv")

with st.sidebar:
    st.write("**Filters**")
    branch = st.selectbox("Branch", all_option(df["branch"]), key="filter_branch")
    city = st.selectbox("City", all_option(df["city"]), key="filter_city")

st.write("**All students**")
st.dataframe(df)
st.write(f"Total: {len(df)} students")

filtered = df
if branch != "All":
    filtered = filtered[filtered["branch"] == branch]
if city != "All":
    filtered = filtered[filtered["city"] == city]

st.write(f"**Filtered: {len(filtered)} students**")
st.dataframe(filtered)

if len(filtered) > 0:
    st.write(f"Average marks: {filtered['marks'].mean():.1f}")
