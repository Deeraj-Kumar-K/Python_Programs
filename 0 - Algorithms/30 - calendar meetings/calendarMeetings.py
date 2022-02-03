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

def calendarMeetings(calendar1, dailyLimits1, calendar2, dailyLimits2, meetingDuration):
    updatedCalendar1 = updateCalendar(calendar1, dailyLimits1)
    updatedCalendar2 = updateCalendar(calendar2, dailyLimits2)
    mergedCalendar = mergeCalendar(updatedCalendar1, updatedCalendar2)
    flattenedCalendar = flatCalendar(mergedCalendar)
    return gapBetweenMeetings(flattenedCalendar, meetingDuration)

def updateCalendar(calendar, limits):
    updatedCalendar = calendar[:]
    updatedCalendar.insert(0, ['0:00', limits[0]])
    updatedCalendar.append([limits[1], '23:59'])
    return list(map(lambda time: [timeToMinutes(time[0]), timeToMinutes(time[1])], updatedCalendar))

def timeToMinutes(time):
    hours, minutes = list(map(int, time.split(':')))
    return hours * 60 + minutes

def mergeCalendar(calendar1, calendar2):
    merged = []
    i = 0
    j = 0
    while i < len(calendar1) and j < len(calendar2):
        meeting1 = calendar1[i]
        meeting2 = calendar2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else:
            merged.append(meeting2)
            j += 1
    while i < len(calendar1):
        merged.append(calendar1[i])
        i += 1
    while j < len(calendar2):
        merged.append(calendar2[j])
        j += 1
    return merged

def flatCalendar(calendar):
    flat = [calendar[0][:]]
    for i in range(1, len(calendar)):
        currentMeeting = calendar[i]
        currStart, currEnd = currentMeeting
        prevMeeting = flat[-1]
        lastStart, lastEnd = prevMeeting
        if lastEnd >= currStart:
            newMeeting = [lastStart, max(lastEnd, currEnd)]
            flat[-1] = newMeeting
        else:
            flat.append(currentMeeting[:])
    return flat
    
def gapBetweenMeetings(calendar, meetingDuration):
    availableTimeSlots = []
    for i in range(1, len(calendar)):
        availableTime = calendar[i][0] - calendar[i - 1][1]
        if availableTime >= meetingDuration:
            availableTimeSlots.append([calendar[i - 1][1], calendar[i][0]])
    return list(map(lambda time: [minutesToTime(time[0]), minutesToTime(time[1])], availableTimeSlots))

def minutesToTime(minutes):
    hrs = minutes // 60
    mins = minutes % 60
    hoursString = str(hrs)
    minutesString = '0' + str(mins) if mins < 10 else str(mins)
    return hoursString + ':' + minutesString
    
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
