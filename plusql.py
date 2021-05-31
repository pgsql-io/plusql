import sqlalchemy

import sys, os


if (len(sys.argv) < 2):
  print("Invalid parameters")
  sys.exit(1)

f_sql = sys.argv[1]


with open(f_sql) as f:
    s_sql = f.readlines()
s_sql  = [x.strip() for x in s_sql]

print(s_sql)



