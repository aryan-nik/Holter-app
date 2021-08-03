
import os
import time


start = time.time()

file_name = "data-files\examples\large_data.txt"
print(f'File Size is {os.stat(file_name).st_size / (1024 * 1024)} MB')


def split_by_delimiter(rows, delimiter):
    for row in rows:
        yield str(row).split(delimiter)


def read_file(fp):
    while True:
        line = fp.readline()
        if line is None:
            break
        yield line




if __name__ == '__main__':
    with open(file_name, "rb") as fp:
        lines = read_file(fp)
        lines = split_by_delimiter(lines, "|")

        for line in lines:
            print(line)
            
    end = time.time()
    print("Execution time in seconds: ",(end - start))







# only of unix baseds
# import resource
# print('Peak Memory Usage =', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
# print('User Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
# print('System Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_stime)
