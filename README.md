# FileManagement
为满足个人日常文件管理需求而诞生的实用小工具库，非常简单
## 一、基本用法
### 1、前提
已安装python，可直接在cmd下使用
### 2、执行方法
简单修改代码设置参数后，直接在cmd下执行.py文件即可，如`python FileMgt_move_file_into_folder.py`，可根据需要选择要执行的文件
## 二、工程简介
### 1、FileMgt_move_file_into_folder.py
#### 需求背景
wallpaper图片文件过多，需要简单整理
#### 参数设置：
##### ①指定要整理的文件夹路径
修改文件`FileMgt_move_file_into_folder.py`中的`dir = r'E:\WallPaper'`
##### ②设置文件夹容量
修改文件`FileMgt_move_file_into_folder.py`中的`FOLDER_CAPACITY = 50`，该参数指定每个文件夹下文件个数上限
#### 整理前：
![截图](https://github.com/apollo315/FileManagement/blob/master/img/FileMgt_move_file_into_folder/before.png)
#### 整理后：
![截图](https://github.com/apollo315/FileManagement/blob/master/img/FileMgt_move_file_into_folder/after.png)
