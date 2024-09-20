# Step 1: Use Python image
FROM python:3.9-slim

# Step 2: Set work directory (inside the container)
WORKDIR /app

# Step 3: Copy requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Step 4: Copy the entire backend directory to the container
COPY ./backend /app

# Step 5: Expose port 8000 for Django
EXPOSE 8000

# Step 6: Run Django migrations and start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
