import re
from collections import Counter 
from datetime import datetime

#reading the file
def read_log():
    with open("sample.log", "r") as f:
        d=f.readlines()
        return d

#parser function
def parse_data(d):
    pd_list=[]
    pattern= r'(\d+\.\d+\.\d+\.\d+) - - \[(.+?)\] \"(.+?)\" (\d{3}) (\d+)'
    for i in d:
        pd=re.match(pattern,i)
        
        if pd: #agr line malformed hua to NONE return hoga
            pd_list.append(pd.groups()) #and agr NONE hua to groups crash hoga
    return pd_list

#a function to count
def analyzer(parsed):
    n=len(parsed)
    ip_frequency=Counter(ip[0] for ip in parsed) #agr ek hi ip waps mila to uski entry badha dega
    # url_frequency=Counter(url[2] for url in parsed)#when we are talking about urls we mean we want just the '/about.html' part from the url
    #therefore to get url part only we need to write
    url_frequency=Counter(url[2].split()[1] for url in parsed)
    status=Counter(stat[3] for stat in parsed)
    
    print(f"Total Requests: {n}")
    print(f"Top 3 ips: {ip_frequency.most_common(3)}")
    print(f"Top 3  Urls: {url_frequency.most_common(3)}") 
    print(f"status codes: {status}")
    return n, ip_frequency, url_frequency, status

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
        
        
data = read_log()
parsed = parse_data(data)
for d in parsed:
    print(d)
total, ip_counts, url_counts, status_counts = analyzer(parsed)
report(total, ip_counts, url_counts, status_counts)




# if (len(sys.argv)<2):
#     print("OOPS GIVE LOG FILE NAME")
#     sys.exit()




# d=read_log()
# for i in d:
#     s=i
#     print(s.split())
    
# print("----------")
# line = '192.168.1.1 - - [10/Apr/2026:10:00:01 +0000] "GET /index.html HTTP/1.1" 200 512'
# pattern=r'(\d+\.\d+\.\d+\.\d+) - - \[(.+?)\] \"(.+?)\" (\d{3}) (\d+)'
# result=re.match(pattern, line)
# print(result.groups())