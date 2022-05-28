# sends frames to virtual Python cam

import pyvirtualcam
import numpy as np

with pyvirtualcam.Camera(width=1280, height=720, fps=20) as cam:
    print(f'Using virtual camera: {cam.device}')
    frame = np.zeros((cam.height, cam.width, 3), np.uint8)  # RGB
    while True:
        frame[:] = cam.frames_sent % 255  # grayscale animation
        cam.send(frame)
        cam.sleep_until_next_frame()

# frame height and width, target frame rate, print_fps can print frame rate every second
class pyvirtualcam.Camera(width, height, fps, *, fmt=PixelFormat.RGB, device=None, backend=None, print_fps=False)

send(frame)