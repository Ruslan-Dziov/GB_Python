"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""
with open('hw_2.txt', 'r') as f:
    lines = 0
    result = {}
    for line in f:
        lines += 1
        line = line.split()
        length = len(line)
        result.update({lines: length})
print(result)
