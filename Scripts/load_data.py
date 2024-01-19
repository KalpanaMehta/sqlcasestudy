import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:root1234@localhost/Famous_painting'
db = create_engine(conn_string)
conn = db.connect()

# df = pd.read_csv('/Users/Kalpana/Desktop/sqlcasestudy/Dataset/artist.csv')
# # print(df)
# df.to_sql('artist',con=conn,if_exists='replace',index=False)

files = ['canvas_size','image_link','museum_hours','museum','product_size','subject','work']

for file in files :
    df = pd.read_csv(f'/Users/Kalpana/Desktop/sqlcasestudy/Dataset/{file}.csv')
    df.to_sql(file,con=conn,if_exists='replace',index=False)
