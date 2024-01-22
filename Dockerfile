FROM python:3.13-rc-alpine
COPY requirements.txt /src/requirements.txt
RUN pip3 install -r /src/requirements.txt