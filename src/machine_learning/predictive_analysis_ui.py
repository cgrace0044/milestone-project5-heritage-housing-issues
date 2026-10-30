
import streamlit as st


def predict_inherited_house_prices(X_live, house_features, pipeline):

    # from live data, subset features related to this pipeline
    X_live_house = X_live.filter(house_features)

    # predict
    house_predictions = pipeline.predict(X_live_house)

    # create a logic to display the results
    st.write("#### 🏠 Estimated Sale Prices")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**House 1**")
        st.write(f"${house_predictions[0]:,.0f}")

    with col2:
        st.write("**House 2**")
        st.write(f"${house_predictions[1]:,.0f}")

    with col3:
        st.write("**House 3**")
        st.write(f"${house_predictions[2]:,.0f}")

    with col4:
        st.write("**House 4**")
        st.write(f"${house_predictions[3]:,.0f}")

    st.write("**Combined Estimated Value**")
    st.markdown(f"### 💰 ${house_predictions.sum():,.0f}")

    st.info(
        "These estimates are based on historical house sales "
        "in Ames, Iowa. Actual sale prices may differ."
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
