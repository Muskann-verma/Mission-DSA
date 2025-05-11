def queensAttack(n, k, r_q, c_q, obstacles):
    attacks = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (-1, 1), (1, -1), (-1, -1)]

    obstacles = set(map(tuple, obstacles))

    for dr, dc in directions:
        r, c = r_q, c_q
        while True:
            r += dr
            c += dc
            if not (1 <= r <= n and 1 <= c <= n):
                break
            if (r, c) in obstacles:
                break
            attacks += 1

    return attacks
