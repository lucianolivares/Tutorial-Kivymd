from vidgear.gears import NetGear, ScreenGear, VideoGear
import cv2

# Capture Screen
stream = ScreenGear().start()

# Capture Video
#stream = VideoGear(source="resources/test.mp4").start()

# define tweak flags
options = {'flag': 0, 'copy': False, 'track': False, 'compression_param': cv2.IMREAD_COLOR}

# Definir Netgear server
server = NetGear(address="192.168.20.33", port="5454", protocol='tcp', pattern=1, logging=True, **options)

while True:
    try:
        frame = stream.read()
        if frame is None:
            break

        server.send(frame)

    except KeyboardInterrupt:
        break

server.close()
