test = []
test.append('Что выведет в консоль эта программа:\n')
test.append(
    'list = [77, 5.0, \'33\', 2]\nnew_list = []\nfor value in list:\n\tif str(value).isdigit():\n\t\tnew_list.append('
    'value)\nprint(new_list[1])')  # 1
test.append('d = {\'a\': 50, \'b\': 150, \'c\': 20}\nprint(f"{d[\'a\'] + d[\'b\']}" + str(d[\'c\']))')  # 2
test.append('a = 15\nc = 7.7\nx = \'3.3\'\nresult = a + int(float(x)) + int(c)\nprint(result)')  # 3
test.append('a = 50\nb = 100\nprint(a + a + float(b))')  # 4
test.append('x = \'x3\'\ny = \'С\'\nprint((y + x)*2)')  # 5
test.append(
    'list = [2, 5, 4, 7]\nmax = list[0]\nfor i in range(len(list) - 1):\n\tif list[i] > max:\n\t\tmax = list['
    'i]\nprint(max)')  # 6
test.append('s = "Contex 3"\nprint(s[0] + s[5] + s[7])')  # 7
test.append('s = "s = "ur4"\ns += \'C\'\nprint(s[-1] + s[1]\n+ s[-4] + s[2])')  # 8
test.append('y = 2**2 - 4\nif y == True:\n\tprint(\'Hallo\')\nelse:\n\tprint(\'Hi\')')  # 9
test.append('y = 2**3 - 7\nx = True\nif y == x:\n\tprint(\'Hallo\')\nelse:\n\tprint(\'Hi\')')  # 10
test.append('list1 = [\'hi\', \'welcome\']\nlist2 = list1\nlist2.append(\'bro\')\nprint(list1[-1])')  # 11
test.append('list1 = [\'hi\', \'bro\']\nlist2 = list1\nlist2.append(\'welcome\')\nprint(len(list1))')  # 12
test.append('b = 4\na = 2\nprint(a // b * a)')  # 13
test.append('b = 10\na = 3\nprint(a + a // b)')  # 14
test.append('b = 6\na = 5\nprint(a**(b // a))')  # 15
test.append('a = 3\ni = 0\nwhile a:\n\ta -= 1\n\ti += 2\nprint(i)')  # 17

answer = []
answer.append('33')
answer.append('20020')
answer.append('25')
answer.append('200.0')
answer.append('Cx3Cx3')
answer.append('5')
answer.append('Cx3')
answer.append('Cru4')
answer.append('Hi')
answer.append('Hallo')
answer.append('bro')
answer.append('3')
answer.append('0')
answer.append('5')
answer.append('6')

test_py = {i: f'{test[0]}{test[i]}' for i in range(0, len(test))}
answer_py = {i + 1: answer[i] for i in range(0, len(answer))}
