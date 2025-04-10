import os
import datetime

class File:
    def __init__(self, path):
        self.path = path

    def getMaxSizeFile(self, n):     
        files = [(file, os.path.getsize(os.path.join(self.path, file))) 
                 for file in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, file))]
         
        files.sort(key=lambda x: x[1] ,reverse=True)  # Sort files by size in descending order
        return [file[0] for file in files[:n]]    #get the top n and also only the file name

    def getLatestFiles(self, date):
        files = [file for file in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, file))]
        latest_files = []    #creating a list
        for file in files:
            modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(self.path, file)))
            if modification_time > date:
                latest_files.append(file)
        return latest_files


# Example usage:
if __name__ == "__main__":
    fs = File(".")  # Initialize the File object with the current directory


    max_files = fs.getMaxSizeFile(2)
    print("Max Size Files:", max_files)

    latest_files = fs.getLatestFiles(datetime.datetime(2018, 2, 1))
    print("Latest Files:", latest_files)
