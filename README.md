# 🧠 Sentiment Analyzer API

A simple FastAPI microservice to analyze sentiment from text input using **TextBlob**.

---

## 🚀 Features

- REST API built with **FastAPI**
- Sentiment analysis via **TextBlob**
- 🐳 Dockerized
- ✅ Tested with **pytest**
- 🔁 **GitHub Actions CI**
- 🧹 Pre-commit hooks for code quality
- 📚 Documentation with **MkDocs**

---

## 🛠️ Installation

### 🔧 Run Locally

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit: [http://localhost:8000](http://localhost:8000)

---

### 🐳 Run with Docker

```bash
# Build the Docker image
docker build -t sentiment-analyzer .

# Run the container
docker run -p 8000:8000 sentiment-analyzer

# Or use docker-compose
docker-compose up --build
```

---

## ⚙️ Configuration

This app uses environment variables for configuration via **Pydantic settings**.

You can set them in a `.env` file or your system.

Example `.env`:
```env
APP_NAME=Sentiment Analyzer API
DEBUG=False
```

---

## 📁 Project Structure

```
.
├── app/
│   ├── main.py
│   ├── config.py
│   └── routes/
│       └── sentiment.py
├── tests/
│   └── test_sentiment.py
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
```

---

## 📄 API Documentation

Once the server is running, access the interactive docs at:  
🔗 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Testing

Run tests using:

```bash
pytest
```
