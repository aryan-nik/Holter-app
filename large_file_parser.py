
import os
import time

start = time.time()

file_name = "data.txt"

print(f'File Size is {os.stat(file_name).st_size / (1024 * 1024)} MB')

txt_file = open(file_name,'rb')

count = 0

for line in txt_file:
    # we can process file line by line here, for simplicity I am taking count of lines
    count += 1

txt_file.close()

print(f'Number of Lines in the file is {count}')

end = time.time()
print("Execution time in seconds: ",(end - start))



# only of unix baseds
# import resource
# print('Peak Memory Usage =', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
# print('User Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
# print('System Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_stime)




# with open(file_name) as f:
#     while True:
#         data = f.read(1024)
#         if not data:
#             break
#         print(data)