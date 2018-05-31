import os
import fcntl
pipe_1_name = "name_1"



pipe_1_wr = open(pipe_1_name,"r")
zz=pipe_1_wr.read()

print(fcntl.fcntl(pipe_1_wr.fileno(), fcntl.F_GETFL))
pipe_1_wr.close()
