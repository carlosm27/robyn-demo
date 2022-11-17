from robyn import Robyn, jsonify
import schemas
import models

import json


app = Robyn(__file__)


fake_database = {
    "1": {"fruit":"Apple"},
    "2": {"fruit":"Orange"},
    "3": {"fruit":"Pinapple"}
}


@app.get("/")
async def h(request):
    print(request)
    return "Hello, world!"



@app.get("/fruits")
def all_fruits(request):
    print(fake_database)
    return jsonify(fake_database)



@app.get("/fruit/:id")
def get_fruit(request):
    id = request['params']['id']
    fruit = fake_database[id]
    print(fruit)
    return jsonify(fruit)

@app.post("/fruit")
def add_fruit(request):
    
    body = bytearray(request['body']).decode("utf-8")
    print(body)
    fruit = json.loads(body)
    print(fruit)
    new_id = len(fake_database.keys()) + 1
    str(new_id)
    
    fake_database[new_id] = fruit
    print(fake_database)
    return jsonify(fruit)




@app.put("/fruit/:id")
def update_fruit(request):
    id = request["params"]["id"]
    body = bytearray(request['body']).decode("utf-8")
    fruit = json.loads(body)
    fake_database[id]['fruit'] = fruit['fruit']
    print(fake_database)
    return jsonify(fake_database)



@app.delete("/fruit/:id")
def delete_fruit(request):
    id = request["params"]["id"]
    print(id)
    print(fake_database[id])
    del fake_database[id]
    
    
    return jsonify({"Message":"Fruit was deleted"})










app.start()