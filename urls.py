from handlers.restaurant__handler import CreateRestaurant, Retrive_Restaurant
from handlers.category_job__handler import CreateCategoryJob
from handlers.job__handler import CreateJob
from handlers.employ__handler import CreateEmploye

urlList  = [

    (r'/restaurant$', Retrive_Restaurant),
    (r'/restaurant/create$', CreateRestaurant),
    (r'/category/create$', CreateCategoryJob),
    (r'/job/create$', CreateJob),
    (r'/employe/create$', CreateEmploye),
]