# Тестовое задание Plarin

### Задача 
Реализовать веб-приложение которое предоставляет один API метод для получения списка определенных сотрудников. Приложение должно быть реализовано с использованием FastAPI и MongoDB.
Список данных прикреплен в json файле.
Плюсом будет использование Docker, покрытие тестами.

### Комментарии
* API метод для получания списка сотрудниуков: `/employee` 
* Доступные `query` параметры: `company`, `name`, `job`
* Пример запроса:    
`http://localhost:8081/employee?company=Google&company=Twitter&job=developer`   
* В качестве MongoDB драйвера использовал `motor`
* Для управления зависимостями и сокращения команд использовал [`pipenv`](https://github.com/pypa/pipenv)

### Запуск в docker-compsoe
С помощью [`pipenv`](https://github.com/pypa/pipenv) скриптов:
```
$ pipenv run docker build up
```
Альтернативно без `pipenv`:
```
$ docker-compose --env-file dotenv/.evn.docker build
$ docker-compose --env-file dotenv/.evn.docker up
```
Тестирование запущенного контейнера
```
# pipenv run docker pytest --test-running
```
Без `pipenv`:
```
$ python -c "from scripts.run import MainRunner as m; m('docker').pytest(True)"
```
### Запуск локально
```
$ pipenv run dev database drop seed create-index
$ pipenv run dev start
```
Тесты:
```
$ pipenv run dev pytest --test-running
```
