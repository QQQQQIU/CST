#!/usr/bin.env python
# -*- coding:utf-8 -*-
# author:Qin Ziqiu
# date:2021-01-09

import turtle as t
import random


def main(x, y):
    # 清空画布
    t.reset()
    # 随机产生长度，递归次数和图形
    length = random.choice([100, 200, 300, 400, 500])
    level = random.choice([6, 5, 4, 3])
    alist = ["koch", "tree_H", "snow", "tree_C", "heart"]
    draw = random.choice(alist)
    # 有的图形过大或过小不太好看，所以此处限定了部分图形的尺寸和递归范围
    if draw == "koch":
        koch(random.choice([100, 150, 200]), level)
    elif draw == "tree_H":
        tree_H(level, 0, 0, length)
    elif draw == "snow":
        snow(random.choice([100, 200, 300]), random.choice([4, 3]))
    elif draw == "tree_C":
        tree_C(length, 11)
    else:
        heart(random.choice([10, 11, 12, 13, 14, 15]))


# 上下对称雪花
def koch(length, level):
    t.penup()
    t.goto(-length / 2, length / 6)
    t.pendown()
    inner(length, level)
    # 水平对称线
    drawLine(-5 * length / 8, 0, 5 * length / 8, 0)
    t.penup()
    t.goto(length / 2, -length / 6)
    t.pendown()
    t.left(180)
    inner(length, level)


# 六边形雪花
def snow(size, n):
    t.penup()
    t.goto(-0.5 * size, 0.866 * size)
    t.pendown()
    for i in range(6):
        inner(size, n)
        t.right(60)


# 老师上课讲的单边递归雪花
def inner(length, level):
    if level == 0:
        t.forward(length)
    else:
        for angle in [0, 60, -120, 60]:
            t.left(angle)
            # 随机画笔的颜色
            t.pencolor([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
            inner(length / 3, level - 1)


# 在(x,y)处画一个H
def draw_H(x, y, l):
    line_a = [[x - l / 2, y + l / 2], [x - l / 2, y - l / 2]]
    line_b = [[x - l / 2, y], [x + l / 2, y]]
    line_c = [[x + l / 2, y + l / 2], [x + l / 2, y - l / 2]]
    t.pencolor([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
    drawLine(line_a[0][0], line_a[0][1], line_a[1][0], line_a[1][1])
    drawLine(line_b[0][0], line_b[0][1], line_b[1][0], line_b[1][1])
    drawLine(line_c[0][0], line_c[0][1], line_c[1][0], line_c[1][1])


# H递归树
def tree_H(n, x, y, l):
    if n == 0:
        return
    draw_H(x, y, l)
    # 每一个 H 有四个顶点，所以有四个自身调用
    tree_H(n - 1, x - l / 2, y + l / 2, l / 2)
    tree_H(n - 1, x - l / 2, y - l / 2, l / 2)
    tree_H(n - 1, x + l / 2, y + l / 2, l / 2)
    tree_H(n - 1, x + l / 2, y - l / 2, l / 2)


# (x1,y1)到(x2,y2)的直线
def drawLine(x1, y1, x2, y2):
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)


# C型递归树
def tree_C(length, level):
    # 根据长度产生初始坐标
    x1 = -length / 2
    x2 = length / 2
    y1 = length / 2
    y2 = length / 2

    def inc(x1, y1, x2, y2, level):
        if level == 0:
            drawLine(x1, y1, x2, y2)
        else:
            newX = (x1 + x2) / 2 + (y2 - y1) / 2
            newY = (y1 + y2) / 2 - (x2 - x1) / 2
            t.pencolor([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
            inc(x1, y1, newX, newY, level - 1)
            inc(newX, newY, x2, y2, level - 1)

    inc(x1, y1, x2, y2, level)


def heart(n):
    def fibonacci(n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibonacci(n - 2) + fibonacci(n - 1)

    def golden_spiral_rt(n):
        if n > 2:
            t.circle(fibonacci(n), 90)
            golden_spiral_rt(n - 1)

    def golden_spiral_lt(n):
        if n > 2:
            t.circle(-fibonacci(n), 90)
            golden_spiral_lt(n - 1)

    t.pencolor("purple")
    t.pensize(3)
    t.fillcolor('pink')
    t.begin_fill()
    t.pu()
    t.goto(0, -fibonacci(n) * 0.5)
    t.pd()
    golden_spiral_rt(n)
    t.pu()
    t.goto(0, fibonacci(n) + fibonacci(n - 1) - fibonacci(n - 2) - fibonacci(n) * 0.5)
    t.goto(0, -fibonacci(n) * 0.5)
    t.pd()
    t.setheading(180)
    golden_spiral_lt(n)
    t.pu()
    t.goto(0, fibonacci(n) + fibonacci(n - 1) - fibonacci(n - 2) - fibonacci(n) * 0.5)
    t.end_fill()


if __name__ == "__main__":
    # t.speed(0)
    t.tracer(False)  # 默认关闭动画
    t.hideturtle()
    t.colormode(255)
    t.write("点击任意位置随机产生图画\n点击任意位置切换下一张", align="center", font=("Arial", 16))
    t.onscreenclick(main)
    t.done()
