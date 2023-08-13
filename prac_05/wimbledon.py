"""
Word Occurrences
Estimate: 50 minutes
Actual:   70 minutes
"""
FILE_NAME = "wimbledon.csv"


def main():
    records = []
    record = []
    result_name = {}
    result_countries = {}
    names = []
    countries = []
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for i in in_file:
            parts = i.strip().split(",")
            records.append(parts)
    print(records[:])
    [record.extend(i) for i in records]
    print(record)
    for i in range(0, len(record)):
        check_digit = is_number(record[i])
        if " " in record[i] and check_digit != "True":
            names.append(record[i])
            countries.append(record[i - 1])
            for j in range(0, len(names)):
                count_name = names.count(names[j])
                result_name[names[j]] = count_name
            for k in range(0, len(countries)):
                count_countries = countries.count(countries[k])
                result_countries[countries[j]] = count_countries
    print("Wimbledon Champions: ")
    for n in range(0, len(result_name)):
        print(list(result_name.keys())[i])
    print(f"These {len(result_countries)} countries have won Wimbledon: ")
    print(list(result_countries.keys())[i])


main()


def is_number(number):
"""Check is the string have the number"""
    try:
        float(number)
        return True
    except ValueError:
        pass
