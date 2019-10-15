import os
import shutil
root='D:/Unity/UnityProject/UnityProjectSystematicAnatomy2/Assets/Textures/图谱/书签'
a=os.walk(root)

"""
D:\Unity\UnityProject\Unity Project Systematic Anatomy 2\Assets\Textures\图谱\书签
Ctrl+/注释(取消注释)选择的行
Shift + Enter开始新行
Cmd b ：跳转到变量、方法、类等定义的位置
Cmd +/- ：展开/折叠代码块
Ctrl + Enter智能换行
TAB Shift+TAB缩进/取消缩进所选择的行
Ctrl + Alt + I自动缩进行
Ctrl + Y删除当前插入符所在的行
Ctrl + D 复制当前行、或者选择的块
Ctrl + Shift + J合并行
Ctrl + Shift + V从最近的缓存区里粘贴
Ctrl + Delete删除到字符结尾
Ctrl + Backspace删除到字符的开始
Ctrl + NumPad+/-展开或者收缩代码块
Ctrl + Shift + NumPad+展开所有的代码块
Ctrl + Shift + NumPad-收缩所有的代码块
Alt F7 ：查找该函数在何处被调用——便于察看相关调用
"""

# for x in a:
#     if len(x)==1
#         print()
    # from shutil import copy
    # dest_dir = 'd:\新建文件夹'
    # if not os.path.isdir(dest_dir):
        # os.makedirs(dest_dir)
    # file_path = 'c:\123\1.txt'
    # copy(root, dest_dir)
  # if len(x)>0 :
  #       pre=os.path.basename(x[0])
def fun():
    for root ,dirs,files in a:
      print(root)
      print(dirs)
      print(files)

fun()



