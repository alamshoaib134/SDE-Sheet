'''You are given the schedule of N meetings with their start time Start[i] and end time End[i]. But you have only 1 meeting room. So, you need to tell the meeting numbers you can organize in the given room, such that the number of meetings organized is maximum.'''


start = [0, 7, 1, 4, 8]
end = [2, 9, 5, 9, 10]
inter = []
for i in range(len(start)):
    inter.append((end[i],start[i],i+1))
inter.sort()
res = []
cur_time = inter[0][0]
res.append(inter[0][2])
for ele in inter[1:]:
    if ele[1] > cur_time:
        res.append(ele[2])
        cur_time = ele[0]
print(res)

