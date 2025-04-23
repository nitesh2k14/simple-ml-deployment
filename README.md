
# Simple ML Deployment

This project serves a basic ML model through an API using FastAPI and Docker.

## Steps to Run

1. Clone the repo
2. Generate the `model.pkl`
3. Run locally: `uvicorn app.api:app --reload`
4. Build Docker image: `docker build -t simple-ml-deployment .`
5. Run Docker: `docker run -p 8000:8000 simple-ml-deployment`

## Deployment

- CI/CD via GitHub Actions
- Docker image pushed to Docker Hub
- Deployed on AWS EC2
