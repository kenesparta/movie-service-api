# Generic Movie service API

## 1. Prerequisites:

| Software          | Version | Importance    |
| ----------------- | ------- | ------------- |
| 🐳 Docker         | 20.10.6 | Required      |
| 🐙 Docker Compose | 1.29.1  | Required      |
| 🐃 GNU Make       | 4.2.1   | Recommendable |

## 2. Getting started

1. Execute the command: `make prepare`.
2. Fill the file `config.py` with your own credentials.

### 2.1 Used ports:

| Port  | Description         |
| ----- | ------------------- |
| 8090  | Main Service        |
| 8091  | Robot               |
| 15672 | RabbitMQ            |
| 5672  | RabbitMQ (internal) |
| 5432  | PostgreSQL          |

## 3. Steps

### 3.1 Read the API documentation

- We can found the documentation on this [link](https://www.omdbapi.com/apikey.aspx).
- We can get the API Key by registering from this [link](https://www.omdbapi.com/apikey.aspx) (with free 1000 API calls
  per day)

## 4. Warnings ⚠️

1. The `config.py.example` values should be empty and do not have to be versioned.
2. The `movie_service` and `robot_service` should be separated on different repositories.
