def most_accessed_endpoint(endpoint_requests):
    """Find the most frequently accessed endpoint."""
    return endpoint_requests.most_common(1)[0]

def detect_suspicious_activity(failed_logins, threshold):
    """Identify IPs with suspicious activity based on failed login threshold."""
    
    suspicious_ips = {}
    for ip, count in failed_logins.items():
        if count > threshold:
            suspicious_ips[ip] = count #####
        
    
    return suspicious_ips

