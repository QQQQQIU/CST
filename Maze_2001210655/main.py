#!/usr/bin.env python
# -*- coding:utf-8 -*-
# author:Qin Ziqiu
# date:2021-01-10
from create import generate_maze
from solve import Solve
from player import startgame

while 1:
    astr = input("\n欢迎体验迷宫游戏\n输入***退出程序\n请问您要尝试几阶迷宫：")
    if astr.isdigit():
        num = int(astr)
        if num % 2 == 0:
            num += 1
        if num <= 3:
            print('阶数太小了，试试大一点的~')
        else:
            maze = generate_maze(num)
            maze_object = Solve(maze[0], maze[1][0], maze[1][1], maze[2][0], maze[2][1])
            player_step = startgame(maze[0], maze[1][0], maze[1][1], maze[2][0], maze[2][1])
            if player_step:
                ministep = maze_object.ministeps
                score = (1 - (player_step - ministep) / ministep) * 100
                print("最少步数为%d步，您的完成度为%.2f%%" % (ministep, score))
                print("以下为最佳路线")
                maze_object.print_minipath()
            else:
                print("游戏结束，下次再见！")
                break
    elif astr == "***":
        print("游戏结束，下次再见！")
        break
    else:
        print("请输入正整数，或***退出游戏\n")
