def predict_house_price(X_live, features, pipeline):

    # Select the features used by the model
    X_live = X_live[features]

    # Predict house prices
    predictions = pipeline.predict(X_live)

    return predictions