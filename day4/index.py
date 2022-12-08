
def is_section_part_contains_the_other(section):
    i, j = section.split(',')
    i_start, i_end = map(int, i.split('-'))
    j_start, j_end = map(int, j.split('-'))

    return (i_start <= j_start and j_end <= i_end) or (i_start >= j_start and j_end >= i_end)


def is_section_has_duplicated_numbers(section):
    i, j = section.split(',')
    i_start, i_end = map(int, i.split('-'))
    j_start, j_end = map(int, j.split('-'))
    return bool(set(range(i_start, i_end + 1)) & set(range(j_start, j_end + 1)))

with open('data.txt', encoding='utf-8') as f:
    sections = [line.replace('\n', '') for line in f.readlines() if line.replace('\n', '')]
    sections_with_part_contains_values = [
            is_section_part_contains_the_other(section)
            for section in sections
    ]
    sections_with_duplicated_values = [
            is_section_has_duplicated_numbers(section)
            for section in sections
    ]
    print(sum(sections_with_part_contains_values))
    print(sum(sections_with_duplicated_values))


