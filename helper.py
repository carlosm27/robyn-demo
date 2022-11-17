
fake_fruit_database = [
    {"id":1, "fruit":"Apple"},
    {"id":2, "fruit":"Orange"},
    {"id":3, "fruit":"Pinapple"}
]
fruit_id = 2

def get_item(id: int, db: list):
    fruit = {}
    for dic in db:
        for val in dic.values():
            if val == id:
                fruit = dic
    return fruit

                


