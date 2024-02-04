def end_string(x, y):
    if len(x) == 0 or len(y) == 0:
        return True
    if len(y) > len(x):
        return False
    if x[-1] == y[-1]:
        return end_string(x[:-1], y[:-1])
    else:
        return False


# examples:
assert end_string("sumo", "umo") is True, "Should be true"
assert end_string("sumo", "omo") is False, "Should be false"
assert end_string("zebra", "eb") is False, "Should be false"
assert end_string("ails", "fails") is False, "Should be false"
assert end_string("fails", "ails") is True, "Should be true"
assert end_string("abc", "abcd") is False, "Should be false"

print(end_string("sumo", "umo"))
