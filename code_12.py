def get_fibonacci_number(position):
    if position <= 0:
        return []
    elif position == 1:
        return [0]
    elif position == 2:
        return [0, 1]
    else:
        sequence = get_fibonacci_number_sequence(position - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence[position - 1]

def get_fibonacci_number_sequence(number):
    temp_1, temp_2 = 0, 1
    sequence = []
    while temp_1 <= number:
        sequence.append(temp_1)
        temp_1, temp_2 = temp_2, temp_1 + temp_2
    return sequence
if __name__ == "__main__":
    x = int(1)
    user_position = input("Please enter a positive integer: ")
    user_position = int(user_position)
    while(x >= 1):
        if user_position < 0:
            user_position = input("This number is not positive, please try another: ")
            user_position = int(user_position)
        else:
            num_at_pos = get_fibonacci_number(user_position)
            sequence = get_fibonacci_number_sequence(num_at_pos)
            print(sequence)
            x = 0