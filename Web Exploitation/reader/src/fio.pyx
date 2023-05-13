from libc.stdio cimport *

def read_file(filename):
    filename_byte_string = filename.encode("UTF-8")
    cdef char* fname = filename_byte_string
 
    cdef FILE* cfile
    cfile = fopen(fname, "rb")
    if cfile == NULL:
        raise FileNotFoundError(2, "No such file or directory: '%s'" % filename)
 
    cdef char * line = NULL
    cdef size_t bufsize = 0
    cdef ssize_t read_len
 
    while True:
        read_len = getline(&line, &bufsize, cfile)
        if read_len == -1: break
 
        yield line
 
    fclose(cfile)
