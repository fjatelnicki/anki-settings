# -*- coding: utf-8 -*-
#
# Review Heatmap Add-on for Anki
# Copyright (C)  2016-2022 Glutanimate <https://glutanimate.com>
#
# This file was automatically generated by Anki Add-on Builder v1.0.0-dev.5
# It is subject to the same licensing terms as the rest of the program
# (see the LICENSE file which accompanies this program).
#
# WARNING! All changes made in this file will be lost!

"""
Initializes generated Qt forms/resources
"""

from pathlib import Path
from aqt.qt import QDir

def initialize_qt_resources():
    QDir.addSearchPath("review_heatmap", str(Path(__file__).parent / "review_heatmap"))

initialize_qt_resources()
