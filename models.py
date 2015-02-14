import peewee

rest_db = peewee.MySQLDatabase('test_peewee', host="localhost", user="root", port=3306, passwd="")

class MyRestModel(peewee.Model):

    class Meta:
        database=rest_db

class Resturant(MyRestModel):
    id= peewee.PrimaryKeyField()
    name=peewee.CharField()
    address=peewee.TextField()

    def employe_restaurant(self):
        return (
            Employe.select()
            .join(Employe_Restaurant, on=Employe_Restaurant.employe)
            .where(Employe_Restaurant.restaurant == self)
        )

class Category_Job(MyRestModel):
    id=peewee.PrimaryKeyField()
    name=peewee.TextField()


class Job(MyRestModel):
    id=peewee.PrimaryKeyField()
    name=peewee.TextField()
    category=peewee.ForeignKeyField(Category_Job, related_name="jobs", on_update="CASCADE", on_delete="RESTRICT")

class Employe(MyRestModel):
    id=peewee.PrimaryKeyField()
    f_name=peewee.TextField()
    l_name=peewee.TextField()
    category_job=peewee.ForeignKeyField(Category_Job, related_name="employes_category_job", on_delete="RESTRICT", on_update="CASCADE")
    job=peewee.ForeignKeyField(Job, related_name="employes_jobs", on_delete="RESTRICT", on_update="CASCADE")
    # restaurant=peewee.ForeignKeyField(Resturant, related_name="employes_restaurants", on_delete="RESTRICT", on_update="CASCADE")
    def rest_employe(self):
        return (Employe.select()
        .join(Employe_Restaurant, on=Employe_Restaurant.restaurant)
        .where(Employe_Restaurant.employe=="self"))

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

class Employe_Restaurant(MyRestModel):
    id = peewee.PrimaryKeyField()
    employe = peewee.ForeignKeyField(Employe, related_name="employes_id", on_update="CASCADE", on_delete="RESTRICT")
    restaurant = peewee.ForeignKeyField(Resturant, related_name="restaurants_id", on_update="CASCADE", on_delete="RESTRICT")

    class Meta:
        indexes = (
            # Specify a unique multi-column index on from/to-user.
            (('employe', 'restaurant'), True),
        )


rest_db.connect()



if __name__ == "__main__":
    # my.create_table()
    rest_db.create_tables([Resturant, Employe, Peripherals, Room, Category_Job, Job, Employe_Restaurant])
    # rest_db.create_table(Category_Job)
    # rest_db.create_tables([Employe_Restaurant, Employe])