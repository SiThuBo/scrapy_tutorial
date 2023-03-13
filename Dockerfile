FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files to working directory
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for MySQL
EXPOSE 3306

# Set environment variables
ENV MYSQL_HOST 172.17.0.1
ENV MYSQL_USER root
ENV MYSQL_PASSWORD root
ENV MYSQL_DATABASE scraped_data
