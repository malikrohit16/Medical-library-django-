import os,sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','miniproject.settings')
import csv
import django 
django.setup()


from firstaid_app.models import Library, Disease

csv_file = "/home/singhrohit41/django/miniproject/disease.csv"
lib = "/home/singhrohit41/django/miniproject"



def populate():
    dataReader = csv.reader(open(csv_file))


    for row in dataReader:
        dis = Library.objects.get_or_create(name = row[0])[0]
        # dis.name = row[0]
        dis.save()
    return dis

if __name__ == '__main__':
    print('populating')
    populate()
    print('done')