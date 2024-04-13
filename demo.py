import tkinter as tk
import itertools

def generate_combinations():
    # 清空文本框
    combinations_text.delete(1.0, tk.END)
    
    # 获取用户输入的信息
    user_input = entry_info.get()
    info = user_input.split(',')
    
    # 获取用户输入的位数，如果为空，则为0
    length_str = entry_length.get()
    if length_str:
        length = int(length_str)
    else:
        length = 0
    
    # 生成排列组合
    all_combinations = get_all_combinations(info, length)
        
    # 显示所有排列组合
    for combination in all_combinations:
        combination_str = ''.join(combination)
        combinations_text.insert(tk.END, combination_str + "\n")

def get_all_combinations(info, length):
    # 如果位数为0，则生成所有可能的排列组合
    if length == 0:
        all_combinations = []
        for r in range(1, len(info) + 1):
                all_combinations.extend(list(itertools.permutations(info, r)))
    else:
        all_combinations = list(itertools.permutations(info, length))
    return all_combinations

def clear_text():
    # 清空文本框
    combinations_text.delete(1.0, tk.END)

# 创建主窗口
root = tk.Tk()
root.title("密码字典生成器 by L1Ha0")

# 输入信息的标签和输入框
label_info = tk.Label(root, text="请输入信息（用逗号分隔）:")
label_info.pack(pady=5)
entry_info = tk.Entry(root, width=50)
entry_info.pack(pady=5)

# 输入位数的标签和输入框
label_length = tk.Label(root, text="请输入要输出的元素位数（留空则输出所有排列组合）：")
label_length.pack(pady=5)
entry_length = tk.Entry(root, width=5)
entry_length.pack(pady=5)

# 生成排列组合按钮
generate_button = tk.Button(root, text="生成排列组合", command=generate_combinations)
generate_button.pack(pady=5)

# 结果文本框
combinations_text = tk.Text(root, height=10, width=50)
combinations_text.pack()

# 清空按钮
clear_button = tk.Button(root, text="清空文本框", command=clear_text)
clear_button.pack(pady=5)

# 运行主循环
root.mainloop()
