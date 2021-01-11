#!/usr/bin.env python
# -*- coding:utf-8 -*-
# author:Qin Ziqiu
# date:2021-01-10

class Solve:
    def __init__(self, maze_list, start_x, start_y, end_x, end_y):
        self.zoom = len(maze_list)
        self.maze_list = maze_list
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.m = self.copymaze()
        self.ministeps = self.solve() - 1
        # self.print_m()
        self.minipath = self.minipath()

    # 产生相同大小的迷宫，所有位置初始化为0，用于计算数值
    def copymaze(self):
        m = []
        for i in range(len(self.maze_list)):
            m.append([])
            for j in range(len(self.maze_list[i])):
                m[-1].append(0)
        # 起点为1
        m[self.start_x][self.start_y] = 1
        return m

    # 改变通路的数值
    def make_step(self, k):
        m = self.m
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == k:
                    if i > 0 and m[i - 1][j] == 0 and self.maze_list[i - 1][j] == 0:
                        m[i - 1][j] = k + 1
                    if j > 0 and m[i][j - 1] == 0 and self.maze_list[i][j - 1] == 0:
                        m[i][j - 1] = k + 1
                    if i < len(m) - 1 and m[i + 1][j] == 0 and self.maze_list[i + 1][j] == 0:
                        m[i + 1][j] = k + 1
                    if j < len(m[i]) - 1 and m[i][j + 1] == 0 and self.maze_list[i][j + 1] == 0:
                        m[i][j + 1] = k + 1

    # 不断增加数值，直到终点值改变，不为0
    def solve(self):
        k = 0
        while self.m[self.end_x][self.end_y] == 0:
            k += 1
            self.make_step(k)
        return self.m[self.end_x][self.end_y]

    # 显示记录数值的迷宫结果
    def print_m(self):
        m = self.m
        for i in range(len(m)):
            for j in range(len(m[i])):
                print(str(m[i][j]).ljust(2), end=' ')
            print()

    # 根据记录的值回溯路线
    def minipath(self):
        m = self.m
        i = self.end_x
        j = self.end_y
        k = m[i][j]
        the_path = [(i, j)]
        while k > 1:
            if i > 0 and m[i - 1][j] == k - 1:
                i, j = i - 1, j
                the_path.append((i, j))
                k -= 1
            elif j > 0 and m[i][j - 1] == k - 1:
                i, j = i, j - 1
                the_path.append((i, j))
                k -= 1
            elif i < len(m) - 1 and m[i + 1][j] == k - 1:
                i, j = i + 1, j
                the_path.append((i, j))
                k -= 1
            elif j < len(m[i]) - 1 and m[i][j + 1] == k - 1:
                i, j = i, j + 1
                the_path.append((i, j))
                k -= 1
        return the_path

    def print_minipath(self):
        minimaze = [[1 for i in range(self.zoom)] for z in range(self.zoom)]
        the_path = self.minipath
        for item in the_path:
            minimaze[item[0]][item[1]] = "-"
        minimaze[self.start_x][self.start_y] = "#"
        minimaze[self.end_x][self.end_y] = "$"
        for row in minimaze:
            for each in row:
                print(each, end=" ")
            print()


if __name__ == '__main__':
    a = [
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
    ]
    mini = Solve(a, 0, 5, 12, 7)
