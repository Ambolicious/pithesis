import socket
from socket import SHUT_RDWR

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

class PhoneBroadcast:

    def __init__(self, host=HOST, port=PORT) -> None:
        self.__host = host
        self.__port = port
        self.setup()

    def setup(self):
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__s.bind((self.__host, self.__port))
        print('Waiting for Phone...')
        self.__s.listen()
        self.__conn, self.__addr = self.__s.accept()
        print('connected on '+str(self.__addr))

        
    def sendData(self, data):
        try:
            self.__conn.send(data.encode())
        except Exception as e:
            print('Error in sendData...')
            print(str(e))
            try:
                self.__s.shutdown(SHUT_RDWR)
                self.__s.close()
                self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.__s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.__s.bind((self.__host, self.__port))
                self.__s.listen()
                self.__conn, self.__addr = self.__s.accept()
                print(str(self.__addr))
            except Exception as ee:
                pass

    def broadcast(self, data:list):
        str_data = ','.join(str(x) for x in data) + '\n'
        self.sendData(str_data)
            

