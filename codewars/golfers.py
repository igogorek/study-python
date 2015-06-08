import difflib


def valid(tournament):
    if len(tournament) == 0:
        return True

    expected_group_count = len(tournament[0])
    if [day_groups for day_groups in tournament if len(day_groups) != expected_group_count]:
        return False

    groups = [group for day_groups in tournament for group in day_groups]
    expected_group_size = len(tournament[0][0])
    if [group for group in groups if len(group) != expected_group_size]:
        return False

    days_flattened = [''.join(day_groups) for day_groups in tournament]
    if [player for day in days_flattened for player in day if days_flattened.count(player) > 1]:
        return False

    for i in xrange(len(groups)-1):
        for j in xrange(i+1, len(groups)):
            if len(difflib.SequenceMatcher(None, groups[i], groups[j]).get_matching_blocks()) > 1:
                return False

    return True