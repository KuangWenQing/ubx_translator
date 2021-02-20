from ubxtranslator.core import Parser
from ubxtranslator.predefined import RXM_CLS

path_file = "./F9P_log/COM7_210219_074646_F9P.ubx"

parser = Parser([RXM_CLS, ])

fd = open(path_file, 'rb')

print(fd.seek(0, 2))
fd.seek(0, 0)
print(fd.tell())
print(type(fd))

while True:
    msg = parser.receive_from(fd)
    if msg == 0:
        break
    elif msg is not None:
        print(msg)


