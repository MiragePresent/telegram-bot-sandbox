FROM python:rc

WORKDIR /usr/src/app

RUN pip install python-telegram-bot --upgrade && \
    pip install -U python-dotenv

CMD ["python", "-B", "main.py"]
