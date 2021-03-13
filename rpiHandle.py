import cv2
import easytello
import socket, pickle, struct
import RPI.GPIO
from subprocess import call

rc = call("./connectTello.sh")