def are_valid_groups():
    # get list of student numbers
    students = int(input("Enter number of students: "))
    lst = []
    print ("Enter student numbers: ")
    for i in range(students):
        lst.append(int(input()))

    #get list of groups
    groupno = int(input("Enter no of groups: "))
    grplst = []
    grp = []
    c = 1
    grouplimno = int(input("Enter group limit: "))
    for i in range(groupno):
        print("group: ", c)
        for j in range(grouplimno):
            grp.append(int(input()))
        c += 1
        grplst.append(grp)
        grp = []

    lst1 = sum(grplst, [])

    if sorted(lst) == sorted(lst1):
        return True
    else:
        return False

are_valid_groups()
