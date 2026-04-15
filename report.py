from datetime import datetime

def report(n, ip_frequency, url_frequency, status):
    with open("report.txt", "w") as f:
        f.write("=" * 40 + "\n")
        f.write("LOG ANALYSIS REPORT".center(40)+"\n")
        f.write("-" * 40 + "\n")
        timestamp=datetime.now().strftime("%d/ %m/ %Y, (%H : %M : %S)")
        f.write(timestamp.center(40)+"\n")
        f.write("=" * 40 + "\n\n")
        
        f.write(f"Total request : {n}\n")
        
        f.write("Top 3 IPs : \n")
        for ip, count in ip_frequency.most_common(3):
            f.write(f"  {ip} -- {count} requests.\n")
            
        f.write("\nTop 3 URLs:\n")
        for url, count in url_frequency.most_common(3):
            f.write(f"  {url} -> {count} requests\n")

        f.write("\nStatus Codes:\n")
        for status, count in status.items():
            f.write(f"  {status} -> {count} times\n")

    print("Report saved to report.txt!")
        