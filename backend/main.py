from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
from src.preprocessors import load_stopwords
import calamancy # load in states in future due to slow loading time

app = FastAPI()

# Allow SvelteKit to make API calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def load_model():
    app.state.model = load("./src/notebooks/serialized/models/RandomForestClassifier.pkl") # temporarily using RF
    app.state.calamancy = calamancy.load("tl_calamancy_md-0.2.0")
    app.state.stopwords = load_stopwords()

@app.get("/api/hello")
async def hello():
    return {"message": "I'm from the backend! Yay! Frontend and backend is connected!"}
