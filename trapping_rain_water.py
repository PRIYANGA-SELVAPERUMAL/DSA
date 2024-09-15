def trap(h):
    l, r = 0, len(h) - 1
    lm, rm = 0, 0
    res = 0
    while l < r:
        if h[l] < h[r]:
            if h[l] >= lm:
                lm = h[l]
            else:
                res += lm - h[l]
            l += 1
        else:
            if h[r] >= rm:
                rm = h[r]
            else:
                res += rm - h[r]
            r -= 1
    return res

h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(h))
