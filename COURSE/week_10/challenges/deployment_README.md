# System Deployment Challenge

## Overview
Welcome to the System Deployment Challenge! In this assignment, you'll prepare the NCAA Soccer Player Analysis System for deployment in various environments. Deployment is a critical part of the software development lifecycle, involving the processes required to make your application available to users. You'll create configuration files, setup scripts, and documentation that ensure your system can be reliably deployed and maintained.

## Learning Objectives
- Prepare an application for production deployment
- Configure environment-specific settings
- Create automated deployment scripts
- Set up monitoring and logging systems
- Generate comprehensive deployment documentation
- Understand containerization with Docker
- Implement secure configuration practices

## NCAA Soccer Application
Deploying your NCAA Division II soccer analysis system will provide several benefits:
- Make player analysis tools accessible to coaches and scouts
- Enable easy updates as new data becomes available
- Provide secure access to authorized users
- Ensure data integrity and backup
- Allow for scaling as more teams and players are added
- Support remote access for distributed coaching staff
- Create a portable system that other NCAA programs can adopt

## Conceptual Background

### Deployment Environments
Most applications are deployed to multiple environments for different purposes:
1. **Development**: For active development and testing new features
2. **Testing/Staging**: For quality assurance and user acceptance testing
3. **Production**: The live environment accessed by end users

Each environment has specific configuration requirements to optimize for its purpose.

### Deployment Components
A complete deployment strategy includes several key components:

1. **Configuration Management**:
   - Environment variables
   - Configuration files
   - Secret management

2. **Infrastructure Setup**:
   - Web servers (e.g., Nginx, Apache)
   - Application servers (e.g., Gunicorn, uWSGI)
   - Database configuration

3. **Deployment Automation**:
   - Deployment scripts
   - Continuous Integration/Continuous Deployment (CI/CD)
   - Rollback procedures

4. **Monitoring and Maintenance**:
   - Logging configuration
   - Health checks
   - Performance monitoring

### Containerization
Containers provide a standardized way to package and deploy applications:
- **Docker**: Platform for developing, shipping, and running applications in containers
- **Docker Compose**: Tool for defining and running multi-container Docker applications
- **Benefits**: Consistency across environments, isolation, resource efficiency

## Challenge Tasks

### Task 1: Create Deployment Directories
Set up the necessary directory structure for deployment:

```python
def create_deployment_directories():
    """Create the necessary directories for deployment."""
    try:
        # Create main deployment directory if it doesn't exist
        os.makedirs(DEPLOYMENT_DIR, exist_ok=True)
        
        # Create subdirectories for different components
        subdirectories = [
            os.path.join(DEPLOYMENT_DIR, "config"),
            os.path.join(DEPLOYMENT_DIR, "scripts"),
            os.path.join(DEPLOYMENT_DIR, "docker"),
            os.path.join(DEPLOYMENT_DIR, "logs"),
            os.path.join(DEPLOYMENT_DIR, "backup"),
            os.path.join(DEPLOYMENT_DIR, "docs")
        ]
        
        for directory in subdirectories:
            os.makedirs(directory, exist_ok=True)
            logger.info(f"Created directory: {directory}")
        
        return True
    except Exception as e:
        logger.error(f"Error creating deployment directories: {str(e)}")
        return False
```

### Task 2: Generate Configuration Files
Create configuration files for different deployment environments:

