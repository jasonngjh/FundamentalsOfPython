def josephus(n):
    seats = []
    for i in range(1, n + 1):
        seats.append(i)

    while True:
        if len(seats) == 1:

            break

        turn = seats[0]
        next_person = seats[1]

        del seats[0]
        del seats[0]

        seats.append(turn)

    return seats[0]


for n in range(2, 100):
    print("{0} kills {1}".format(n, josephus(n)))
