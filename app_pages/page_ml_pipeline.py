import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


def page_ml_pipeline_body():

    st.write("### 🤖 ML Pipeline Performance")

    # Load saved model artifacts
    version = "v1"
    model_path = Path(
        f"outputs/ml_pipeline/predict_house_prices/{version}"
    )

    pipeline = joblib.load(model_path / "reg_pipeline.pkl")

    features = pd.read_csv(
        model_path / "X_train.csv"
    ).columns.to_list()

    # Model performance summary
    st.info(
        "The house price regression model achieved an "
        "**R² score of 0.923 on the training dataset** "
        "and **0.813 on the test dataset**. "
        "Both scores exceed the project's minimum "
        "requirement of 0.75."
    )

    st.divider()

    # Pipeline steps
    st.write("#### ML Pipeline Steps")

    st.write(pipeline)

    st.caption(
        "The pipeline uses 150 trees. Parameters set to their "
        "default values (max_depth=None, max_features=1.0 and "
        "min_impurity_decrease=0.0) are not shown in the pipeline "
        "summary but are still applied."
    )

    st.divider()

    # Model features
    st.write("#### Features Used to Train the Model")

    st.write(
        "The model uses nine property attributes "
        "to predict house sale prices."
    )

    st.write(features)

    st.divider()

    # Performance metrics
    st.write("#### Model Evaluation Results")

    performance = pd.DataFrame({
        "Metric": [
            "R² Score",
            "Mean Absolute Error (MAE)",
            "Root Mean Squared Error (RMSE)"
        ],
        "Training": [
            "0.923",
            "$12,659",
            "$21,711"
        ],
        "Test": [
            "0.813",
            "$19,293",
            "$35,892"
        ]
    })

    st.table(performance)

    st.divider()

    # Feature importance
    st.write("#### Feature Importance")

    st.write(
        "The feature importance chart shows which property "
        "attributes have the greatest influence on the "
        "model's house price predictions."
    )

    if st.checkbox("Show Feature Importance Plot"):
        st.image(
            str(model_path / "features_importance.png"),
            use_container_width=True
        )

    st.divider()

    # Interpretation
    st.write("#### Model Performance Interpretation")

    st.success(
        "The model successfully met the project's "
        "performance requirement, achieving an R² "
        "score above 0.75 on both the training "
        "and test datasets."
    )

    st.write(
        "On the test dataset, the model's predictions "
        "differed from actual sale prices by approximately "
        "**$19,293 on average**."
    )

    st.write(
        "This means Lydia can use the model to estimate "
        "house prices in Ames, Iowa, while understanding "
        "that predictions are estimates rather than "
        "guaranteed selling prices."
    )


if __name__ == "__main__":
    page_ml_pipeline_body()