from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{userId}")
async def handleQueryAndPathParameters(userId: int, name: str):
    return {"details": {"userId":userId, "name":name}}

# KeyPoints of this code ==>
    #* Both paramters (userId and name) are required.
    #* userId is a path parameter and name is query parameter


# And of course, you can define some parameters as required, some as having a default value, and some entirely optional:

    # from typing import Optional
    # from fastapi import FastAPI

    # app = FastAPI()


    # @app.get("/items/{item_id}")
    # async def read_user_item(
    #     item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
    # ):
    #     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    #     return item

# In this case, there are 3 query parameters:
    #* needy, a required str.
    #* skip, an int with a default value of 0.
    #* limit, an optional int.

# Tip ==>
    #* You could also use Enums the same way as with Path Parameters.