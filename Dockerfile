FROM python:3.11

COPY . .

RUN pip install -r req.txt

CMD ["pytest", "dumb_test.py"]