#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio

@asyncio.coroutine
def work(tag):
    print('work: (%s)' % threading.currentThread())
    for i in range(5):
        print(tag)
        print(i)

@asyncio.coroutine
def hello1():
    print('Hello world1! (%s)' % threading.currentThread())
    yield from work('111')
    print('Hello again1! (%s)' % threading.currentThread())


@asyncio.coroutine
def hello2():
    print('Hello world2! (%s)' % threading.currentThread())
    yield from work('222')
    print('Hello again2! (%s)' % threading.currentThread())



@asyncio.coroutine
def hello3():
    print('Hello world3! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again3! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello2(), hello1(), hello3()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


# Hello world3! (<_MainThread(MainThread, started 140736720917440)>)
# Hello world2! (<_MainThread(MainThread, started 140736720917440)>)
# work: (<_MainThread(MainThread, started 140736720917440)>)
# 222
# 0
# 222
# 1
# 222
# 2
# 222
# 3
# 222
# 4
# Hello again2! (<_MainThread(MainThread, started 140736720917440)>)
# Hello world1! (<_MainThread(MainThread, started 140736720917440)>)
# work: (<_MainThread(MainThread, started 140736720917440)>)
# 111
# 0
# 111
# 1
# 111
# 2
# 111
# 3
# 111
# 4
# Hello again1! (<_MainThread(MainThread, started 140736720917440)>)
# Hello again3! (<_MainThread(MainThread, started 140736720917440)>)
