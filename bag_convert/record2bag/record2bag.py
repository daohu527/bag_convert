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

import logging

import rosbag
import rospy
from cyber_record.record import Record


from compressed_image import to_compressed_image
from image import to_image
from imu import to_imu
from pointcloud2 import to_pointcloud
from pose import to_pose


def convert_msg(cyber_msg):
  msg_type = cyber_msg.__class__.__name__
  if "CorrectedImu" in msg_type:
    return to_imu(cyber_msg)
  elif "LocalizationEstimate" in msg_type:
    return to_pose(cyber_msg)  
  elif "PointCloud" in msg_type:
    return to_pointcloud(cyber_msg)
  elif "Image" in msg_type:
    return to_image(cyber_msg)
  elif "CompressedImage" in msg_type:
    return to_compressed_image(cyber_msg)
  else:
    return None

def convert(record_file, bag_file = "result.bag"):
  record = Record(record_file)
  with rosbag.Bag(bag_file, 'w') as bag:
    for topic, msg, t in record.read_messages():
      logging.debug("{},{},{}".format(topic, type(msg), t))
      msg = convert_msg(msg)
      t = rospy.Time.from_sec(t / (10**9))
      if msg:
        bag.write(topic, msg, t)
  record.close()

if __name__ == "__main__":
  convert("../../data/demo_sensor_data_for_vision.record")
