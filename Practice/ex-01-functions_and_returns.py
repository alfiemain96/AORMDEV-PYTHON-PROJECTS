

def get_input(): # Getting Input for The First and Second Values to be used in math 
    first_value = float(input("Please Give first Input: "))
    second_value = float(input("Please Give Second Value: "))
    return first_value, second_value

def choose_operation_type(): # Selection for the 
    print("1: Addition")
    print("2: Multiplication")
    print("3: Division")
    print("4: Subtraction")
    return (int(input("Choose What Type of Operator: ")))

def operation_type_select(choose_operation, first_variable, second_variable): # Selection for what type of math operation to do
    if choose_operation == 1:
        return lambda: first_variable + second_variable
    elif choose_operation == 2:
        return lambda: first_variable * second_variable
    elif choose_operation == 3:
        return lambda: first_variable / second_variable
    elif choose_operation == 4:
        return lambda: first_variable - second_variable
    else:
        print("Error: Value isnt Accepted: At Operation_Type_Select")

def print_result(first_variable, second_variable, choose_operation,operation_result): # Printing the results of the combination numbers
    if choose_operation == 1:
        print(f"{first_variable} + {second_variable} = {operation_result()}")
    elif choose_operation == 2:
        print(f"{first_variable} * {second_variable} = {operation_result()}")
    elif choose_operation == 3:
        print(f"{first_variable} / {second_variable} = {operation_result()}")
    elif choose_operation == 4:
        print(f"{first_variable} - {second_variable} = {operation_result()}")
    else:
        pass


def main(): # Main loop for the Program
    first_variable, second_variable = get_input()
    choose_operation = choose_operation_type()
    operation_result = operation_type_select(choose_operation, first_variable, second_variable)
    print_result(first_variable, second_variable, choose_operation, operation_result)




if __name__ == "__main__":
    main()