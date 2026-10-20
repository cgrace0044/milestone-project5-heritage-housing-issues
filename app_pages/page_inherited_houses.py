
import streamlit as st
import pandas as pd
import joblib


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
def load_inherited_houses():
    return pd.read_csv(
        "outputs/datasets/collection/inherited_houses.csv"
    )


def page_inherited_houses_body():

    st.write("### 🔑 Inherited Houses Valuation")

    st.info(
        "Lydia Doe has inherited four houses in Ames, Iowa. "
        "This page uses the trained machine learning model "
        "to estimate the sale price of each property."
    )

    pipeline = load_model()
    features = load_model_features()
    inherited_houses = load_inherited_houses()

    # Inspect the four inherited houses
    if st.checkbox("Inspect Four Inherited Houses"):
        st.write(
            f"The dataset contains {inherited_houses.shape[0]} "
            f"houses and {inherited_houses.shape[1]} attributes."
        )

        st.dataframe(inherited_houses)

    st.divider()

    st.write("### 🏠 Predicted Sale Prices")

    if st.button("Predict Inherited House Prices"):

        # Select only the model features
        X_inherited = inherited_houses[features].copy()

        # Predict the four house prices
        predictions = pipeline.predict(X_inherited)

        results = pd.DataFrame({
            "House": [
                f"House {i + 1}"
                for i in range(len(predictions))
            ],
            "Estimated Sale Price ($)": predictions
        })

        st.success(
            "The estimated sale prices of Lydia's "
            "four inherited houses are:"
        )

        st.dataframe(
            results.style.format({
                "Estimated Sale Price ($)": "${:,.0f}"
            }),
            hide_index=True
        )

        st.metric(
            "Total Estimated Value",
            f"${predictions.sum():,.0f}"
        )

        st.write(
            "These values are estimates based on historical "
            "house sales in Ames, Iowa. Actual sale prices "
            "may differ."
        )


if __name__ == "__main__":
    page_inherited_houses_body()
