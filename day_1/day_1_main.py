import re


def remove_letters(original_str):
    number_str = re.sub(r'[a-zA-Z]', '', original_str)

    return number_str


def part_1():
    total_value = 0

    file_1 = open('day_1_input.txt', 'r')

    for line in file_1:
        stripped_line = line.strip()
        digit_string = remove_letters(stripped_line)

        first_number = digit_string[0]
        last_number = digit_string[-1]

        final_number = int(first_number + last_number)

        total_value += final_number

    file_1.close()

    print("Total Value: " + str(total_value))
    return


def part_2():
    total_value = 0
    number_strings_dict = {
        'one': 'one1one',
        'two': 'two2two',
        'three': 'three3three',
        'four': 'four4four',
        'five': 'five5five',
        'six': 'six6six',
        'seven': 'seven7seven',
        'eight': 'eight8eight',
        'nine': 'nine9nine'
    }

    file_1 = open('day_1_input.txt', 'r')
    # file_1 = open('test_input.txt', 'r')

    for line in file_1:
        stripped_line = line.strip()
        converted_line = stripped_line
        print(converted_line)

        for number_string in number_strings_dict:
            converted_line = converted_line.replace(number_string, str(number_strings_dict[number_string]))

        print(converted_line)
        converted_line = remove_letters(converted_line)

        first_number = converted_line[0]
        last_number = converted_line[-1]

        final_number = int(first_number + last_number)
        print(str(first_number) + " + " + str(last_number) + " = " + str(final_number))

        total_value += final_number

    file_1.close()
    print(total_value)
    return

def main():
    # part_1()
    part_2()

    return


if __name__=="__main__":
    main()