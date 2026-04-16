import re
import sys

#reading the file
def read_log(filepath):
    try:
        with open(filepath, "r") as f:
            d=f.readlines()
            return d
    except FileNotFoundError:
        print(f"Error: File '{filepath}' Not Found!")
        sys.exit()
#parser function
def parse_data(d):
    pd_list=[]
    pattern= r'(\d+\.\d+\.\d+\.\d+) - - \[(.+?)\] \"(.+?)\" (\d{3}) (\d+)'
    for i in d:
        pd=re.match(pattern,i)
        
        if pd: #agr line malformed hua to NONE return hoga
            pd_list.append(pd.groups()) #and agr NONE hua to groups crash hoga
    return pd_list
