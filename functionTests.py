def dropDuplicateRoads(val):
    listRoads = x = val.split(",")
    return list(dict.fromkeys(listRoads))

print(dropDuplicateRoads("N101,N101,N101,N101,N105,N101"))
