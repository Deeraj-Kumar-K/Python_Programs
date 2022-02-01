# Calendar Meetings

# Write a function that takes in your's and your coworker's calendar, daily limits,
# and the duration of the meeting that you want to schedule.
# Return a list of all the time slots during which you could schedule the meeting.
'''
Explanation:

You want to schedule a meeting of a certain duration with a coworker.
You are given a calendar, that has a list of all your meetings and your coworker's calendar.
Meetings are in the form [startTime, endTime].
The daily limits of you and your coworker is also given.
Daily limits is the time when you reach office and leave your office.
Times will be given and also should be returned in military time.
Example time: '9:30', '8:01', '22:55'
'''


#############################################################################
# Inputs

calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
dailyLimits1 = ["9:00", "20:00"]
calendar2 = [
                ["10:00", "11:30"],["12:30", "14:30"],
                ["14:30", "15:00"],["16:00", "17:00"],
            ]
dailyLimits2 = ["10:00", "18:30"]
meetingDuration = 30 #minutes

print(calendarMeetings(calendar1, dailyLimits1, calendar2, dailyLimits2, meetingDuration))

#output = [["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]
