def luckBalance(k, contests):
    total_luck=0
    important = []
    
    for luck, importance in contests:
        if importance == 0:
            total_luck += luck
        else:
            important.append(luck)
    important.sort(reverse = True)    
    total_luck += sum(important[:k])
    total_luck -= sum(important[k:])
    return total_luck  