# 创建一个字典，存储每个选手的胜率
win_rate = {'A1': 0, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0}

# 根据历史数据，计算每个选手的胜率
win_rate['A1'] = (23 + 21 + 20 + 18 + 18 + 21) / 6
win_rate['A2'] = (21 + 21 + 21 + 21 + 13 + 23) / 6
win_rate['A3'] = (0 + 0 + 0 + 0 + 0 + 0) / 6
win_rate['A4'] = (0 + 0 + 0 + 0 + 0 + 0) / 6
win_rate['A5'] = (0 + 0 + 0 + 0 + 0 + 0) / 6

# 根据胜率从高到低排序选手
sorted_win_rate = sorted(win_rate.items(), key=lambda x: x[1], reverse=True)

# 输出最优出场顺序
print("最优出场顺序为：")
for i in range(5):
    print(sorted_win_rate[i][0])