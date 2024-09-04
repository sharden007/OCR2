import socket

# Function to check if the server is running
def is_server_running(host='127.0.0.1', port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            return True
        except (socket.error, socket.gaierror):
            return False

# Check server status
if not is_server_running():
    print("Server is not running on 127.0.0.1:5000")
else:
    print("Server is running")