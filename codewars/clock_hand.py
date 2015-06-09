import datetime


def clock_hands(angle):
    def clock_hands_generator(angle):
        hour_hand_speed = 360.0 / (3600.0 * 12.0)
        minute_hand_speed = 360.0 / 3600.0
        hour = 0
        while hour < 11:
            yield datetime.datetime.utcfromtimestamp(
                int((angle + hour * 3600 * minute_hand_speed) / (minute_hand_speed - hour_hand_speed)))
            hour += 1

    return ['{:0>2}:{:0>2}:{:0>2}'.format((12 - (12 - a_time.hour) % 12), a_time.minute, a_time.second)
            for a_time in clock_hands_generator(angle)]


print clock_hands(270)

