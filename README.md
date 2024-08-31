

## Project Structure

- **Dockerfile**: Contains instructions to build a Docker image for the application.
- **docker-compose.yml**: Defines the services for the application and test environment.
- **main.py**: The main Python script that runs the application.
- **orders.csv**: A CSV file with sample data used for analysis in the application.
- **test_main.py**: Unit tests for the application's data processing functions.

## Architecture

The project follows a simple architecture with a focus on modularity and containerization. Here is a brief overview of the components:

1. **Docker**: Used to containerize the application and manage dependencies.
2. **Python**: Main programming language used for data processing and analysis.
3. **CSV Data**: Sample data stored in `orders.csv` is read and processed by the application.
4. **Docker Compose**: Manages multi-container applications and orchestrates the setup.

## Getting Started

Follow these steps to set up and run the project using Docker:

## Prerequisites

- Install [Docker](https://www.docker.com/get-started)
- Install [Docker Compose](https://docs.docker.com/compose/install/)

## Steps to Run the Project

### 1. Clone the Repository

    ```sh
    https://github.com/SammitBathla/tanX-Assessment-.git
    cd your-repo
    ```

### 2. Build the Docker Images

    ```sh
    docker-compose build
    ```

### 3. Run the Application

    ```sh
    docker-compose up app
    ```

    This command will start the application and make it available on your local machine.

### 4. Access the Application

    The application should now be running, and you can access it via your web browser at `http://localhost:8000` (adjust the port if necessary based on your `docker-compose.yml` configuration).

### Running Tests

To run tests, use the following command:

    ```sh
    docker-compose up test
    ```

This command will execute the unit tests defined in the `test_main.py` script.


