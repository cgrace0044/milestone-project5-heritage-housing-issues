
import streamlit as st
import pandas as pd

from src.data_management import load_pkl_file
from src.machine_learning.evaluate_reg import regression_performance


def page_ml_pipeline_body():

    st.write("### 🤖 ML Pipeline Performance")

    st.info(
        "The final machine learning pipeline predicts house sale prices "
        "using seven selected property attributes. This page presents "
        "the pipeline, feature importance, and model performance "
        "on the training and test datasets."
    )

    version = "v1"
    path = f"outputs/ml_pipeline/predict_house_prices/{version}"

    pipeline = load_pkl_file(f"{path}/reg_pipeline.pkl")

    X_train = pd.read_csv(f"{path}/X_train.csv")
    X_test = pd.read_csv(f"{path}/X_test.csv")

    y_train = pd.read_csv(f"{path}/y_train.csv").squeeze("columns")
    y_test = pd.read_csv(f"{path}/y_test.csv").squeeze("columns")

    st.write("---")

    # ML Pipeline
    st.write("#### ⚙️ ML Pipeline")

    st.write(
        "The final model uses **ExtraTreesRegressor** with optimised "
        "hyperparameters and the seven most important house attributes."
    )

    if st.checkbox("View ML Pipeline"):

        st.write(pipeline)

        st.caption(
            "The hyperparameters `max_features=1.0` and "
            "`min_impurity_decrease=0.0` do not appear above because "
            "they match the default values of ExtraTreesRegressor. "
            "Both were explicitly defined during optimisation."
        )

    st.write("---")

    # Selected features
    st.write("#### 🏡 Selected House Attributes")

    st.write(
        "- Overall Quality (`OverallQual`)\n"
        "- Above-Ground Living Area (`GrLivArea`)\n"
        "- Year Built (`YearBuilt`)\n"
        "- Garage Area (`GarageArea`)\n"
        "- Total Basement Area (`TotalBsmtSF`)\n"
        "- First-Floor Area (`1stFlrSF`)\n"
        "- Year Last Remodelled (`YearRemodAdd`)"
    )

    if st.checkbox("View Feature Importance"):

        col1, col2 = st.columns([3, 1])

        with col1:
            st.image(f"{path}/features_importance.png")

        st.success(
            "**Feature importance interpretation:** "
            "Overall quality was the most important feature "
            "by a considerable margin."
        )

    st.write("---")

    # Model evaluation
    st.write("#### 📊 Model Evaluation Results")

    regression_performance(
        X_train,
        y_train,
        X_test,
        y_test,
        pipeline
    )


if __name__ == "__main__":
    page_ml_pipeline_body()
