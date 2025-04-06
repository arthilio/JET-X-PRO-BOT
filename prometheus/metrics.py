from prometheus_client import start_http_server, Counter

REQUEST_COUNT = Counter('prediction_requests_total', 'Total des requêtes de prédiction')

def setup_metrics(app):
    import threading
    start_http_server(8001)  # Port Prometheus
    @app.middleware("http")
    async def metrics_middleware(request, call_next):
        REQUEST_COUNT.inc()
        response = await call_next(request)
        return response