```python
def generate_configuration_files():
    """Generate configuration files for different deployment environments."""
    config_dir = os.path.join(DEPLOYMENT_DIR, "config")
    config_files = {}
    
    # Development configuration
    dev_config = {
        "ENV": "development",
        "DEBUG": True,
        "DATABASE_URL": "sqlite:///PROJECT/data/soccer_stats.db",
        "SECRET_KEY": "dev-key-for-testing-replace-in-production",
        "FLASK_APP": "PROJECT/src/dashboard/app.py",
        "HOST": "127.0.0.1",
        "PORT": 5000,
        "LOG_LEVEL": "DEBUG"
    }
    
    # Testing configuration
    test_config = {
        "ENV": "testing",
        "DEBUG": False,
        "TESTING": True,
        "DATABASE_URL": "sqlite:///PROJECT/data/test_soccer_stats.db",
        "SECRET_KEY": "test-key-for-testing-only",
        "FLASK_APP": "PROJECT/src/dashboard/app.py",
        "HOST": "127.0.0.1",
        "PORT": 5000,
        "LOG_LEVEL": "INFO"
    }
    
    # Production configuration
    prod_config = {
        "ENV": "production",
        "DEBUG": False,
        "DATABASE_URL": "postgresql://user:${DB_PASSWORD}@db:5432/soccer_stats",
        "SECRET_KEY": "${SECRET_KEY}",
        "FLASK_APP": "PROJECT/src/dashboard/app.py",
        "HOST": "0.0.0.0",
        "PORT": 8000,
        "LOG_LEVEL": "WARNING",
        "WORKERS": 4,
        "TIMEOUT": 60
    }
    
    # Write configuration files
    for env, config in [
        ("development", dev_config),
        ("testing", test_config),
        ("production", prod_config)
    ]:
        # Create Python config file
        py_file_path = os.path.join(config_dir, f"{env}_config.py")
        with open(py_file_path, "w") as f:
            f.write("# Configuration for {} environment\n\n".format(env.capitalize()))
            for key, value in config.items():
                if isinstance(value, str):
                    f.write(f"{key} = '{value}'\n")
                else:
                    f.write(f"{key} = {value}\n")
        
        # Create JSON config file
        json_file_path = os.path.join(config_dir, f"{env}_config.json")
        with open(json_file_path, "w") as f:
            json.dump(config, f, indent=2)
        
        # Store file paths
        config_files[env] = {
            "python": py_file_path,
            "json": json_file_path
        }
    
    logger.info(f"Generated configuration files for all environments")
    return config_files
```

### Task 3: Prepare Database Configuration
Set up database initialization and backup procedures:

```python
def prepare_database():
    """Prepare the database for deployment."""
    db_scripts_dir = os.path.join(DEPLOYMENT_DIR, "scripts", "database")
    os.makedirs(db_scripts_dir, exist_ok=True)
    
    # Create initialization script
    init_script_path = os.path.join(db_scripts_dir, "init_database.py")
    init_script = """#!/usr/bin/env python3
\"\"\"
Database initialization script for NCAA Soccer Player Analysis System.
\"\"\"
import os
import sys
import sqlite3
import pandas as pd
from datetime import datetime

# Add project root to path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, project_root)

# Import database models (adjust import path as needed)
# from PROJECT.src.models import db, Player, Team, Match, Statistic

def init_database():
    \"\"\"Initialize the database with schema and sample data.\"\"\"
    print("Initializing database...")
    
    # Get database URL from environment or use default
    database_url = os.getenv("DATABASE_URL", "sqlite:///PROJECT/data/soccer_stats.db")
    
    # For SQLite, extract file path
    if database_url.startswith("sqlite:///"):
        db_path = database_url.replace("sqlite:///", "")
        db_dir = os.path.dirname(os.path.join(project_root, db_path))
        os.makedirs(db_dir, exist_ok=True)
        
        # Create database and tables
        conn = sqlite3.connect(os.path.join(project_root, db_path))
        
        # Create tables
        cursor = conn.cursor()
        
        # Players table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            team_id INTEGER,
            age INTEGER,
            height REAL,
            weight REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Teams table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            division TEXT,
            conference TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Statistics table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS statistics (
            id INTEGER PRIMARY KEY,
            player_id INTEGER,
            season TEXT,
            games_played INTEGER,
            minutes INTEGER,
            goals INTEGER,
            assists INTEGER,
            shots INTEGER,
            shots_on_goal INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (player_id) REFERENCES players (id)
        )
        ''')
        
        conn.commit()
        conn.close()
        
        print(f"Database initialized at {db_path}")
        return True
    else:
        print("Only SQLite databases supported by this script.")
        print("For other database types, please run migrations manually.")
        return False

def load_sample_data():
    \"\"\"Load sample data into the database.\"\"\"
    # Implementation would go here
    pass

if __name__ == "__main__":
    init_database()
    # Uncomment to load sample data
    # load_sample_data()
"""
    
    with open(init_script_path, "w") as f:
        f.write(init_script)
    
    # Make the script executable
    os.chmod(init_script_path, 0o755)
    
    # Create backup script
    backup_script_path = os.path.join(db_scripts_dir, "backup_database.sh")
    backup_script = """#!/bin/bash
# Database backup script for NCAA Soccer Player Analysis System

set -e

# Get the current date for backup filename
CURRENT_DATE=$(date +%Y-%m-%d_%H-%M-%S)
BACKUP_DIR="./deployment/backup"
mkdir -p $BACKUP_DIR

# Get database URL from environment or use default
DB_URL=${DATABASE_URL:-"sqlite:///PROJECT/data/soccer_stats.db"}

# Extract database type and path
if [[ $DB_URL == sqlite://* ]]; then
    # SQLite backup
    DB_PATH=${DB_URL#sqlite:///}
    echo "Backing up SQLite database from $DB_PATH"
    
    # Create backup file
    BACKUP_FILE="$BACKUP_DIR/soccer_stats_$CURRENT_DATE.sql"
    
    # Check if database file exists
    if [ -f "$DB_PATH" ]; then
        # Create SQL dump
        echo "Creating backup at $BACKUP_FILE"
        sqlite3 "$DB_PATH" .dump > "$BACKUP_FILE"
        
        # Create compressed archive
        gzip "$BACKUP_FILE"
        echo "Backup completed: ${BACKUP_FILE}.gz"
    else
        echo "Error: Database file not found at $DB_PATH"
        exit 1
    fi
elif [[ $DB_URL == postgresql://* ]]; then
    # PostgreSQL backup
    echo "PostgreSQL backup not implemented in this script yet"
    # Implementation would go here using pg_dump
    exit 1
else
    echo "Unsupported database type in URL: $DB_URL"
    exit 1
fi
"""
    
    with open(backup_script_path, "w") as f:
        f.write(backup_script)
    
    # Make the script executable
    os.chmod(backup_script_path, 0o755)
    
    logger.info(f"Created database initialization and backup scripts")
    return {"init_script": init_script_path, "backup_script": backup_script_path}
```

