# Student ID: 1201201699
# Student Name: Lalu Muhammad Safuan

def get_bonus(sal, sol):

    bonus = 0

    if(sol > 1000):
        bonus = 20/100 * sal
    elif(sol >= 501):
        bonus = 10/100 * sal
    
    return bonus

def get_nett_salary(sal, bonus):

    nett_salary = sal + bonus
    return nett_salary

def display(id, salary, sold, bon, nett):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("           SALARY SLIP                      ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Staff ID                : ",id)
    print("Staff salary            :  RM {:.2f}".format(salary))
    print("Units sold              : ",sold)
    print("Bonus                   :  RM {:.2f}".format(bon))
    print("Nett Salary             :  RM {:.2f}".format(nett))

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("            DATA ENTRY                      ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    id = int(input("Enter staff id : "))
    salary = float(input("Enter staff salary : RM "))
    sold = int(input("Enter total units sold : "))

    bon = get_bonus(salary, sold)

    nett = get_nett_salary(salary, bon)

    display(id, salary, sold, bon, nett)

main()

    