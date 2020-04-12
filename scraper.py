import requests
import json
import csv

def print_comments(url, amount):
    video_name = url[url.rfind('/') + 1:]
    comment_url = 'https://www.khanacademy.org/api/internal/discussions/video/' + video_name + '/questions?casing=camel&limit=' + str(amount) + '&page=0&sort=1&lang=e'
    comment_json = requests.get(comment_url).json()
    for i in comment_json['feedback']:
        print(i['content'])

def csv_comments(url, amount):
    video_name = url[url.rfind('/') + 1:]
    comment_url = 'https://www.khanacademy.org/api/internal/discussions/video/' + video_name + '/questions?casing=camel&limit=' + str(amount) + '&page=0&sort=1&lang=e'
    comment_json = requests.get(comment_url).json()

    csv.register_dialect("comment", lineterminator='\r\n\n')
    with open('comments.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, dialect='comment')
        for i in comment_json['feedback']:
            writer.writerow([i['content']])
