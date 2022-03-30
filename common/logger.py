import logging
import os
import time



class Log():
    # 创建logger对象, 定义一个日志收集器
    logger = logging.getLogger()
    # 设置logger对象的日志级别
    logger.setLevel(logging.WARNING)
    # 获取脚本的上级路径
    file_path =os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # 创建一个存放log日志的文件
    log_path =file_path + r'\logs' + r'\{}.txt'.format(time.strftime('%Y_%m_%d__%H时%M分%S秒'))
    # 设置处理器，将日志输出到文件内
    file_headler = logging.FileHandler(filename=log_path,mode="w")
    # 处理日志 设置日志级别
    file_headler.setLevel(logging.WARNING)
    # 设置日志格式
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # 将日志格式添加到处理器中
    file_headler.setFormatter(formatter)
    # 添加处理器到logger对象中
    logger.addHandler(file_headler)

    def warning(self,msg):
        self.logger.warning(msg)

    def error(self,msg):
        self.logger.error(msg)

    def citical(self,msg):
        self.logger.critical(msg)

if __name__ == 'main':
    print(Log().file_path)
