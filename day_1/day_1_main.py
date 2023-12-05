import re

def part_1():
    total_value = 0

    file_1 = open('day_1_input.txt', 'r')

    for line in file_1:
        stripped_line = line.strip()
        digit_string = re.sub(r'[a-zA-Z]', '', stripped_line)

        first_number = digit_string[0]
        last_number = digit_string[-1]

        final_number = int(first_number + last_number)

        total_value += final_number

    file_1.close()

    print("Total Value: " + str(total_value))
    return

def main():
    part_1()

    return


if __name__=="__main__":
    main()