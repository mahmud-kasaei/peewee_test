from handlers.restaurant__handler import CreateRestaurant, Retrive_Restaurant

urlList  = [

    (r'/', Retrive_Restaurant),
    (r'/restaurant/add',CreateRestaurant )
]