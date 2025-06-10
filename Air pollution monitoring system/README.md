# Air Pollution Monitoring System

A real-time air pollution monitoring system that tracks and visualizes various air quality parameters.

## Features

- Real-time monitoring of air quality parameters:
  - PM2.5 and PM10 (Particulate Matter)
  - CO2 (Carbon Dioxide)
  - CO (Carbon Monoxide)
  - Temperature
  - Humidity
- Interactive dashboard with real-time updates
- Historical data tracking and visualization
- Alert system for dangerous pollution levels
- REST API for data access

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the application:
```bash
python main.py
```
        
4. Access the web interface at : http://localhost:8000

## Project Structure

```
├── app/
│   ├── api/            # API endpoints
│   ├── models/         # Database models
│   ├── schemas/        # Pydantic schemas
│   ├── services/       # Business logic
│   ├── static/         # Static files
│   └── templates/      # HTML templates
├── database/           # Database configuration
├── tests/              # Unit tests
├── main.py            # Application entry point
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation
```

## API Documentation

The API documentation is available at: http://localhost:8000/docs

## License

MIT License 