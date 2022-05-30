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
    question_url = 'https://www.khanacademy.org/api/internal/discussions/video/' + video_name + '/questions?casing=camel&limit=' + str(amount) + '&page=0&sort=1&lang=e'
    question_json = requests.get(question_url).json() # This is actually only the questions/answers, replies aren't in this file

    csv.register_dialect("comment", lineterminator='\r\n')
    with open(video_name + '.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, dialect='comment')
        # Loop through the questions
        writer.writerow(['comment', 'score'])
        for question in question_json['feedback']:
            # Write the content of the question
            writer.writerow([question['content']])
            # Loop through the question replies
            reply_url = 'https://www.khanacademy.org/api/internal/discussions/' + question['key'] + '/replies?casing=camel&lang=en'
            reply_json = requests.get(reply_url).json()
            for reply in reply_json:
                writer.writerow([reply['content']])
            # Loop through the answers
            for answer in question['answers']:
                writer.writerow([answer['content']])
                # Loop through the answer replies
                reply_url = 'https://www.khanacademy.org/api/internal/discussions/' + answer['key'] + '/replies?casing=camel&lang=en'
                reply_json = requests.get(reply_url).json()
                for reply in reply_json:
                    writer.writerow([reply['content']])
