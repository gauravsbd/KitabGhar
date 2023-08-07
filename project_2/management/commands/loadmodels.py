from django.core.management.base import BaseCommand
from bookinfo.models import Bookinfo
import pandas as pd
class Command(BaseCommand):
    help='import books'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        #database connection is here
        df=pd.read_csv('model_data.csv')
        for title, description,seller,original_price,  selling_price, condition, category,image,latitude, longitude, added_date in zip(df.title,df.description,df.seller,df.original_price, df.selling_price,df.condition,df.category,df.image,df.latitude, df.longitude,df.added_date):
            models=Bookinfo(title=title,
                            description=description, 
                            seller=seller,
                            original_price=original_price,
                            selling_price=selling_price,
                            condition=condition,
                            category=category,
                            image=image,
                            latitude=latitude,
                            longitude=longitude,
                            added_data=added_date
                            )
            models.save()
            

        
      
        
