def get_number_of_employees():
    num_employees = int(input("Enter the number of employees: "))
    while num_employees < 1:
        print("Error must have at least 1 employee.")
        num_employees = int(input("Please enter a number of employees: "))
    return num_employees

def get_total_days_absent(num_employees):
    total_days = 0
    for employee in range(1, num_employees + 1):
        days_missed = int(input(f"Enter the number of days missed {employee}: "))
        while days_missed < 0:
            print("Error: Days missed cannot be negative.")
            days_missed = int(input(f"Enter the days missed for Employee {employee}: "))
        total_days += days_missed
    return total_days

def calculate_average_days_absent(num_employees, total_days_absent):
    average = total_days_absent / num_employees
    return float(average)

def main():
    employees = get_number_of_employees()
    total_absent = get_total_days_absent(employees)
    average_absent = calculate_average_days_absent(employees, total_absent)
    print(f"\nThe average number of days absent is: {average_absent:.2f}")

main()