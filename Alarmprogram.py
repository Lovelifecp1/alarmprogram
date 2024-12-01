

# Get the current tie from the user
current_time = int(input("Enter the current time (in hours, 0-23): "))

# Get the number of hours to waIt for the alarm
wait_hours = int(input("Enter the current number of hours to waIt for the alarm: "))

# Calculate the time the alarm will go off
raw_alarm_time = current_time + wait_hours
alarm_time = raw_alarm_time % 24

# Display results
print(f" If it is currently {current_time:02d}:00, the alarm will go off at {alarm_time:02d}:00.")


