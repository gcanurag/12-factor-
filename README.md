Sentiment Analyzer API
A simple FastAPI microservice to analyze sentiment from text input.

🚀 Features
REST API with FastAPI

Sentiment analysis using TextBlob

Dockerized

Tested with pytest

GitHub Actions CI

Pre-commit hooks for code quality

MkDocs for documentation

🛠️ Installation
Run Locally
Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run the FastAPI app with auto-reload:
uvicorn app.main:app --reload

The API will be accessible at http://localhost:8000.

Run with Docker
Build the Docker image:
docker build -t sentiment-analyzer .

Run the container:
docker run -p 8000:8000 sentiment-analyzer

Or use docker-compose:
docker-compose up --build

⚙️ Configuration
This app uses environment variables for configuration via Pydantic settings.

You can set environment variables in a .env file or directly in your system.

Example .env:
APP_NAME=Sentiment Analyzer API
DEBUG=False

📁 Project Structure
.
├── app/
│ ├── main.py
│ ├── config.py
│ └── routes/
│ └── sentiment.py
├── tests/
│ └── test_sentiment.py
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md

📄 API Documentation
Once running, visit http://localhost:8000/docs for interactive API docs.

🧪 Testing
Run tests with:
pytest