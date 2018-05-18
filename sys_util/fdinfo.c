#include <sys/syslimits.h>
#include <fcntl.h>

char filePath[PATH_MAX];
if (fcntl(fd, F_GETPATH, filePath) != -1)
{
    // do something with the file path
}
