from pymongo import MongoClient
from config import settings

def connectDb():
    """Function to connect to MongoDB and return the database instance."""
    try:
        client = MongoClient(settings.MONGO_URI)
        db = client[settings.DATABASE_NAME]
        print(f"Connected to MongoDB: {settings.DATABASE_NAME}")
        return db
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        return None  # Return None if connection fails