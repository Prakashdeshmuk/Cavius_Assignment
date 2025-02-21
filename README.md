## 🚀 Live Demo

You can check out the live version of this project here:  

🔗 **[Live Demo](https://caviusassignment-production.up.railway.app/docs)**  

Click the link above to explore the application in action! 🚀  

## 📽️ Video Walkthrough

[![Watch the Video](https://img.youtube.com/vi/_ZE1sPowpPw/maxresdefault.jpg)](https://youtu.be/_ZE1sPowpPw)

🔗 **Click the image above to watch the full walkthrough on YouTube.**


## Run Locally 

Clone the project

```bash
  git clone https://github.com/Prakashdeshmuk/Cavius_Assignment.git
```

Go to the project directory

```bash
  Cavius_Assignment
```

Set up a virtual environment

```bash
  python -m venv venv
  source venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```
Set up environment variables(Create a .env file in the root directory and add:)
```bash
  MONGO_URI="your_mongodb_connection_string"
  DATABASE_NAME="ai_assistant"
  COLLECTION_NAME="interactions"
  DEBUG=True
  API_KEY="your_api_key"
```

Run the server using Uvicorn

```bash
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```


## Run Locally 

Clone the project

```bash
  git clone https://github.com/Prakashdeshmuk/Cavius_Assignment.git
```

Go to the project directory

```bash
  Cavius_Assignment
```

Set up a virtual environment

```bash
  python -m venv venv
  source venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```
Set up environment variables(Create a .env file in the root directory and add:)
```bash
  MONGO_URI="your_mongodb_connection_string"
  DATABASE_NAME="ai_assistant"
  COLLECTION_NAME="interactions"
  DEBUG=True
  API_KEY="your_api_key"
```

Run the server using Uvicorn

```bash
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Run Locally with docker

Pull docker Image

```bash
  docker pull prakashdeshmukh/cavius-assignment:latest

```

Run the application using docker command
```bash
  docker run -p 8000:8000 \
  -e MONGO_URI="your_mongodb_connection_string" \
  -e DATABASE_NAME="ai_assistant" \
  -e COLLECTION_NAME="interactions" \
  -e API_KEY="your_api_key" \
  prakashdeshmukh/cavius-assignment:latest
```


