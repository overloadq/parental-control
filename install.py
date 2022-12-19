import subprocess

# Install the dependencies
subprocess.call(["pip", "install", "-r", "requirements.txt"])

# Install the service
subprocess.call(["python", "win_service.py", "install"])

# Start the service
subprocess.call(["python", "win_service.py", "start"])
