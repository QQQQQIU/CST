#!/usr/bin.env python
# -*- coding:utf-8 -*-
# author:Qin Ziqiu
# date:2021-01-10

def startgame(maze_list, start_x, start_y, end_x, end_y):
    print("欢迎游戏!")
    print("按键盘d向右走，w,a,s,分别向上、左、下前行。")
    print("【1是墙壁，无法通行】  【#是您当前所在位置】  【—是您走过的路】  【$是目的地】")

    player = [start_x, start_y]
    target = (end_x, end_y)
    maze_list[start_x][start_y] = "#"
    maze_list[end_x][end_y] = "$"
    player_steps = 0

    def drawmaze(maze_list):
        for item in maze_list:
            for each in item:
                print(each, end=" ")
            print()

    while (1):
        drawmaze(maze_list)
        if (player[0] == target[0] and player[1] == target[1]):
            print(f"祝贺你游戏成功！\n共用{player_steps}步~")
            break

        inpi = str(input(f"已走{player_steps}步\n请输入下一步："))
        if (inpi == "***"):
            return False
        elif (inpi == "s"):
            if (maze_list[player[0] + 1][player[1]] == 1):
                print("此路不通!\n")
                continue
            else:
                print()
            maze_list[player[0]][player[1]] = "-"
            player[0] += 1
            maze_list[player[0]][player[1]] = "#"
            player_steps += 1
        elif (inpi == "w"):
            if (maze_list[player[0] - 1][player[1]] == 1):
                print("此路不通!\n")
                continue
            else:
                print()
            maze_list[player[0]][player[1]] = "-"
            player[0] -= 1
            maze_list[player[0]][player[1]] = "#"
            player_steps += 1
        elif (inpi == "d"):
            if (maze_list[player[0]][player[1] + 1] == 1):
                print("此路不通!\n")
                continue
            else:
                print()
            maze_list[player[0]][player[1]] = "-"
            player[1] += 1
            maze_list[player[0]][player[1]] = "#"
            player_steps += 1
        elif (inpi == "a"):
            if (maze_list[player[0]][player[1] - 1] == 1):
                print("此路不通!\n")
                continue
            else:
                print()
            maze_list[player[0]][player[1]] = "-"
            player[1] -= 1
            maze_list[player[0]][player[1]] = "#"
            player_steps += 1
        else:
            print("请输入移动方向（a左w上s下d右）")

    return player_steps


if __name__ == '__main__':
    a = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
    startgame(a, 1, 1, 2, 2)
