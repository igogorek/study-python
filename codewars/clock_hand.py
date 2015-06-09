import datetime

DEGREES_IN_CIRCLE = 360.0
SECONDS_IN_HOUR = 60.0 * 60.0
HOUR_HAND_SPEED = DEGREES_IN_CIRCLE / (SECONDS_IN_HOUR * 12.0)
MINUTE_HAND_SPEED = DEGREES_IN_CIRCLE / SECONDS_IN_HOUR


def clock_hands(angle):
    def time_gen(angle):
        hour = 0
        while hour < 11:
            yield datetime.datetime.utcfromtimestamp(
                # angle = second_of_hour * MINUTE_HAND_SPEED - second_of_day * HOUR_HAND_SPEED
                # second_of_hour = second_of_day - hour * SECONDS_IN_HOUR , then second_of_day is
                (angle + hour * SECONDS_IN_HOUR * MINUTE_HAND_SPEED) / (MINUTE_HAND_SPEED - HOUR_HAND_SPEED))
            hour += 1

    return ['{:0>2}:{:0>2}:{:0>2}'.format(t.hour or 12, t.minute, t.second) for t in time_gen(angle % 360)]


print clock_hands(120)



