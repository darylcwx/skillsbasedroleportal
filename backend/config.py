import os

# Establish MySQL connection
user='root'
password='root'
# password = ''
host='localhost'
port = 3306
# ===== MAC USER ====
# port = 8889
db='SBRP_Ais_Kachang'
db_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"


