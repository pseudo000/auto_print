import os

dir_path = 'G:\\共有ドライブ\\LSE 共有フォルダ\\海上輸入トライアル\\3次　20230324\\ETA0324検査指定票'

for filename in os.listdir(dir_path):
    new_filename = filename[:11]
    os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename + ".PDF"))
