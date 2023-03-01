FROM python:3-slim-buster
WORKDIR /app
COPY . /app
#COPY migrations /app/migrations
#COPY yoyo.ini /app/
RUN pip install -r requirements.txt
#RUN yoyo list
#RUN yoyo apply -c /app/yoyo.ini
EXPOSE 8000
#CMD ["python", "src/app.py"]
# CMD  flask run --port 7001 --host 0.0.0.0 
CMD ["flask", "run", "--host=0.0.0.0", "--port=9300"]


# docker build -t jaimesalvador/app-authors:1.0.0 .
# FROM python:3.10-alpine AS builder
# RUN apk update && \
# 	apk add musl-dev libpq-dev gcc
# RUN python -m venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"
# COPY requirements.txt .
# RUN pip install -r requirements.txt



# FROM python:3.10-alpine
# RUN apk update && \
# 	apk add libpq-dev
# COPY --from=builder /opt/venv /opt/venv
# ENV PYTHONDONTWRITEBYTECODE=1 \
# 	PYHTONUNBUFFERED=1 \
# 	PATH="/opt/venv/bin:$PATH"
# WORKDIR /code
# COPY . /code
# CMD ["python","./src/app.py"] 