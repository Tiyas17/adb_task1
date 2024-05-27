# Set base image (host OS)
FROM python:3.8

# Update and install system packages
RUN apt-get update && apt-get install -y \
    curl \
    nano \
    wget \
    nginx \
    git \
    yarn \
    python3-pip

# Set environment variables
ENV ENV_TYPE staging
ENV MONGO_HOST mongo
ENV MONGO_PORT 27017

# Set working directory
WORKDIR /app

# Copy the dependencies file to the working directory
COPY src/requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose any necessary ports (if needed)
# EXPOSE 5000

# Optional: Add your application code
# COPY src/ /app/

# Example CMD (replace with your actual command)
CMD ["python", "src/app.py"]