'''
Problem: A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
Each LED represents a zero or one, with the least significant bit on the right.

top 4 LEDs - [8,4,2,1]
bottom 6 LEDs - [32,16,8,4,2,1]

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
For example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Input: n = 2
Return: ['10:00', '9:00', '8:32', '8:16', '8:08', '8:04', '8:02', '8:01', '6:00', '5:00', '4:32', '4:16', '4:08', '4:04', '4:02', '4:01', '3:00', '2:32', '2:16', '2:08', '2:04', '2:02', '2:01', '1:32', '1:16', '1:08', '1:04', '1:02', '1:01', '0:48', '0:40', '0:36', '0:34', '0:33', '0:24', '0:20', '0:18', '0:17', '0:12', '0:10', '0:09', '0:06', '0:05', '0:03']

Recursive/Backtracking/DFS Approach:
Put all the LEDs in one array [8,4,2,1,32,16,8,4,2,1], start from left to right and if i<4 (represents hour) else (represents minutes)
pass only hour and minutes array along with index i in a backtrack function. Base case would be when combined length of both the arrays
is equal to num (which means n number of LEDs are on), inside it form the required time from hour and minutes array.

Snapshot of how the below code will execute and create a recursive tree

                                      i  0 1 2 3  4  5 6 7 8 9
                                        [8,4,2,1,32,16,8,4,2,1]

                                            ([],[],0)
                                        /                           ................
                                ([8],[],1)
                 /       /               \               \              .............
    ([8,4],[],2)    ([8,2],[],3)      ([8,1],[],4)    ([8],[32],5)
                    res:['10:00']     res:['10:00',   res:['10:00',     
                                          '9:00']          '9:00',
                                                           '8:32'] 

'''


def readBinaryWatch(num):
        def backtrack(tmp_h, tmp_m, start):
            #if found the required number of turned on lights
            if len(tmp_h) + len(tmp_m) == num:
                h, m = sum(tmp_h), sum(tmp_m)
                if h <= 11 and m <= 59:#restriction as given in the problem
                    concat_str = ":0" if m < 10 else ":"                
                    res.append(str(h) + concat_str + str(m))
                return
            #iterate through the LEDs from left to right
            for i in range(start, 10):
                if i < 4:
                    backtrack(tmp_h + [nums[i]], tmp_m, i + 1)
                else:
                    backtrack(tmp_h, tmp_m + [nums[i]], i + 1)

        nums = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        res = []
        backtrack([], [], 0)
        return res

print readBinaryWatch(2)