### Task 4: Set Up Web Server Configuration
Create configuration files for web servers like Nginx and application servers like Gunicorn:

```python
def setup_web_server_config():
    """Configure the web server for deployment."""
    config_dir = os.path.join(DEPLOYMENT_DIR, "config")
    
    # Generate WSGI file
    wsgi_file_path = os.path.join(config_dir, "wsgi.py")
    wsgi_content = """#!/usr/bin/env python3
\"\"\"
WSGI entry point for the NCAA Soccer Player Analysis System.
\"\"\"
import os
import sys

# Add the project directory to path
project_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, project_root)

# Import the Flask application
# Adjust the import path according to your project structure
from PROJECT.src.dashboard.app import app as application

if __name__ == "__main__":
    application.run()
"""
    
    with open(wsgi_file_path, "w") as f:
        f.write(wsgi_content)
    
    # Generate Gunicorn configuration
    gunicorn_conf_path = os.path.join(config_dir, "gunicorn.conf.py")
    gunicorn_content = """#!/usr/bin/env python3
\"\"\"
Gunicorn configuration for NCAA Soccer Player Analysis System.
\"\"\"
import os
import multiprocessing

# Bind to the host and port from environment variables or use defaults
bind = f"{os.getenv('HOST', '0.0.0.0')}:{os.getenv('PORT', '8000')}"

# Number of worker processes
workers = int(os.getenv('WORKERS', multiprocessing.cpu_count() * 2 + 1))

# Number of threads per worker
threads = int(os.getenv('THREADS', '2'))

# Worker class
worker_class = 'sync'

# Timeout in seconds
timeout = int(os.getenv('TIMEOUT', '60'))

# Access log and error log
accesslog = os.getenv('ACCESS_LOG', 'deployment/logs/gunicorn_access.log')
errorlog = os.getenv('ERROR_LOG', 'deployment/logs/gunicorn_error.log')

# Log level
loglevel = os.getenv('LOG_LEVEL', 'info')

# Process name
proc_name = 'ncaa_soccer_analysis'

# Preload application
preload_app = True

# Daemon mode
daemon = False
"""
    
    with open(gunicorn_conf_path, "w") as f:
        f.write(gunicorn_content)
    
    # Generate Nginx configuration
    nginx_conf_path = os.path.join(config_dir, "nginx.conf")
    nginx_content = """# Nginx configuration for NCAA Soccer Player Analysis System

server {
    listen 80;
    server_name ncaa-soccer-analysis.example.com;

    # Redirect HTTP to HTTPS
    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name ncaa-soccer-analysis.example.com;

    # SSL configuration
    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    
    # Security headers
    add_header X-Content-Type-Options nosniff;
    add_header X-Frame-Options SAMEORIGIN;
    add_header X-XSS-Protection "1; mode=block";
    
    # Static files
    location /static {
        alias /app/PROJECT/src/dashboard/static;
        expires 1d;
    }
    
    # Proxy requests to Gunicorn
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # Logs
    access_log /var/log/nginx/ncaa-soccer-access.log;
    error_log /var/log/nginx/ncaa-soccer-error.log;
}
"""
    
    with open(nginx_conf_path, "w") as f:
        f.write(nginx_content)
    
    # Generate systemd service file for automatic startup
    systemd_service_path = os.path.join(config_dir, "ncaa-soccer.service")
    systemd_content = """[Unit]
Description=NCAA Soccer Player Analysis System
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/app
Environment="PATH=/app/venv/bin"
ExecStart=/app/venv/bin/gunicorn --config /app/deployment/config/gunicorn.conf.py wsgi:application
Restart=always
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
"""
    
    with open(systemd_service_path, "w") as f:
        f.write(systemd_content)
    
    logger.info(f"Generated web server configuration files")
    return {
        "wsgi": wsgi_file_path,
        "gunicorn": gunicorn_conf_path,
        "nginx": nginx_conf_path,
        "systemd": systemd_service_path
    }
```

