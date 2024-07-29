# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install pandas
RUN pip install pandas

# Run the main.py script
CMD ["python", "main.py"]
