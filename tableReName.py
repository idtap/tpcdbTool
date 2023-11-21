# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os, _pg

def get_rename_cmd_list(db) :

    cmdList = []

    sel = "select f_table_name,f_geometry_column,f_table_schema from geometry_columns;"
    sel = conn.query(sel)
    result = sel.getresult()
    ct = len(result)       
    if ct > 1:
        for row in result:
            old_name = str(row[2]) + '."' + str(row[0]) + '"'
            new_name = str(row[2]) + '."' + str(row[0]).replace('-','') + '"'
            if old_name != new_name :
                new_name = '"'+str(row[0]).replace('-','')+'"'
                cmd = 'ALTER TABLE IF EXISTS '+old_name
                cmd += ' RENAME TO '+new_name+' ;'
                cmdList.append(cmd)

    return cmdList


if __name__ == '__main__':

    # PostGIS 資料庫 connect
    host = "127.0.0.1"
    username = "postgres"
    password = "`1QAZSE45"
    db = "tpcdb"

    # connect
    conn = _pg.connect(dbname = db, host= host, port= 5432, user = username, passwd= password)
    cmd_list = get_rename_cmd_list(db)
    for cmd in cmd_list:
        print(cmd)
        conn.query(cmd)

