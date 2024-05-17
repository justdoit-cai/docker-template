FROM python:3.7.1

WORKDIR /app/
COPY app.py .
COPY requirement.txt .
RUN pip install -r requirement.txt
EXPOSE 10002

CMD ["python", "app.py"]
