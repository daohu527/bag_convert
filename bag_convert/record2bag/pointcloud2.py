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

from std_msgs.msg import Header
from sensor_msgs.msg import PointField
from sensor_msgs import point_cloud2

from bag_convert.record2bag.header import to_header


def to_pointcloud(cyber_pointcloud):
    ros_header = Header()
    to_header(ros_header, cyber_pointcloud.header)

    # todo(zero): Need to parse "ros_pointcloud2.fields" for assignment
    points = []
    for point_xyzit in cyber_pointcloud.point:
        points.append([point_xyzit.x, point_xyzit.y, point_xyzit.z,
                       point_xyzit.intensity, point_xyzit.timestamp])

    fields = [PointField('x', 0, PointField.FLOAT32, 1),
              PointField('y', 4, PointField.FLOAT32, 1),
              PointField('z', 8, PointField.FLOAT32, 1),
              PointField('intensity', 12, PointField.UINT32, 1),
              PointField('timestamp', 16, PointField.FLOAT64, 1)]

    return point_cloud2.create_cloud(ros_header, fields, points)
