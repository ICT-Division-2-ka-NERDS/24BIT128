d1 = {"milk":50,"bread":33,"toothpast":98}
d2 = {"milk":2,"bread":4,"toothpast":1}
totle_bill = 0
for k1,v1 in d1.items():
    for k2,v2 in d2.items():
        if (k1 == k2):
            totle_bill += v1 * v2
            break
print(totle_bill)