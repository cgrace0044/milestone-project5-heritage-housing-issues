
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_reg import reg_performance


def page_ml_pipeline_body():

    # Load pipeline files
    version = 'v1'
    path = f"outputs/ml_pipeline/predict_house_prices/{version}"

    pipeline = load_pkl_file(f"{path}/reg_pipeline.pkl")
    features_importance = plt.imread(f"{path}/features_importance.png")
    X_train = pd.read_csv(f"{path}/X_train.csv")
    X_test = pd.read_csv(f"{path}/X_test.csv")
    y_train = pd.read_csv(f"{path}/y_train.csv").squeeze("columns")
    y_test = pd.read_csv(f"{path}/y_test.csv").squeeze("columns")

    st.write("### 🤖 ML Pipeline Performance")

    st.info(
        "The house price regression model achieved an "
        "**R² score of 0.912 on the training dataset** "
        "and **0.808 on the test dataset**. "
        "Both scores exceed the project's minimum requirement of 0.75."
    )

    st.write("---")

    # ML pipeline
    st.write("#### ML Pipeline Steps")
    st.write(pipeline)

    st.caption(
        "The final pipeline applies numerical transformations and "
        "feature scaling before predicting house prices using an "
        "ExtraTreesRegressor."
    )

    st.caption(
        "Note: max_features=1.0 and min_impurity_decrease=0.0 are not "
        "shown in the pipeline display because they use their default values."
    )

    st.write("---")

    # Features
    st.write("#### Features Used to Train the Model")
    st.write("The model uses seven property attributes to predict house sale prices.")
    st.write(X_train.columns.to_list())

    st.write("#### Feature Importance")

    st.info(
        "The feature importance chart shows which property attributes "
        "contribute most to the model's house price predictions."
    )

    if st.checkbox("Show Feature Importance Plot"):
        col1, col2, col3 = st.columns([1, 3, 1])

        with col2:
            st.image(features_importance, use_container_width=True)

    st.write("---")

    # Pipeline performance
    st.write("### Pipeline Performance")
    reg_performance(X_train, y_train, X_test, y_test, pipeline)


if __name__ == "__main__":
    page_ml_pipeline_body()


