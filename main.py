# -*- coding: UTF-8 -*-
# “你帮我助”物资交换软件v1.0

# 打印每行时通用的格式化
fmt = "{0:{4}<6}\t{1:{4}<6}\t{2:{4}<6}\t{3:<10}"

# 一个辅助函数，可以将整个物品清单对齐打印，更加美观
def Print_List():
    print(fmt.format("物品名称", "物品数量", "联系人姓名", "联系电话", chr(12288)))
    print('-----------------------------------------------')
    with open("goods_data.txt", encoding='utf-8') as data:
        for line in data:
            print(fmt.format(line.split()[0], line.split()[1], line.split()[2], line.split()[3], chr(12288)))


print('欢迎使用“你帮我助”v1.0\n')

help = '使用说明：\n' \
       '输入“Add”--在平台上添加物品信息\n' \
       '输入“Delete”--根据物品名称+联系电话删除物品信息\n' \
       '输入“Print”--打印在列表中的物品信息\n' \
       '输入“Search”--根据物品名称查找物品\n' \
       '输入“Help”--打印帮助\n' \
       '输入“Quit”--结束程序\n'
print(help)

prompt = '\n请输入您希望进行的操作(Quit可终止程序)：'
choice = ''
while choice != 'Quit':
    choice = input(prompt)
    choice = choice.replace(" ", "")
    choice = choice.capitalize()

    if choice == 'Add':
        print('请根据提示输入需要添加的物品信息')
        goods = input('物品名称： ')
        quantity = input('物品数量： ')
        owner = input('联系人姓名： ')
        tele = input('联系电话： ')
        with open("goods_data.txt", mode='a', encoding='utf-8') as data:
            data.write(goods + '\t' + quantity + '\t' + owner + '\t' + tele + '\n')
    elif choice == 'Delete':
        print('请根据提示依次输入要删除的物品名称，持有者联系电话')
        goods = input('物品名称： ')
        tele = input('联系电话： ')
        is_finded = False
        # 将文件逐行读取并存于lines中，以便找到对应信息后将整行删去
        with open("goods_data.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            # print(lines)
        with open("goods_data.txt", "w", encoding="utf-8") as f_w:
            for line in lines:
                if not is_finded and line.split()[0] == goods and line.split()[3] == tele:
                    is_finded = True
                    continue
                f_w.write(line)
            if is_finded:
                print('已删除')
            else:
                print('未找到对应信息，无法删除')
    elif choice == 'Print':
        Print_List()
    elif choice == 'Search':
        is_finded = False
        goods = input('请输入您想要寻找的物品名称： ')
        with open("goods_data.txt", encoding='utf-8') as data:
            for line in data:
                if line.split()[0] == goods:
                    is_finded = True
                    print(fmt.format(line.split()[0], line.split()[1], line.split()[2], line.split()[3], chr(12288)))
            if not is_finded:
                print('未找到对应信息')
    elif choice == 'Help':
        print(help)
    elif choice == 'Quit':
        continue
    else:
        print('您的输入不合规范(输入“Help”获取帮助)，请检查后重新输入，谢谢！')
