
# sorted
example_list = [5, 0, 6, 1, 2, 7, 3, 4]
result_list = sorted(example_list, key=lambda x: x*-1)
print("ret: ", result_list)
print("ret1: ", sorted(example_list, reverse=False))

array = [{"age":20,"name":"a"},{"age":25,"name":"b"},{"age":10,"name":"c"}]
array = sorted(array,key=lambda x:x["age"])
print(array)

d1 = [{'name':'alice', 'score':38}, {'name':'bob', 'score':18}, {'name':'darl', 'score':28}, {'name':'christ', 'score':28}]
l = sorted(d1, key=lambda x:(-x['score'], x['name']))
print(l)

s = "德国 10 11 16\n意大利 10 10 20\n荷兰 10 12 14\n法国 10 12 11\n英国 22 21 22\n中国 38 32 18\n日本 27 14 17\n美国 39 41 33\n俄罗斯奥委会 20 28 23\n澳大利亚 17 7 22\n匈牙利 6 7 7\n加拿大 7 6 11\n古巴 7 3 5\n巴西 7 6 8\n新西兰 7 6 7"
stodata = s.split('\n',-1)
# 使用sorted
para = {}
for line in range(len(stodata)):
    # 每一行数据
    data = stodata[line].split(' ')
    print(data)
    # 组装数据结构para={'China': [], 'Russia': []}
    para[data[0]] = [int('-' + i) for i in data[1:]]
# 开始排序(x[1]代表奖牌数目, x[0]代表国家)
new_para = sorted(para.items(), key=lambda x: (x[1], x[0]))
print()
c=[]
for i in new_para:
     c.append((i[0]))
for j in range(10):
    print(f"{(j+1):2d}  {c[j]}")

