############################################################
#  Copyright(c) 2021  Denis Lussier.  All rights reserved. #
############################################################

import sys, json

import pg8000.native

PROMPT = "SQL> "

commands = ['@', '@@', 'acc', 'accept', 'bre', 'break', 'btitle', 'cl', 'clear',
            'col', 'column', 'comp', 'compute', 'conn', 'connect', 'copy',
            'def', 'define', 'desc', 'describe', 'disc', 'disconnect',
            'exec', 'execute', 'exit', 'get', 'help', 'ho', 'host', 'l', 'list',
            'passw', 'password', 'pau', 'pause', 'pri', 'print', 'pro', 'prompt',
            'quit', 'recover', 'rem', 'remark', 'repf', 'repfooter',
            'reph', 'repheader', 'r', 'run', 'sav', 'save', 'set', 'sho', 'show',
            'shutdown', 'sp', 'spool', 'sta', 'start', 'startup', 'store',
            'timi', 'timing', 'ttitle', 'undef', 'undefine', 'var', 'variable', 'whenever']


def main_loop():
    s_sql = load_sql_file(f_sql)

    stmt = ""
    line_num = 0
    is_multi_line_comment = False
    is_multi_line_stmt = False

    for line in s_sql:
        line_num = line_num + 1

        ## empty lines & single line comments
        if line == "" or line.startswith("--"):
            print(f"{line}")
            continue

        ## multi-line comments
        if line.startswith('/*'):
            if line.endswith('*/'):
                print(f"{line}")
                continue
            is_multi_line_comment = True
            print(f"{line}")
            continue
        if is_multi_line_comment:
            print(f"{line}")
            if line.endswith('*/'):
                is_multi_line_comment = False
            continue

        if line.endswith(";"):
            stmt = stmt + line
            exec_sql(stmt, line_num)
            stmt = ""
            is_multi_line_stmt = False
            continue
        if is_multi_line_stmt:
            stmt = stmt + line + "\n"
            continue

        l_line = line.lower()
        tokens = l_line.split()
        if tokens[0] in commands:
            process_command(tokens, line)
            continue

        # starting a multi-line statement
        stmt = stmt + line + "\n"
        is_multi_line_stmt = True


def process_command(tkns, ln):
    print(f"COMMAND: {ln}")
    if tkns[0] in ('@', '@@'): c_at(tkns, ln)
    elif tkns[0] in ('acc', 'accept'): c_accept(tkns, ln)
    elif tkns[0] in ('bre', 'break'): c_break(tkns, ln)
    elif tkns[0] == 'btitle': c_btitle(tkns, ln)
    elif tkns[0] in ('cl', 'clear'): c_clear(tkns, ln)
    elif tkns[0] in ('col', 'column'): c_column(tkns, ln)
    elif tkns[0] in ('comp', 'compute'): c_compute(tkns, ln)
    elif tkns[0] in ('conn', 'connect'): c_connect(tkns, ln)
    elif tkns[0] == 'copy': c_copy(tkns, ln)
    elif tkns[0] in ('def', 'define'): c_define(tkns, ln)
    elif tkns[0] in ('desc', 'describe'): c_describe(tkns, ln)
    elif tkns[0] in ('disc', 'disconnect'): c_disconnect(tkns, ln)
    elif tkns[0] in ('exec', 'execute'): c_execute(tkns, ln)
    elif tkns[0] == 'exit': c_exit(tkns, ln)
    elif tkns[0] == 'get': c_get(tkns, ln)
    elif tkns[0] == 'help': c_help(tkns, ln)
    elif tkns[0] in ('ho', 'host'): c_host(tkns, ln)
    elif tkns[0] in ('l', 'list'): c_list(tkns, ln)
    elif tkns[0] in ('passw', 'password'): c_password(tkns, ln)
    elif tkns[0] in ('pau', 'pause'): c_pause(tkns, ln)
    elif tkns[0] in ('pri', 'print'): c_print(tkns, ln)
    elif tkns[0] in ('pro', 'prompt'): c_prompt(tkns, ln)
    elif tkns[0] == 'quit': c_quit(tkns, ln)
    elif tkns[0] == 'recover': c_recover(tkns, ln)
    elif tkns[0] in ('rem', 'remark'): c_remark(tkns, ln)
    elif tkns[0] in ('repf', 'repfooter'): c_repfooter(tkns, ln)
    elif tkns[0] in ('reph', 'repheader'): c_repheader(tkns, ln)
    elif tkns[0] in ('r', 'run'): c_run(tkns, ln)
    elif tkns[0] in ('sav', 'save'): c_save(tkns, ln)
    elif tkns[0] == 'set': c_set(tkns, ln)
    elif tkns[0] in ('sho', 'show'): c_show(tkns, ln)
    elif tkns[0] == 'shutdown': c_shutdown(tkns, ln)
    elif tkns[0] in ('sp', 'spool'): c_spool(tkns, ln)
    elif tkns[0] in ('sta', 'start'): c_start(tkns, ln)
    elif tkns[0] == 'startup': c_startup(tkns, ln)
    elif tkns[0] == 'store': c_store(tkns, ln)
    elif tkns[0] in ('timi', 'timing'): c_timing(tkns, ln)
    elif tkns[0] == 'ttitle': c_ttile(tkns, ln)
    elif tkns[0] in ('undef', 'undefine'): c_undefine(tkns, ln)
    elif tkns[0] in ('var', 'variable'): c_variable(tkns, ln)
    elif tkns[0] == 'whenever': c_whenever(tkns, ln)

