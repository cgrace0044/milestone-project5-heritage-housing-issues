
from app_pages.multipage import MultiPage
from app_pages.page_summary import page_summary_body
from app_pages.page_house_price_study import page_house_price_study_body
from pathlib import Path
import streamlit as st


def load_css():
    css = Path("assets/style.css").read_text()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


app = MultiPage(app_name="Heritage Housing Issues")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("House Sales Price Study", page_house_price_study_body)

load_css()

app.run()
