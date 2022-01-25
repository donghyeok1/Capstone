import cv2
import mediapipe as mp
import numpy as np
import time, os

directory="."
scaler = 0.5
actions = ['rewind','advance','stop']
seq_length=45

# MediaPipe hands model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
created_time=int(time.time())
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

for idx_dir, subdir in enumerate(actions):
    action = subdir
    subdir = directory + "/" + subdir
    listdir = os.listdir(subdir)
    print(listdir)
    data = []
    for idx_mov, mov in enumerate(listdir):
        vfile = cv2.VideoCapture(subdir + "/" + mov)
        if vfile.isOpened():
            while True:
                vret, img = vfile.read()
                if vret:
                    img = cv2.resize(img,(int(img.shape[1] * scaler),int(img.shape[0] * scaler)))
                    img = cv2.flip(img,1)
                    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                    result = hands.process(img)
                    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
                    if result.multi_hand_landmarks is not None:
                        for res in result.multi_hand_landmarks:
                            if False:    
                                print(1)
                            mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)
                            joint = np.zeros((21,4))
                            for j, lm in enumerate(res.landmark):
                                joint[j] = [lm.x, lm.y, lm.z, lm.visibility]
                            # Compute angles between joints
                            v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19], :3] # Parent joint
                            v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], :3] # Child joint
                            v = v2 - v1 # [20, 3]
                            # Normalize v
                            v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

                            # Get angle using arcos of dot product
                            angle = np.arccos(np.einsum('nt,nt->n',
                                v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                                v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

                            angle = np.degrees(angle) # Convert radian to degree

                            angle_label = np.array([angle], dtype=np.float32)
                            angle_label = np.append(angle_label, idx_dir)

                            d = np.concatenate([joint.flatten(), angle_label])

                            data.append(d)
                    #if result.multi_hand_landmarks is not None:
                        #mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)
                    cv2.imshow('img',img)
                    cv2.waitKey(1)
                else:
                    break
        else:
            print("파일을 열 수 없습니다.")
        vfile.release()
        cv2.destroyAllWindows()
    data=np.array(data)
    np.save(os.path.join('dataset',f'raw_{action}1'),data)
    full_seq_data=[]
    for seq in range(len(data)-seq_length):
        full_seq_data.append(data[seq:seq + seq_length])
    full_seq_data=np.array(full_seq_data)
    print(subdir,full_seq_data.shape)
    np.save(os.path.join('dataset',f'seq_{action}1'),full_seq_data)