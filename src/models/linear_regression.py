#TEST ONLY


from src.preprocessing.preprocessing import test_df, train_df
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def evaluate(model, X, y, dataset_name="Dataset"):
    y_pred = model.predict(X)

    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    print(f"{dataset_name} set MSE: {mse}")
    print(f"{dataset_name} set R²: {r2}")


features = ['Open', 'High', 'Low', 'Volume', 'SMA_10', 'SMA_50', 'EMA_10', 'EMA_50', 'RSI_14']
target = 'Close'

X_train = train_df[features]
y_train = train_df[target]

X_test = test_df[features]
y_test = test_df[target]

model = LinearRegression()
model.fit(X_train, y_train)


evaluate(model, X_train, y_train, dataset_name="Training")
evaluate(model, X_test, y_test, dataset_name="Test")

