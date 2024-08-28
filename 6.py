def perfect_squares(start, end):
    perfect_squares_list = []
    for number in range(start, end + 1):
        if number >= 0 and int(number**0.5)**2 == number:
            perfect_squares_list.append(number)
    return perfect_squares_list

# Example usage:
start_range = 1
end_range = 100
perfect_squares_list = perfect_squares(start_range, end_range)
print("Perfect squares between", start_range, "and", end_range, "are:", perfect_s
