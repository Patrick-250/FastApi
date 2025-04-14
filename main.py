from fastapi import FastAPI
app=FastAPI()

items=[]

@app.get("/")
def root():
    return "hello FastAPI"

@app.post("/items")
def add_item(item:str):
    items.append(item)
    return items
#fast as in fast way to get on with apis