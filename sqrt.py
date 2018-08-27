import math

def get_lines_sum(filename):
    lines_sum = []
    with open(filename) as file:
        for line in file:
            lines_sum.append(sum([int(number_str) for number_str in line.strip().split(',')]))
    return lines_sum


def get_sum_sqrt(numbers):
    sum_sqrt = 0

    for number in numbers:    
        sum_sqrt += math.sqrt(number)
    return sum_sqrt


def main():
    lines_sum = get_lines_sum('100.txt')
    sum_sqrt = get_sum_sqrt(lines_sum)
    print(sum_sqrt)

if __name__ == '__main__':
    main()
