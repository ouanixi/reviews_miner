import csv
from utils import remove_nonascii

numbers = {"ratingone": 1, "ratingtwo": 2, "ratingthree": 3, "ratingfour": 4, "ratingfive": 5}
reviews = []


def clean_informative_files():
    with open('/home/ouanixi/Work/reviews_miner/datasets/datasets/info_noninfo/merged_info.txt') as f:
        lines = f.readlines()
        for line in lines:
            l = line.strip('\r\n').split(' ', 1)[1:]
            l = ' '.join(l).split(' ', 1)
            try:
                reviews.append({"rating": numbers[l[0]], "review": remove_nonascii(l[1].strip()), "class": "informative"})
            except Exception as e:
                continue

    keys = reviews[0].keys()
    with open('informative.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(reviews)

    print len(reviews)

if __name__ == "__main__":
    clean_informative_files()