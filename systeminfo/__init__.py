# coding=utf-8
"""

"""

__author__  = 'Shine tong<linuxtong@gmail.com>'
__version__  = "0.1.0"
__date__     = "2013-04-08"
__all__      = ['cpu','physicalMem','buffersMem','swapMem','partition','uptime',
                'process','netCard','iostat','total']

from systeminfo import top,free,net,df,io
from ipaddress import ipaddress

def cpu():
    return top.processStatus()

def physicalMem():
    return free.physicalMem()

def buffersMem():
    return free.bufferslMem()

def swapMem():
    return free.swapMem()

def partition():
    return df.detail()

def uptime():
    return top.uptime()

def process():
    return top.processStatus()

def netCard():
    return net.detail()

def iostat():
    return io.detail()

def maxInetipadd():
    result = []
    cardInfo = net.detail()
    for card in cardInfo.keys():
        netInfo = cardInfo[card]
        ip = netInfo['ip']
        if ip is not None:
            result.append(ip)
    if result:
        return  ipaddress.maxInetip(result)
    else:
        return None

def total():
    """
    """
    project = ['cpu','physicalMem','buffersMem','swapMem','partition','uptime',
               'process','netCard','io']
    info = [cpu(),physicalMem(),buffersMem(),swapMem(),partition(),uptime(),process(),netCard(),iostat()]
    totalInfo = dict(zip(project,info))
    return totalInfo