FROM python:3-alpine

WORKDIR /app
RUN apk add --no-cache gcc musl-dev

COPY src/web/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY src/web /app

EXPOSE 5000
CMD ["hypercorn", "app:app", "-b", "0.0.0.0"]