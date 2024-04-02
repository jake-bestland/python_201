from pathlib import Path
import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/desk_file_count')
connection = engine.connect()
metadata = sqlalchemy.MetaData()


filecount_table = sqlalchemy.Table('filecounter', metadata, autoload_with=engine)

del_filecount_query = sqlalchemy.delete(filecount_table)
del_filecount_proxy = connection.execute(del_filecount_query)

query = sqlalchemy.insert(filecount_table)
desktop = Path("/Users/jakebestland/Desktop")

fct_query = sqlalchemy.select(filecount_table.columns.file_name).select_from(filecount_table)
fct_proxy = connection.execute(fct_query)
fct_results = fct_proxy.fetchall()

for filepath in desktop.iterdir():
    new_records = [{'file_name': filepath.name, 'file_type': filepath.suffix}]
    result_proxy = connection.execute(query,new_records)


count_fn = sqlalchemy.func.count(filecount_table.columns.file_id)

###file_types table###
f_t_table = sqlalchemy.Table('file_types', metadata, autoload_with=engine)

del_ft_query = sqlalchemy.delete(f_t_table)
del_ft_proxy = connection.execute(del_ft_query)

ft_query = sqlalchemy.select(count_fn, filecount_table.columns.file_type).select_from(filecount_table).group_by(filecount_table.columns.file_type).order_by(sqlalchemy.desc(count_fn))

ft_ins_query = sqlalchemy.insert(f_t_table)

ft_proxy = connection.execute(ft_query)
ft_results = ft_proxy.fetchall()

for x, y in ft_results:
    ft_records = [{'num_files': x, 'file_type': y}]
    result_proxy = connection.execute(ft_ins_query, ft_records)

###most_common table###
mc_table = sqlalchemy.Table('most_common', metadata, autoload_with=engine)

del_mc_query = sqlalchemy.delete(mc_table)
del_mc_proxy = connection.execute(del_mc_query)

mc_query = sqlalchemy.select(count_fn, filecount_table.columns.file_type).select_from(filecount_table).group_by(filecount_table.columns.file_type).order_by(sqlalchemy.desc(count_fn)).limit(1)

mc_ins_query = sqlalchemy.insert(mc_table)

mc_proxy = connection.execute(mc_query)
mc_results = mc_proxy.fetchall()
for x, y in mc_results:
    mc_records = [{'num_files': x, 'file_type': y}]
    result_proxy = connection.execute(mc_ins_query, mc_records)

###most_file_date table
mfd_table = sqlalchemy.Table('most_files_date', metadata, autoload_with=engine)

mfd_query = sqlalchemy.select(count_fn, filecount_table.columns.date_updated).select_from(filecount_table).group_by(filecount_table.columns.date_updated).order_by(sqlalchemy.desc(count_fn)).limit(1)

mfd_ins_query = sqlalchemy.insert(mfd_table)

mfd_proxy = connection.execute(mfd_query)
mfd_results = mfd_proxy.fetchall()
for x, y in mfd_results:
    mfd_records = [{'num_files': x, 'date_updated': y}]
    result_proxy = connection.execute(mfd_ins_query, mfd_records)

connection.commit()