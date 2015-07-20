#Roommate Finder - Dylan Bowman 2015


#Rate function, dot product of 2 vectors assuming vectors have same domain
def rate(lista,listb):
    #Ensure the dot product works, if not print an error.
    if len(lista) == len(listb):
        return sum([(a-3)*(b-3) for (a,b) in zip(lista,listb)])
    else:
        print ("Vector domains are not equal! Returned 0.")
        return 0

#Interpret file into dictionaries (Name/Gender, Name/Vector, Name/Hall)
fileHandle=open("girls.csv", "r")
personList = fileHandle.readlines()
genDict = {}
vecDict = {}
hallDict = {}

#Put each person into the proper dictionaries
for person in personList:
    #Turn string into list, strip whitespace
    dataList = [x.strip() for x in person.split(",")]
    #Put gender into genDict, remove gender from list
    genDict[dataList[0]] = dataList[1].lower()
    dataList.remove(dataList[1])
    #Put hall into hallDict, remove hall from list
    hallDict[dataList[0]] = dataList[len(dataList)-1].lower()
    dataList.remove(dataList[len(dataList)-1])
    #Put vec into vecDict
    vecDict[dataList[0]] = [int(x) for x in dataList[1:]]

#Find the best roommate for each person.
for person in vecDict.keys():
    roommateList=list(vecDict.keys())
    roommateList.remove(person)
    dictionary = {}
    for roommate in roommateList:
        rating = rate(vecDict[person],vecDict[roommate])
        dictionary[roommate]=rating
    #The max function only returns one max, so there's a safeguard in case of multiple.
    bestRoommate = max(dictionary, key=dictionary.get)
    bestList = [bestRoommate]
    rating = dictionary[bestRoommate]
    for x in roommateList:
        if dictionary[x]==rating and x != bestRoommate:
            bestList.append(x)
    worstRoommate = min(dictionary, key=dictionary.get)
    worstList = [worstRoommate]
    rating = dictionary[worstRoommate]
    for x in roommateList:
        if dictionary[x]==rating and x != worstRoommate:
            worstList.append(x)
    print (person+":")
    if len(bestList)==1:
        print ("   Best: "+bestRoommate+" (Score:"+str(dictionary[bestRoommate])+")")
    else:
        string = ""
        for x in bestList:
            string = string + ", "+x
        print ("   Best: "+string[2:]+" (Score:"+str(dictionary[bestRoommate])+")")
    if len(worstList)==1:
        print ("   Worst: "+worstRoommate+" (Score:"+str(dictionary[worstRoommate])+")")
    else:
        string = ""
        for x in worstList:
            string = string + ", "+x
        print ("   Worst: "+string[2:]+" (Score:"+str(dictionary[worstRoommate])+")")





fileHandle.close()
