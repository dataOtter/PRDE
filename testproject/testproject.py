from CommonREST import *
import constants as c

if __name__ == "__main__":
    print("THIS IS A NEW VERSION")
    DOWNLOAD_FILES_PATH = "/home/user/PRDE/testproject/outputs/"
    c.DOWNLOAD_FILES_PATH = DOWNLOAD_FILES_PATH
    app.run(debug=True, host="192.168.1.10")
