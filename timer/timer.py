import time

calculate = int(input("How many seconds should it take? "))
print("This is the start of the program.")
start_time = time.time()
time.sleep(calculate)

end_time = time.time()
elapsed_time = int(end_time - start_time)
print(elapsed_time)

print("This is the end of the program.")