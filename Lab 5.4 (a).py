# Student ID: 1201201699
# Student Name: Lalu Muhammad Safuan

def rectangle(w, l):
    area = w * l
    print("Rectangle area : {:.2f}".format(area))

def triangle(w, l):
    area = 1/2 *w *l
    print("Triangle area : {:.2f}".format(area))

def main():
    width = int(input("Enter width : "))
    length = int(input("Enter length : "))

    rectangle(width, length)
    triangle(width, length)

main()