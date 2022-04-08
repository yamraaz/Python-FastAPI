from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{userId}/items/{itemId}")
async def optionalQueryParameters(userId: int, 
                                  itemId: str, 
                                  description: Optional[str] = None):
    return {"userId": userId, "itemId":itemId}

# this code can be used when we need to keep one extra optional parameters
#


