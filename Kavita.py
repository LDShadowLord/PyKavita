pyKavita_version = [0,0,1,3,"alpha"]
pluginName = "pyKavita"+" : "+str(pyKavita_version[0])+"."+str(pyKavita_version[1])+"."+str(pyKavita_version[2])+"."+str(pyKavita_version[3])+"-"+pyKavita_version[4]

import requests, json

class Kavita:
    def __init__(self, url, apiKey, pluginName=pluginName):
        """
        Create a Kavita item
        The 'url' argument is for a kavita API endpoint
        The 'apiKey' argument is for the users apiKey.
        The 'pluginName' argument is for overriding the default pluginName of this module.
        """
        self._url = url

        try:
            self.auth = json.loads(requests.post(self._url+"Plugin"+"/"+"authenticate"+"?apiKey="+requests.utils.quote(apiKey)+"&pluginName="+requests.utils.quote(pluginName)).text)
            self._header = {'Authorization': 'Bearer '+self.auth["token"]}
        except:
            print("Unable to authenticate, please check your apiKey and URL are correct")

    def _handle(self, response):
        if response.status_code != 200:
            if response.text == "":
                return [False]
            else:
                return [False, response.text]
            return [False, response.text]
        else:
            try:
                response.headers['Content-Type']
            except:
                response.headers['Content-Type'] = "text/plain"
            if response.headers['Content-Type'] == "application/json" or response.headers['Content-Type'] == "text/json":
                return [True, json.loads(response.text)]
            else:
                if response.text == "":
                    return [True]
                else:
                    return [True, response.text]

    # Commands in /Server/ namespace
    def serverServerInfo(self):
        """
        No Arguments Required. Returns Information about the Installation.
        """
        _command = "server-info"
        return self._handle(requests.get(self._url+"Server"+"/"+_command,headers=self._header))

    def serverBackupDB(self):
        """
        No Arguments Required. Forces a Database Backup command. Returns True if successful.
        """
        _command = "backup-db"
        return self._handle(requests.post(self._url+"Server"+"/"+_command,headers=self._header))

    def serverClearCache(self):
        """
        No Arguments Required. Clears Server cache. Returns True if successful.
        """
        _command = "clear-cache"
        return self._handle(requests.post(self._url+"Server"+"/"+_command,headers=self._header))

    # Commands in /Series/ namespace
    def seriesBaseData(self, id=0):
        """
        Returns basic data about that series.
        ID: The numeric ID for that series.
        """
        _command = 0000
        if not isinstance(id, int):
            raise TypeError("This function requires an INT object in the 'id' position.")

        return self._handle(requests.get(self._url+"Series"+"/"+str(id),headers=self._header))

    def seriesMetadata(self, id=0):
        """
        Returns metadata about that series.
        ID: The numeric ID for that series.
        """
        _command = "metadata"
        if not isinstance(id, int):
            raise TypeError("This function requires an INT object in the 'id' position.")

        return self._handle(requests.get(self._url+"Series"+"/"+_command+"?seriesID="+str(id),headers=self._header))

    def seriesScan(self, id=0, library=0):
        """
        Returns metadata about that series.
        ID: The numeric ID for that series.
        Library: The numeric ID for the container library.
        """
        _command = "scan"
        if not isinstance(id, int):
            raise TypeError("This function requires an INT object in the 'id' position.")
        if not isinstance(id, library):
            raise TypeError("This function requires an INT object in the 'library' position.")

        return self._handle(requests.post(self._url+"Series"+"/"+_command,json={"libraryID":library,"seriesId":id},headers=self._header))