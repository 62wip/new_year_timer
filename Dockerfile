FROM python:3.12

WORKDIR /home/wip/python/new_year_bot
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./run.py" ]
