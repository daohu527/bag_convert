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


from geometry_msgs.msg import Pose

from header import add_header


def to_pose(cyber_localization):
    ros_pose = Pose()

    pose = cyber_localization.pose
    ros_pose.position.x = pose.position.x
    ros_pose.position.y = pose.position.y
    ros_pose.position.z = pose.position.z

    ros_pose.orientation.x = pose.orientation.qx
    ros_pose.orientation.y = pose.orientation.qy
    ros_pose.orientation.z = pose.orientation.qz
    ros_pose.orientation.w = pose.orientation.qw
    return ros_pose
