# Use the official Python 3.7 image
FROM python:3.7

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

# Install Pipenv
RUN pip install pipenv

# Install project dependencies
RUN pipenv install --deploy --ignore-pipfile

# Copy the rest of the application code to the container
COPY . /app/

# Expose the port that your FastAPI application will run on (e.g., 8000)
EXPOSE 8000

# Command to run your FastAPI application
CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
