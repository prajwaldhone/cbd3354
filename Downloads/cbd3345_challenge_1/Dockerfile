# Step 1: The base image of the container
FROM python:3.11-slim

# Step 2: Define the working directory
WORKDIR /

# Step 3: Copy the project files
COPY . .

# Step 4: Install the dependencies
RUN pip install -r requirements.txt

# Step 5: Expose the port and run
EXPOSE 5000
CMD ["python", "-u", "main.py"]
