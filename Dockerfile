
FROM python:3.9-slim


WORKDIR /app


COPY . .


EXPOSE 8888


RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi

CMD ["python", "app.py"]
