from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
	return 'Hi Yashwant, Welcome to the FastApi...'

@app.get("/item/{itemId}")
def readItem(itemId:int):
	return {"itemId: ":itemId}

# In that case, the URL would be: /files//home/johndoe/myfile.txt, with a double slash (//) between files and home.
@app.get("/files/{filePath:path}")
def read_file(filePath: str):
    return {"file_path": filePath}

@app.get("/qryparm/")
async def qryparmExample(skip:int = 0, limit: int = 10,name: str = ''):
	fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
	return 'Hi :) ' + name + "\n" + str(fake_items_db[skip : skip + limit] )


