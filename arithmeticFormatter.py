def arithmetic_arranger(problems, result=False):

  # Checks if there is at least 5 problems
  if len(problems) > 5:
    print("\nError: Too many problems.\n")
    
  # Checks if the problem is valid
  for func in problems:
    if '+' in func or '-' in func:
      continue
    else:
      print("\nError: Operator must be '+' or '-'.\n")

  # Checks if numbers are no longer than 4 digits
  for func in problems:
    func = func.split()
    for item in func:
      if len(item) > 4:
        print("\nError: Numbers cannot be more than four digits.\n")
  # Checks if there is only numbers on the problems
    if func[0].isdigit() and func[2].isdigit():
      continue
    else:
      print("\nError: Numbers must only contain digits.\n")

  # Format problems
  operation = ""
  topRow = ""
  downRow = ""
  line = ""
  resultRow = ""
  for func in problems:
    if result:
      operation = eval(func)
    func = func.split()
    if (len(func[0])) >= (len(func[1]) + len(func[2])):
      width = len(func[0]) + 2
    else:
      width = (len(func[1]) + len(func[2])) + 1
    topRow += "{0:>{1}}    ".format(func[0], width)
    downRow += "{0}{1:>{2}}    ".format(func[1], func[2], (width - 1))
    line += ('-' * width) + (4 * ' ')
    resultRow += "{0:>{1}}    ".format(operation, width)
    #print("{0:>5}\n{1} {2:>3}\n-----\n{3:>5}".format(func[0], func[1], func[2], operation))
  
  print()
  print(topRow)
  print(downRow)
  print(line)
  print(resultRow)
  print()

  return problems

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)