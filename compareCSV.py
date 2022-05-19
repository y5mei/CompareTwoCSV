
# Current Solution
with open("input1.csv") as t1, open("input2.csv") as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open("current_result.csv", "w") as outFile:
    for line in filetwo:
        if line not in fileone: # 这行让你速度变慢的，这个 implementation 不好
            outFile.write(line)

# 这个写法有问题哈， 如果你 input1.csv 中是 1\n 2\n 3\n, input2.csv 中是 3\n 2\n 1\n;
# 注 \n 是换行符的意思
# 你想要一个什么样的 output.csv? 你目前的写法返回的是 empty file， 因为 input1 中的每一行 input2 中都有，只是顺序不同
# 这个是你想要的结果吗？【顺序是否有关？重复的行怎么处理？】


# 假设没有重复的行，顺序有关的话
# 例如： input1.csv 中是 1\n 2\n 3\n, input2.csv 中是 3\n 2\n 1\n;
# 期待返回 1\n 3\n 的话，可以这么写：

with open("proposed_result.csv", "w") as outFile:
    for lineNum in range(len(fileone)):
        if fileone[lineNum] != filetwo[lineNum]:
            outFile.write(fileone[lineNum])

# 这样就把你 O(N^2) 的解法变成 O(N) 线性时间复杂度了，
# 能做的优化还有一些，比如如果文件很大的话（几百兆），不要直接读到内存，读成 buffer，stream 这种，主体留在硬盘上，用多少往内存 stream 多少
# Ref: https://stackoverflow.com/questions/6556078/how-to-read-a-csv-file-from-a-stream-and-process-each-line-as-it-is-written


# 如果顺序无关的话，考虑把 fileone 和 filetwo 变成 hashset，这样可以保证时间复杂度还是 O(N) 的