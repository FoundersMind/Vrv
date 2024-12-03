import csv

def display_results(ip_requests, most_accessed_endpoint, suspicious_activity):
    
    print("Requests per IP: in Descending Order")
    print(f"{'IP Address':<20} {'Request Count':<15}")
    y=sorted(ip_requests.items(),key=lambda x:x[1],reverse=True)
    for ip, count in y:
        print(f"{ip:<20} {count:<15}")
    
    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed_endpoint[0]} (Accessed {most_accessed_endpoint[1]} times)")
    
    
    if suspicious_activity:
        print("\nSuspicious Activity Detected:")
        print(f"{'IP Address':<20} {'Failed Login Attempts':<20}")
        for ip, count in suspicious_activity.items():
            print(f"{ip:<20} {count:<20}")
    else:
        print("\nSuspicious activity not detected.")
import csv

def save_to_csv(ip_requests, most_accessed_endpoint, suspicious_activity, output_file):
    """Save analysis results to a CSV file with properly aligned columns."""
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        
        # Write requests per IP with serial numbers
        writer.writerow(["S.No.", "IP Address", "Request Count"])
        for sno, (ip, count) in enumerate(ip_requests.items(), start=1):
            writer.writerow([f"{sno:<5}", f"{ip:<20}", f"{count:<15}"])
        
        # Add a blank line for separation
        writer.writerow([])
        
        # Write most accessed endpoint with serial number
        writer.writerow(["S.No.", "Endpoint", "Access Count"])
        writer.writerow([f"{1:<5}", f"{most_accessed_endpoint[0]:<20}", f"{most_accessed_endpoint[1]:<15}"])  # Most accessed endpoint
        
        # Add a blank line for separation
        writer.writerow([])
        
        # Write suspicious activity with serial numbers
        writer.writerow(["S.No.", "IP Address", "Failed Login Count"])
        for sno, (ip, count) in enumerate(suspicious_activity.items(), start=1):
            writer.writerow([f"{sno:<5}", f"{ip:<20}", f"{count:<15}"])

