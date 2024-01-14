import os

def organize_music():
    # 获取当前工作目录
    folder_path = os.getcwd()

    # 获取文件夹内所有文件
    files = os.listdir(folder_path)

    # 创建一个字典来存储歌手及其对应的歌曲列表
    artist_songs = {}

    for file in files:
        # 拼接文件的完整路径
        file_path = os.path.join(folder_path, file)

        # 检查是否为文件
        if os.path.isfile(file_path):
            # 获取文件名和后缀
            file_name, file_extension = os.path.splitext(file)

            # 使用 "-" 分割文件名，只考虑第一部分
            parts = file_name.split('-', 1)

            # 获取歌手名部分
            artist_name = parts[-1].strip()

            # 在字典中添加歌手及其歌曲
            if artist_name in artist_songs:
                artist_songs[artist_name].append(file)
            else:
                artist_songs[artist_name] = [file]

            # 获取或创建对应的歌手文件夹
            artist_folder = os.path.join(folder_path, artist_name)
            os.makedirs(artist_folder, exist_ok=True)

            # 移动文件到对应的歌手文件夹
            os.rename(file_path, os.path.join(artist_folder, file))

    # 打印整理后的歌手及其歌曲信息
    for artist, songs in artist_songs.items():
        print(f'{artist}: {songs}')

# 执行整理音乐的函数
organize_music()
