# Open the file in read mode ('r')
with open('filename.csv', 'r') as file:
    # Iterate over each line in the file
    counter = {}
    for i, line in enumerate(file):
        columns = line.split(',')
        if len(columns) < 13:
            continue

        counter[columns[4]] = [columns[7], columns[9]]
    print(counter)
# TODO use multithreading to speed up the process