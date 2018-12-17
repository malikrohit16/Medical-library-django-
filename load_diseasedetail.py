import os,sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','miniproject.settings')
import csv
import django 
django.setup()


from firstaid_app.models import Library, Disease

csv_file = "/home/singhrohit41/django/miniproject/disease_detail.csv"
lib = "/home/singhrohit41/django/miniproject"



def populate():
    dataReader = csv.reader(open(csv_file))
    

    for row in dataReader:
        lib = Library.objects.get_or_create(name=row[0])[0]
        dis = Disease.objects.get_or_create(name = lib,about= row[1],treatment=row[4],causes=row[3],symptoms=row[2])[0]
        # dis.name = row[0]
        dis.save()
    return dis

if __name__ == '__main__':
    print('populating')
    populate()
    print('done')