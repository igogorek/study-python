def clock_hands(angle):
    # in degrees every second
    hour_hand_moves = 360.0 / (360.0 * 12.0)
    minute_hand_moves = 360.0 / 360.0

    # angle = sec_of_hour*minute_hand_moves - sec_of_day*hour_hand_moves
    # sec_of_day = hour_in_sec + sec_of_hour
    sec_of_hour_list = [int((angle + hour * 360 * hour_hand_moves) / (minute_hand_moves - hour_hand_moves))
                        for hour in xrange(12)]
    return ['{0}:{1}:{2}'.format((12 - (12 - hour) % 12), sec_of_hour / 60, sec_of_hour % 60)
            for hour, sec_of_hour in enumerate(sec_of_hour_list)]
