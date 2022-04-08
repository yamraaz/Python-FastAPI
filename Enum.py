from enum import Enum

from fastapi import FastAPI

app = FastAPI()

class ModelName(str, Enum):
    name = 'Yashwant'
    name1 = 'Pradeep'

@app.get("/{modelName}")
async def home(modelName: ModelName):
    status = 'Logged in with ' + modelName
    if modelName == ModelName.name:
        return {"status":status}
    
    elif modelName.value == ModelName.name1:
        return {"status":status}

# You could also access the value "lenet" with ModelName.lenet.value.


# Recap ==>
# With FastAPI, by using short, intuitive and standard Python type declarations, you get:

# Editor support: error checks, autocompletion, etc.
# Data "parsing"
# Data validation
# API annotation and automatic documentation
# And you only have to declare them once.

# That's probably the main visible advantage of FastAPI compared to alternative frameworks (apart from the raw performance).
