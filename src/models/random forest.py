from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from src.preprocessing.preprocessing import test_df, train_df
import numpy as np
import pandas as pd
import statsmodels.api as sm
"""Overfitted zu viel zu viel..."""
def evaluate(model, X, y, dataset_name="Dataset"):
    y_pred = model.predict(X)

    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)


    return mse, r2


n_estimators_values = [30, 100, 200]
max_depth_values = [5, 10, 15, None]
min_samples_split_values = [2, 5]
min_samples_leaf_values = [1, 4]


results_df = pd.DataFrame(columns=[
    'n_estimators', 'max_depth', 'min_samples_split', 'min_samples_leaf',
    'train_MSE', 'train_R²', 'test_MSE', 'test_R²'
])



features = ['Open', 'High', 'Low', 'Volume', 'SMA_10', 'SMA_50', 'EMA_10', 'EMA_50', 'RSI_14']
target = 'Close'

X_train = train_df[features]
y_train = train_df[target]
X_test = test_df[features]
y_test = test_df[target]


model = RandomForestRegressor(n_estimators=100, random_state=42)

model.fit(X_train, y_train)



for n_estimators in n_estimators_values:
    print("BIIIIG ITERATION LIKE MY ....")
    for max_depth in max_depth_values:
        for min_samples_split in min_samples_split_values:
            for min_samples_leaf in min_samples_leaf_values:
                print("iteration")
                model = RandomForestRegressor(
                    n_estimators=n_estimators,
                    max_depth=max_depth,
                    min_samples_split=min_samples_split,
                    min_samples_leaf=min_samples_leaf,
                    random_state=42
                )
                model.fit(X_train, y_train)

                train_mse, train_r2 = evaluate(model, X_train, y_train)
                test_mse, test_r2 = evaluate(model, X_test, y_test)


                results_df = results_df._append({
                    'n_estimators': n_estimators,
                    'max_depth': max_depth,
                    'min_samples_split': min_samples_split,
                    'min_samples_leaf': min_samples_leaf,
                    'train_MSE': train_mse,
                    'train_R²': train_r2,
                    'test_MSE': test_mse,
                    'test_R²': test_r2
                }, ignore_index=True)

#evaluation via OLS

independent_vars = ['n_estimators', 'max_depth', 'min_samples_split', 'min_samples_leaf']
ols_data = results_df[results_df['max_depth'].notna()]

#TEST
dependent_var_test = 'test_MSE'
X_test = ols_data[independent_vars]
y_test = ols_data[dependent_var_test]
X_test = sm.add_constant(X_test)
ols_model_test = sm.OLS(y_test, X_test).fit()

#TRAIN
dependent_var_train = 'train_MSE'
X_train = ols_data[independent_vars]
y_train = ols_data[dependent_var_train]
X_train = sm.add_constant(X_train)  # Add constant for the intercept
ols_model_train = sm.OLS(y_train, X_train).fit()


print("\n=== TRAIN ===")
print(ols_model_train.summary())
print("=== TEST ===")
print(ols_model_test.summary())

