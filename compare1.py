# -*- coding: utf-8 -*-
file1 = "D:\\1.txt"
file2 = "D:\\2.txt"
f_diff = "D:\\diff.txt"

# ---------- 对比文件内容，输出差异
f1 = open(file1, "r")
f2 = open(file2, "r")
file1 = f1.readlines()
file2 = f2.readlines()
f1.close()
f2.close()
outfile = open(f_diff, "w")
flag = 0
outfile.write("file1独有的数据：\n")
for i in file1:
    if i not in file2:
        outfile.write(i)
        flag = 1
        outfile.write("\nfile2独有的数据：\n")
for i in file2:
    if i not in file1:
        outfile.write(i)
        flag = 1
outfile.close()
if flag == 1:
    print "数据存在差异，请仔细核对！"
else:
    print "数据一致"