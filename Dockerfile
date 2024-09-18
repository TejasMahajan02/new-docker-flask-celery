FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Expose the app
EXPOSE 5000

# Start Gunicorn with multiple workers (adjust number of workers as needed)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app", "--workers=1", "--log-level=debug"]
