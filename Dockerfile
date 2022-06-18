FROM python:3.9
WORKDIR /code
COPY ./code/requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY ./code /code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
