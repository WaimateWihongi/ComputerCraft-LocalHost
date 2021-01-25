import tkinter
from tkinter import filedialog
from http.server import BaseHTTPRequestHandler, HTTPServer
import time, os

hostName = "localhost"
serverPort = 8080

def getFilePath():
    root = tkinter.Tk()
    root.wm_withdraw()
    path=filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select LUA Script",filetypes = (("all files","*.*"),("LUA files","*.lua")))
    root.destroy()
    return path

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(fp,'r+') as f:
            con = f.read()
        self.wfile.write(bytes(con, encoding='utf-8'))
if __name__ == "__main__":
    fp = getFilePath()
    serverPort = input("Port: ")
    print(serverPort)
    if serverPort == '' or len(serverPort) != 4 or (not serverPort.isdigit()):
        print("Invalid Port!")
        serverPort = 8080
    webServer = HTTPServer((hostName, int(serverPort)), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
