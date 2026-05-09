from sklearn.linear_model import LinearRegression
import numpy as np

def predict_future_price(data):

    data = data.reset_index()

    data["Days"] = np.arange(len(data))

    X = data[["Days"]]

    y = data["Close"]

    model = LinearRegression()

    model.fit(X, y)

    future_day = np.array([[len(data) + 30]])

    prediction = model.predict(future_day)

    return prediction[0]