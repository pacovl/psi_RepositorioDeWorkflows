import dj_database_url
import psycopg2
import sys

D = dj_database_url.config()

#set databae variables
print "export PGUSER=%s\nexport PGPASSWORD=%s\nexport PGHOST=%s\nexport PGDATABASE=%s "%(D['USER'], D['PASSWORD'], D['HOST'], D['NAME'])
