from log_parser import read_log, parse_data
from analyzer import analyzer
from report import report

# Flow
data = read_log()
parsed = parse_data(data)
for d in parsed:
    print(d)
total, ip_counts, url_counts, status_counts = analyzer(parsed)
report(total, ip_counts, url_counts, status_counts)
