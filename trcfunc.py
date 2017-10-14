#!/usr/bin/env python
#coding:utf-8
"""
created on 24.08.2017
author:Leon Lee
User-Agent:{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0'}
"""
import time,datetime
import os
class tracer:
    def __init__(self,func):
        self.call=0
        self.func=func
    def __call__(self, *args, **kwargs):
        self.call += 1
        now_before=datetime.datetime.now()
        now_str=now_before.strftime('%Y-%m-%d %H:%M:%S ')
        second_before=now_before.second
        self.func(*args,**kwargs)
        now_after = datetime.datetime.now()
        second_after=now_after.second
        second_tot=second_after-second_before+(int(now_after.strftime('%f'))-int(now_before.strftime('%f')))/1000000
        second_tot+=(now_after.minute-now_before.minute)*60
        call_log='{}:function"{}" is called {} times which takes {} seconds.'.format(now_str,self.func.__name__,self.call,second_tot)
        with open('{}_log.txt'.format(self.func.__name__),'a') as file:
            file.write(call_log+'\n')
            file.close()
    def logclean(self):
        func=self.func
        try:
            os.remove('{}_log.txt'.format(self.func.__name__))
        except FileNotFoundError:
            print('{} hasn\'t got a log file.'.format(func.__name__))
if __name__ == '__main__':
    pass


