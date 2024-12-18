from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def root():
    return 'Главная страница'


@app.get('/user')
async def name_age(username: str, age: int):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


@app.get('/user/admin')
async def admin():
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def id_(user_id: int):
    return f'Вы вошли как пользователь № {user_id}'
