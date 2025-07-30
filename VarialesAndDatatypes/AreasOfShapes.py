import math

print("Area Calculator")
print("Choose a shape:")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")
print("5. Parallelogram")
print("6. Trapezium")

choice = input("Enter the number of your choice (1-6): ")

if choice == "1":
    r = float(input("Enter the radius of the circle: "))
    area = math.pi * r ** 2
    print("Area of the circle is:", round(area, 2))

elif choice == "2":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = length * width
    print("Area of the rectangle is:", round(area, 2))

elif choice == "3":
    side = float(input("Enter the side of the square: "))
    area = side ** 2
    print("Area of the square is:", round(area, 2))

elif choice == "4":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height: "))
    area = 0.5 * base * height
    print("Area of the triangle is:", round(area, 2))

elif choice == "5":
    base = float(input("Enter the base of the parallelogram: "))
    height = float(input("Enter the height: "))
    area = base * height
    print("Area of the parallelogram is:", round(area, 2))

elif choice == "6":
    a = float(input("Enter the length of first parallel side: "))
    b = float(input("Enter the length of second parallel side: "))
    height = float(input("Enter the height: "))
    area = 0.5 * (a + b) * height
    print("Area of the trapezium is:", round(area, 2))

else:
    print("Invalid choice. Please run the program again.")
