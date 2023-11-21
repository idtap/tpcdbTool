# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os, _pg
import subprocess

def exportShp2Sql(shp_file_name,sql_table_name):

    cmd = 'D:/PostgreSQL/10/bin/shp2pgsql.exe'
    cmd += ' -s 3857 ' + shp_file_name 
    cmd += ' ' + sql_table_name + " > temp.sql"
    os.system(cmd)
    cmd = "D:/PostgreSQL/10/bin/psql -h 127.0.0.1 -p 5432 -d tpcdb -U postgres " + ' -f temp.sql'
    os.system(cmd)
    #subprocess.call(cmd, shell=True)

if __name__ == '__main__':

    exportShp2Sql('D:/配電/EsriNapervilleElectricNetwork/Shapefiles/ElectricDistributionAssembly.shp','test1.ElectricDistributionAssembly')
    exportShp2Sql('D:/配電/EsriNapervilleElectricNetwork/Shapefiles/ElectricDistributionDevice.shp','test1.ElectricDistributionDevice')
    exportShp2Sql('D:/配電/EsriNapervilleElectricNetwork/Shapefiles/ElectricDistributionJunction.shp','test1.ElectricDistributionJunction')
    exportShp2Sql('D:/配電/EsriNapervilleElectricNetwork/Shapefiles/ElectricDistributionLine.shp','test1.ElectricDistributionLine')
    exportShp2Sql('D:/配電/EsriNapervilleElectricNetwork/Shapefiles/ElectricDistributionSubnetLine.shp','test1.ElectricDistributionSubnetLine')
    exportShp2Sql('D:/配電/EsriNapervilleElectricNetwork/Shapefiles/ServiceTerritory.shp','test1.ServiceTerritory')
    exportShp2Sql('D:/配電/EsriNapervilleElectricNetwork/Shapefiles/StructureBoundary.shp','test1.StructureBoundary')
    exportShp2Sql('D:/配電/EsriNapervilleElectricNetwork/Shapefiles/StructureJunction.shp','test1.StructureJunction')
    exportShp2Sql('D:/配電/EsriNapervilleElectricNetwork/Shapefiles/StructureLine.shp','test1.StructureLine')


