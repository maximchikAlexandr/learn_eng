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
# App parameters
SECRET_KEY="the_key_used_for_encryption"
YANDEX_DICTIONARY_KEY="your_Yandex_Dictionary_API_key"

# database parameter
POSTGRES_DB="database_name"
POSTGRES_USER="your_database_username"
POSTGRES_PASSWORD="your_database_password"
DB_HOST="your_database_host"
DB_PORT="port_of_your_database_in_container"
DB_OUT_PORT="outer_port_of_your_database"
```

Create and start the docker containers:

```sh
docker compose up -d
```

Open up the browser and navigate to the main page of the project at 
```sh
http://localhost:5001/
```

## Yandex Dictionary API key

To get the Yandex Dictionary API key, follow the official documentation:
```sh
https://yandex.com/dev/dictionary/keys/get/?service=dict
```