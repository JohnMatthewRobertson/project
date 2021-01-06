# Pull base image
FROM python:3.9.0

# Set environment variables

# python will not try and writte .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# ensure console output looks familiar and not buffered by docker
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project into directory on docker
COPY . /code/