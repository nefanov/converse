import psutil

for proc in psutil.process_iter():
     try:
         pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
     except psutil.NoSuchProcess:
         pass
     else:
         print(pinfo)
