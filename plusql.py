import sqlalchemy

import sys, os


if (len(sys.argv) < 2):
  print("Invalid parameters")
  sys.exit(1)

f_sql = sys.argv[1]


def mainline():
  with open(f_sql) as f:
    s_sql = f.readlines()
  s_sql  = [x.rstrip() for x in s_sql]

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


def exec_sql(p_stmt):
  print(p_stmt)


####################################
mainline()
sys.exit(0)
