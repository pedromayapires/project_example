# Project example
> Basic example project for either companies that require a test or just my own samples for future copy pasting in other projects

## TODO
* Add unit testing
    * Use Django temp DB
    * Create post requests examples to skip postman testing
* Add authentication and throtteling
* Update installation process for ubuntu 20.04

## Installation
### Environment variables (these need to be set for production):
* DJANGO_SECRET_KEY
* DB_USER
* DB_PASSWORD
* DB_NAME
* DB_HOST
* DB_PORT

### Ubuntu 18.04 installation:
* sudo apt install -y python3 python3-pip python-psycopg2 postgresql libpq-dev python-dev default-libmysqlclient-dev
* mkdir workspace; cd workspace; sudo pip3 install virtualenv
* git clone git@github.com:pedromayapires/project_example.git
* cd project_example; virtualenv venv; . venv/bin/activate; pip3 install -r requirements.txt
* echo "CREATE DATABASE django_db;CREATE USER django WITH PASSWORD '1234';ALTER ROLE django SET client_encoding TO 'utf8';GRANT ALL PRIVILEGES ON DATABASE django_db TO django ;" | sudo -u postgres psql -U postgres;
* python manage.py makemigrations; python manage.py migrate
* python manage.py createsuperuser
* python manage.py runserver 0.0.0.0:8000

### Docker in Ubuntu 18.04 & 20.04:
* sudo apt update
* sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
* curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
* sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
* sudo apt update
* apt-cache policy docker-ce
* sudo apt install -y docker-ce
* sudo curl -L "https://github.com/docker/compose/releases/download/1.25.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
* sudo chmod +x /usr/local/bin/docker-compose
* sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
* sudo docker-compose up
    * this must be run inside the project folder where the "docker-compose.yml" file is located


## Extras
* Good example of a README.md at https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46#file-samplereadme-md