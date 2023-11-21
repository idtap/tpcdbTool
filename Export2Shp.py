# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os, _pg

def get_export_cmd_list(db) :

    cmdList = []

    sel = "select f_table_name,f_geometry_column,f_table_schema from geometry_columns;"
    sel = conn.query(sel)
    result = sel.getresult()
    #result = sel.namedresult()
    #result = sel.dictresult()
    ct = len(result)       
    if ct > 1:
        for row in result:
            #print(str(row[0]))
            cmd = "D:/PostgreSQL/10/bin/pgsql2shp.exe"
            cmd += " -f "+export_path+str(row[0]).replace('-','')+'_' + str(row[1]) + ".shp" 
            cmd += " -h "+ host
            cmd += " -u "+ username
            cmd += " -P "+ password
            cmd += " -p 5432 " + db
            cmd += ' "' + str(row[2]) + '"."' + str(row[0]) + '"'
            cmdList.append(cmd)

    return cmdList


if __name__ == '__main__':

    # 輸出路徑
    export_path = "D:/配電/tpcdb2shp/outputShp/"

    # PostGIS 資料庫 connect
    host = "127.0.0.1"
    username = "postgres"
    password = "`1QAZSE45"
    db = "tpcdb"

    # connect
    conn = _pg.connect(dbname = db, host= host, port= 5432, user = username, passwd= password)
    
    # 由 public.geometry_columns 表格取得各有 geom 欄的表格，並直接組合 pgsql2shp 指令執行
    cmd_list = get_export_cmd_list(db)

    for cmd in cmd_list:
        print( cmd )
        os.system(cmd)

