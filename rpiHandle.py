import cv2
import easytello
import socket, pickle, struct
import RPi.GPIO
from subprocess import call

rc = call("./connectTello.sh")