import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import os

csv_path = os.path.join(os.path.dirname(__file__), 'data', 'train.csv')
dataset = pd.read_csv(csv_path)
dataset_novo = dataset[["OverallQual", "GrLivArea",
                        "GarageCars", "SalePrice", "SaleCondition"]].dropna() #deletando valores nulos

dataset_novo["SaleCondition"] = dataset_novo["SaleCondition"].map({'Normal': 0, 'Abnorml': 1, 'AdjLand':2, 'Alloca':3, 'Family':4, 'Partial':5})
dataset_novo["SaleCondition"]

x = dataset_novo[["OverallQual", "GrLivArea", "GarageCars", "SaleCondition"]] #x -> dados
y = dataset_novo["SalePrice"] #target y->target/gabarito

scaler = StandardScaler()
xEscalado = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(xEscalado, y, test_size=0.2, random_state=42)


knn = KNeighborsRegressor(n_neighbors=2)
knn.fit(x_train, y_train)
joblib.dump(knn, 'knn_model.pkl')
joblib.dump(scaler, 'scaler.pkl')