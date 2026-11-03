
import streamlit as st
import pandas as pd
from datetime import datetime
from src.data_management import load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_house_price


def page_predict_house_prices_body():

    # load predict house price files
    version = 'v1'
    pipeline = load_pkl_file(
        f"outputs/ml_pipeline/predict_house_prices/{version}/reg_pipeline.pkl")
    features = (pd.read_csv(
        f"outputs/ml_pipeline/predict_house_prices/{version}/X_train.csv")
        .columns
        .to_list()
        )

    st.write("### 🏠 Predict a House Price")

    st.info(
        "This page allows Lydia to estimate the sale price "
        "of any other house in Ames, Iowa, by entering "
        "its property attributes."
    )

    st.write("---")

    # Generate Live Data
    X_live = DrawInputsWidgets()

    st.write("---")

    # predict on live data
    if st.button(
        "Predict House Price",
        icon=":material/house:",
    ):
        predict_house_price(X_live, features, pipeline)


def DrawInputsWidgets():

    # load dataset
    train = pd.read_csv("outputs/datasets/cleaned/TrainSetCleaned.csv")
    test = pd.read_csv("outputs/datasets/cleaned/TestSetCleaned.csv")
    df = pd.concat([train, test], ignore_index=True)

    st.write("### 🏡 Enter House Details")

    st.write(
        "Enter the characteristics of a house in Ames, Iowa, "
        "to estimate its sale price."
    )

    # we create input widgets only for 7 features
    col1, col2, col3 = st.columns(3)

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type (numerical)
    # and set initial values
    with col1:
        feature = "OverallQual"
        st_widget = st.number_input(
            label="Overall House Quality (1–10)",
            min_value=1,
            max_value=10,
            value=5,
            step=1
        )
    X_live[feature] = st_widget

    with col1:
        feature = "GrLivArea"
        st_widget = st.number_input(
            label="Above-Ground Living Area (sq ft)",
            min_value=0,
            value=int(df[feature].median()),
            step=50
        )
    X_live[feature] = st_widget

    with col1:
        feature = "GarageArea"
        st_widget = st.number_input(
            label="Garage Area (sq ft)",
            min_value=0,
            value=int(df[feature].median()),
            step=25
        )
    X_live[feature] = st_widget

    with col2:
        feature = "YearBuilt"
        st_widget = st.number_input(
            label="Year Built",
            min_value=1800,
            max_value=datetime.now().year,
            value=int(df[feature].median()),
            step=1
        )
    X_live[feature] = st_widget

    with col2:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label="Total Basement Area (sq ft)",
            min_value=0,
            value=int(df[feature].median()),
            step=50
        )
    X_live[feature] = st_widget

    with col2:
        feature = "YearRemodAdd"
        st_widget = st.number_input(
            label="Year Last Remodelled",
            min_value=1800,
            max_value=datetime.now().year,
            value=int(df[feature].median()),
            step=1
        )
    X_live[feature] = st_widget

    with col3:
        feature = "1stFlrSF"
        st_widget = st.number_input(
            label="First-Floor Area (sq ft)",
            min_value=0,
            value=int(df[feature].median()),
            step=50
        )
    X_live[feature] = st_widget

    return X_live


if __name__ == "__main__":
    page_predict_house_prices_body()
