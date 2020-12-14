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

### Запуск в docker-compsoe
С помошью [`pipenv`](https://github.com/pypa/pipenv) скриптов:
```
$ pipenv run docker build up
```
Альтернативно:
```
$ docker-compose --env-file dotenv/.evn.docker build
$ docker-compose --env-file dotenv/.evn.docker up
```
Тестирование запущенного контейнера
```
# todo
```
### Запуск локально
```
$ pipenv run dev database drop seed create-index
$ pipenv run dev start
```
