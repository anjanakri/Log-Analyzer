from collections import Counter


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