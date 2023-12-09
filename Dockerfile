
FROM python:3.8-slim

# Setting the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Makking the port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Running the app server.py when the container launches
CMD ["python", "server.py"]