### Task 5: Create Docker Configuration
Set up Docker for containerized deployment:

```python
def create_docker_files():
    """Create Docker configuration files for containerized deployment."""
    docker_dir = os.path.join(DEPLOYMENT_DIR, "docker")
    
    # Create Dockerfile
    dockerfile_path = os.path.join(docker_dir, "Dockerfile")
    dockerfile_content = """# Dockerfile for NCAA Soccer Player Analysis System
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Create and set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \\
    build-essential \\
    libpq-dev \\
    && apt-get clean \\
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY PROJECT/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copy project files
COPY PROJECT/ /app/PROJECT/
COPY deployment/config/wsgi.py /app/wsgi.py
COPY deployment/config/gunicorn.conf.py /app/gunicorn.conf.py

# Create non-root user for security
RUN useradd -m appuser
RUN chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Run the application with Gunicorn
CMD ["gunicorn", "--config", "gunicorn.conf.py", "wsgi:application"]
"""
    
    with open(dockerfile_path, "w") as f:
        f.write(dockerfile_content)
    
    # Create docker-compose.yml
    compose_path = os.path.join(docker_dir, "docker-compose.yml")
    compose_content = """version: '3.8'

services:
  web:
    build:
      context: ../..
      dockerfile: deployment/docker/Dockerfile
    restart: always
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://postgres:${DB_PASSWORD}@db:5432/soccer_stats
      - SECRET_KEY=${SECRET_KEY}
      - LOG_LEVEL=info
    volumes:
      - ../..:/app
      - static_volume:/app/PROJECT/src/dashboard/static
    command: gunicorn --config gunicorn.conf.py wsgi:application

  db:
    image: postgres:13
    restart: always
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=soccer_stats
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  nginx:
    image: nginx:latest
    restart: always
    depends_on:
      - web
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - static_volume:/app/PROJECT/src/dashboard/static
      - ./config/nginx.conf:/etc/nginx/conf.d/default.conf
      - ./ssl:/etc/nginx/ssl

volumes:
  postgres_data:
  static_volume:
"""
    
    with open(compose_path, "w") as f:
        f.write(compose_content)
    
    # Create .dockerignore
    dockerignore_path = os.path.join(docker_dir, ".dockerignore")
    dockerignore_content = """# Git
.git
.gitignore

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/

# Docker
.dockerignore
Dockerfile
docker-compose.yml

# IDE
.idea/
.vscode/
*.swp
*.swo

# Test files
tests/
test_*.py

# Deployment files
deployment/backup/
deployment/logs/

# Other
.DS_Store
*.log
*.sqlite
"""
    
    with open(dockerignore_path, "w") as f:
        f.write(dockerignore_content)
    
    logger.info(f"Created Docker configuration files")
    return {
        "dockerfile": dockerfile_path,
        "docker_compose": compose_path,
        "dockerignore": dockerignore_path
    }
```

### Task 6: Generate Deployment Documentation
Create comprehensive documentation for the deployment process:

