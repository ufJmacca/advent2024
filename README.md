My attempt at advent of code 2024, this time using python

## Quick Start

1. Spin up docker container: `docker-compose up -d`
2. Within the container make sure you are in the /app directory. This is where the code is stored, and synced to the host machine
3. Install depednencies with `pip install -r requirements.txt`
4. While developing you can test using pytest by running: `pytest day_<number>`
5. Once tests are passing run solution for a given day: `python day_<number>/code.py`