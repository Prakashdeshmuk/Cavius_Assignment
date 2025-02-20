from pydantic import BaseModel
from datetime import datetime

class Interaction(BaseModel):
    user_input: str
    intent: str
    timestamp: datetime = datetime.utcnow()  # Store interaction time

    def to_dict(self):
        """Convert Pydantic model to a dictionary for MongoDB."""
        return self.model_dump()  # Use model_dump() instead of dict()
