from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import List
import os

app = FastAPI()

# Enable CORS to allow requests from R Shiny apps
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For demo; restrict this in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the CSV file once when the app starts
CSV_PATH = os.path.join(os.path.dirname(__file__), "Groups_data.csv")
df = pd.read_csv(CSV_PATH)

@app.get("/get_data/")
def get_data(groups: List[str] = Query(...)):
    filtered_df = df[df["Group"].isin(groups)]
    return filtered_df.to_dict(orient="records")
