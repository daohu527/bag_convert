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

from modules.localization.proto.imu_pb2 import CorrectedImu

from header import add_header


@add_header
def to_imu(ros_imu):
  cyber_imu = CorrectedImu()

  pose = cyber_imu.imu
  pose.orientation.qx = ros_imu.orientation.x
  pose.orientation.qy = ros_imu.orientation.y
  pose.orientation.qz = ros_imu.orientation.z
  pose.orientation.qw = ros_imu.orientation.w

  pose.angular_velocity.x = ros_imu.angular_velocity.x
  pose.angular_velocity.y = ros_imu.angular_velocity.y
  pose.angular_velocity.z = ros_imu.angular_velocity.z

  pose.linear_acceleration.x = ros_imu.linear_acceleration.x
  pose.linear_acceleration.y = ros_imu.linear_acceleration.y
  pose.linear_acceleration.z = ros_imu.linear_acceleration.z
  return cyber_imu
