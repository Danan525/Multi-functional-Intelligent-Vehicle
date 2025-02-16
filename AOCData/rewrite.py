import os

# 设置目标文件夹路径
folder_path = 'D:/yolov5/AOCData/labels'
# 设置文件名中应包含的关键词
keyword = 'Kid'
print("test")

# 遍历指定文件夹下的所有文件
for filename in os.listdir(folder_path):
    # 检查文件名是否包含关键词且为.txt文件
    if keyword in filename and filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)  # 构建文件完整路径'
        print(file_path)
        
        try:
            # 尝试读取文件内容
            with open(file_path, 'r') as file:
                lines = file.readlines()  # 读取所有行
            
            if lines:  # 检查文件是否为空
                parts = lines[0].strip().split()  # 分割第一行的内容
                if parts:  # 检查第一行是否为空
                    parts[0] = '1'  # 修改第一个数字为1
                    lines[0] = ' '.join(parts) + '\n'  # 重新组装第一行
                    print(file_path)
                
                # 将修改后的内容写回文件
                with open(file_path, 'w') as file:
                    file.writelines(lines)
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

