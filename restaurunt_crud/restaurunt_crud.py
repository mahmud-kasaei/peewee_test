import peewee
from models import Resturant

class Crud:
    def create(self):
        name = raw_input('Enter the name of Restaurant:')
        add = raw_input('Enter Address of Restaurant:')
        # print name
        res=Resturant(name=name, address=add)
        res.save()

    def retrive(self):
        for re in Resturant.select():
            print re.name

    def retrive_one(self,name):
        for res in Resturant.select().where(Resturant.name==name):
            print res.name, res.id, res.address


if __name__=="__main__":
    # Crud().create()
    # Crud().retrive()
    name=raw_input("Enter name of restaurant:")
    Crud().retrive_one(name=name)