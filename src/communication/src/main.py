#!/usr/bin/env python3

import rospy
import requests
import json
import sys
from std_msgs.msg import String
import time

url = "http://localhost:4242"
user_id = "0"

def request():
    rospy.init_node('basic_communication', anonymous=False)
    pub = rospy.Publisher('/task', String, queue_size=1)
        
    r = requests.post(url=url, json={"payload": " ".join(sys.argv[1:]),
                                     "user_id": user_id})
    answer = r.json().get("response")
    print("Dream answer is:", answer)

    if '#+#' in answer and not "track_object" in answer:
        answer = answer.split('#+#')[0].strip()
        print(answer)
        pub.publish(answer)
        time.sleep(1)


if __name__ == '__main__':
    request()