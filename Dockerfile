
# Use a base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy requirements.txt first to install dependencies
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Check installed package versions (for debugging)
RUN pip show flask werkzeug

# Command to run the application
CMD ["python", "app.py"]
