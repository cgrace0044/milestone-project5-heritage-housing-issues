
import streamlit as st
import pandas as pd
from src.data_management import load_pkl_file
from src.machine_learning.predictive_analysis_ui import predict_inherited_house_prices


def page_inherited_houses_body():

    st.write("### 🔑 Inherited Houses Valuation")

    st.info(
        "Lydia Doe has inherited four houses in Ames, Iowa. "
        "This page uses the trained machine learning model "
        "to estimate the sale price of each property."
    )

    # Load pipeline files
    version = 'v1'
    path = f"outputs/ml_pipeline/predict_house_prices/{version}"

    pipeline = load_pkl_file(f"{path}/reg_pipeline.pkl")
    features = pd.read_csv(f"{path}/X_train.csv").columns.to_list()

    # Load inherited houses data
    inherited_houses = pd.read_csv(
        "outputs/datasets/collection/inherited_houses.csv"
    )

    st.write("---")

    # Display inherited houses
    st.write("#### 🏡 The Four Inherited Houses")

    st.write(
        "Explore the property details before generating "
        "their estimated sale prices."
    )

    if st.checkbox("Show Inherited Houses Data"):

        st.write(
            f"The dataset contains {inherited_houses.shape[0]} "
            f"houses and {inherited_houses.shape[1]} attributes."
        )

        st.dataframe(inherited_houses, use_container_width=True)

    st.write("---")

    # Predict inherited house prices
    st.write("#### 💰 Property Valuation")

    st.write(
        "Click the button below to estimate the sale price "
        "of each inherited house and their combined value."
    )

    if st.button(
        "Predict House Prices",
        icon=":material/house:",
        type="secondary"
    ):

        predict_inherited_house_prices(
            X_live=inherited_houses,
            house_features=features,
            pipeline=pipeline
        )


if __name__ == "__main__":
    page_inherited_houses_body()
