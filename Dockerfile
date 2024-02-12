FROM python:3.8-alpine
ENV PYTHONBUFFERED 1
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /app
ADD . /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


COPY . /app

# Expose port 8000 to the outside world
EXPOSE 8000

# Run migrations and start the Django development server
CMD ["./run.sh"]
