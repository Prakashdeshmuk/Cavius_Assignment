from fastapi import FastAPI
from connectdb import connectDb
import groq
from config import settings
from datetime import datetime
from schema import Interaction
import logging


client = groq.Groq(api_key=settings.API_KEY)
app = FastAPI()

# Configure logging
logging.basicConfig(
    filename="api.log",  # Log file name
    level=logging.INFO,  # Log level
    format="%(asctime)s - %(levelname)s - %(message)s",
)

db = connectDb()
collection = db[settings.DATABASE_NAME]

@app.get('/')
def read_root():
    if db is not None:
        logging.info("MongoDB Connected Successfully!")
        return {"message": "MongoDB Connected Successfully!"}
    else:
        logging.error("Database Connection Failed!")
        return {"error": "Database Connection Failed"}
    

@app.post('/')
async def intent_recognition(user_input: str):
    try:
        logging.info(f"Received request: {user_input}")
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",  # Choose a Groq-supported model
            messages=[
                {"role": "system", "content": "You are an AI that classifies user intent. Respond with only the intent label."},
                {"role": "user", "content": user_input}
            ]
        )
        intent = response.choices[0].message.content

        interaction = Interaction(user_input=user_input,intent=intent,datetime=datetime.utcnow())

        collection.insert_one(interaction.to_dict())

        return {"intent": intent, "message": "Interaction saved successfully!"}
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return {"error": "Failed to process request"}
    
