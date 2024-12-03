from log_reader import parse_log_file
from analyzer import most_accessed_endpoint, detect_suspicious_activity
from report import display_results, save_to_csv

LOG_FILE = "sample.log"
OUTPUT_FILE = "log_analysis_results.csv"
FAILED_LOGIN_THRESHOLD = 10

def main():
    # Step 1: Parse log file
    ip_requests, endpoint_requests, failed_logins = parse_log_file(LOG_FILE)
    
    # Step 2: Analyze data
    most_accessed = most_accessed_endpoint(endpoint_requests)
    suspicious_activity = detect_suspicious_activity(failed_logins, FAILED_LOGIN_THRESHOLD)
    
    # Step 3: Display and save results
    display_results(ip_requests, most_accessed, suspicious_activity)
    save_to_csv(ip_requests, most_accessed, suspicious_activity, OUTPUT_FILE)

if __name__ == "__main__":
    main()
