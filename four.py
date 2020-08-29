x = abs(int(input('введи число ')))
num = x % 10
while x >= 1:
      x = x // 10
      if x % 10 > num:
            num = x % 10
      if x > 9:
            continue
      else:
            print('максимальная цифра в числе - ', num)
            break
