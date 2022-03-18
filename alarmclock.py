class AlarmClock:
    def __init__(self, time, alarm_status, alarm_time):
        self.current_time = time
        self.alarm_on = alarm_status
        self.alarm_one = alarm_time

    def set_time(self):
        self.current_time = input("What time would you like to sent the current time to be?")
        print(f'You set the current time to {self.current_time}')
    
    def toggle_alarm(self):
        if self.alarm_on == False:
            self.alarm_on = True
            print("You turn the alarm on")
        elif self.alarm_on == True:
            self.alarm_on - False
            print("You turn the alarm off")

    
    def set_alarm(self):
        self.alarm_one = input("What time would you like to set the current time to be?")
        print(f'You set the alarm time to {self.alarm_one}')


    