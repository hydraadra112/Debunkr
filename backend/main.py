from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
from src.preprocessors import load_stopwords, preprocess_text, parse_and_clean_link
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
async def load_dependencies():
    app.state.model = load("./src/notebooks/serialized/models/RandomForestClassifier.pkl") # temporarily using RF
    app.state.calamancy = calamancy.load("tl_calamancy_md-0.2.0")
    app.state.stopwords = load_stopwords()
    app.state.vectorizer = load("./src/notebooks/serialized/tfidf-vectorizer.pkl")

@app.get("/api/hello")
async def hello():
    return {"message": "I'm from the backend! Yay! Frontend and backend is connected!"}

@app.post("/api/predict-text-link")
async def predict(request: Request):
    data = await request.json()
    input_text = data.get("text", "")
    
    # Check if it is a link, then parse
    if input_text.startswith(('http://', 'https://', 'www.')):
        input_text = parse_and_clean_link(input_text)
    
    preprocessed = preprocess_text(input_text, app.state.calamancy, app.state.stopwords, join=True)
    
    tfidf = app.state.vectorizer.transform([preprocessed])
    
    pred = app.state.model.predict(tfidf)[0]
    
    verdict = "Unknown Type"
    if pred == 1:
        verdict = "Fake News"
    elif pred == 2:
        verdict = "Real News"
    
    return {"result": verdict}
