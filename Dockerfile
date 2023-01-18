FROM python:3.8-alpine

RUN mkdir /server

WORKDIR /server

COPY requirements.txt /server

RUN pip3 install virtualenv 
RUN python3 -m virtualenv . 
RUN source bin/activate    
RUN python3 -m pip install -r requirements.txt --no-cache-dir

COPY . /server

ENV PYTHONPATH=/server

RUN mkdir /server/logs
RUN mkdir /server/data

CMD ["python3", "/server/src/api/app.py"]