```python
def generate_deployment_documentation():
    """Generate documentation for the deployment process."""
    docs_dir = os.path.join(DEPLOYMENT_DIR, "docs")
    
    # Create main deployment guide
    guide_path = os.path.join(docs_dir, "deployment_guide.md")
    guide_content = """# NCAA Soccer Player Analysis System - Deployment Guide

## Table of Contents
1. [Introduction](#introduction)
2. [System Requirements](#system-requirements)
3. [Deployment Options](#deployment-options)
   - [Standard Deployment](#standard-deployment)
   - [Docker Deployment](#docker-deployment)
4. [Environment Setup](#environment-setup)
5. [Database Setup](#database-setup)
6. [Web Server Configuration](#web-server-configuration)
7. [Deployment Procedure](#deployment-procedure)
8. [Monitoring and Maintenance](#monitoring-and-maintenance)
9. [Backup and Recovery](#backup-and-recovery)
10. [Troubleshooting](#troubleshooting)

## Introduction
This guide provides detailed instructions for deploying the NCAA Soccer Player Analysis System in different environments. It covers standard deployment on a server as well as containerized deployment using Docker.

## System Requirements
- Python 3.9 or higher
- PostgreSQL 13 or SQLite 3.35+
- Nginx (for production)
- 2GB RAM minimum (4GB recommended)
- 20GB disk space
- Internet connectivity for external data sources

## Deployment Options

### Standard Deployment
Standard deployment involves setting up the application on a server with Python, a database, and a web server. This is suitable for most use cases and provides direct access to the server for monitoring and maintenance.

### Docker Deployment
Docker deployment uses containers to package the application with all its dependencies. This provides consistency across environments and simplifies the deployment process. It's recommended for larger installations or when multiple services need to be deployed together.

## Environment Setup
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ncaa-soccer-analysis.git
   cd ncaa-soccer-analysis
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. Install dependencies:
   ```
   pip install -r PROJECT/requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file based on the provided template.
   ```
   cp deployment/config/env.template .env
   ```
   Edit the `.env` file with your specific configuration.

## Database Setup
1. Initialize the database:
   ```
   python deployment/scripts/database/init_database.py
   ```

2. Run any necessary migrations:
   ```
   flask db upgrade
   ```

3. Load sample data (optional):
   ```
   python deployment/scripts/database/load_sample_data.py
   ```

## Web Server Configuration
1. Configure Gunicorn:
   ```
   cp deployment/config/gunicorn.conf.py .
   ```

2. Set up Nginx (for production):
   ```
   sudo cp deployment/config/nginx.conf /etc/nginx/sites-available/ncaa-soccer
   sudo ln -s /etc/nginx/sites-available/ncaa-soccer /etc/nginx/sites-enabled/
   sudo systemctl restart nginx
   ```

3. Set up systemd service (for auto-start on boot):
   ```
   sudo cp deployment/config/ncaa-soccer.service /etc/systemd/system/
   sudo systemctl enable ncaa-soccer
   sudo systemctl start ncaa-soccer
   ```

## Deployment Procedure

### Standard Deployment
1. Pull the latest changes:
   ```
   git pull origin main
   ```

2. Install/update dependencies:
   ```
   pip install -r PROJECT/requirements.txt
   ```

3. Run database migrations:
   ```
   flask db upgrade
   ```

4. Restart the application:
   ```
   sudo systemctl restart ncaa-soccer
   ```

### Docker Deployment
1. Build and start containers:
   ```
   docker-compose -f deployment/docker/docker-compose.yml up -d --build
   ```

2. Verify services are running:
   ```
   docker-compose -f deployment/docker/docker-compose.yml ps
   ```

## Monitoring and Maintenance
1. View application logs:
   ```
   sudo journalctl -u ncaa-soccer
   ```

2. Monitor system health:
   ```
   python deployment/scripts/monitoring/check_health.py
   ```

3. Update the application:
   ```
   ./deployment/scripts/update.sh
   ```

## Backup and Recovery
1. Backup database:
   ```
   ./deployment/scripts/database/backup_database.sh
   ```

2. Restore from backup:
   ```
   ./deployment/scripts/database/restore_database.sh deployment/backup/backup_file.sql
   ```

## Troubleshooting
### Common Issues
1. **Application not starting:**
   - Check logs: `sudo journalctl -u ncaa-soccer`
   - Verify environment variables: `cat .env`
   - Check permissions: `ls -la`

2. **Database connection issues:**
   - Verify database is running: `pg_isready -h localhost`
   - Check connection parameters in `.env`
   - Restart the database: `sudo systemctl restart postgresql`

