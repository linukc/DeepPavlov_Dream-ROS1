#!/usr/bin/env python3

import rospy
import requests
import json
import sys
from std_msgs.msg import String
import time

url = "http://0.0.0.0:8014/detect"


def map_answer_to_command(text):
    accordance = {"turn_around": "turn_360_clockwise",
                  "move_forward": "forward_1",
                  "move_backward": "backward_1",
                  "I don't know": "I don't know"}
    return accordance.get(text)

def request():
    rospy.init_node('basic_communication', anonymous=False)
    pub = rospy.Publisher('/task', String, queue_size=1)
        
    r = requests.post(url=url, json={"sentences": [[" ".join(sys.argv[1:])]]}).json()[0]
    answer = [k for k in r.keys() if (int(r.get(k).get("detected")) == 1)]
    if not answer:
        answer = "I don't know"
    else:
        answer = answer[0].strip()
    print("Dream answer is ", answer)

    time.sleep(1)
    pub.publish(map_answer_to_command(answer))


if __name__ == '__main__':
    request()