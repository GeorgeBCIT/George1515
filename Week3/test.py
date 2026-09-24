KB = 1024
MB = 1048576
GB = 1073741824

num_entries = input("Please enter the number of entries per second: ")
entry_size = input("Please enter the average number of bytes per entry: ")

bytes_per_sec = int(num_entries) * int(entry_size)
bytes_per_min = bytes_per_sec * 60
bytes_per_hour = bytes_per_sec * 3600
bytes_per_day = bytes_per_sec * 86400

kb_size = (bytes_per_min) / KB
mb_size = (bytes_per_hour) / MB
gb_size = (bytes_per_day) / GB
print("Storage Estimates")
print(f"Per minute: {kb_size}KB")
print(f"Per hour: {mb_size}MB")
print(f"Per day: {gb_size}GB")

