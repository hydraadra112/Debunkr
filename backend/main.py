from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from joblib import load
import asyncio
from src import preprocessors, parsers, LIME
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
    app.state.stopwords = preprocessors.load_stopwords()
    app.state.vectorizer = load("./src/notebooks/serialized/tfidf-vectorizer.pkl")

@app.get("/api/hello")
async def hello():
    return {"message": "I'm from the backend! Yay! Frontend and backend is connected!"}

import asyncio

@app.post("/api/predict-text-link")
async def predict(request: Request):
    data = await request.json()
    input_text = data.get("text", "")
    
    # Check if it is a link, then parse
    if input_text.startswith(('http://', 'https://', 'www.')):
        input_text = parsers.parse_link(input_text)
    
    preprocessed = preprocessors.preprocess_text(
        input_text,
        app.state.calamancy,
        app.state.stopwords,
        join=True
    )
    
    interpreter = LIME.LIMEInterpreter(
        app.state.vectorizer,
        app.state.model,
        class_names=["Real News", "Fake News"]
    )

    # Define tasks for parallelism
    async def run_task1():
        return await asyncio.to_thread(interpreter.explain, preprocessed, num_features=10)

    async def run_task2():
        return await asyncio.to_thread(predict_label, preprocessed)

    def predict_label(text):
        tfidf = app.state.vectorizer.transform([text])
        return app.state.model.predict(tfidf)[0]

    # Run both tasks concurrently
    word_scores, pred = await asyncio.gather(run_task1(), run_task2())

    verdict = "Unknown Type"
    if pred == 1:
        verdict = "Fake News"
    elif pred == 2:
        verdict = "Real News"
    
    return {
        "result": verdict,
        "scores": word_scores
    }

