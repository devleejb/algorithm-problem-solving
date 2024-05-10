def ConvertListStrToSet(listStr):
    return set(map(int, listStr.split(",")))


def FindIntersection(strArr):
    firstSet, secondSet = map(ConvertListStrToSet, strArr)
    intersection = firstSet.intersection(secondSet)

    if not intersection:
        return "false"

    return ",".join(map(str, sorted(list(intersection))))


print(FindIntersection(input()))
