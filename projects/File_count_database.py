from pathlib import Path
import sqlalchemy

desktop = Path("/Users/jakebestland/Desktop")

engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/desk_file_count')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

new_table = sqlalchemy.Table('Filecounter', metadata, autoload_with=engine)

query = sqlalchemy.insert(new_table)  
for filepath in desktop.iterdir():
    new_records = [{'file_name': filepath.name, 'file_type': filepath.suffix}] 
    result_proxy = connection.execute(query,new_records)

connection.commit()