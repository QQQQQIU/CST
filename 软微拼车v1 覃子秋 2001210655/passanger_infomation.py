# 自定义地点需要计算路程相似度，所以此处限定新宫、高米店南、校本部、大兴校区四个目的地
# 每人有确切的目的地 不能多选

import easygui as g
import datetime as dt


class Passanger:
    def __init__(self):
        title = '软微拼车'
        while 1:
            self.status = 1
            n = Passanger.pass_info(title)
            self.name = n[0]
            self.wechat = n[1]
            self.num = Passanger.number(title)
            m = Passanger.place(title)
            self.p1 = m[0]
            self.p2 = m[1]
            time = Passanger.time_period(title)
            self.t1 = time[0]
            self.t2 = time[1]
            info = ['姓名：%s' % self.name, '微信：%s' % self.wechat, '拼座数：%d' % self.num, '起点：%s' % self.p1,
                    '终点：%s' % self.p2, '最早出发时间：%s' % self.t1, '最晚出发时间：%s' % self.t2]
            if not Passanger.check_info(title, info):
                break

    def pass_info(title):
        msg = '您好，欢迎使用软微拼车。'
        info = g.multenterbox(msg, title, ['用户名', '微信'])
        return info

    def number(title):
        msg = '请问您需要几个拼座？'
        num = g.buttonbox(msg=msg, title=title, choices=['1', '2', '3'])
        return int(num)

    def place(title):
        msg = '请问您出村，还是回村？'
        direction = g.buttonbox(msg=msg, title=title, choices=['出村', '回村'])
        dests = ['新宫', '高米店南', '校本部']
        if direction == '出村':
            p1 = '大兴校区'
            msg2 = '请问您想去哪？'
            p2 = g.buttonbox(msg=msg2, title=title, choices=dests)
        else:
            p2 = '大兴校区'
            msg3 = '请问您计划在哪上车？'
            p1 = g.buttonbox(msg=msg3, title=title, choices=dests)
        return [p1, p2]

    def time_period(title):
        msg = '请问您准备何时出发？'
        a = g.buttonbox(msg, title, ['10分钟以内', '预约拼车'])
        if a == '10分钟以内':
            t1 = dt.datetime.now()
            t2 = t1 + dt.timedelta(minutes=10)
        else:
            msg2 = '请输入出发时间\n时间格式为“年-月-日-时-分”，如“2020-12-13-15-23”'
            b = g.multenterbox(msg2, title, ['最早出发时间', '最晚出发时间'])
            t1 = [int(i) for i in b[0].split('-')]
            t1 = dt.datetime(t1[0], t1[1], t1[2], t1[3], t1[4])
            t2 = [int(i) for i in b[1].split('-')]
            t2 = dt.datetime(t2[0], t2[1], t2[2], t2[3], t2[4])
        time = [t1.strftime('%Y-%m-%d %H:%M'), t2.strftime('%Y-%m-%d %H:%M')]
        return time

    def check_info(title, info):
        msg = '您好,请确认以下信息：\n\n选择有误信息重新填写，无误清空选择后确认'
        a = g.multchoicebox(msg, title, info)
        return a


if __name__ == '__main__':
    a = Passanger()
    print('''
    姓名：%s
    微信：%s
    拼座数：%d
    起点：%s'
    终点：%s
    最早出发时间：%s
    最晚出发时间：%s'''% (a.name, a.wechat,a.num,a.p1,a.p2,a.t1, a.t2) )
