'''
棋子定位计算，输入棋子圆心坐标列表，输出棋子位置列表
'''
# 棋盘单格间距 80
CenterPo_list = [[73, 79], [81, 629]]
xposi_list = [0, 80, 160, 240, 320, 382, 462, 542, 622, 702]  #棋盘x方向节点的像素列表
yposi_list = [0, 80, 160, 240, 320, 400, 480, 560, 640, 720]
xy_list = []


# 定义函数来找到坐标距离列表中哪一个节点最近
def FindNearPoint(point, PoList):
    distance = []
    for id, posi in enumerate(PoList):
        distance.append(abs(posi - point))
    return distance.index(min(distance))

# 判定棋子在左侧还是右侧
for chess_xy in CenterPo_list:
    xy_list.append([FindNearPoint(chess_xy[0], xposi_list),FindNearPoint(chess_xy[1], yposi_list)])

print(xy_list)