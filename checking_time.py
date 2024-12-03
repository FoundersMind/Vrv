import time
import io

# Function for line-by-line reading
def process_line_by_line(file_path):
    with open(file_path, "r") as file:
        for line in file:
            process_line(line)

# Function for buffered reading
# Function for buffered reading (using binary mode)
def process_buffered_reading(file_path):
    with open(file_path, "rb") as file:  # Open in binary mode ('rb')
        buffered_file = io.BufferedReader(file)
        for line in buffered_file:
            process_line(line.decode('utf-8'))  # Decode binary data to string


# Dummy function to simulate processing each line
def process_line(line):
    # Replace with actual logic (e.g., extracting IPs, endpoints, etc.)
    pass  

# Measure time for line-by-line reading
def measure_line_by_line_time(file_path):
    start_time = time.time()
    process_line_by_line(file_path)
    end_time = time.time()
    return end_time - start_time

# Measure time for buffered reading
def measure_buffered_reading_time(file_path):
    start_time = time.time()
    process_buffered_reading(file_path)
    end_time = time.time()
    return end_time - start_time

def main():
    log_file = "sample.log"  # Replace with your actual log file path
    
    # Measure and print time for line-by-line reading
    line_by_line_time = measure_line_by_line_time(log_file)
    print(f"Time taken for line-by-line reading: {line_by_line_time:.4f} seconds")

    # Measure and print time for buffered reading
    buffered_reading_time = measure_buffered_reading_time(log_file)
    print(f"Time taken for buffered reading: {buffered_reading_time:.4f} seconds")

if __name__ == "__main__":
    main()
