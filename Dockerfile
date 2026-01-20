# что использует за сборку языка
FROM python:3.12-slim

WORKDIR /APP
# уст системные зависимости
RUN apt-get update && apt-get install -y \
    gcc\
    postgersql-client\
    && rm -rf /var/lib/apt/list/*

# копируем все зависимости проект
COPY requirements.txt

# устанавливаем зависимости python
RUN pip insall --no-cashe-dir -r requirements.txt

# копируем проект
COPY src/app/src/

# порт на котором разворачиваем
EXPOSE 8000

# команды запуска 
CMD [ "python","src/manage.py", "runserver","0.0.0.0:8000" ]