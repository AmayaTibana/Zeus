def function_4(num):
   if num > 1:
      num = num - 2
   else:
      num = num + 2
   return num
 
def function_3(num):
   if num > 1:
      num = num / 2
   else:
      num = num / -2
   return num

def function_2(num):
   if num > 1:
      num = num * 2
      num = function_3(num)
   else:
      num = num * -2
      num = function_4(num)
   return num

def function_1(num):
   if num > 0:
      num += 1
      num = function_2(function_3(num))
   else:
      num -=1
      num = function_2(function_4(num))
   return num
 
print('output = ', function_1(5))