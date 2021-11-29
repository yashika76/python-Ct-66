def change_sring(str1):
      return str1[0:1]+str1[-1:] + str1[2:-1] + str1[1:2]
	  
print(change_sring('abcd'))
print(change_sring('12345'))