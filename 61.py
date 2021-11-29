def calculate_distance(argument):
  if type(argument) == int or type(argument) == float:
      return abs(argument)
  else:
      print("No value")

print("the absolute value : " ,calculate_distance(33.20))

calculate_distance("what?")