def returnMatches(*lists):
    matches = []

    for i in lists[0]:
        if i in lists[1]:
            matches.append(i)
    return {"matches": list(matches), "count": len(matches)}

if __name__ == '__main__':
    list1 = [1,2,3,6]
    list2 = [3, 8, 1, 2]
    result = returnMatches(list1, list2)
    print(f"mas: {result['matches']}, count: {result['count']}")
