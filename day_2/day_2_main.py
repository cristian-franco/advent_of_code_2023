import re


def remove_letters(original_str):
    number_str = re.sub(r'[a-zA-Z ]', '', original_str)

    return number_str


def validate_pull(pull_dict):
    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    if 'red' in pull_dict and pull_dict['red'] > 12:
        return False
    if 'green' in pull_dict and pull_dict['green'] > 13:
        return False
    if 'blue' in pull_dict and pull_dict['blue'] > 14:
        return False

    return True


def process_pull(pull_line):
    # input: 1 green, 6 red, 4 blue
    color_dict = {}

    color_pull_list = pull_line.split(',')
    # print(color_pull_list)

    for color_pull in color_pull_list:
        # print(color_pull)
        num_color_list = color_pull.split(' ')
        num_color_list.pop(0)
        # print(num_color_list)
        num_color_str = int(num_color_list[0])
        color_str = num_color_list[1]

        color_dict[color_str] = num_color_str

    # print(color_dict)

    return color_dict


def process_game(game_line):
    game_id_split = game_line.split(':')
    game_id = str(remove_letters(game_id_split[0]))

    pull_lines = game_id_split[1]

    pull_list = pull_lines.split(';')
    # print(pull_list)
    for pull_line in pull_list:
        pull_dict = process_pull(pull_line)
        is_pull_valid = validate_pull(pull_dict)

        if not is_pull_valid:
            return [game_id, False]

    return [game_id, True]


def part_1():
    id_total = 0
    # only 12 red cubes, 13 green cubes, and 14 blue cubes
    file_1 = open('day_2_input.txt', 'r')

    for line in file_1:
        stripped_line = line.strip()
        print(stripped_line)

        id_result_list = process_game(stripped_line)
        if id_result_list[1]:
            id_total += int(id_result_list[0])

    print(str(id_total))

    return

def main():
    part_1()

    return


if __name__ == "__main__":
    main()