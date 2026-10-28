
from app_pages.multipage import MultiPage
from app_pages.page_summary import page_summary_body
from app_pages.page_data_cleaning import page_data_cleaning_body
from app_pages.page_house_price_study import page_house_price_study_body
from app_pages.page_inherited_houses import page_inherited_houses_body
from app_pages.page_predict_house_prices import page_predict_house_prices_body
from app_pages.page_ml_pipeline import page_ml_pipeline_body
from app_pages.page_project_hypothesis_body import page_project_hypothesis_body

from pathlib import Path
import streamlit as st


def load_css():
    css = Path("assets/style.css").read_text()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


app = MultiPage(app_name="Heritage Housing Issues")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Data Cleaning", page_data_cleaning_body)
app.add_page("House Sales Price Study", page_house_price_study_body)
app.add_page("Inherited Houses Valuation", page_inherited_houses_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("Predict a House Price", page_predict_house_prices_body)
app.add_page("ML Pipeline Performance", page_ml_pipeline_body)

load_css()

app.run()
