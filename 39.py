def even_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2!= 0:
      result = result + str[i]
  return result
print(even_values_string('abcdef'))
print(even_values_string('python'))