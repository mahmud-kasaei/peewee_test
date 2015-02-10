import peewee
rest_db = peewee.MySQLDatabase('restaurant_db', host="localhost", user="root", port=3306, passwd="")

class MyRestModel(peewee.Model):

    class Meta:
        database=rest_db

class Resturant(MyRestModel):
    id= peewee.PrimaryKeyField()
    name=peewee.CharField()
    address=peewee.TextField()

class Employe(MyRestModel):
    id=peewee.PrimaryKeyField()
    f_name=peewee.TextField()
    l_name=peewee.TextField()
    job=peewee.ForeignKeyField(Job)
    resturant=peewee.ForeignKeyField(Resturant,related_name="employes", on_delete="RESTRICT", on_update="CASCADE")

class Peripherals(MyRestModel):
    id=peewee.PrimaryKeyField()
    name=peewee.CharField()
    count=peewee.IntegerField()
    restaurant=peewee.ForeignKeyField(Resturant,related_name="peripherals", on_delete="RESTRICT", on_update="CASCADE")

class Room(MyRestModel):
    id=peewee.PrimaryKeyField()
    name=peewee.TextField()
    peripherals=peewee.ForeignKeyField(Peripherals)
    restaurant=peewee.ForeignKeyField(Resturant)
    emoloye=peewee.ForeignKeyField(Employe)

class Job(MyRestModel):
    id=peewee.PrimaryKeyField()
    name=peewee.TextField()

class Category_Job(MyRestModel):
    id=peewee.PrimaryKeyField()
    name=peewee.TextField()
    job=peewee.ForeignKeyField(Job)
