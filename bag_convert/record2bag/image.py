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

from sensor_msgs.msg import Image

from header import add_header


@add_header
def to_image(cyber_image):
    ros_image = Image()

    ros_image.height = cyber_image.height
    ros_image.width = cyber_image.width
    ros_image.encoding = cyber_image.encoding
    ros_image.step = cyber_image.step

    ros_image.data = cyber_image.data
    return ros_image
