FROM python:3.9
ADD requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
ADD . /app
CMD ["python3", "-u", "app.py"]