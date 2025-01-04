#!/bin/bash
# SPDX-FileCopyrightText: 2024 Yuuya Tanaka s23c1086uu@s.chibakoudai.jp
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 5 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log
cat /tmp/mypkg.log |
grep 'Listen: 10000.05'
