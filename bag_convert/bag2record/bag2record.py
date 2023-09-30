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
from cyber_record.record import Record


from imu import to_imu
from localization import to_localization
from pointcloud import to_pointcloud
from sensor_image import to_image, to_compressed_image


def convert_msg(ros_msg):
  msg_type = ros_msg.__class__.__name__
  if "Imu" in msg_type:
    return to_imu(ros_msg)
  elif "Pose" in msg_type:
    return to_localization(ros_msg)  
  elif "PointCloud2" in msg_type:
    return to_pointcloud(ros_msg)
  elif "Image" in msg_type:
    return to_image(ros_msg)
  elif "CompressedImage" in msg_type:
    return to_compressed_image(ros_msg)
  else:
    return None

def convert(bag_file, record_file = "result.record"):
  bag = rosbag.Bag(bag_file)
  with Record(record_file, mode='w') as record:
    for topic, msg, t in bag.read_messages():
      logging.debug("{},{},{}".format(topic, type(msg), t))
      msg = convert_msg(msg)
      t = t.secs * (10**9) + t.nsecs
      if msg:
        record.write(topic, msg, t)
  bag.close()

if __name__ == "__main__":
  convert("../../data/b0-2014-07-11-10-58-16.bag")
