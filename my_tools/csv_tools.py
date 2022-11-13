import csv


def read_csv(path):
    print('Se ejecutó la función read_csv')

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        #print(headers)

        data = []

        for row in reader:
            iterable = zip(headers, row)
            data_dict = {key: value for key, value in iterable}
            data.append(data_dict)

        return headers, data


if __name__ == '__main__':
    read_csv('../world_population.csv')
