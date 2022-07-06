FROM python:latest

COPY ./api /api
WORKDIR /api

RUN pip install -r requirements.txt

EXPOSE 8007

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8007"]