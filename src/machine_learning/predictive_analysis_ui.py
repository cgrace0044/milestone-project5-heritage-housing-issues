
import streamlit as st
import pandas as pd


def predict_inherited_house_prices(X_live, house_features, pipeline):

    # from live data, subset features related to this pipeline
    X_live_house = X_live.filter(house_features)

    # predict
    house_predictions = pipeline.predict(X_live_house)

    # create a logic to display the results
    results = pd.DataFrame({
        "House": [f"House {i + 1}" for i in range(len(house_predictions))],
        "Estimated Sale Price ($)": house_predictions
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
        f"${house_predictions.sum():,.0f}"
    )

    st.write(
        "These values are estimates based on historical "
        "house sales in Ames, Iowa. Actual sale prices may differ."
    )

    return house_predictions


def predict_house_price(X_live, house_features, pipeline):

    # from live data, subset features related to this pipeline
    X_live_house = X_live.filter(house_features)

    # predict
    house_prediction = pipeline.predict(X_live_house)

    # create a logic to display the results
    st.success("House price prediction completed.")

    st.metric(
        "Estimated House Sale Price",
        f"${house_prediction[0]:,.0f}"
    )

    st.write(
        "This estimate is based on historical housing "
        "data from Ames, Iowa. Actual sale prices may differ."
    )

    return house_prediction
