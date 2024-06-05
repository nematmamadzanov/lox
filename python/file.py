file1 = open('text1.txt', 'r')
content1 = file1.read()
file1.close()

file2 = open('text2.txt', 'r')
content2 = file2.read()
file2.close()

content3 = content1 + "\n" + content2

file3 = open('text3.txt', 'r')
file3.write(content3)
file3.close()