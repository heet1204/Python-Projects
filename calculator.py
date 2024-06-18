def add(n1, n2):
  return n1 + n2 
def subtract(n1, n2):
  return n1 - n2 
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2
  
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
  num1 = float(input("\nEnter the number: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation : ")
    num2 = float(input("Enter the next number: "))
    calculation = operations[operation_symbol]
    answer = calculation(num1, num2)

    print(f"\n{num1} {operation_symbol} {num2} = {answer}")

    result = input(f"\nEnter 'y' to continue calculations with {answer}"
                   ", 'n' to start new calculation or 'e' to exit : ")
    if result == "y":
      print("\n")
      num1 = answer
    elif result == "n":
      should_continue = False
      calculator()
    else:
      print("\n GOODBYE!!!!")
      should_continue = False
      
calculator()
