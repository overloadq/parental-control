from file_ops import write_time, get_current_date

time_file = "c:\\temp\\time.txt"

# on shutdown write the closing PC time
now = get_current_date()
write_time(time_file, now)
