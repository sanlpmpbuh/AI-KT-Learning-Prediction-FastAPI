#import
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

#instance/obj 
app = FastAPI()

#data 
inventory = {
        1: {
                "name":"phone",
                "price":36000,
                "brand":"sony"            
            },
        2: {
                "name":"milk",
                "price":60,
                "brand":"nandini"  
            },
        3: {
                "name":"shoe",
                "price":8000,
                "brand":"wood-land"  
            }
}

print(inventory)


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None # brand name is made optional, and if you give nothing then 'None' it takes
    
class UpdateItem(BaseModel): #why seperate class for update? , we may update only a single info about the item.
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None
    

#endpoint #route #/after slash
#GET 
@app.get("/get-item/{item_id}") 
def get_item(item_id: int): 
    return inventory[item_id]

#POST
@app.post("/create-item")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists"}
    inventory[item_id] = item  #putting item <object> here
    return inventory[item_id]

#PUT
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item ID does not exists"}
    if item.name !=None:
        inventory[item_id] = item.name
    if item.price !=None:
        inventory[item_id] = item.price
    if item.brand !=None:
        inventory[item_id] = item.brand
    return inventory[item_id]

#DELETE
@app.delete("/update-item/{item_id}")
def delete_item(item_id: int ):
    if item_id not in inventory:
        return {"Error": "ID does not exist"}
    
    del inventory[item_id]
    return {"Success":"Item deleted"}