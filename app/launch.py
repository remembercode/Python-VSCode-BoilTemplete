import sys
import os

# add app to lib path for import
# 增加app目录到搜索路径中，方便后续的项目import自己写的py文件lib
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

def main():
    print(sys.version_info)
    print("main start !")

if __name__ == "__main__":
    main()
