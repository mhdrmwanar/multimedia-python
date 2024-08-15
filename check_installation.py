import pygame
import PIL
import cv2
import moviepy.editor as mp
import pydub
import tkinter as tk

def check_installation():
    print("✅ Pygame version:", pygame.__version__)
    print("✅ Pillow version:", PIL.__version__)
    print("✅ OpenCV version:", cv2.__version__)
    print("✅ MoviePy version:", mp.__version__)
    print("✅ Pydub version:", pydub.__version__)
    print("✅ Tkinter is installed and working!")

if __name__ == "__main__":
    check_installation()