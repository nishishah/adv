from flask import Flask, render_template, request
from datetime import datetime
from json import loads, dumps
import pypyodbc
# import pandas as pd
import random
import time
import redis
import hashlib
# from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='', template_folder='static') 

server = 'nishishah3.database.windows.net'
database = 'Q3'
username = 'nishishah'
password = 'Ilovemyself@19'
driver= '{ODBC Driver 17 for SQL Server}'
# cnxn = pypyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

myHostname = "nishishah.redis.cache.windows.net"
myPassword = "8TEP0CYKZDavcU6RiQUvrD1uKqxQejjHt+qmQDusMx0="

r = redis.StrictRedis(host=myHostname, port=6380,password=myPassword,ssl=True)

@app.route('/')
def hello_world():
    conn = pypyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    lstDictionaryData = []
    cursor = conn.cursor()
    startTime = time.time()
    query = "SELECT TOP 10 time, latitude, longitude, mag, place FROM Quakes6"
    # print(query)
    cursor.execute(query)
    # print(tmp)
    endTime = time.time()
    row = cursor.fetchone()
    while row:
        lstDictionaryData.append(row)
        # print("hi!" + str(row))
        row = cursor.fetchone()
    # return "hello!!"
    conn.close()
    executionTime = (endTime - startTime) * 1000
    return render_template('index.html', tableData=lstDictionaryData, tableDataLen=lstDictionaryData.__len__(), executionTime=executionTime)

# @app.route('/createtable')
# def createTable():
#     lstDictionaryData = []
#     conn = pypyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
#     cursor = conn.cursor()
#     # query = "CREATE TABLE dbo.all_month (\"time\" datetime, \"latitude\" FLOAT, \"longitude\" FLOAT, \"depth\" FLOAT, \"mag\" FLOAT, \"magType\" TEXT, \"nst\" INT, \"gap\" INT, \"dmin\" FLOAT, \"rms\" FLOAT, \"net\" TEXT, \"id\" TEXT, \"updated\" datetime, \"place\" TEXT, \"type\" TEXT, \"horontalError\" FLOAT, \"depthError\" FLOAT, \"magError\" FLOAT, \"magNst\" INT, \"status\" TEXT, \"locationSource\" TEXT, \"magSource\" TEXT)"
#     query = "CREATE TABLE cloudsqldb.dbo.all_month(time DATETIME,latitude FLOAT,longitude FLOAT,depth FLOAT,mag FLOAT,magType TEXT,nst INT,gap INT,dmin FLOAT,rms FLOAT,net TEXT,id TEXT,updated DATETIME,place TEXT,type TEXT,horontalError FLOAT,depthError FLOAT,magError FLOAT,magNst INT,status TEXT,locationSource TEXT,magSource TEXT)"
#     # print(query)
#     startTime = time.time()
#     # cursor.execute(query)
#     cursor.execdirect(query)
#     cursor.execdirect("CREATE INDEX all_month_mag__index ON cloudsqldb.dbo.earthquake (mag)")
#     cursor.execdirect("CREATE INDEX all_month_lat__index ON cloudsqldb.dbo.earthquake (latitude)")
#     cursor.execdirect("CREATE INDEX all_month_long__index ON cloudsqldb.dbo.earthquake (longitude)")
#     endTime = time.time()
#     conn.close()
#     executionTime = (endTime - startTime) * 1000
#     return render_template('index.html', tableData=lstDictionaryData, tableDataLen=lstDictionaryData.__len__(), executionTime=executionTime)

@app.route('/Q5')
def Q_5():
    d1 = float(request.args.get('d1', ''))
    d2 = float(request.args.get('d2', ''))
    long1 = float(request.args.get('long', ''))
    conn = pypyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    lstDictionaryData = []
    cursor = conn.cursor()
    startTime = time.time()
    query = "SELECT \"time\", \"latitude\", \"longitude\", \"depthError\" FROM Quakes6 WHERE \"depthError\" BETWEEN '" + str(d1) + "' AND '"+ str(d2) +"' AND \"longitude\" > '"+ str(long1) +"'"
    # print(query)
    cursor.execute(query)
    # print(tmp)
    endTime = time.time()
    row = cursor.fetchone()
    while row:
        lstDictionaryData.append(row)
        # print("hi!" + str(row))
        row = cursor.fetchone()
    # return "hello!!"
    conn.close()
    executionTime = (endTime - startTime) * 1000
    return render_template('index.html', tableData=lstDictionaryData, tableDataLen=lstDictionaryData.__len__(), executionTime=executionTime)


