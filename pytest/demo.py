import csv

from jinja2.runtime import exported


def read_csv():
    f = open('D:\\workspace\\ai-agent-journey\\pytest\\data.csv')
    reader = csv.reader(f)
    print(list(reader)[1:0])
read_csv()

exported