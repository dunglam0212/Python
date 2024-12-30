import json
import os

from LearnPyQtDesign.S26LearnModelViewPart1.Employee import Employee


class FileFactory:
    #path: path to serialize array of Employee
    #arrData: array of Employee
    def writeData(self, path, arrData):
        jsonString = json.dumps([item.__dict__ for item in arrData], default=str)
        jsonFile = open(path, "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    #path: path to deserialize array of Employee
    #ClassName: Employee
    def readData(self, path, ClassName):
        if os.path.isfile(path) == False:
            return []
        file = open(path, "r")
        #Reading from file:
        self.arrData = json.loads(file.read(), object_hook=lambda d: Employee(**d))
        file.close()
        return self.arrData
