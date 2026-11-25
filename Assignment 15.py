
# Assignment No. 15
# Step 1: Import the required modules
import gc
import tracemalloc
import time

# Step 2: Define a class for creating cyclic objects
class Node:
    def __init__(self):
        # Each node stores a reference to another node
        self.reference = None

# Step 3: Start memory tracking
# tracemalloc monitors memory allocations
tracemalloc.start()

# Step 4: Define a function to create reference cycles
def create_cycles(number):
    for i in range(number):

        # Create two Node objects
        a = Node()
        b = Node()

        # Make both objects refer to each other
        a.reference = b
        b.reference = a

        # This creates a reference cycle
        # Garbage collector will clean these objects later

# Step 5: Create 10,000 cyclic objects
create_cycles(10000)

# Step 6: Measure memory before garbage collection
current_before, peak_before = tracemalloc.get_traced_memory()

# Display memory usage in KB
print("Memory before GC:",
      round(current_before / 1024, 2), "KB")

# Step 7: Measure garbage collection execution time
start_time = time.perf_counter()

# Manually run garbage collection
collected = gc.collect()

# Calculate the time taken
gc_time = time.perf_counter() - start_time

# Step 8: Measure memory after garbage collection
current_after, peak_after = tracemalloc.get_traced_memory()

# Step 9: Display the results
print("Objects collected:", collected)

print("Memory after GC:",
      round(current_after / 1024, 2), "KB")

print("Peak traced memory:",
      round(peak_after / 1024, 2), "KB")

print("GC execution time:",
      round(gc_time, 6), "seconds")

# Step 10: Stop memory tracking
tracemalloc.stop()

# End of program
print("Garbage collection completed successfully!")
