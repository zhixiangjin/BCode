'''
动物牛牛是一个聪明的动物，它现在面临一个字符串解码的问题。给定一个经过编码的字符串，牛牛需要将其解码成原始的字符串。

编码规则为：k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

请你编写一个函数decodeString，接收一个字符串s作为参数，返回解码后的字符串
'''
def decodeString(s: str) -> str:
    stack = []  # 用于存储字符串和数字
    current_num = 0  # 当前的数字，用于确定方括号内字符串的重复次数
    current_str = ""  # 当前的字符串部分
    
    for char in s:
        if char.isdigit():
            # 构建数字，可能是多位数
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # 遇到 '['，把当前的数字和字符串压入栈中
            stack.append((current_str, current_num))
            current_str = ""  # 重置当前字符串
            current_num = 0  # 重置当前数字
        elif char == ']':
            # 遇到 ']'，出栈，进行字符串解码
            last_str, repeat_num = stack.pop()
            current_str = last_str + current_str * repeat_num
        else:
            # 当前字符是普通字符，追加到当前字符串部分
            current_str += char
    
    return current_str

if __name__ == '__main__':
    s = "3[a2[c]]"
    result = decodeString(s)
    print(result)
# 示例
# print(decodeString("3[a]2[bc]"))  # 输出 "aaabcbc"
# print(decodeString("3[a2[c]]"))  # 输出 "accaccacc"
# print(decodeString("2[abc]3[cd]ef"))  # 输出 "abcabccdcdcdef"
