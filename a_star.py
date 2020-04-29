#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from mapinfo import MapInfo
from copy import deepcopy
import math


class AStar(object):
    def __init__(self, start, end, map_info):
        self._s = start
        self._e = end
        self._map_info = map_info
        self._openset = dict()
        self._closeset = dict()

    def distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def neighbor_nodes(self, x):
        plist = [(x[0] - 1, x[1] - 1), (x[0] - 1, x[1]), (x[0] - 1, x[1] + 1), (x[0], x[1] + 1), (x[0] + 1, x[1] + 1),
                 (x[0] + 1, x[1]), (x[0] + 1, x[1] - 1), (x[0], x[1] - 1)]
        for p in plist:
            if not self._map_info.is_collision(point=p):
                yield p

    def reconstruct_path(self):
        pt = self._e
        path = []
        while pt:
            path.append(pt)
            pt = self._closeset[pt]['camefrom']
        return path[::-1]

    def run(self, display=False):
        h = self.distance(self._s, self._e)
        # 字典套字典
        self._openset[self._s] = {'g': 0, 'h': h, 'f': h, 'camefrom': None}
        while self._openset:
            # 找到当前openlist中的最小点
            x = min(self._openset, key=lambda key: self._openset[key]['f'])
            # 拷贝到closeList
            self._closeset[x] = deepcopy(self._openset[x])
            # 从openlist中删除X
            del self._openset[x]
            # 如果找到目标点，结束while循环
            if self.distance(x, self._e) < 1.0:
                if x != self._e:
                    self._closeset[self._e] = {'camefrom': x}
                return True
            # 所有曾经扩展的节点
            if display:
                self._map_info.close = x
            # 否则查看所有的邻居
            for y in self.neighbor_nodes(x):
                if y in self._closeset:
                    continue
                tentative_g_score = self._closeset[x]['g'] + self.distance(x, y)
                if y not in self._openset:
                    tentative_is_better = True
                elif tentative_g_score < self._openset[y]['g']:
                    tentative_is_better = True
                else:
                    tentative_is_better = False
                if tentative_is_better:
                    h = self.distance(y, self._e)
                    self._openset[y] = {'g': tentative_g_score, 'h': h, 'f': tentative_g_score + h, 'camefrom': x}
                    if display:
                        self._map_info.open = y
        return False

# 任务流程：
# 1. 地图流程
# 2. 将jps的改写
if __name__ == "__main__":
    m = MapInfo(60, 40)
    m.show()
    m.start = (10.5, 10)
    m.end = (50, 30)
    m.obstacle = [(20, i) for i in range(30)] + [(40, 40 - i) for i in range(30)]
    plan = AStar(m.start, m.end, m)
    if plan.run(display=False):
        m.path = plan.reconstruct_path()
    m.wait_close()
