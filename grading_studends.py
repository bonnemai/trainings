def _round(grade:int)->int:
    if grade < 38:
        return grade
    r = grade % 5
    if r >= 3:
        grade += (5 - r)
    return grade