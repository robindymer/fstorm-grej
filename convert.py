import csv
filename = 'fstorm_anmalningar.csv'
out_file = 'coolare_format.csv'

post_mapping = {
    0: 'Vice ordförande',
    1: 'Utbildningsansvarig',
    2: 'IT-ansvarig',
    3: 'Idrottsansvarig',
    4: 'Klubbmästare',
    5: 'FUM-ledamot'
}

rows = []
heading = []

# Read file
with open(filename) as file:
    reader = csv.reader(file)
    heading = next(file)
    
    for row in reader:
        # Convert string to list
        st = row[5][1:len(row[5])-1]
        li = list(st.split(","))

        indices = [i for i, x in enumerate(li) if x.strip() == '1']
        poster = [post_mapping[int(i)] for i in indices]
        
        # Switcheroo
        row[5] = poster
        # Appenderoo
        rows.append(row)

# Write with the modifications done above
with open(out_file, 'w') as file:
    csvwriter = csv.writer(file)
    # csvwriter.writerow(heading.split(","))
    csvwriter.writerows(rows)