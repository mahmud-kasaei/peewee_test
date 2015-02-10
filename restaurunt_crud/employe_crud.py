from models import Employe, Resturant
class Crud():

    def create(self, job_id, res_id):
        f_name=raw_input("Enter first name of Employe:")
        l_name=raw_input("Enter last name of Employe:")
        Employe.create(f_name=f_name, l_name=l_name, job=job_id, resturant=res_id)

    def retrive(self):
        for e in Employe.select():
            print e.f_name, e.l_name

    def retrive_res(self, res_id):
        res1=(Employe.select().join(Resturant).where(Employe.resturant==res_id))
        for r in res1:
            print r.f_name, r.l_name

if __name__=="__main__":
    # ids=input("insert job_id, restaurant_id:")
    # print ids[0], ids[1]
    # Crud().create(job_id=ids[0], res_id=ids[1])
    # Crud().retrive()
    #  print Employes that work on restaurant --1--
    res_id=input("Enter res_id to fetch Employes that work on:")
    Crud().retrive_res(res_id=res_id)