3. **Web server errors:**
   - Check Nginx logs: `sudo tail -f /var/log/nginx/error.log`
   - Verify Nginx configuration: `sudo nginx -t`
   - Restart Nginx: `sudo systemctl restart nginx`

### Getting Help
For additional support, please contact the system administrator or refer to the project documentation.
"""
    
    with open(guide_path, "w") as f:
        f.write(guide_content)
    
    # Create quick start guide
    quickstart_path = os.path.join(docs_dir, "quickstart.md")
    quickstart_content = """# NCAA Soccer Player Analysis System - Quick Start Guide

This guide provides a quick overview of how to deploy the NCAA Soccer Player Analysis System in a development environment.

## Prerequisites
- Python 3.9 or higher
- Git
- SQLite (for development)

## Quick Deployment Steps

1. **Clone the repository**
   ```
   git clone https://github.com/yourusername/ncaa-soccer-analysis.git
   cd ncaa-soccer-analysis
   ```

2. **Set up Python environment**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   pip install -r PROJECT/requirements.txt
   ```

3. **Initialize the database**
   ```
   python deployment/scripts/database/init_database.py
   ```

4. **Run the application**
   ```
   export FLASK_APP=PROJECT/src/dashboard/app.py
   export FLASK_ENV=development
   flask run
   ```

5. **Access the application**
   Open your web browser and navigate to http://127.0.0.1:5000

## Next Steps
- For a complete deployment guide, see deployment_guide.md
- For Docker deployment, see docker_deployment.md
- For database setup details, see database_setup.md
"""
    
    with open(quickstart_path, "w") as f:
        f.write(quickstart_content)
    
    # Create Docker deployment guide
    docker_guide_path = os.path.join(docs_dir, "docker_deployment.md")
    docker_guide_content = """# NCAA Soccer Player Analysis System - Docker Deployment Guide

This guide provides detailed instructions for deploying the NCAA Soccer Player Analysis System using Docker and Docker Compose.

## Prerequisites
- Docker (version 19.03 or higher)
- Docker Compose (version 1.27 or higher)
- Git
- 4GB RAM minimum

## Deployment Steps

1. **Clone the repository**
   ```
   git clone https://github.com/yourusername/ncaa-soccer-analysis.git
   cd ncaa-soccer-analysis
   ```

2. **Set up environment variables**
   ```
   cp deployment/config/env.template .env
   ```
   Edit the `.env` file and set the required variables:
   ```
   DB_PASSWORD=your_secure_password
   SECRET_KEY=your_secret_key
   ```

3. **Build and start Docker containers**
   ```
   docker-compose -f deployment/docker/docker-compose.yml up -d --build
   ```

4. **Initialize the database**
   ```
   docker-compose -f deployment/docker/docker-compose.yml exec web python deployment/scripts/database/init_database.py
   ```

5. **Access the application**
   Open your web browser and navigate to http://localhost

## Container Management

- **View logs**
  ```
  docker-compose -f deployment/docker/docker-compose.yml logs -f
  ```

- **Restart services**
  ```
  docker-compose -f deployment/docker/docker-compose.yml restart
  ```

- **Stop all containers**
  ```
  docker-compose -f deployment/docker/docker-compose.yml down
  ```

- **Update the application**
  ```
  git pull
  docker-compose -f deployment/docker/docker-compose.yml up -d --build
  ```

## Data Persistence
Docker volumes are used to persist data:
- `postgres_data`: Database data
- `static_volume`: Static files

## Custom Configuration
To customize the configuration:
1. Modify the appropriate files in `deployment/config/`
2. Rebuild and restart the containers
   ```
   docker-compose -f deployment/docker/docker-compose.yml up -d --build
   ```

## Troubleshooting
- **Container fails to start:**
  Check logs: `docker-compose -f deployment/docker/docker-compose.yml logs`

- **Database connection issues:**
  Verify environment variables in `.env` file

- **Nginx configuration errors:**
  Check Nginx logs: `docker-compose -f deployment/docker/docker-compose.yml logs nginx`
"""
    
    with open(docker_guide_path, "w") as f:
        f.write(docker_guide_content)
    
    logger.info(f"Generated deployment documentation")
    return {
        "deployment_guide": guide_path,
        "quickstart": quickstart_path,
        "docker_guide": docker_guide_path
    }
```

### Task 7: Create a Deployment Package
Create a complete package for deployment:

