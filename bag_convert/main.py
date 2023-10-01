# -*- coding: utf-8 -*-
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

import argparse
import logging
import sys
from pathlib import Path

import bag_convert.bag2record.bag2record as bag2record
import bag_convert.record2bag.record2bag as record2bag


def main(args=sys.argv):
    parser = argparse.ArgumentParser(
        description="bag_convert is a tool to convert rosbag to record or reverse.",
        prog="main.py")

    parser.add_argument(
        "-m", "--mode", action="store", type=str, required=False,
        help="conversion method")
    parser.add_argument(
        "-b", "--bag_file", action="store", type=str, required=False,
        help="Ros bag file path")
    parser.add_argument(
        "-r", "--record_file", action="store", type=str, required=False,
        help="Cyber record file path")

    args = parser.parse_args(args[1:])

    # 1. Check if parameters are valid
    bag_file = Path(args.bag_file)
    record_file = Path(args.record_file)
    if not bag_file.is_file():
        logging.error("File not exist! '{}'".format(args.bag_file))
    if not record_file.is_file():
        logging.error("File not exist! '{}'".format(args.record_file))

    # 2. conversion package
    if args.mode == 'b2r':
        bag2record.convert(bag_file, record_file)
    elif args.mode == 'r2b':
        record2bag.convert(record_file, bag_file)
    else:
        logging.error("Mode not exist! '{}'".format(args.mode))
