from runapp.models import Proxy_List

def loadlistbypath():
    f = open("/home/max/Рабочий стол/ForProjects/myvirtual/workproject/testproject/list_proxy.txt")
    for line in f.readlines():
        butline = filter_non_printable(line)
        alllist = Proxy_List.objects.all()
        lastnum = len(alllist) + 1
        newproxy = Proxy_List(num = lastnum, proxy_host = butline)
        newproxy.save()
        print(butline)


def filter_non_printable(str):
  return ''.join([c for c in str if ord(c) > 31 or ord(c) == 9])