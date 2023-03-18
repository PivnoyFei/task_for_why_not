[![Build Status](https://github.com/PivnoyFei/task_for_why_not/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/PivnoyFei/task_for_why_not/actions/workflows/main.yml)

<h1 align="center"><a target="_blank" href="">Тестовое задание для WhyNot</a></h1>

### Стек
![Python](https://img.shields.io/badge/Python-171515?style=flat-square&logo=Python)![3.11](https://img.shields.io/badge/3.11-blue?style=flat-square&logo=3.11)
![FastAPI](https://img.shields.io/badge/FastAPI-171515?style=flat-square&logo=FastAPI)![0.94.1](https://img.shields.io/badge/0.94.1-blue?style=flat-square&logo=0.94.1)
![Pytest](https://img.shields.io/badge/Pytest-171515?style=flat-square&logo=Pytest)

#### Сделать сервис на FastAPI, предоставляющий один метод: ```GET /test```

В качестве полезной работы метод спит 3 секунды:
```bash
async def work() -> None:
    asyncio.sleep(3)
```
#### При этом не допускается одновременная работа нескольких функций work()
#### В качестве овета метод возвращает фактически затраченое время на обработку запроса:
```bash
class TestResponse(BaseModel):
    elapsed: float
```
```bash
@router.get("/test", response_model=TestResponse)
async def handler() -> TestResponse:
    ts1 = monotonic()
    ... организация вызовы функции work() ...
    ts2 = monotonic()
    return TestResponse(elapsed=ts2 - ts1)
```
#### Тестирование:
Метод считается успешным, если при одновременном вызове каждый возвращающийся
ответ содержит elapsed отличающийся от предыдущего не менее чем на 3 секунды


### Запуск проекта
Клонируем репозиторий и переходим в него:
```bash
gh clone https://github.com/PivnoyFei/task_for_why_not
cd task_for_why_not
```

#### Создаем и активируем виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```
#### для Windows
```bash
python -m venv venv
source venv/Scripts/activate
```
#### Обновиляем pip и ставим зависимости из requirements.txt:
```bash
python -m pip install --upgrade pip
pip install -r backend/requirements.txt
```

#### Тестируем приложение:
```bash
pytest
```

#### Открываем в консоли папку backend и запускаем сервер:
```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0
```

### Документация будет доступна по адресу:
```bash
http://127.0.0.1:8000/docs/
http://127.0.0.1:8000/redoc/
```

#### Автор
[Смелов Илья](https://github.com/PivnoyFei)