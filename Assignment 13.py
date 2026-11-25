# assignment code for 13 
# Step 1: Import the threading module
import threading

# Step 2: Define the first task
def task1():
    for i in range(1, 4):
        print("Task 1 - Counting:", i)

# Step 3: Define the second task
def task2():
    for i in range(1, 4):
        print("Task 2 - Counting:", i)

# Step 4: Define the third task
def task3():
    for i in range(1, 4):
        print("Task 3 - Counting:", i)

# Step 5: Create separate threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)

# Step 6: Start all threads
t1.start()
t2.start()
t3.start()

# Step 7: Wait until all threads finish
t1.join()
t2.join()
t3.join()

# Step 8: Print the final message
print("All tasks completed!")
