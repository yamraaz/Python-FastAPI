from fastapi import FastAPI

app = FastAPI()

# Use 'None' to keep the parameter default clear value
# As we didnot define any parameter in route so these are optional parameters

@app.get("/mypath")
async def handerQueryparameters(name: str = None, age: int = None, isSuccess: bool = False):
    return {"details":{"name":name,"age":age, "isSuccess":isSuccess}}


# As they are part of the URL, they are "naturally" strings.

# But when you declare them with Python types (in the example above, as int), they are converted to that type and validated against it.

# All the same process that applied for path parameters also applies for query parameters:

# Editor support (obviously)
# Data "parsing"
# Data validation
# Automatic documentation


# In this case, if you go to:

# http://127.0.0.1:8000/mypath?isSuccess=1
# or

# http://127.0.0.1:8000/mypath?isSuccess=True
# or

# http://127.0.0.1:8000/mypath?isSuccess=true
# or

# http://127.0.0.1:8000/mypath?isSuccess=on
# or

# http://127.0.0.1:8000/mypath?isSuccess=yes
# or any other case variation (uppercase, first letter in uppercase, etc), your function will see the parameter isSuccess with a bool value of True. Otherwise as False.