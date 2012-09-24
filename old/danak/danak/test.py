import os
test = os.path.join(os.path.dirname("."), 'templates').replace('\\', '/')
print test
import datetime
import time
n=datetime.datetime(1979, 06, 07)
n.timetuple()
print time.mktime(n.timetuple())