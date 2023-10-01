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

from modules.drivers.proto.pointcloud_pb2 import PointCloud
from sensor_msgs import point_cloud2

from bag_convert.bag2record.header import add_header


@add_header
def to_pointcloud(ros_pointcloud2):
    cyber_pointcloud = PointCloud()

    cyber_pointcloud.height = ros_pointcloud2.height
    cyber_pointcloud.width = ros_pointcloud2.width

    # todo(zero): Need to parse "ros_pointcloud2.fields" for assignment
    for p in point_cloud2.read_points(ros_pointcloud2):
        point_xyzit = cyber_pointcloud.point.add()
        point_xyzit.x = p[0]
        point_xyzit.y = p[1]
        point_xyzit.z = p[2]
        if len(p) > 3:
            point_xyzit.intensity = p[3]
        if len(p) > 4:
            point_xyzit.timestamp = p[4]

    cyber_pointcloud.is_dense = ros_pointcloud2.is_dense
    return cyber_pointcloud
