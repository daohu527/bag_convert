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

from modules.common.proto.header_pb2 import Header


def to_timestamp(ros_stamp):
  return ros_stamp.secs + (ros_stamp.nsecs / 1e9)

def to_header(ros_header):
  cyber_header = Header()
  cyber_header.sequence_num = ros_header.seq
  cyber_header.timestamp_sec = to_timestamp(ros_header.stamp)
  cyber_header.frame_id = ros_header.frame_id
  return cyber_header

def add_header(func):
  def inner(ros_msg):
    cyber_msg = func(ros_msg)
    cyber_msg.header.CopyFrom(to_header(ros_msg.header))
    return cyber_msg
  return inner
