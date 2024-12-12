# Base Image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"] 
