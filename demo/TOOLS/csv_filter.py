# Open the file in read mode ('r')
try:
    with open('filename.csv', 'r') as file:
        # Iterate over each line in the file
        counter = {}
        for i, line in enumerate(file):
            columns = line.split(',')
            if len(columns) < 13:
                continue

            counter[columns[4]] = [columns[7], columns[9]]
        print(counter)
except OSError as err:
    print("Open file failed: {0}".format(err))

# TODO use multithreading to speed up the process
