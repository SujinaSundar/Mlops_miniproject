from fastapi import FastAPI
import pickle

app = FastAPI()

#Load model
model = pickle.load(open("model.pickle","rb"))

#home route
@app.get("/")
def home():
    return {"message":"Ml api is running"}

@app.get("/predict")
def predict(hours:float):
    prediction = model.predict([[hours]])
    return {"prediction": int(prediction[0])}