def dice_rolls():
    for i in range(1,7):
        for j in range(1,7):
            for k in range(1,7):
                print i,j,k 

def dice_rolls_backtracking(res,dice):
    if dice == 0:
        print res 
    else:
        for i in range(1,7):
            res.append(i)
            dice_rolls_backtracking(res,dice-1)
            res.pop()

#dice_rolls_backtracking([],2)

def dice_rolls_backtracking_sum(res,dice,desired):
    if dice == 0:
        if sum(res) == desired:
            print res  
    else:
        for i in range(1,7):
            res.append(i)
            dice_rolls_backtracking_sum(res,dice-1,desired)
            res.pop()

#dice_rolls_backtracking_sum([],2,3)

def dice_rolls_backtracking_sum_pruned(res,dice,desired):
    if dice == 0:
        if sum(res) == desired:
            print res  
    else:
        if sum(res) <= desired and sum(res) + 6*dice >= desired: 
            for i in range(1,7):
                res.append(i)
                dice_rolls_backtracking_sum(res,dice-1,desired)
                res.pop()

dice_rolls_backtracking_sum_pruned([],2,3)