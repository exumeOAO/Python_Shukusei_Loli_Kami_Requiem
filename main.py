import os
import subprocess
import time

# 文件夹路径
folder_path = 'C:\\Users\\ASUS\\Desktop\\Python_Shukusei_Loli_Kami_Requiem\\alltxt'

# 获取文件夹下的所有txt文件
txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

# 遍历txt文件
for txt_file in txt_files:
    # 清屏
    subprocess.call('cls', shell=True)

    # 输出txt文件内容
    with open(os.path.join(folder_path, txt_file), 'r') as f:
        content = f.readlines()
        for line in content:
            print(line, end = '\n')

    # 等待0.02秒
    time.sleep(0.02)
