# Engineering Data API

[![CI](https://github.com/dariaaksianova/engineering-data-api/actions/workflows/ci.yml/badge.svg)](https://github.com/dariaaksianova/engineering-data-api/actions/workflows/ci.yml)

A FastAPI service that helps to validate and analyse engineering measurement data.

The project demonstrates API development, typed data validation, statistical analysis, automated testing, containerisation and continuous integration.

## Capabilities 

- REST API built with FastAPI
- Typed request and response models
- Engineering measurement analysis
- Mean, standard deviation, minimum and maximum calculations
- Optional reference-value and tolerance checking
- Input validation with Pydantic
- Automated API tests with pytest
- Static type checking with mypy
- Code quality checks with Ruff
- Docker support
- GitHub Actions continuous integration

## Sample request

`POST /measurements/analyse`

```json
{
  "name": "brake_disc_temperature",
  "unit": "degC",
  "values": [412.4, 418.1, 415.7, 421.0],
  "reference": 416.0,
  "tolerance": 6.0
}
```

## Sample response

```json
{
  "name": "brake_disc_temperature",
  "unit": "degC",
  "count": 4,
  "mean": 416.8,
  "standard_deviation": 3.1583,
  "minimum": 412.4,
  "maximum": 421.0,
  "within_tolerance": true
}
```

## Local run

Create and activate a virtual environment, then install the dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app.main:app --reload
```

Interactive API documentation will be available at:

```text
http://127.0.0.1:8000/docs
```

A simple health check is available at:

```text
http://127.0.0.1:8000/health
```

## Tests 

```bash
pytest
```

## Code quality

Run Ruff:

```bash
ruff check .
```

Run mypy:

```bash
mypy app
```

## Docker

Build the image:

```bash
docker build -t engineering-data-api .
```

Run the container:

```bash
docker run -p 8000:8000 engineering-data-api
```

The API will then be available at:

```text
http://localhost:8000
```

## Structure

```text
engineering-data-api/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_api.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── pyproject.toml
├── README.md
└── requirements.txt
```