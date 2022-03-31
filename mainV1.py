# check V1.0
import os
import xlrd

os_path = os.getcwd()

def get_classes(path = os_path + "/file"):
    classes = dict()
    j = 0
    for i in os.listdir(path):
        classes[j] = i
        j += 1
    return classes


def show(chosed_class, username):
    classes = get_classes()

    path1 = os_path + "/file/" + classes[int(chosed_class)]
    xl1 = xlrd.open_workbook(path1)
    sheet_name = xl1.sheet_names()[0]
    data_all = xl1.sheet_by_name(sheet_name)
    set_all = set(data_all.col_values(0))

    path2 = os_path + "/upload/" + username + ".xlsx"
    xl2 = xlrd.open_workbook(path2)
    sheet_name2 = xl2.sheet_names()[0]
    data1 = xl2.sheet_by_name(sheet_name2)
    set_set1 = set(data1.col_values(0))
    
    t = classes[int(chosed_class)]
    class_name = t.split('.')[0]
# 主要利用集合操作 并差交补|-&^
#
#     print(f"未完成：{set_all - set_set1}")  # 未完成的
#
# # print(d_set_all ^ d_set1)  # 未完成的和非本班的
#     print(f"非本班：{(set_all ^ set_set1) - (set_all - set_set1)}")

    return f"{class_name}---未完成：{set_all - set_set1}" #  + '<p>' + f"非本班：{(set_all ^ set_set1) - (set_all - set_set1)}"
