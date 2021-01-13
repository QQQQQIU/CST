import sqlite3, passanger_infomation as ps
import datetime as dt
import easygui as g


class Md_db:
    def __init__(self):
        # 创建数据表
        self.createdb_sql = '''
        create table pass_info
        (id integer not null
        primary key autoincrement, 
        status int not null,
        name text not null,
        wechat text not null,
        num int not null,
        p1 text not null,
        p2 text not null,
        t1 int not null,
        t2 int not null);
    '''
        # 删除数据
        self.delete_info_sql = "delete from pass_info where id='{}';".format(id)

    def md_db(sql):
        conn = sqlite3.connect('passanger_infomation.db')
        c = conn.cursor()
        c.execute(sql)
        conn.commit()
        conn.close()

    # 插入数据
    def writedb(user):
        t11 = int(dt.datetime.timestamp(dt.datetime.strptime(user.t1, '%Y-%m-%d %H:%M')))
        t22 = int(dt.datetime.timestamp(dt.datetime.strptime(user.t2, '%Y-%m-%d %H:%M')))
        sql = '''
            insert into pass_info (status,name, wechat, num, p1,p2,t1,t2) 
            values ('{}','{}','{}','{}','{}','{}','{}','{}')
            '''.format(user.status, user.name, user.wechat, user.num, user.p1, user.p2, t11, t22)
        Md_db.md_db(sql)

    # 修改数据
    def md_status(id):
        sql = "update pass_info set status=0 where id='{}';".format(id)
        Md_db.md_db(sql)


# 查询数据
def sear_info(sql):
    conn = sqlite3.connect('passanger_infomation.db')
    c = conn.cursor()
    try:
        c.execute(sql)
        results = c.fetchall()
    except:
        results = []
    conn.close()
    return results


def match(user):
    p1, p2 = user.p1, user.p2
    sql_trip = '''
    select id,num,t1,t2 from pass_info where status=1 and p1='%s' and p2='%s' order by id asc 
    ''' % (p1, p2)
    results = sear_info(sql_trip)
    # print('路线相同所有匹配对象有：', results)

    t1 = results[-1][2]
    t2 = results[-1][3]
    # print('user_time:',t1,t2)
    user_time = set([i for i in range(t1, t2 + 1)])
    user_seats = user.num
    user_id = results[-1][0]

    trip_ids = []
    trip_time = set()

    if len(results) == 1:  # 除自己外没有别人拼车
        # print('len(results) == 1 除自己外没有别人拼车此路线')
        msg = '此路线暂无拼友，请您稍等。'
        g.msgbox(msg, '软微拼车')
    else:  # 数据库有同样路线的乘客，但需要匹配时间是否有重合
        trip_ids.append(user_id)
        trip_seats = user_seats
        trip_time = user_time
        # print('trip_time = user_time',inter_time(trip_time)[0],inter_time(trip_time)[1])
        results.pop()  # 把自己加入信息后删除
        # print('将自己加入trip 遍历其余匹配的人', trip_seats, trip_ids, results)
        # 此时trip里已经有自己的信息了，results里面没有自己，全是路线吻合的对象

        for item in results:
            item_time = [i for i in range(item[2], item[3] + 1)]
            # print('item_time',item[2], item[3] )
            item_id = item[0]
            item_seats = item[1]

            if trip_time.intersection(item_time):  # 时间重合
                if (trip_seats + item_seats) == 4:  # 座位刚好
                    trip_seats = trip_seats + item_seats
                    trip_time = trip_time.intersection(item_time)
                    # print('trip_time_final',inter_time(trip_time)[0],inter_time(trip_time)[1])
                    trip_ids.append(item_id)
                    for n in trip_ids:
                        Md_db.md_status(n)
                    # print('拼车成功')
                    break
                elif (trip_seats + item_seats) < 4:  # 座位充裕
                    trip_seats = trip_seats + item_seats
                    trip_time = trip_time.intersection(item_time)
                    trip_ids.append(item_id)
                    # print('座位未满')

        if user_seats < trip_seats < 4:
            msg = '加上您的预订，拼座数未满4个，现有%d个，继续等待或立即出发？' % trip_seats
            x = g.buttonbox(msg, '软微拼车', ['继续等待', '立即出发'])
            if x == '立即出发':
                # ！每个ID应当发送询问请求
                for n in trip_ids:
                    Md_db.md_status(n)
                # print('未满4人，立即出发')
            else:
                trip_ids = []
                # print('未满4人，继续等待')
        elif user_seats==trip_seats:
            # print('有同路线 但是没有座位和时间合适的')
            msg = '此路线暂无合适拼友，请您稍等。'
            g.msgbox(msg, '软微拼车')
            trip_ids = []
    return [trip_ids, trip_time, p1, p2]


# 将时间集合转化为列表，在将最早和最晚时间提取出来，组装到只有两个元素的列表
def inter_time(s):
    l = list(s)
    t1 = (dt.datetime.fromtimestamp(l[0])).strftime('%Y-%m-%d %H:%M')
    t2 = (dt.datetime.fromtimestamp(l[- 1])).strftime('%Y-%m-%d %H:%M')
    return [t1, t2]


def check_trip(output):
    # print('match结果为：（trip_ids, trip_time, p1, p2）', output)
    if output[0]:
        # print('trip_ids不为空，拼车成功')
        trip_ids = output[0]
        trip_time = output[1]
        l = inter_time(trip_time)  # 将时间集合进行转化
        t1, t2 = l[0], l[1]  # 得到起末时间
        p1, p2 = output[2], output[3]

        # 在数据库中根据id查询拼车用户信息
        s = ''
        for id in trip_ids:
            sql = "select name,wechat,num from pass_info where id='%d'" % id
            info = sear_info(sql)[0]
            s += '\n姓名：' + info[0] + '；微信：' + info[1] + '；拼座数：' + str(info[2])
        ss = s.replace('\n', '', 1)
        msg = "此次行程由 %s 前往 %s。\n\n出发时间为 %s 至 %s。\n\n乘客信息如下：\n\n%s\n\n祝您旅途愉快！" % (p1, p2, t1, t2, ss)
        g.msgbox(msg, '软微拼车')


if __name__ == "__main__":
    a = ps.Passanger()
    Md_db.writedb(a)
    output = match(a)
    check_trip(output)

    # 清空表格
    # sql = "delete from pass_info ;"
    # Md_db.md_db(sql)
