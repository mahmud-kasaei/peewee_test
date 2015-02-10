import peewee
rest_db = peewee.MySQLDatabase('test_peewee', host="localhost", user="root", port=3306, passwd="")

class MyRestModel(peewee.Model):

    class Meta:
        database=rest_db

class Resturant(MyRestModel):
    id= peewee.PrimaryKeyField()
    name=peewee.CharField()
    address=peewee.TextField()

class Job(MyRestModel):
    id=peewee.PrimaryKeyField()
    name=peewee.TextField()

class Employe(MyRestModel):
    id=peewee.PrimaryKeyField()
    f_name=peewee.TextField()
    l_name=peewee.TextField()
    job=peewee.ForeignKeyField(Job, related_name="employes", on_delete="RESTRICT", on_update="CASCADE")
    resturant=peewee.ForeignKeyField(Resturant,related_name="employes", on_delete="RESTRICT", on_update="CASCADE")

class Peripherals(MyRestModel):
    id=peewee.PrimaryKeyField()
    name=peewee.CharField()
    count=peewee.IntegerField()
    restaurant=peewee.ForeignKeyField(Resturant,related_name="peripherals", on_delete="RESTRICT", on_update="CASCADE")

class Room(MyRestModel):
    id=peewee.PrimaryKeyField()
    name=peewee.TextField()
    peripherals=peewee.ForeignKeyField(Peripherals, related_name="rooms", on_update="CASCADE", on_delete="RESTRICT")
    restaurant=peewee.ForeignKeyField(Resturant, related_name="rooms",on_update="CASCADE", on_delete="RESTRICT")
    emoloye=peewee.ForeignKeyField(Employe, related_name="rooms", on_update="CASCADE", on_delete="RESTRICT")

class Category_Job(MyRestModel):
    id=peewee.PrimaryKeyField()
    name=peewee.TextField()
    job=peewee.ForeignKeyField(Job, related_name="categories", on_update="CASCADE", on_delete="RESTRICT")

rest_db.connect()

if __name__ == "__main__":
    rest_db.create_tables([Resturant, Employe, Peripherals, Room, Job, Category_Job])