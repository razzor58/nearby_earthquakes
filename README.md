![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/razzor58/4b0b2165685931159ff9aeb4200fc867/raw/coverage.json) ![style check](https://github.com/razzor58/nearby_earthquakes/actions/workflows/style_check.yaml/badge.svg) ![typing check](https://github.com/razzor58/nearby_earthquakes/actions/workflows/typing_check.yaml/badge.svg)

## Searching nearby earthquakes
Program implement the test challenge described [here](https://github.com/smartrecruiters-coding/ict-nearby-earthquakes-ilya-davydov)

### Pre-requirements
 - Make sure [docker](https://www.docker.com/products/docker-desktop/) is installed and running on your machine

### Run main program
 - Clone repository:
    ```
    git clone https://github.com/razzor58/nearby_earthquakes.git
    ```
 - Build the program:
    ```
    docker build -t program .
    ```
 - Execute the program:
    ```
    docker run -it program python main.py
    ```

### Run test
```
docker run -it program  pytest --cov=app ./tests
```

### Run type checking
```
docker run -it program  mypy ./app
```