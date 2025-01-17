FROM python:3
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
COPY . /code/
CMD=["python manage.py runserver"]
