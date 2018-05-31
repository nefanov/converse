import os
import fcntl

pipe_1_name = "name_1"

if os.path.exists(pipe_1_name):
    os.remove(pipe_1_name)
    os.mkfifo(pipe_1_name)
else:
    os.mkfifo(pipe_1_name)


pipe_1 = open(pipe_1_name, "w")
pipe_1.write("aaa")
#pipe_1_wr = open(pipe_1_name,"r")

print(pipe_1.fileno())
print(os.path.realpath('/proc/self/fd/'+str(pipe_1.fileno())))
