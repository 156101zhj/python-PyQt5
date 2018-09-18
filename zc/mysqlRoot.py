# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pymysql


def creatConnect():
    conn = pymysql.connect(host="localhost", user="root",
                           password="123456", db="RootDB", port=3306, charset="utf8")
    cur = conn.cursor()
    return (conn, cur)


def close(conn, cur):
    cur.close()
    conn.close()


def main():
    try:
        conn, cur = creatConnect()
        create_users(conn)
        create_friends(conn)
        create_history(conn)
        conn.commit()
    except:
        conn = pymysql.connect(host="localhost", user="root",
                               password="123456", port=3306, charset="utf8")
        cur = conn.cursor()
        cur.execute('create database RootDB default character set utf8;')
        conn.commit()
        create_users(conn)
        create_friends(conn)
        create_history(conn)
        conn.commit()
    close(conn, cur)


def create_users(conn):
    s = 'create table users(\
    id int auto_increment primary key,\
    rootname int,\
    nickname varchar(20),\
    pwd varchar(32),\
    gender enum("男","女","保密"),\
    tel varchar(11),\
    address varchar(100),\
    email varchar(30),\
    birthday varchar(15),\
    avatar text,\
    style varchar(100),\
    onlinestatus enum("在线","离线"),\
    time timestamp default now(),\
    last_online timestamp default now())character set utf8;'
    cur = conn.cursor()
    try:
        cur.execute(s)
        conn.commit()
        print('users ok')
    except:
        print("create_users FILL")
        conn.rollback()


def insert_users(rootname, nickname, pwd, gender, tel, address, email, birthday, avatar, style, onlinestatus):
    conn, cur = creatConnect()
    s = '''insert into users
        (rootname, nickname, pwd, gender, tel, address, email, birthday, avatar, style, onlinestatus)
        values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")''' % (rootname, nickname, pwd, gender, tel, address, email, birthday, avatar, style, onlinestatus)
    try:
        cur.execute(s)
        conn.commit()
        print("insert_users is ok")
    except:
        print("insert_users FILL")
        conn.rollback()
    close(conn, cur)


def updatestatus_users(rootname, status):
    conn, cur = creatConnect()
    s = "update users set onlinestatus='%s', last_online=now() where rootname='%s'" % (
        status, rootname)
    try:
        cur.execute(s)
        conn.commit()
        print("update_users is ok")
    except:
        print("updatestatus_users FILL")
        conn.rollback()
    close(conn, cur)


def login(rootname, pwd):
    conn, cur = creatConnect()
    s = "select rootname,nickname,gender,tel,address,email,birthday,avatar,style,onlinestatus,last_online from users where rootname='%s' and pwd='%s'" % (
        rootname, pwd)
    cur.execute(s)
    data = cur.fetchone()
    close(conn, cur)
    return data


def select_users(rootname):
    conn, cur = creatConnect()
    s = "select rootname,nickname,gender,tel,address,email,birthday,avatar,style,onlinestatus from users where rootname='%s'" % rootname
    cur.execute(s)
    data = cur.fetchone()
    close(conn, cur)
    return data


def create_friends(conn):
    s = '''create table friends(
        id int auto_increment primary key,
        rootname int not null,
        f_rootname int not null)character set utf8;'''
    cur = conn.cursor()
    try:
        cur.execute(s)
        conn.commit()
        print('create_friends is ok')
    except:
        print("create_friends FILL")
        conn.rollback()


def insert_friends(rootname, f_rootname):
    conn, cur = creatConnect()
    s = 'insert into friends(rootname,f_rootname) values("%s","%s")' % (
        rootname, f_rootname)
    try:
        cur.execute(s)
        conn.commit()
        print("insert_friends is ok")
    except Exception as e:
        print(e)
        conn.rollback()
    close(conn, cur)


def select_friends(rootname):
    conn, cur = creatConnect()
    s = "select users.nickname, friends.f_rootname, users.avatar from friends,users where friends.rootname='%s' and users.rootname=friends.f_rootname;" % rootname
    cur.execute(s)
    data = cur.fetchall()
    close(conn, cur)
    return data


def create_history(conn):
    s = '''create table history(
    id int auto_increment primary key,
    rootname int not null,
    f_rootname int not null,
    record text,
    time timestamp default now())character set utf8;'''
    cur = conn.cursor()
    try:
        cur.execute(s)
        conn.commit()
        print('create_history ok')
    except:
        print("create_history FILL")
        conn.rollback()


def insert_history(rootname, f_rootname, record):
    conn, cur = creatConnect()
    print("history:", rootname, f_rootname)
    s = "insert into history(rootname, f_rootname, record) values('%s', '%s', '%s')" % (
        rootname, f_rootname, record)
    try:
        cur.execute(s)
        conn.commit()
        print("insert_hist is ok")
    except:
        print("insert_history FILL")
        conn.rollback()
    close(conn, cur)


def select_history(rootname, f_rootname):
    conn, cur = creatConnect()
    s = "select record from history where ((rootname = '%s')and(f_rootname = '%s')) or (( f_rootname = '%s')and(rootname = '%s'))" % (
        rootname, f_rootname, f_rootname, rootname)
    cur.execute(s)
    data = cur.fetchall()
    close(conn, cur)
    return data


def selectfive_history(rootname, f_rootname):
    conn, cur = creatConnect()
    s = "select record from history where (rootname = '%s' and f_rootname = '%s') or (rootname = '%s' and f_rootname = '%s') order by id desc limit 5;" % (
        rootname, f_rootname, f_rootname, rootname)
    cur.execute(s)
    data = cur.fetchall()
    close(conn, cur)
    return data


def selectlast_online_history(last_online, rootname):
    conn, cur = creatConnect()
    print("mySQL>", last_online)
    s = "select record from history where time > ('%s') and f_rootname = '%s' order by rootname;" % (
        last_online, rootname)
    cur.execute(s)
    data = cur.fetchall()
    close(conn, cur)
    return data

main()
