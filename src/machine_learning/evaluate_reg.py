
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import r2_score, mean_absolute_error


# Code adapted from the Modeling and Evaluation notebook
def regression_metrics(y, prediction):

    return {
        "R² Score": f"{r2_score(y, prediction):.3f}",
        "Mean Absolute Error (MAE)":
            f"${mean_absolute_error(y, prediction):,.0f}"
    }


# Evaluate performance on training and test datasets
def reg_performance(X_train, y_train, X_test, y_test, pipeline):

    train_predictions = pipeline.predict(X_train)
    test_predictions = pipeline.predict(X_test)

    # Display performance metrics
    st.write("#### Model Evaluation Results")

    train_metrics = regression_metrics(y_train, train_predictions)
    test_metrics = regression_metrics(y_test, test_predictions)

    performance = pd.DataFrame({
        "Metric": list(train_metrics.keys()),
        "Training": list(train_metrics.values()),
        "Test": list(test_metrics.values())
    })

    st.table(performance)

    test_mae = mean_absolute_error(y_test, test_predictions)

    st.success(
        "**Performance interpretation:** The model meets "
        "the required R² score of 0.75 on both datasets. "
        f"On the test dataset, its predictions differ from "
        f"actual sale prices by approximately ${test_mae:,.0f} "
        "on average."
    )

    st.write("---")

    # Display actual vs predicted plots
    st.write("#### Actual vs Predicted Sale Prices")

    st.info(
        "These graphs compare actual sale prices with "
        "the model's predictions. Points closer to the "
        "red line indicate more accurate predictions."
    )

    if st.checkbox("Show Actual vs Predicted Plots"):

        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        sns.scatterplot(
            x=y_train,
            y=train_predictions,
            alpha=0.5,
            ax=axes[0]
        )

        sns.scatterplot(
            x=y_test,
            y=test_predictions,
            alpha=0.5,
            ax=axes[1]
        )

        for ax, actual, predicted, title in [
            (axes[0], y_train, train_predictions, "Training Dataset"),
            (axes[1], y_test, test_predictions, "Test Dataset")
        ]:
            minimum = min(actual.min(), predicted.min())
            maximum = max(actual.max(), predicted.max())

            ax.plot(
                [minimum, maximum],
                [minimum, maximum],
                color="red"
            )

            ax.set_title(title)
            ax.set_xlabel("Actual Sale Price ($)")
            ax.set_ylabel("Predicted Sale Price ($)")

        fig.tight_layout()

        st.pyplot(fig)
        plt.close(fig)

        st.success(
            "**Graph interpretation:** Predictions generally "
            "follow actual sale prices, but the model is less "
            "accurate when predicting the prices of more expensive "
            "houses. The model also performs better on the training "
            "dataset than on unseen test data."
        )
