## Searching nearby earthquakes
Program implement the test challange described [here](https://github.com/smartrecruiters-coding/ict-nearby-earthquakes-ilya-davydov)

### Pre-requirements
 - Make sure [docker](https://www.docker.com/products/docker-desktop/) is installed and running on your machine

### Run main program
 - Clone repository:
    ```
    git clone https://github.com/razzor58/nearby-earthquakes.git
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