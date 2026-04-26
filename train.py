import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
#load dataset
df = pd.read_csv("data/data.csv")
#define X&Y
X = df[["hours"]]
Y=df["pass"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)
#fit to model
model = LogisticRegression()
model.fit(X_train,y_train)

# Evaluate
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)
if accuracy < 0.5:
    raise Exception("Model accuracy too low!")
# Save model
pickle.dump(model, open("model.pkl", "wb"))


print("Model trained and saved!")