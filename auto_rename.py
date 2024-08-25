import os
from datetime import datetime

# 设置文件夹路径（请根据需要修改）
folder_path = r'C:\Users\40666\Desktop\222'

# 获取当前日期
current_date = datetime.now().strftime('%Y%m%d')

# 切换到目标文件夹
os.chdir(folder_path)

# 获取文件夹中的所有文件
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 按文件名排序（可选，根据实际需要）
files.sort()

# 重新命名文件
for index, file_name in enumerate(files, start=1):
    # 获取文件扩展名
    file_extension = os.path.splitext(file_name)[1]
    # 构造新的文件名
    new_name = f"{current_date}{index:02d}{file_extension}"
    # 重命名文件
    os.rename(file_name, new_name)

print("文件重命名完成")
