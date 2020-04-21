from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from loader import load_data
from data import Base, Table14, CableCalculation, InstallMethod, SystemParameter

print("cable calc v1")

# setup database + session
database_engine = create_engine('sqlite:///cable_calc_v1.db', echo=False)
Session = sessionmaker(bind=database_engine)
sql_session = Session()

# drop tables, as per named tables
drop_tables = [CableCalculation.__table__, InstallMethod.__table__,
               SystemParameter.__table__]
Base.metadata.drop_all(database_engine, tables=drop_tables)
# create required tables
Base.metadata.create_all(database_engine)

# load sample data
load_data(sql_session=sql_session)


print()
print("cable calculations")
for cable_calculation in sql_session.query(CableCalculation).all():
    print(cable_calculation, ", load kw: ", cable_calculation.LOAD_KW)

print()
print("install methods")
for install_method in sql_session.query(InstallMethod).all():
    print(install_method)

print()
print("system parameters")
for system_parameter in sql_session.query(SystemParameter).all():
    print(system_parameter)

print()
print("Table14")
for table14_lookup in sql_session.query(Table14).all():
    print(table14_lookup)
