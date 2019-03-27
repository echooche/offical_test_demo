import time

class LogInfo:
    def __init__(self,path = '',mode = 'w'):
        fname = path+time.strftime('%Y-%m-%d-%H-%M-%S',time.gmtime())+'.txt'
        self.log = open(fname,mode)

    def log_write(self,msg):
        self.log.write(msg)

    def log_close(self):
        self.log.close()


if __name__ == '__main__':
    log = LogInfo()
    log.log_write("测试")
    log.log_close()
