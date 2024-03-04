import os
import random
import string

# 生成随机汉字
def generate_random_chinese(length):
    chinese_chars = ''.join(random.sample('你好，世界！这是一行随机汉字。', length))
    return chinese_chars

# 创建文件夹和文本文件
def create_folders_and_text_files(num_folders, num_lines):
    for i in range(num_folders):
        folder_name = generate_random_chinese(5)  # 生成5个随机汉字作为文件夹名称
        os.makedirs(folder_name)

        file_content = ''
        for j in range(num_lines):
            chinese_chars = generate_random_chinese(10)  # 生成10个随机汉字
            file_content += chinese_chars + '\n'

        file_name = generate_random_chinese(5) + '.txt'  # 生成5个随机汉字作为文本文件名称
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(file_content)

# 设置要创建的文件夹和文本文件的数量
num_folders = 30
num_lines = 30

# 调用函数创建文件夹和文本文件
create_folders_and_text_files(num_folders, num_lines)
