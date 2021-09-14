Mathew = []
John = []
Mathew_John = []

list1 = []



T1 = int(input("Enter the upper limit of the series:"))
T2 = int(input("Enter the lower limit of the series:"))
M = input("Enter the position:")

if T1 < 0 or T2 < 0 or T1 >= 10000000 or T2 >= 10000000:
    print("Invalid Input")
    
elif M == 'a':
    print("Invalid Input")

else:
    M = int(M)
    
    for i in range(1, 710):
        q = (i * ((2 * i) - 1))

        if q > T1:
            break
        else:
            Mathew.append(q)

    for j in range(1, 710):

        q1 = (j * (j + 1)) / 2

        if q1 > T1:
            break

        else:
            John.append(round(q1))

    for i in range(0, len(Mathew)):
        if Mathew[i] in John:
            Mathew_John.append(Mathew[i])

    # print(Mathew)
    # print(John)
    # print(Mathew_John)

    for i in range(0, len(Mathew_John)):
        if Mathew_John[i] >= T2 and Mathew_John[i] <= T1:
            list1.append(Mathew_John[i])

    if len(list1) < M:
        print("No number is present at this index")

    else:
        print(list1[M-1])