def c_at(tkns, ln):
  pass


def c_accept(tkns, ln):
  pass


def c_break(tkns, ln):
  pass


def c_btitle(tkns, ln):
  pass


def c_clear(tkns, ln):
  pass


def c_column(tkns, ln):
  pass


def c_compute(tkns, ln):
  pass


def c_connect(tkns, ln):
  pass


def c_copy(tkns, ln):
  pass


def c_define(tkns, ln):
  pass


def c_describe(tkns, ln):
  pass


def c_disconnect(tkns, ln):
  pass


def c_execute(tkns, ln):
  pass


def c_exit(tkns, ln):
  pass


def c_get(tkns, ln):
  pass


def c_help(tkns, ln):
  pass


def c_host(tkns, ln):
  pass


def c_list(tkns, ln):
  pass


def c_password(tkns, ln):
  pass


def c_pause(tkns, ln):
  pass


def c_print(tkns, ln):
  pass


def c_prompt(tkns, ln):
  pass


def c_quit(tkns, ln):
  pass


def c_recover(tkns, ln):
  pass


def c_remark(tkns, ln):
  pass


def c_repfooter(tkns, ln):
  pass


def c_repheader(tkns, ln):
  pass


def c_run(tkns, ln):
  pass


def c_save(tkns, ln):
  pass


def c_set(tkns, ln):
  pass


def c_show(tkns, ln):
  pass


def c_shutdown(tkns, ln):
  pass


def c_spool(tkns, ln):
  pass


def c_start(tkns, ln):
  pass


def c_startup(tkns, ln):
  pass


def c_store(tkns, ln):
  pass


def c_timing(tkns, ln):
  pass


def c_ttitle(tkns, ln):
  pass


def c_undefine(tkns, ln):
  pass


def c_variable(tkns, ln):
  pass


def c_whenever(tkns, ln):
  pass


def load_sql_file(p_f_sql):
    try:
        with open(p_f_sql) as f:
            s_sql = f.readlines()
    except Exception as e:
        print(e)
        sys.exit(1)

    s_sql = [x.rstrip() for x in s_sql]
    return s_sql


def exec_sql(p_stmt, p_line_num):
    print_sql_stmt(p_stmt, p_line_num)

    # figure out what to do by looking at the first token
    sp_stmt = p_stmt.split()
    rc = 0
    for token in sp_stmt:
        l_token = token.lower()
        if l_token == "select":
            rc = execute_sql_select(p_stmt, p_line_num)
        else:
            rc = execute_sql(p_stmt, p_line_num)

        break

    return rc


def print_sql_stmt(p_sql, p_line_num):
    print(f"{PROMPT} {p_sql.rstrip()}")


def execute_sql_select(p_stmt, p_line_num):
    try:
        result = g_con.run(p_stmt)
    except Exception as e:
        print_sql_exception(e, p_line_num)
        return False

    for row in result:
      print_row(row)

    return True


def execute_sql(p_stmt, p_line_num):
    try:
        g_con.run(p_stmt)
    except Exception as e:
        print_sql_exception(e, p_line_num)
        return False

    return True


def print_row(p_row):
    if p_row:
        print(str(p_row))


def print_empty_line():
    print("")


def print_sql_exception(e, p_line_num=0):
  print(e)
  return


def connect(p_usr, p_pwd, p_host, p_port, p_db):
  try:
    con = pg8000.native.Connection(p_usr, database=p_db, password=p_pwd, host=p_host, port=p_port)
  except Exception as e:
    con = None
    message(e, "error")

  return con


def message(p_msg, p_lvl=None):
  if p_lvl == "debug":
    msg = f"DEBUG: {p_msg}"
  elif p_lvl == "error":
    msg = f"\nERROR: {p_msg}"
  else:
    msg = p_msg

  print(msg)


# MAINLINE #####################################################

if len(sys.argv) < 2:
    print("Invalid parameters")
    sys.exit(1)

f_sql = sys.argv[1]
user = ""
passwd = ""
host = ""
portdb = ""
port = ""
db = ""

if len(sys.argv) > 1:
  arg = sys.argv[1]

  # user/password@host:port/database
  if "@" in arg:
    f_sql = ""
    arg_s = arg.split("@")
    userpass = arg_s[0]
    conn = arg_s[1]

    # user/password
    if "/" in userpass:
      up_s = userpass.split("/")
      user = up_s[0]
      passwd = up_s[1]
    else:
      user = userpass
      passwd = ""

    # @host:port/database
    if ((not ":" in conn) and (not "/" in conn)):
      host = conn
    elif ":" in conn:
      cn_s = conn.split(":")
      host = cn_s[0]
      portdb = cn_s[1]
      if "/" in portdb:
        pdb_s = portdb.split("/")
        port = pdb_s[0]
        db = pdb_s[1]
      else:
        db = portdb

## set defaults for variables not specified
if host == "":
  host = "localhost"

if port == "":
  port = "5432"

if db == "":
  db = "postgres"

if len(sys.argv) > 2:
  f_name = sys.argv[2]
  if f_name.startswith("@"):
    f_sql = f_name[1:]

message(f"f_sql: {f_sql}", "debug")
message(f" User: {user}", "debug")
message(f" Host: {host}", "debug")
message(f" Port: {port}", "debug")
message(f"   DB: {db}", "debug")

g_con = connect(user, passwd, host, port, db)

if g_con:
  main_loop()

sys.exit(0)
