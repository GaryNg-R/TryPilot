# 1+1 function
def add(a, b):
    return a + b    

# ping google.com
def ping():
    import os
    hostname = "google.com"
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
    return pingstatus   
