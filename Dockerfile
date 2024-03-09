FROM python:3.11

ENV DB_HOST='localhost'
ENV DB_PORT=5432
ENV DB_NAME='flask_restapi'
ENV DB_USER='flask_restapi'
ENV DB_PASSWORD='flask_restapi_pass'


WORKDIR /opt/app

COPY . .

# Install Poetry
RUN pip install poetry
# Install dependencies
RUN poetry install

VOLUME /data_store
EXPOSE 5000

# Command to start server
CMD ["poetry", "run", "python3", "-m", "flask", "run", "--host=0.0.0.0"]

