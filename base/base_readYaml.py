import yaml
import os

# 读取yaml文件
class ReadYaml:
    def read_yaml_data(self, file_path):
        file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + r'\config\{}'.format(file_path)
        with open(file_path, 'r', encoding='utf-8')as f:
            # 如果读出来是字符串
            data = f.read()
            # 转换一下
            yaml_data = yaml.load(data, Loader=yaml.Loader)
            return yaml_data


if __name__ == '__main__':
    A = ReadYaml()
    print(A.read_yaml_data('test_usercase.yaml')['test_user']['phone'])