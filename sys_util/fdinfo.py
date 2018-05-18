import sys, os, psutil, fnctl
import statvfs

# returns max filename length according to the fs type
def fn_len_loc(path)
    return os.statvfs(path)[statvfs.F_NAMEMAX]
# res = fnctl(...)
# fd, F_GETPATH, filePath
