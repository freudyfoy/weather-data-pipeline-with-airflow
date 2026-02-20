# weather-data-pipeline-with-airflow
This project implements an automated, end-to-end ETL pipeline that automates the collection, transformation, and visualization of global weather data. By orchestrating a suite of modern data tools within `WSL` and `Docker` environment, the system transforms raw JSON payloads from external API into actionable insights for climate trend analysis.

## Tech stack

- OS: WSL (Ubuntu 24.04)
- External Weather API: [Weatherstack](https://weatherstack.com/)
- Orchestration: Apache Airflow
- Database: PostgreSQL
- Containerization: Docker
- Transformation: dbt
- Visualization: Apache Superset


## The ETL Pipeline Workflow

1. **Extraction:** The pipeline makes scheduled requests to an external weather API to capture real-time atmospheric metrics including temperature, weather, wind speed.

2. **Processing:** Raw `JSON` returned by API are parsed and cleaned using `Python`.

3. **Transformation:** Cleans raw data by handling null values and duplicate data.

4. **Storage:** Cleaned data is loaded into a `PostgreSQL` schema.

5. **Visualization:** Using `Apache Superset`, the stored data is transformed into interactive charts. Users can track weather patterns, compare regional climates, and visualize environmental changes over time.

