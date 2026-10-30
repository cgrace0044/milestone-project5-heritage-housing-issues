
import streamlit as st
import pandas as pd
from datetime import datetime
from src.data_management import load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_house_price


@st.cache_data
def load_historical_data():

    train = pd.read_csv("outputs/datasets/cleaned/TrainSetCleaned.csv")
    test = pd.read_csv("outputs/datasets/cleaned/TestSetCleaned.csv")

    return pd.concat([train, test], ignore_index=True)


def DrawHouseInputsWidgets(df):

    st.write("### 🏡 Enter House Details")

    st.write(
        "Enter the characteristics of a house in Ames, Iowa, "
        "to estimate its sale price."
    )

    col1, col2, col3 = st.columns(3)

    X_live = pd.DataFrame(index=[0])

    with col1:
        X_live["OverallQual"] = st.number_input(
            "Overall House Quality (1–10)",
            min_value=1,
            max_value=10,
            value=5,
            step=1
        )

        X_live["GrLivArea"] = st.number_input(
            "Above-Ground Living Area (sq ft)",
            min_value=0,
            value=int(df["GrLivArea"].median()),
            step=50
        )

        X_live["GarageArea"] = st.number_input(
            "Garage Area (sq ft)",
            min_value=0,
            value=int(df["GarageArea"].median()),
            step=25
        )

    with col2:
        X_live["YearBuilt"] = st.number_input(
            "Year Built",
            min_value=1800,
            max_value=datetime.now().year,
            value=int(df["YearBuilt"].median()),
            step=1
        )

        X_live["TotalBsmtSF"] = st.number_input(
            "Total Basement Area (sq ft)",
            min_value=0,
            value=int(df["TotalBsmtSF"].median()),
            step=50
        )

        X_live["YearRemodAdd"] = st.number_input(
            "Year Built or Last Remodelled",
            min_value=1800,
            max_value=datetime.now().year,
            value=int(df["YearRemodAdd"].median()),
            step=1
        )

    with col3:
        X_live["1stFlrSF"] = st.number_input(
            "First-Floor Area (sq ft)",
            min_value=0,
            value=int(df["1stFlrSF"].median()),
            step=50
        )

    return X_live


def page_predict_house_prices_body():

    st.write("### 🏠 Predict a House Price")

    st.info(
        "This page allows Lydia to estimate the sale price "
        "of any other house in Ames, Iowa, by entering "
        "its property characteristics."
    )

    # Load pipeline and datasets
    version = 'v1'
    path = f"outputs/ml_pipeline/predict_house_prices/{version}"

    pipeline = load_pkl_file(f"{path}/reg_pipeline.pkl")
    features = pd.read_csv(f"{path}/X_train.csv").columns.to_list()
    historical_df = load_historical_data()

    # Draw house input widgets
    X_live = DrawHouseInputsWidgets(historical_df)

    st.divider()

    # Predict house price
    if st.button("Predict House Price"):

        predict_house_price(
            X_live=X_live,
            house_features=features,
            pipeline=pipeline
        )


if __name__ == "__main__":
    page_predict_house_prices_body()
