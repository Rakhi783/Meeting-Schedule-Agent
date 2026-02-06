def get_time(text):
    words = text.lower().split()
    for word in words:
        if word.isdigit():
            hour = int(word)
            if hour < 9:
                hour += 12
            return f"{hour}:00"
    return None


def is_free(date, time, meetings):
    if date not in meetings:
        return True
    for slot in meetings[date]:
        if time in slot:
            return False
    return True
