############################################################
#  Copyright(c) 2021  Denis Lussier.  All rights reserved. #
############################################################

import sqlalchemy

from sqlalchemy import create_engine

import sys, os

PREFIX="SQL> "


def main_loop():
  s_sql = load_sql_file(f_sql)

  stmt = ""
  for line in s_sql:

    ## skip some lines
    if line == "":
      continue
    if line.startswith("--"):
      continue

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
  print_sql_stmt(p_stmt)

  ## figure out what to do by looking at the first token
  sp_stmt = p_stmt.split()
  for token in sp_stmt:
    l_token = token.lower()
    if l_token == "select":
      rc = execute_sql_select(p_stmt)
    else:
      rc = execute_sql(p_stmt)
    break

  print_empty_line()
  return(rc)


def print_sql_stmt(p_sql):
  print(PREFIX + str(p_sql))


def execute_sql_select(p_stmt):
  try:
    result = con1.execute(p_stmt)
  except Exception as e:
    print_sql_exception(e)
    return(False)

  print_rows(result.fetchall())

  return(True)


def execute_sql(p_stmt):
  try:
    con1.execute(p_stmt)
  except Exception as e:
    print_sql_exception(e)
    return(False)
  return(True)


def print_rows(p_rows):
  print(PREFIX + str(p_rows))
  print_empty_line()


def print_empty_line():
  #print(PREFIX)
  print("")
  


def print_sql_exception(e):
    ##for line in e.response['Error']['Message']:
    ##  print(line)
    ##(Background on this error

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
