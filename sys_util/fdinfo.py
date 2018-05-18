import sys, os, psutil
import fnctl, statvfs, socket

# returns max filename length according to the fs type
def fn_len_loc(path)
    return os.statvfs(path)[statvfs.F_NAMEMAX]

def get_sock_info(fd):
    host, port = socket.getsockname()
    return (host, port)
# res = fnctl(...)
# fd, F_GETPATH, filePath
