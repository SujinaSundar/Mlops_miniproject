import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
#load dataset
df = pd.read_csv("data/data.csv")
#define X&Y
X = df[["hours"]]
Y=df["pass"]
#fit to model
model = LogisticRegression()
model.fit(X,Y)
pickle.dump(model,open("model.pickle","wb"))

print("Model trained and saved!")