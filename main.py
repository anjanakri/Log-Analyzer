import sys
import argparse

parser=argparse.ArgumentParser(description="Log File Analyzer") #welcomes, and checks if they gave right info
parser.add_argument("--file", help="Path to the log file", required=True) #arguemnet me  --file filename pass hoga
args=parser.parse_args() #reading
print(args.file)
# if (len(sys.argv)<2):
#     print("OOPS GIVE LOG FILE NAME")
#     sys.exit()
    
from log_parser import read_log, parse_data
from analyzer import analyzer
from report import report

# file=sys.argv[1]
# Flow
data = read_log(args.file)
parsed = parse_data(data)
total, ip_counts, url_counts, status_counts = analyzer(parsed)
report(total, ip_counts, url_counts, status_counts)
