import sys
import os
import app

# 将tts模块的父目录添加到sys.path中
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_dir)

app.main()