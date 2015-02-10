import peewee
rest_db = peewee.MySQLDatabase('my_database', host="localhost", user="root", port=3306, passwd="")

class MyRestModel(peewee.Model):

    class Meta:
        database=rest_db

class Resturant(MyRestModel):
    id= peewee.PrimaryKeyField()
    name=peewee.CharField()
    address=peewee.TextField()

class Employe(MyRestModel):
    id=peewee.PrimaryKeyField()
    name=peewee.TextField()
    resturant=peewee.ForeignKeyField(related_name="employes", on_delete="RESTRICT", on_update="CASCADE")

class pr