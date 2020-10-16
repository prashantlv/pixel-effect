import cv2


def pixelate(im):
    height, width = frame.shape[:2]

    w, h = (30, 30)

    temp = cv2.resize(im, (w, h), interpolation=cv2.INTER_LINEAR)
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    return output


cap = cv2.VideoCapture('motion.avi')
out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))


while(cap.isOpened()):
    ret, frame = cap.read()
    output = pixelate(frame)
    out.write(output)
    cv2.imshow('frame',output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
