import time
import io

# Function for line-by-line reading
def process_line_by_line(file_path):
    with open(file_path, "r") as file:
        for line in file:
            pass  

# Function for buffered reading (using binary mode)
def process_buffered_reading(file_path):
    with open(file_path, "rb") as file:  # Open in binary mode ('rb')
        buffered_file = io.BufferedReader(file)
        for line in buffered_file:
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
    log_file = "sample.log"  
    
    # Measure and print time for line-by-line reading
    line_by_line_time = measure_line_by_line_time(log_file)
    print(f"Time taken for line-by-line reading: {line_by_line_time:.8f} seconds")

    # Measure and print time for buffered reading
    buffered_reading_time = measure_buffered_reading_time(log_file)
    print(f"Time taken for buffered reading: {buffered_reading_time:.8f} seconds")

if __name__ == "__main__":
    main()
