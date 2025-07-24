from fastapi import FastAPI

app=FastAPI() #function call
#PARAMETER PASSING
"""@app.get('/users/{user_id}')
def read_items(user_id:int):
    return{'user_id':user_id}
"""

#QUERY PASSING
"""@app.get('/users/')
def val_print(id:int,name:str):
    return {'id':id,'name':name}"""

#combination
@app.get('/users/{user_id}/details')
def comb(user_id:int,email_check:bool=False):
    if email_check:
        return {'user_id':user_id,'email_check':"email is included"}
    else :
        return{'user_id':user_id,'email_check':"email not included"}