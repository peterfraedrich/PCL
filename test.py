#!/usr/bin/env python3

import pcl

if __name__ == '__main__':
    print('Starting test!')
    p = pcl.Load('test.pcl')
    print(type(p))
