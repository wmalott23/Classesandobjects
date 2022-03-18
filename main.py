# As a developer, I want to use Python’s proper snake_case for variable names.

# As a developer, I want to create a AlarmClock class.

# As a developer, I want the AlarmClock class to have class instance variables to keep track of the AlarmClock’s current time, whether the alarm is on or off, and the time the alarm is set to. (You can use arbitrary strings to represent the time, it does not need to accurately tell the current time or change over time).

# As a developer, I want the AlarmClock class to have a method to set (or change) the current time and print to the console the current time.

# As a developer, I want the AlarmClock class to have a method to toggle the alarm on or off.

# As a developer, I want the AlarmClock class to have a method to set the current alarm time and print to the console the current alarm time.

# As a developer, I want to import the AlarmClock class into main.py so I can instantiate it as a new AlarmClock object and call methods on it.


from alarmclock import AlarmClock

alarm_clock = AlarmClock("5 PM", False, "")

print(alarm_clock.current_time)

alarm_clock.set_time()

alarm_clock.toggle_alarm()