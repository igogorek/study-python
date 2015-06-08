def valid(tournament):
    print tournament
    # desired behaviour was not specified in instructions
    if len(tournament) == 0:
        return True

    expected_group_count = len(tournament[0])
    # fail if days have different count of groups
    if any([len(day_groups) != expected_group_count for day_groups in tournament]):
        return False

    groups = [group for day_groups in tournament for group in day_groups]
    expected_group_size = len(tournament[0][0])
    # fail if days have groups of different size
    if any([len(group) != expected_group_size for group in groups]):
        return False

    days_flattened = [''.join(day_groups) for day_groups in tournament]
    # fail if player plays more than once a day
    if any([days_flattened.count(player) > 1 for day in days_flattened for player in day]):
        return False

    # fail if two players play more than once
    for i in xrange(len(groups) - 1):
        for j in xrange(i + 1, len(groups)):
            if len(set(groups[i]).intersection(set(groups[j]))) > 1:
                return False

    expected_day_players = set(days_flattened[0])
    if [day for day in days_flattened if set(day) != expected_day_players]:
        return False

    return True


s = [['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'], ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'], ['AGKO', 'BIPT', 'CJMS', 'DHFR', 'ELNQ'], ['AHLP', 'NKBS', 'CEOR', 'DFIQ', 'MJGT'], ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']]
print valid(s)