@app.route('/Q6')
def randomQueries():
    noOfQueries = int(request.args.get('num', ''))
    # withCache = int(request.args.get('withCache', ''))
    # magnitudeStart = float(request.args.get('magnitudeStart', ''))
    # magnitudeEnd = float(request.args.get('magnitudeEnd', ''))
    d1 = float(request.args.get('d11', ''))
    d2 = float(request.args.get('d22', ''))

    lstDictionaryData = []
    lstDictionaryDataDisplay = []

    conn = pypyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = conn.cursor()
    totalExecutionTime = 0
    columns = ['time', 'latitude', 'longitude', 'place', 'mag']

    # # without cache
    # # if withCache == 0:
    #     # print("hi!")

    # drand = random.uniform(d1, d2)
    # startTime = time.time()
    # query = "SELECT \"time\", \"latitude\", \"longitude\", \"depthError\" FROM Quakes6 WHERE \"depthError\" = '" + str(drand) + "'"
    # cursor.execute(query)
    # endTime = time.time()
    #     # print(query)
    # lstDictionaryDataDisplay = cursor.fetchall()
    #     # print(lstDictionaryDataDisplay)
    # executionTime = (endTime - startTime) * 1000
    # firstExecutionTime = executionTime

    # for i in range(noOfQueries-1):
    #     totalExecutionTime = totalExecutionTime + executionTime
    #     ddrand = random.uniform(d1, d2)
    #     startTime = time.time()
    #     query = "SELECT \"time\", \"latitude\", \"longitude\", \"depthError\" FROM Quakes6 WHERE \"depthError\" = '" + str(ddrand) + "'"
    #     cursor.execute(query)
    #     endTime = time.time()
    #     lstDictionaryData = list(cursor.fetchall())
    #     lstDictionaryDataDisplay = lstDictionaryData
  

    #     memData = []
    #     for row in lstDictionaryData:
    #         memDataDict = dict()
    #         for i, val in enumerate(row):
    #             if type(val) == datetime:
    #                 val = time.mktime(val.timetuple())
    #             memDataDict[columns[i]] = val
    #         memData.append(memDataDict)
    #     r.set(query, dumps(memData))

    #     executionTime = (endTime - startTime) * 1000
           
    
    for i in range(noOfQueries):
        magnitude_value = round(random.uniform(1, 10), 2)
        query = "SELECT \"time\", \"latitude\", \"longitude\", \"depthError\" FROM Quakes6 WHERE \"depthError\" = '" + str(ddrand) + "'"
            # print("inside else")
        memhash = hashlib.sha256(query.encode()).hexdigest()
        startTime = time.time()
        lstDictionaryData = r.get(memhash)

            # print(lstDictionaryData[0])
            # print(i)
        if not lstDictionaryData:
                # print("from db")

            cursor.execute(query)
            lstDictionaryData = cursor.fetchall()
            if i == 0:
                    # print("from db")
                lstDictionaryDataDisplay = lstDictionaryData
            endTime = time.time()
            memData = []
            for row in lstDictionaryData:
                memDataDict = dict()
                for i, val in enumerate(row):
                    if type(val) == datetime:
                        val = time.mktime(val.timetuple())
                    memDataDict[columns[i]] = val
                memData.append(memDataDict)
            r.set(memhash, dumps(memData))
        else:
            lstDictionaryData = loads(lstDictionaryData.decode())
            if i == 0:
                lstDictionaryDataDisplay = lstDictionaryData
            endTime = time.time()
        executionTime = (endTime - startTime) * 1000
            # if i == 0:
            #     firstExecutionTime = executionTime
        totalExecutionTime = totalExecutionTime + executionTime
    conn.close()
    # print(lstDictionaryData)
    return render_template('index.html', tableData=lstDictionaryDataDisplay, tableDataLen=lstDictionaryDataDisplay.__len__(), executionTime=totalExecutionTime)


# @app.route('/upload_  data', methods=['POST'])
# def upload():
#     sqlquery = 'Insert into "all_month" ({columns}) values ({values})'
#     tempfile = request.files['files']
#     filename = 'tempcsv'
#     tempfile.save(os.path.join(filename))
#
#     csv_file = open(filename, 'r')
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         cols = '"' + '","'.join(row.keys()) + '"'
#         vals = '\'' + '\',\''.join(row.values()) + '\''
#         q = sqlquery.format(columns=cols, values=vals)
#         print("QUERy:", q)
#         cursor = database.connection.cursor()
#         cursor.execute(q)
#     csv_file.close()

# @app.route('/uploaddata')
# def uploadData():
#     return render_template('index.html', tableData=lstDictionaryData, tableDataLen=lstDictionaryData.__len__())

if __name__ == '__main__':
  app.run(debug=True)
