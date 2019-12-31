Dependencies

firebase: pip install firebase_admin
tkinter : pip install tkinter
pytz	: pip install pytz


---------------------------------------------------------------------------
for runing machine learning component
---------------------------------------------------------------------------

Installing the requirements

1) Start your terminal of cmd depending on your os and change directory to Attendance-using-Face folder.

2) If you have a NVidia GPU then make sure you have the prerequisites for Tensorflow GPU installation (Refer to official site). Then use this commmand

 pip install -r requirements_gpu.txt

3) In case you do not have a GPU then use this command

 pip install -r requirements_cpu.txt



Run

1) type following command to run entry detection script

python recognizer.py


2) type following command to run exit detection script

python recognizerexit.py

using these steps model will work for already trained individuals if your internet connection is working
firebase database will be updated automatically.

-------------------------------------------------------------------------------------
for running web server
-------------------------------------------------------------------------------------

1) agian Open other terminal and change directory to web 

2) type command "python manage.py runserver"
	it will show a local host address
3) go to web browser and type that local host address