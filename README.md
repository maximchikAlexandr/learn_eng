# learn_eng
## About project

**Learn_eng** is a web application designed for learning English. 


This backend of this project is written in Python using the *Flask* framework. For installation 
using the *Docker*, the project contains two containers: the Django application 
and the *PostgreSQL* database.


## Installation

Clone the repository from GitHub:

```sh
git clone https://github.com/maximchikAlexandr/learn_eng.git
```

Create a file named '.env' in the root directory:

```sh
cd learn_eng/
nano .env
```

and fill it with the following environment variables:

```sh
SECRET_KEY=some_key
YANDEX_DICTIONARY_KEY=our_Yandex_Dictionary_API_key
POSTGRES_DB=some_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=some_password
DB_HOST=postgres_db
DB_PORT=some_port1
DB_OUT_PORT=some_port2
```

Create and start the docker containers:

```sh
docker compose up -d
```

Open up the browser and navigate to the main page of the project at http://localhost:5001/.


## Yandex Dictionary API key

To get the Yandex Dictionary API key, follow the official documentation:

https://yandex.com/dev/dictionary/keys/get/?service=dict