```python
def create_deployment_package():
    """Create a deployment package with all necessary files."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    package_dir = os.path.join(DEPLOYMENT_DIR, f"release_{timestamp}")
    os.makedirs(package_dir, exist_ok=True)
    
    # Create directory structure
    for subdir in ["project", "config", "scripts", "docs"]:
        os.makedirs(os.path.join(package_dir, subdir), exist_ok=True)
    
    # Copy project files
    project_src = os.path.join(PROJECT_ROOT, "PROJECT", "src")
    project_dest = os.path.join(package_dir, "project", "src")
    shutil.copytree(project_src, project_dest, dirs_exist_ok=True)
    
    # Copy requirements file
    requirements_src = os.path.join(PROJECT_ROOT, "PROJECT", "requirements.txt")
    requirements_dest = os.path.join(package_dir, "project", "requirements.txt")
    shutil.copy2(requirements_src, requirements_dest)
    
    # Copy configuration files
    config_src = os.path.join(DEPLOYMENT_DIR, "config")
    config_dest = os.path.join(package_dir, "config")
    for file in os.listdir(config_src):
        if not file.startswith("."):
            src_file = os.path.join(config_src, file)
            dst_file = os.path.join(config_dest, file)
            if os.path.isfile(src_file):
                shutil.copy2(src_file, dst_file)
    
    # Copy scripts
    scripts_src = os.path.join(DEPLOYMENT_DIR, "scripts")
    scripts_dest = os.path.join(package_dir, "scripts")
    if os.path.exists(scripts_src):
        shutil.copytree(scripts_src, scripts_dest, dirs_exist_ok=True)
    
    # Copy documentation
    docs_src = os.path.join(DEPLOYMENT_DIR, "docs")
    docs_dest = os.path.join(package_dir, "docs")
    if os.path.exists(docs_src):
        shutil.copytree(docs_src, docs_dest, dirs_exist_ok=True)
    
    # Create deployment script
    deploy_script_path = os.path.join(package_dir, "deploy.sh")
    deploy_script = """#!/bin/bash
# Deployment script for NCAA Soccer Player Analysis System

set -e

# Default values
ENV="development"
DOCKER=false
DB_INIT=true

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --env=*)
            ENV="${1#*=}"
            ;;
        --docker)
            DOCKER=true
            ;;
        --skip-db-init)
            DB_INIT=false
            ;;
        --help)
            echo "Usage: deploy.sh [options]"
            echo "Options:"
            echo "  --env=ENVIRONMENT    Deployment environment (development, testing, production)"
            echo "  --docker             Use Docker for deployment"
            echo "  --skip-db-init       Skip database initialization"
            echo "  --help               Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
    shift
done

echo "Deploying NCAA Soccer Player Analysis System..."
echo "Environment: $ENV"
echo "Docker: $DOCKER"

# Create deployment log
LOGFILE="deployment_$(date +%Y%m%d_%H%M%S).log"
exec > >(tee -a "$LOGFILE") 2>&1

echo "Deployment started at $(date)"

# Load environment-specific configuration
if [ -f "config/${ENV}_config.sh" ]; then
    echo "Loading $ENV environment configuration..."
    source "config/${ENV}_config.sh"
else
    echo "Warning: No environment-specific configuration found for $ENV"
fi

if [ "$DOCKER" = true ]; then
    echo "Using Docker deployment..."
    
    # Check if docker-compose is installed
    if ! command -v docker-compose &> /dev/null; then
        echo "Error: docker-compose is not installed"
        exit 1
    fi
    
    # Build and start Docker containers
    echo "Building and starting Docker containers..."
    docker-compose -f config/docker-compose.yml up -d --build
    
    # Initialize database if needed
    if [ "$DB_INIT" = true ]; then
        echo "Initializing database..."
        docker-compose -f config/docker-compose.yml exec web python scripts/database/init_database.py
    fi
    
    echo "Docker deployment completed successfully"
else
    echo "Using standard deployment..."
    
    # Create virtual environment if it doesn't exist
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python3 -m venv venv
    fi
    
    # Activate virtual environment
    echo "Activating virtual environment..."
    source venv/bin/activate
    
    # Install dependencies
    echo "Installing dependencies..."
    pip install -r project/requirements.txt
    
    # Initialize database if needed
    if [ "$DB_INIT" = true ]; then
        echo "Initializing database..."
        python scripts/database/init_database.py
    fi
    
    # Start the application based on environment
    if [ "$ENV" = "production" ]; then
        echo "Starting application in production mode..."
        # Start with Gunicorn
        gunicorn --config config/gunicorn.conf.py wsgi:application
    else
        echo "Starting application in development mode..."
        # Start with Flask development server
        export FLASK_APP=project/src/dashboard/app.py
        export FLASK_ENV=$ENV
        flask run
    fi
fi

echo "Deployment completed at $(date)"
"""
    
    with open(deploy_script_path, "w") as f:
        f.write(deploy_script)
    
    # Make the script executable
    os.chmod(deploy_script_path, 0o755)
    
    # Create a README file for the package
    readme_path = os.path.join(package_dir, "README.md")
    readme_content = f"""# NCAA Soccer Player Analysis System - Deployment Package

## Version Information
- Release Date: {datetime.now().strftime("%Y-%m-%d")}
- Release Time: {datetime.now().strftime("%H:%M:%S")}
- Package ID: {timestamp}

## Quick Start
1. Unpack this deployment package
2. Review the documentation in the `docs` directory
3. Set up your environment variables (see `config/env.template`)
4. Run the deployment script:
   ```
   ./deploy.sh --env=development
   ```

## Package Contents
- `project/`: Application source code
- `config/`: Configuration files for different environments
- `scripts/`: Utility scripts for deployment and maintenance
- `docs/`: Documentation

## Additional Resources
For detailed deployment instructions, please refer to the documentation in the `docs` directory.
"""
    
    with open(readme_path, "w") as f:
        f.write(readme_content)
    
    # Create a zip archive of the package
    package_zip_path = os.path.join(DEPLOYMENT_DIR, f"ncaa_soccer_analysis_{timestamp}.zip")
    shutil.make_archive(
        os.path.splitext(package_zip_path)[0],  # Path without .zip extension
        'zip',
        package_dir
    )
    
    logger.info(f"Created deployment package at {package_zip_path}")
    return package_zip_path
```

