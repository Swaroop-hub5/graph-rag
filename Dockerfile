# 1. Use an official lightweight Python runtime
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy dependencies first (for better caching)
COPY requirements.txt .

# 4. Install Python dependencies
# We add --no-cache-dir to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code
COPY . .

# 6. Expose the port Streamlit runs on
EXPOSE 8501

# 7. Define the command to run your app
# We use "--server.address=0.0.0.0" so it's accessible outside the container
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]