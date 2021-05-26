from singleton import singleton
import os, json

METADATA_PATH = os.getenv('APPDATA')+"\ClarityReportingTool\meta.data"

@singleton
class MetaData ():
    def __init__(self):
        # try:
        #     with open(METADATA_PATH) as file:
        #         self._metadata = json.load(file)
        # except FileNotFoundError:
        #     try:
        #         os.mkdir("\\".join(METADATA_PATH.split("\\")[:-1]))
        #     except FileExistsError:
        #         pass
            self._metadata = self.__CreateDefault()

    def SaveSettings(self):
        with open(METADATA_PATH,"w") as file:
            file.write(json.dumps(self._metadata))


    # @property
    # def ExcelContent (self):
    #     return self._metadata["ExcelContent"]
    # @ExcelContent.setter
    # def ExcelContent (self,dic):
    #     self._metadata["ExcelContent"]=dic

    @property
    def SelectedYears (self):
        return self._metadata["SelectedYears"]
    @SelectedYears.setter
    def SelectedYears (self,dic):
        self._metadata["SelectedYears"].update(dic)

    @property
    def ReferenceTablePath (self):
        return self._metadata["FilePath"]["Reference"]
    @ReferenceTablePath.setter
    def ReferenceTablePath (self, new):
        self._metadata["FilePath"]["Reference"]=new

    @property
    def CostTablePath (self):
        return self._metadata["FilePath"]["Cost"]
    @CostTablePath.setter
    def CostTablePath (self, new):
        self._metadata["FilePath"]["Cost"]=new

    @property
    def ExcelPath (self):
        return self._metadata["FilePath"]["Final"]
    @ExcelPath.setter
    def ExcelPath (self, new):
        self._metadata["FilePath"]["Final"]=new

    def __CreateDefault(self):
        return {
        #         "ExcelContent":{
        #             "Month":{"Active":1},
        #             "Quarter":{"Active":1},
        #             "Year":{"Active":1}
        #             },
                "SelectedYears":{},
                "FilePath":{
                    "Cost":"",
                    "Reference":"",
                    "Final":""
                    }
                }