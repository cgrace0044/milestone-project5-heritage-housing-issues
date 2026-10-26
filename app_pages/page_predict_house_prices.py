
import streamlit as st
import pandas as pd
import joblib
from datetime import datetime


@st.cache_resource
def load_model():
    return joblib.load(
        "outputs/ml_pipeline/predict_house_prices/v1/reg_pipeline.pkl"
    )


@st.cache_data
def load_model_features():
    return pd.read_csv(
        "outputs/ml_pipeline/predict_house_prices/v1/X_train.csv"
    ).columns.to_list()


@st.cache_data
def load_historical_data():
    train = pd.read_csv(
        "outputs/datasets/cleaned/TrainSetCleaned.csv"
    )

    test = pd.read_csv(
        "outputs/datasets/cleaned/TestSetCleaned.csv"
    )

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

        X_live["BsmtFinSF1"] = st.number_input(
            "Finished Basement Area (sq ft)",
            min_value=0,
            value=int(df["BsmtFinSF1"].median()),
            step=50
        )

        X_live["KitchenQual"] = st.selectbox(
            "Kitchen Quality",
            options=["Ex", "Gd", "TA", "Fa"],
            index=2,
            format_func=lambda value: {
                "Ex": "Excellent",
                "Gd": "Good",
                "TA": "Typical / Average",
                "Fa": "Fair"
            }[value]
        )

    return X_live


def page_predict_house_prices_body():

    st.write("### 🏠 Predict a House Price")

    st.info(
        "This page allows Lydia to estimate the sale price "
        "of any other house in Ames, Iowa, by entering "
        "its property characteristics."
    )

    pipeline = load_model()
    features = load_model_features()
    historical_df = load_historical_data()

    X_live = DrawHouseInputsWidgets(historical_df)

    # Match the model's training feature order
    X_live = X_live[features]

    st.divider()

    if st.button("Predict House Price"):

        prediction = pipeline.predict(X_live)[0]

        st.success("House price prediction completed.")

        st.metric(
            "Estimated House Sale Price",
            f"${prediction:,.0f}"
        )

        st.write(
            "This estimate is based on historical housing "
            "data from Ames, Iowa. Actual sale prices "
            "may differ."
        )


if __name__ == "__main__":
    page_predict_house_prices_body()
