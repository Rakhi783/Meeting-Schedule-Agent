from calendar import meetings
from helper import get_time, is_free

saved_date = None
saved_time = None


def add_meeting(date, time):
    slot = f"{time}-{int(time[:2])+1}:00"
    if date in meetings:
        meetings[date].append(slot)
    else:
        meetings[date] = [slot]


def agent_reply(user_input):
    global saved_date, saved_time

    if "tomorrow" in user_input.lower():
        saved_date = "2026-02-07"

    if saved_time is None:
        saved_time = get_time(user_input)

    if saved_date is None:
        return "Please tell the meeting day."

    if saved_time is None:
        return "Please tell the meeting time."

    if is_free(saved_date, saved_time, meetings):
        add_meeting(saved_date, saved_time)
        saved_date = None
        saved_time = None
        return "Meeting scheduled successfully."
    else:
        saved_time = None
        return "That time is already booked. Try another time."
