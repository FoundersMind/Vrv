import re
from collections import Counter
import os 

def determine_chunk_size(file_path):
    """Determine the chunk size based on the file size."""
    file_size = os.path.getsize(file_path)

    # Dynamically set chunk size based on file size
    if file_size < 10 * 1024 * 1024:  # Less than 10 MB
        return 4096  # 4 KB
    elif file_size < 100 * 1024 * 1024:  # Less than 100 MB
        return 8192  # 8 KB
    else:  # For larger files
        return 65536  # 64 KB


def parse_log_file(log_file):
    """Parse the log file and return extracted data."""
    ip_requests = Counter()
    endpoint_requests = Counter()
    failed_logins = Counter()

    # Open the file in text mode (default) to avoid manual decoding
    with open(log_file, "r", encoding="utf-8") as file:
        # Read the file in chunks
        chunk_size = determine_chunk_size(log_file)
        buffer = file.read(chunk_size)
        
        while buffer:
            # Process each line in the current buffer
            lines = buffer.splitlines()  # Split by lines directly
            for line in lines:
                # Extract IP address
                ip_match = re.match(r"(\d+\.\d+\.\d+\.\d+)", line)
                if not ip_match:
                    continue
                ip_address = ip_match.group(1)
                ip_requests[ip_address] += 1

                # Extract endpoint
                endpoint_match = re.search(r'"[A-Z]+ (.+?) HTTP', line)
                status_code_match = re.search(r'HTTP/\d\.\d" (\d{3}) (\d+)', line)
                
                if endpoint_match and status_code_match:
                    endpoint = endpoint_match.group(1)
                    status_code = status_code_match.group(1)  # Extract status code
                    
                    # Only count endpoints with status code 200
                    if status_code == "200":
                        endpoint_requests[endpoint] += 1
                
                # Match status code and the "Invalid credentials" part
                if status_code_match:
                    status_code = status_code_match.group(1)  # This captures the HTTP status code (e.g., 401)
                    if status_code == "401" or "Invalid credentials" in line:
                        failed_logins[ip_address] += 1
            
            # Read the next chunk
            buffer = file.read(chunk_size)

    return ip_requests, endpoint_requests, failed_logins


