import time

# Get the current time
t = time.localtime()

# Print the time since the Epoch
print("Seconds since January 1, 1970:", "{:,}".format(time.mktime(t)), "or", "{:.1e}".format(time.mktime(t)), "in scientific notation")

# Print the current date
print(time.strftime("%b %d %Y", t))