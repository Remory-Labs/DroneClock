import cv2
import socket, pickle, struct

socket_address = ("192.168.0.109", 5000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(socket_address)
server_socket.listen(5)
print("Server up and running.")

while True:
    client_socket, address = server_socket.accept()
    print("Computer connected.")

    if client_socket:
        camera = cv2.VideoCapture(0)

        while(camera.isOpened()):
            _, frame = camera.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            client_socket.sendall(message)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()