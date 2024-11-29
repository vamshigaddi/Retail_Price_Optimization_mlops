import pandas as pd
from index import RetailPrices, Session, Base, engine

# Ensure tables are created in the database
Base.metadata.create_all(engine)

with Session.begin() as db:
    data = pd.read_csv(r'data/retail_price.csv')
    for index, row in data.iterrows():
        try:
            retail_prices = RetailPrices(
                product_id=row[0],
                product_category_name=row[1],
                month_year=pd.to_datetime(row[2]),  # Ensure DateTime conversion
                qty=int(row[3]),
                total_price=row[4],
                freight_price=row[5],
                unit_price=row[6],
                product_name_lenght=int(row[7]),
                product_description_lenght=int(row[8]),
                product_photos_qty=int(row[9]),
                product_weight_g=int(row[10]),
                product_score=row[11],
                customers=int(row[12]),
                weekday=int(row[13]),
                weekend=int(row[14]),
                holiday=int(row[15]),
                month=int(row[16]),
                year=int(row[17]),
                s=row[18],
                volume=int(row[19]),
                comp_1=row[20],
                ps1=row[21],
                fp1=row[22],
                comp_2=row[23],
                ps2=row[24],
                fp2=row[25],
                comp_3=row[26],
                ps3=row[27],
                fp3=row[28],
                lag_price=row[29],
            )
            db.add(retail_prices)
        except Exception as e:
            print(f"Error inserting row {index}: {e}")
