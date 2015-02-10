import peewee
from models import Job
class Crud():
    def create(self):
        name= raw_input("enter name of job:")
        Job.create(name=name)

    def RetriveAllJob(self):
        for j in Job.select():
            print j.name

if __name__=="__main__":
    # Crud().create()
    Crud().RetriveAllJob()