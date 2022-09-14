def combinations(group, members):
    if members == 0:
        return None
    elif members == 1:
        return group
    return int((group / members) * combinations(group-1, members-1))
