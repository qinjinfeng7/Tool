#! /usr/bin/env python
import sys
from utils import get_device_state,screencap
from time import localtime,strftime

'''
截图文件名可以通过运行py的时候带参数修改，默认为当前时间戳
如：python *.py sceen1
'''
def main():
    get_device_state()
    if len(sys.argv)==2:
        screencap(sys.argv[1])
    else:
        file_name = strftime('%Y%m%d%H%M%S',localtime())
        screencap(file_name)

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)
