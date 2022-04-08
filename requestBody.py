from ast import alias
from lib2to3.pgen2.token import OP
from tkinter.messagebox import NO
from typing import List, Optional
from fastapi import FastAPI, Query

from pydantic import BaseModel

app = FastAPI()

class Students(BaseModel):
    name: str = None
    mobile: Optional[int] = None
    age: int = None
    department: Optional[str] = None


@app.post("/")
async def handlePostRequest(students: Students):
    return students

@app.post("/users/{userId}")
async def handlePostRequestWithPathParameters(
                                            userId  : int, 
                                            students: Students):
    return {"data":{"userId": userId, "students":students}}

@app.post("/users1/{userId}")
async def handlePostRequestWithPathAndQueryParameters(userId  : int, 
                                                      students: Students, 
                                                      books   : Optional[list]=Query(
                                                                                ['Develop Python'],
                                                                                title='List of books',
                                                                                description="Query string for the items to search in the database that have a good match",
                                                                                #  min_length=2,
                                                                                alias='library-books',
                                                                                deprecated=True,
                                                                                include_in_schema=False),
                                                      name    : Optional[List[str]]=Query(None)
                                                                            ):
    return {"data":{"userId": userId,"name": name, "books":books, "students":students}}


# url for list parameters will be as below
    # http://localhost:8000/items/?q=foo&q=bar

# Tip
    # use Query while using list parameters
    # Have in mind that in this case, FastAPI won't check the contents of the list.
        # For example, List[int] would check (and document) that the contents of the list are integers. But list alone wouldn't.



# You can declare additional validations and metadata for your parameters.

# Generic validations and metadata:

# alias
# title
# description
# deprecated
# Validations specific for strings:

# min_length
# max_length
# regex
# In these examples you saw how to declare validations for str values.

# See the next chapters to see how to declare validations for other types, like numbers.