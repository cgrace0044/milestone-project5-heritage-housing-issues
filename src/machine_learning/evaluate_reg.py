
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


# Code adapted from the Modeling and Evaluation notebook
def regression_performance(X_train, y_train, X_test, y_test, pipeline):

    train_results = regression_evaluation(X_train, y_train, pipeline)
    test_results = regression_evaluation(X_test, y_test, pipeline)

    performance = pd.DataFrame({
        "Train Set": train_results,
        "Test Set": test_results
    })

    st.table(performance)

    st.info(
        "**Performance interpretation:**\n\n"
        "- **R²:** The model achieved 0.925 on the training set "
        "and 0.825 on the test set, meeting the client's "
        "minimum requirement of 0.75.\n"
        "- **Prediction error:** The average absolute error was "
        "approximately 13,489 on the training set and 19,714 "
        "on the test set. The higher RMSE indicates some "
        "larger prediction errors.\n"
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

        regression_evaluation_plots(
            X_train,
            y_train,
            X_test,
            y_test,
            pipeline,
            alpha_scatter=0.5
        )

        st.write(
            "**Graph interpretation:** Predictions generally follow actual "
            "sale prices, although errors are larger for more expensive houses. "
            "The model performs better on training data than on unseen test data."
        )


# Regression Evaluation function taken from Modelling and Evaluation Notebook
def regression_evaluation(X, y, pipeline):

    prediction = pipeline.predict(X)

    return {
        "R² Score": r2_score(y, prediction).round(3),
        "Mean Absolute Error": mean_absolute_error(y, prediction).round(3),
        "Mean Squared Error": mean_squared_error(y, prediction).round(3),
        "Root Mean Squared Error":
            np.sqrt(mean_squared_error(y, prediction)).round(3)
    }


# Regression Evaluation Plots function taken from Modelling and Evaluation Notebook
def regression_evaluation_plots(
    X_train, y_train, X_test, y_test, pipeline, alpha_scatter=0.5
):

    pred_train = pipeline.predict(X_train)
    pred_test = pipeline.predict(X_test)

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

    sns.scatterplot(
        x=y_train, y=pred_train,
        alpha=alpha_scatter, ax=axes[0]
    )
    sns.lineplot(x=y_train, y=y_train, color='red', ax=axes[0])
    axes[0].set_xlabel("Actual")
    axes[0].set_ylabel("Predictions")
    axes[0].set_title("Train Set")

    sns.scatterplot(
        x=y_test, y=pred_test,
        alpha=alpha_scatter, ax=axes[1]
    )
    sns.lineplot(x=y_test, y=y_test, color='red', ax=axes[1])
    axes[1].set_xlabel("Actual")
    axes[1].set_ylabel("Predictions")
    axes[1].set_title("Test Set")

    st.pyplot(fig)
    plt.close(fig)
