import sqlalchemy

from sqlalchemy import create_engine

import sys, os


def main_loop():
  s_sql = load_sql_file(f_sql)

  stmt = ""
  for line in s_sql:

    ## skip some lines
    if line == "":
      ##print(line)
      continue
    if line.startswith("--"):
      ##print(line)
      continue

    ## sql statements are terminated by a semicolon
    if line.endswith(";"):
      stmt = stmt + line
      exec_sql(stmt)
      stmt = ""
    else:
      stmt = stmt + line + "\n"


def load_sql_file(p_f_sql):
  try:
    with open(p_f_sql) as f:
      s_sql = f.readlines()
  except Exception as e:
    print(e)
    sys.exit(1)
    
  s_sql  = [x.rstrip() for x in s_sql]
  return(s_sql)


def exec_sql(p_stmt):
  print(p_stmt)
  print("")
  try:
    con1.execute(p_stmt)
  except Exception as e:
    print(e)
    print("")


#############################################
## MAINLINE
#############################################

if (len(sys.argv) < 2):
  print("Invalid parameters")
  sys.exit(1)
f_sql = sys.argv[1]

eng1 = create_engine('sqlite:///:memory:')
con1 = eng1.connect()
main_loop()

sys.exit(0)
