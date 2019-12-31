import firebase_admin
from firebase_admin import credentials, firestore
import datetime
import pytz

cred = credentials.Certificate("se-project-ffa20-firebase-adminsdk-op4y5-c5904a7846.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()


'''
Name of Programmer: Sabir
Job: Marks attendance of emloyee (with time employee enters the building) on firebase database
Possible Failure : As database is online good internet connection is required otherwise it will
						generate entry failure error.
'''
def markAttend(id,dayIn,monIn,yearIn,minIn,hourIn,dayOut,monOut,yearOut,minOut,hourOut):

    doc_ref = db.collection(u'Employees').where("eid","==",id)

    us=doc_ref.get()
    cond = 0
    obj={}
    for item in us:
        obj = item.to_dict()
        cond = 1
    if(cond == 0):
	    return -1;

    doc_ref = db.collection(u'Employees').document(str(id)).collection(u'Attendance')
    local_tz = pytz.timezone('Asia/Karachi')

    entryDay = datetime.date(1, 1, 1)
    entryTime= datetime.time(0,0,0)
    dt = datetime.datetime.combine(entryDay, entryTime)
    dt = dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    local_tz.normalize(dt)

    dt=dt.replace(day=dayIn)
    dt=dt.replace(month=monIn)
    dt=dt.replace(year=yearIn)
    dt=dt.replace(minute=minIn)
    dt=dt.replace(hour=hourIn)


    local_dt = dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    local_tz.normalize(local_dt)

    local_dt=local_dt.replace(day=10)

    local_dt=local_dt.replace(day=dayIn)
    local_dt=local_dt.replace(month=monIn)
    local_dt=local_dt.replace(year=yearIn)
    local_dt=local_dt.replace(minute=minIn)
    local_dt=local_dt.replace(hour=hourIn)

    print(local_dt)





    exitDay = datetime.date(1, 1, 1)
    exitTime= datetime.time(0,0,0)
    dt2 = datetime.datetime.combine(exitDay, exitTime)
    dt2 = dt2.replace(tzinfo=pytz.utc).astimezone(local_tz)	
    local_tz.normalize(dt2)
	
	

    dt2=dt2.replace(day=dayOut)
    dt2=dt2.replace(month=monOut)
    dt2=dt2.replace(year=yearOut)
    dt2=dt2.replace(minute=minOut)
    dt2=dt2.replace(hour=hourOut)
	



    local_dt2 = dt2.replace(tzinfo=pytz.utc).astimezone(local_tz)
    local_tz.normalize(local_dt2)

    local_dt2=local_dt2.replace(day=10)

    local_dt2=local_dt2.replace(day=dayOut)
    local_dt2=local_dt2.replace(month=monOut)
    local_dt2=local_dt2.replace(year=yearOut)
    local_dt2=local_dt2.replace(minute=minOut)
    local_dt2=local_dt2.replace(hour=hourOut)

    print(local_dt)
    print(local_dt2)
	
    attendance={}
    attendance['time_in']=local_dt
    attendance['time_out']=local_dt2


    print(doc_ref.add(attendance));	
	
    return 1

'''
Name of Programmer: Sabir
Job: Marks attendance of emloyee (with time employee exits the building) on firebase database
Possible Failure : As database is online good internet connection is required otherwise it will
						generate entry failure error.
'''	
def markEnd(id,dayOut,monOut,yearOut,minOut,hourOut):

    doc_ref = db.collection(u'Employees').where("eid","==",id)

    us=doc_ref.get()
    cond = 0
    obj={}
    for item in us:
        obj = item.to_dict()
        cond=1
    if(cond == 0):
        return -1;

    doc_ref = db.collection(u'Employees').document(str(id)).collection(u'Attendance').order_by(u'time_in', direction=firestore.Query.DESCENDING).limit(1).get()
    local_tz = pytz.timezone('Asia/Karachi')


    exitDay = datetime.date(1, 1, 1)
    exitTime= datetime.time(0,0,0)
    dt2 = datetime.datetime.combine(exitDay, exitTime)
    dt2 = dt2.replace(tzinfo=pytz.utc).astimezone(local_tz)	
    local_tz.normalize(dt2)
	
	

    dt2=dt2.replace(day=dayOut)
    dt2=dt2.replace(month=monOut)
    dt2=dt2.replace(year=yearOut)
    dt2=dt2.replace(minute=minOut)
    dt2=dt2.replace(hour=hourOut)
	

    local_dt2 = dt2.replace(tzinfo=pytz.utc).astimezone(local_tz)
    local_tz.normalize(local_dt2)

    local_dt2=local_dt2.replace(day=10)

    local_dt2=local_dt2.replace(day=dayOut)
    local_dt2=local_dt2.replace(month=monOut)
    local_dt2=local_dt2.replace(year=yearOut)
    local_dt2=local_dt2.replace(minute=minOut)
    local_dt2=local_dt2.replace(hour=hourOut)

	#print(local_dt2)
	
    attendance={}
    attendance['time_out']=local_dt2


    for item in doc_ref:	

        db.collection(u'Employees').document(str(id)).collection(u'Attendance').document(str(item.id)).update({u'time_out':local_dt2})

    return 1

#print(markAttend(1,20,11,2018,30,1,20,11,2018,50,2))




