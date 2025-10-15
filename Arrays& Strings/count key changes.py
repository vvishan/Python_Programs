def countkeychanges(d):
    changes = 0
    last_used = d[0].lower()

    for i in d[1:]:
        if d.lower() != last_used.lower():
            changes += 1

    return changes