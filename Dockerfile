FROM naxa/python:3.9-slim
# Uses naxa/python:3.9-slim instead of python:3.9-slim so that
# apt/requirement doesn't have to reinstall everytime

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code
RUN mkdir -p /sock
RUN mkdir -p /logs
WORKDIR /code


COPY requirements.txt /code/

RUN pip install --no-cache-dir setuptools==57.5.0
RUN pip install --no-cache-dir -r requirements.txt


COPY . /code

# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]

