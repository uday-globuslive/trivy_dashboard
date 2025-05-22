# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app (for completeness, but you will mount as volume)
COPY . .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
