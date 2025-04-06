from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.prediction import predict_match
from app.database import init_db, SessionLocal
from app.models import Match
from prometheus.metrics import setup_metrics

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

init_db()
setup_metrics(app)  # Intégration Prometheus

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    prediction = predict_match("Real Madrid", "Barcelone")
    return templates.TemplateResponse("index.html", {
        "request": request,
        "home_team": prediction["home_team"],
        "away_team": prediction["away_team"],
        "score": prediction["score"],
        "confidence": prediction["confidence"]
    })
