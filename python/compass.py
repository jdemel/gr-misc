#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2013 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
from QwtCompassWidget import *
from PyQt4 import QtCore, QtGui, Qt, Qwt5

class compass(gr.sync_block, Qt.QWidget):
    """
    Qt Compass for direction indication.
    """
    def __init__(self, use_radians, needle_style, needle_type, number_rate):
        gr.sync_block.__init__(self,
            name="compass",
            in_sig=[numpy.float32],
            out_sig=None)

        print use_radians, needle_style, needle_type
        self.use_radians = use_radians
        if needle_style == "nice":
            self.needle_style = 0
        if needle_style == "simple":
            self.needle_style = 1
        else:
            self.needle_style = 0
        #needle_type = "simple" # magnet or simple
        #needle_style = 1 # 0: nice, 1: simple

        # Set up GUI Widget
        QtGui.QWidget.__init__(self)
        self.ui = Ui_QwtCompassWidget()
        self.ui.setupUi(self)

        #rose = Qwt5.QwtRoundScaleDraw()
        #self.ui.Compass.setRose(rose)

        # set compasss needle
        needle = None
        if needle_type == "magnet":
            needle = Qwt5.QwtCompassMagnetNeedle(self.needle_style)
        else:
            needle = Qwt5.QwtDialSimpleNeedle(self.needle_style)
        self.ui.Compass.setNeedle(needle)


        self.last_update = 0
        self.update_res = 0
        self.number_rate = 0
        self.set_number_rate(number_rate)

    def get_pyqwidget(self):
        return self

    def setCompassValue(self, val):
        self.emit(QtCore.SIGNAL("setCompassValue(double)"), val)

    def set_number_rate(self, rate):
        self.number_rate = rate
        self.update_res = gr.high_res_timer_tps() * (1.0 / rate)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        for i in range(len(in0)):
            time = gr.high_res_timer_now()
            if time > self.last_update + self.update_res:
                self.setCompassValue(in0[i])
                self.last_update = gr.high_res_timer_now()

        return len(input_items[0])



