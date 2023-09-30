#!/usr/bin/env python

# Copyright 2021 daohu527 <daohu527@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rospy
from std_msgs.msg import Header


def to_header(ros_header, cyber_header):
  ros_header.seq = cyber_header.sequence_num
  ros_header.stamp = rospy.Time.from_sec(cyber_header.timestamp_sec)
  ros_header.frame_id = cyber_header.frame_id

def add_header(func):
  def inner(cyber_msg):
    ros_msg = func(cyber_msg)
    to_header(ros_msg.header, cyber_msg.header)
    return ros_msg
  return inner
