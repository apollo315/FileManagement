# 需求：wallpaper图片文件过多，需要简单整理；
# 功能：每50个图片文件，放在一个文件夹下，动态新增文件夹；
# 日期：2018-09-21
# 版本：v2.0

# 思路：动态移动和创建文件夹
# 1、只要当前目录下还有文件要处理，就一直循环；
# 2、文件夹从1开始计数，若满了就创建新文件夹；
# 3、移动文件到相应文件夹下
import shutil
from tools_file import *

dir = r'E:\WallPaper'
FOLDER_CAPACITY = 50  # 文件夹容量
complete = False
folder_name = 0
while not complete:
    if get_file_count(dir) == 0:  # 文件已全部处理完毕；
        complete = True
    else:
        folder_name = folder_name + 1
        folder_path = os.path.join(dir, str(folder_name))
        # 2、生成文件夹
        my_mkdir(folder_path)
        # 3、移动文件到文件夹
        for file in get_file_list(dir):
            file_path_old = os.path.join(dir, file)
            if get_file_count(folder_path) < FOLDER_CAPACITY:  # 文件夹未满
                shutil.move(file_path_old, folder_path)  # 文件移动到文件夹
                print('文件', file, '已移动至', folder_path)
            else:
                print('文件夹', folder_path, '已满！')
                break  # 跳出for循环，继续while循环，切换容器文件夹