## Hints and Tips

1. **Environment Variables**:
   - Use environment variables for sensitive information (credentials, API keys)
   - Create templates with placeholder values for documentation
   - Load environment variables from a `.env` file in development
   - Use a secure method for managing secrets in production

2. **Configuration Management**:
   - Create separate configurations for each environment
   - Use a configuration hierarchy (defaults ⟶ environment-specific ⟶ local overrides)
   - Validate configuration values at startup
   - Document all configuration options

3. **Database Handling**:
   - Create scripts for database initialization and migrations
   - Implement regular backup procedures
   - Test database restoration procedures
   - Use connection pooling in production

4. **Security Considerations**:
   - Use HTTPS in production
   - Set appropriate file permissions
   - Run services with minimal required privileges
   - Implement proper authentication and authorization
   - Configure secure headers in web servers

5. **Docker Best Practices**:
   - Use multi-stage builds to reduce image size
   - Don't run containers as root
   - Use specific version tags for base images
   - Create a `.dockerignore` file
   - Use volumes for persistent data

## Extension Opportunities

1. **CI/CD Pipeline**: Set up a continuous integration and deployment pipeline using GitHub Actions or similar tools.

2. **Multi-environment Deployment**: Expand the configuration for more complex deployment scenarios with staging, QA, etc.

3. **Kubernetes Deployment**: Create Kubernetes configuration files for container orchestration.

4. **Blue-Green Deployment**: Implement a blue-green deployment strategy for zero-downtime upgrades.

5. **Infrastructure as Code**: Use tools like Terraform or Ansible to define and provision infrastructure.

6. **Monitoring Stack**: Integrate with monitoring solutions like Prometheus and Grafana.

7. **Performance Optimization**: Add caching layers and performance optimizations for production.

## Resources

- [Flask Deployment Documentation](https://flask.palletsprojects.com/en/2.0.x/deploying/)
- [Docker Documentation](https://docs.docker.com/)
- [Nginx Configuration Guide](https://www.nginx.com/resources/wiki/)
- [12 Factor App Methodology](https://12factor.net/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Web Application Security Best Practices](https://owasp.org/www-project-top-ten/)
- [Database Backup Strategies](https://www.postgresql.org/docs/current/backup.html)

## Submission

Complete the implementation of the functions in `deployment.py`. When you run the script, it should create all the necessary deployment files and configuration in the 'deployment' directory.