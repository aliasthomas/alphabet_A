# This program is to make a alphabrt 'A'

n = 11

for i in range(n):
    
  if n - i - 1 == n // 2: # To find middle or center of 'A'
      
      #  print '*' at the middle
      
      print(' ' * (n - i) + '*' + '*' * 2 * (i + 1) + '*')
      
  else:
      
      #  print '*' at the other than middle
      
      print(' ' * (n - i) + '*' + ' ' * 2 * (i + 1) + '*')
      
      