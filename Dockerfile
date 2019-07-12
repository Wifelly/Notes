FROM python:alpine
LABEL Name=notes Version=0.0.1
EXPOSE 3000
WORKDIR /app
ADD . /app
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN python3 -m pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
