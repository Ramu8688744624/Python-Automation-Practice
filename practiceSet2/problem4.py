import csv
try:
    with open('posts.csv','r') as f:
        data = csv.reader(f)
        count = 0
        next(data)
        for post in data:
            if not post:   # empty row
                continue

            try:
                 userId = int(post[2])
                 if userId == 1:
                        count = count + 1
            except(ValueError,TypeError):
                print('skipping row',post[0])
        print('Count: ',count)
except FileNotFoundError:
    print('File Not Found')
finally:
    if 'f' in locals():
        f.close()