# FastAPI Model Deployment on Health Universe

Welcome to the Health Universe platform, where we standardize the deployment of statistical and machine learning models using FastAPI. FastAPI is a modern, fast, web framework for building APIs with Python 3.7+ based on standard Python type hints.

This project provides a sample implementation of a FastAPI model deployment on the Health Universe platform. In this example, we will show you how to create a simple linear regression model using FastAPI.

## Prerequisites

To get started, you'll need to have Python 3.7 or later installed on your machine, as well as the following packages:

```
pip install fastapi
pip install numpy
pip install pandas
pip install uvicorn
```

## Creating a FastAPI Model

Let's create a simple linear regression model using FastAPI.

```
from fastapi import FastAPI
import numpy as np
import pandas as pd


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World"}

@app.post("/predict")
async def predict(x: float, y: float):
    # Creating a sample data
    data = {"x": [x], "y": [y]}
    df = pd.DataFrame(data)
    
    # Calculating the regression coefficients
    b = np.cov(df["x"], df["y"])[0, 1] / np.var(df["x"])
    a = df["y"].mean() - b * df["x"].mean()
    
    # Predicting the result
    result = a + b * x
    return {"prediction": result}
```

## Running the FastAPI Model

You can run the FastAPI model using the following command:

```
uvicorn main:app --reload
```

You should now be able to make predictions using the /predict endpoint by sending a POST request with the parameters x and y.

## Conclusion

This is a simple example of how you can create and deploy a FastAPI model on the Health Universe platform. You can use this sample implementation as a starting point for your own projects and customize it to your specific needs.

We hope this helps and we look forward to seeing your contributions to the Health Universe platform.