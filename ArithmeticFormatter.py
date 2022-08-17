def arithmetic_arranger(*args):
  arranged_problems = []
  problems = args[0]
  giveAnswer = False
  if len(args) == 2:
    if args[1] == True:
      giveAnswer = True
  #Sort out any erroneous problems
  if len(problems) > 5:
    return("Error: Too many problems.")
  for problem in problems:
    if problem.__contains__('+'):
      numbers = problem.split('+')
      for num in numbers:
        number = num.strip()
        if not number.isdigit():
          return("Error: Numbers must only contain digits.")
        elif len(number) > 4:
          return("Error: Numbers cannot be more than four digits.")
      arranged_problem = numbers[0] + "+" + numbers[1]
      arranged_problems.append(arranged_problem)
    elif problem.__contains__('-'):
      numbers = problem.split('-')
      for num in numbers:
        number = num.strip()
        if not number.isdigit():
          return("Error: Numbers must only contain digits.")
        if len(number) > 4:
          return("Error: Numbers cannot be more than four digits.")
      arranged_problem = numbers[0] + "-" + numbers[1]
      arranged_problems.append(arranged_problem)
    else:
      return("Error: Operator must be '+' or '-'.")

  #Rearrange the problems now
  tops = []
  arrangedTops = []
  bottoms = []
  dashes = []
  answers = []
  problemNum = 0
  for problem in problems:
    terms = problem.split(" ")
    tops.append(terms[0])
    
    btmTerm = ""
    if len(terms[0]) <= len(terms[2]):
      btmTerm = terms[1] + " " + terms[2]
    else:
      btmTerm = terms[1] + " "*(len(terms[0]) - len(terms[2]) + 1) + terms[2]
    bottoms.append(btmTerm)

    arrangedTops.append(" "*(len(bottoms[problemNum]) - len(tops[problemNum])) + terms[0])

    dashes.append("-"*(len(bottoms[problemNum])))
      
    if problem.__contains__("+") and giveAnswer == True:
      answer = int(terms[0]) + int(terms[2])
      answers.append(" "*(len(bottoms[problemNum]) - len(str(answer))) + str(answer))
    elif problem.__contains__("-") and giveAnswer == True:
      answer = int(terms[0]) - int(terms[2])
      answers.append(" "*(len(bottoms[problemNum]) - len(str(answer))) + str(answer))

    problemNum+=1

  spacedTops = "    ".join(arrangedTops)
  spacedBottoms = "    ".join(bottoms)
  spacedDashes = "    ".join(dashes)
  spacedAnswers  = "    ".join(answers)

  if giveAnswer == True:
    arrangedProblems = spacedTops + "\n" + spacedBottoms + "\n" + spacedDashes + "\n" + spacedAnswers
  else:
    arrangedProblems = spacedTops + "\n" + spacedBottoms + "\n" + spacedDashes
      

  return arrangedProblems


print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
