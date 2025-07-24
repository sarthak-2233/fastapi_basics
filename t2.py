from fastapi import FastAPI

app=FastAPI()

#USING POST METHOD '''
'''
@app.post('/items/')
def create_items(name:str,price:float):
    return{'name':name,'price':price}
'''
#USING PUT METHOD '''
"""
@app.put('/items/')
def put_items(item_id:int,name:str,price:float):
    return{'item_id':item_id,'name':name,'price':price}"""

#USING DELETE METHOD
@app.delete('/item/{item_id}/')
def del_items(item_id:int):
    return{'message :' f'item id {item_id} deleted successfully'}