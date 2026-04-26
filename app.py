from fastapi import FastAPI
import pickle
import logging



# Setup logging
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

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
     # Log input + output
    logging.info(f"Input: {hours}, Prediction: {prediction[0]}")

    return {"prediction": int(prediction[0])}
   