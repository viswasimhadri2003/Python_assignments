import pkg2
import datetime

fs = pkg2.File(".")  


max_files = fs.getMaxSizeFile(2)
print("Max Size Files:", max_files)

latest_files = fs.getLatestFiles(datetime.datetime(2018, 2, 1))
print("Latest Files:", latest_files)