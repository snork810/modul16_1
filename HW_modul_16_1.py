from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def GetMainPage():
    return 'Главная страница'

@app.get('/user/admin')
async def GetAdminPage():
    return 'Вы вошли как администратор'

@app.get('/user/{userID}')
async def GetUserNumber(userID:int):
    return f'Вы вошли как пользователь №{userID}'

@app.get('/user')
async def GetUserInfo(username:str, age:int):
    return f'Информация о пользователе. Имя {username}, возраст {age}'
