# VRV Assignment

This project is designed to parse and analyze log files. It processes logs to extract relevant data such as IP addresses, endpoints, status codes, and failed login attempts. The purpose of this project is to efficiently read and analyze large log files by implementing a buffered reading mechanism.

## Features

- **Buffered File Reading**: Efficiently processes large log files in chunks.
- **Log Parsing**: Extracts information such as IP addresses, HTTP endpoints, status codes, and failed login attempts.
- **Dynamic Chunk Size**: Adjusts the chunk size for reading based on the file size.
- **Data Aggregation**: Counts occurrences of IP addresses, endpoint requests, and failed logins.
- **Performance Comparison**: Includes the ability to compare the performance between normal file reading and buffered file reading using `checking_time`.

## Installation

To use this project, follow the steps below.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)

# Performance Comparison (Normal vs Buffered File Reading)
This project includes functionality to compare the performance of normal file reading and buffered file reading. The checking_time method is used to measure and compare the time taken by both methods to process the log file.

## Normal File Reading:
Normal file reading reads the entire file at once, consuming more memory for large files. This method doesn't optimize memory usage and can be slower when dealing with very large log files.

## Buffered File Reading:
Buffered reading reads the file in chunks, which allows it to handle large files more efficiently by reducing memory consumption and improving performance.

To compare the performance of both methods, the script will output the time taken for each approach in the console.

# Results :
   
   1. PS C:\Users\KIIT\Documents\vrv_assignment> python checking_time.py
   Time taken for line-by-line reading: 0.00103545 seconds
   Time taken for buffered reading: 0.00000000 seconds

## Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/FoundersMind/Vrv.git
2. Navigate to the project directory:
   ```bash
    cd Vrv
3. Install the required dependencies:
   ```bash 
  No such additional packages as re,os and others are already provided with python 

4. run using 
   ```bash 
   python main.py


## output:
1.
   ```bash
      Requests per IP: in Descending Order
      IP Address           Request Count
      203.0.113.5          8
      198.51.100.23        8
      192.168.1.1          7
      10.0.0.2             6
      192.168.1.100        5

      Most Frequently Accessed Endpoint:
      /home (Accessed 5 times)

      Suspicious activity not detected.


## usage
  This will parse the log file and output the following:

IP Address Requests: A count of requests per IP.
Endpoint Requests: A count of successful (status code 200) requests per endpoint.
Failed Logins: A count of failed login attempts by IP address (based on status code 401 or invalid credentials).

## Additional Information
The script employs a buffered reading technique that helps process large log files efficiently by splitting them into smaller chunks. The chunk size is determined dynamically based on the file size, which ensures that the script performs optimally for both small and large files. This helps reduce memory usage and improves performance when dealing with log files that could potentially contain millions of lines.

## Handling Different Log Formats
The script is designed to handle logs in a general format, where each log line may contain an IP address, HTTP method, endpoint, status code, and other potential fields. Adjustments can be made to the regular expressions used in the script to accommodate different log formats if necessary.

# Customization
You can modify the script to fit your specific log analysis needs. For example:

Adjust the regular expressions for different log formats.
Add more data aggregation logic, such as counting the number of unique endpoints.
Implement custom filters based on status codes or specific keywords.

## Various Regex:
1.
ip_match = re.match(r"(\d+\.\d+\.\d+\.\d+)", line)

endpoint_match = re.search(r'"[A-Z]+ (.+?) HTTP', line)

status_code_match = re.search(r'HTTP/\d\.\d" (\d{3}) (\d+)', line)

## Important Files:
1.log_reader.py (contains the code for reading the file in buffered chunks instead of line by line to reduce time complexity)

2.analyzer.py (contains code for finding most accessed endpoint  and threshold logic=10)

3.report.py (where we are displaying in terminal and saving in csv file)

4.sample.log (where we have info about the log files)

5.main.py (where we are calling all the functions and finally using python main.py to run the code)






