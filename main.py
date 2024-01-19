def print_star_triangle(rows):
    for i in range(1, rows + 1):
        print('* ' * i)

# Set the number of rows for the star triangle
num_rows = int(input("Enter the number of rows for the star triangle: "))

# Call the function to print the star triangle
print_star_triangle(num_rows)