# -*- coding: utf-8 -*-
import sqlite3 as db
import os
import shutil
class MySqlite3:
    
    def __init__(self, dbpath):
        self.openDb(dbpath);
    def openDb(self,dbpath):
        self.conn = db.connect(dbpath)
        self.cursor=self.conn.cursor()         
        pass
    def querry(self,exectCmd):
        self.cursor.execute(exectCmd)
        rows=self.cursor.fetchall()
        #res = cur.fetchone()
        #print('row:', cur.rowcount) 
        return rows
    def execute(self,exectCmd):
        self.cursor.execute(exectCmd)
    def executeWithObjs(self,exectCmd,objs):
        self.cursor.execute(exectCmd,objs)
    def closeDb(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
    def get_i_sql(self,table, dic):
        '''
        生成insert的sql语句
        @table，插入记录的表名
        @dict,插入的数据，字典
        '''
        sql = 'insert into %s ' % table
        subsql,objs = self.dic_2_bindArgs(dic)
        sql += subsql
        return sql,objs


    def get_s_sql(self,table, keys, conditions, isdistinct=0):
        '''
            生成select的sql语句
        @table，查询记录的表名
        @key，需要查询的字段
        @conditions,插入的数据，字典
        @isdistinct,查询的数据是否不重复
        '''
        if isdistinct:
            sql = 'select distinct %s ' % ",".join(keys)
        else:
            sql = 'select  %s ' % ",".join(keys)
        sql += ' from %s ' % table
        if conditions:
            sql += ' where %s ' % self.dict_2_str_and(conditions)
        return sql


    def get_u_sql(self,table, value, conditions):
        '''
            生成update的sql语句
        @table，查询记录的表名
        @value，dict,需要更新的字段
        @conditions,插入的数据，字典
        '''
        sql = 'update %s set ' % table
        sql += self.dict_2_str(value)
        if conditions:
            sql += ' where %s ' % self.dict_2_str_and(conditions)
        return sql


    def get_d_sql(self,table, conditions):
        '''
            生成detele的sql语句
        @table，查询记录的表名

        @conditions,插入的数据，字典
        '''
        sql = 'delete from  %s  ' % table
        if conditions:
            sql += ' where %s ' % self.dict_2_str_and(conditions)
        return sql
    def dic_2_bindArgs(self,dictin):
        '''
        将字典变成，() VALUES () 的形式
        '''
        keys = []
        values = []
        objects = []
        for k, v in dictin.items():
            keys.append(str(k))
            values.append("?")
            objects.append(v)
        return ' ('+','.join(keys) +') VALUES ('+','.join(values)+')',objects
    def dict_2_str(self,dictin):
        '''
        将字典变成，key='value',key='value' 的形式
        '''
        tmplist = []
        for k, v in dictin.items():
            tmp = "%s=\"%s\"" % (str(k), str(v))
            tmplist.append(' ' + tmp + ' ')
        return ','.join(tmplist)
    def dict_2_str_and(self,dictin):
        '''
        将字典变成，key='value' and key='value'的形式
        '''
        tmplist = []
        for k, v in dictin.items():
            tmp = "%s='%s'" % (str(k), str(v))
            tmplist.append(' ' + tmp + ' ')
        return ' and '.join(tmplist)
    def resetTable(self,tableName):
        #自增长ID为0
        try:
            sql = "delete from "+tableName +" where 1=1;";
            self.cursor.execute(sql)
            sql = "VACUUM"
            self.conn.execute(sql)
            sql = "update sqlite_sequence SET seq = 0 where name ='{0}'".format(tableName)
            self.cursor.execute(sql)
        except:
            pass
    def commit(self):
        self.conn.commit()

# if __name__=="__main__":
#     downloadpath="D:/pythonDownload/vesali.db"
#     if not os.path.isfile(downloadpath):
#         shutil.copyfile("C:/Users/Administrator/AppData/LocalLow/Vesal/ruanyikeji_vesal_vesal/db/vesali.db",downloadpath)
#     localDb = MySqlite3(downloadpath)
#     alltablesql = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
#     rows = localDb.querry(alltablesql)
#     for row in rows:
#         localDb.resetTable(row[0])
#     sql = "select * from CommonAssetLib"
#     rows = localDb.querry(sql)
#     #pc
#     #ios
#     #android
#     for row in rows:
#         if row[5] == "android":
#             print(row[2])
#     localDb.closeDb()

if __name__ == '__main__':
    workPath = "D:/pythonWorkSpaces/pythonlib/MyPythonLib/Util/datas/cameraParms/"
    os.chdir(workPath)
    localDb_pos = MySqlite3(workPath+"SignNewJG.db")
    localDb_main = MySqlite3(workPath+"SignNewJG_main.db")
    sql = "SELECT sm_name,camera_params FROM SignNewInfo"
    rows = localDb_pos.querry(sql)
    for row in rows:
        sql = "update SignNewInfo set camera_params = ? where sm_name = ?"
        objs = []
        objs.append(row[1])
        objs.append(row[0])
        localDb_main.executeWithObjs(sql,objs)
    print("down.")
    localDb_pos.closeDb()
    localDb_main.commit()
    localDb_main.closeDb()