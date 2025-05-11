def getMinimumCost(k, c):
    c.sort(reverse=True)  # buy expensive flowers first
    total_cost = 0

    for i in range(len(c)):
        person = i % k  # distribute evenly
        times_bought = i // k  # how many times this person has already bought
        total_cost += (times_bought + 1) * c[i]

    return total_cost