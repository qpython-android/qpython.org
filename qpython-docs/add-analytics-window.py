import sys
import os

def process_file(input_file, output_file, extra_file):
    # 确保 extra.txt 文件存在
    if not os.path.exists(extra_file):
        print(f"Error: The file '{extra_file}' does not exist.")
        return

    # 获取 extra.txt 文件内容
    with open(extra_file, 'r', encoding='utf-8') as e:
        extra = e.read().replace("{{PTH}}", input_file[1:])  # 用路径替换 {{PTH}}

    # 逐行读取输入文件并处理内容
    with open(input_file, 'r', encoding='utf-8') as f, open(output_file, 'w', encoding='utf-8') as g:
        for line in f:
            line = line.strip()  # 去除行首和行尾空白字符
            if line:  # 忽略空行
                # 如果是特定标签，添加 extra 和 <hr/> 内容
                if line == '<div role="contentinfo">':
                    g.write(extra + "<hr/>\n")
                else:
                    g.write(line + '\n')  # 写入处理后的行

    # 替换原始文件
    os.rename(output_file, input_file)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        return

    input_file = sys.argv[1]
    output_file = './qpydoc.tmp'
    extra_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'extra.txt')

    # 处理文件
    process_file(input_file, output_file, extra_file)

if __name__ == '__main__':
    main()
