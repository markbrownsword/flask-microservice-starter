## Python Flask Microservice Starter Project
A basic starter project for building a Microservice in Python with Flask

### Prerequisites (for Ubuntu 18.10)
[Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), Python 3 [venv](https://docs.python.org/3/library/venv.html) and [pip](https://packaging.python.org/guides/installing-using-linux-tools/#debian-ubuntu)
```bash
sudo apt install python3-venv python3-pip
```

### Setup
```bash
mkdir FlaskMicroserviceStarter  
cd FlaskMicroserviceStarter  
git clone <https://github.com/markbrownsword/flask-microservice-starter.git> .

# Setup the Python virtual environment
python3 -m venv .venv

# Activate the virtual environment
source ./.venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run (for Development)

```bash
flask run
```
