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
from QtNumberSinkWidget import *
from PyQt4 import Qt, QtGui, QtCore


class numbersink(gr.sync_block, Qt.QWidget):
    """
    Qt sink to display numbers.
    """
    def __init__(self, type, title, units, samp_rate, minval, maxval, factor, decimal_places, ref_level, number_rate, average, avg_alpha, label, peak_hold, show_gauge):
        # Call init for Qt
        QtGui.QWidget.__init__(self)

        # determine actual type
        if type == complex:
            sig = numpy.complex64
        else:
            sig = numpy.float32

        # Call init for sync block
        gr.sync_block.__init__(self,
            name="numbersink",
            in_sig=[sig],
            out_sig=None)

        # create class members for all parameters
        self.type = type
        self.title = title
        self.units = units
        self.samp_rate = samp_rate
        self.factor = factor
        self.decimal_places = decimal_places
        self.ref_level = ref_level
        self.number_rate = number_rate

        # members which are set later
        self.average = False
        self.avg_alpha = 0.0
        self.peak_hold = False
        self.minval = 0
        self.maxval = 100
        self.peak_hold = False
        self.show_gauge = False

        # members calculated for later use
        self.update_res = gr.high_res_timer_tps() * (1.0 / self.number_rate)
        self.last_update = 0
        self.update_samps = int(self.samp_rate)
        self.hold = False

        #self.nsamps_read = 0
        self.avgval = 0
        #self.label = label
        self.peakval = 0


        self.bar_expand = 1

        # Create QtWidget. Hold it as a class member to make things more clear.
        self.ui = Ui_NumberSinkWidget()
        self.ui.setupUi(self)

        # These functions rely on an existing UI
        self.setAverage(average)
        self.setAvgAlpha(avg_alpha)
        self.setPeakHold(peak_hold)
        self.setBarRange(minval, maxval)
        self.setShowGauge(show_gauge)
        self.setWidgetTitle(title)

    def get_pyqwidget(self):
        # return self, to be added to the GUI.
        return self

    def setWidgetTitle(self, text):
        # There seems to be no slot for setTitle. At least not in Qt Designer.
        self.ui.groupBox_data.setTitle(self.title)

    def setShowGauge(self, show_gauge):
        self.show_gauge = show_gauge
        if self.type == complex:
            self.setBarVisible(show_gauge, show_gauge)
        else:
            self.setBarVisible(show_gauge, False)

    def setBarVisible(self, realbar, imagbar):
        self.emit(QtCore.SIGNAL("setRealBarVisible(bool)"), realbar)
        self.emit(QtCore.SIGNAL("setImagBarVisible(bool)"), imagbar)

    def setBarRange(self, min, max):
        self.minval = min
        self.maxval = max
        if max-min < 100:
            self.bar_expand = 100
        elif max-min < 1000:
            self.bar_expand = 10
        else:
            self.bar_expand = 1
        self.emit(QtCore.SIGNAL("setBarRange(int,int)"), min * self.bar_expand, max * self.bar_expand)

    def setPeakHold(self, ena):
        self.peak_hold = ena
        self.emit(QtCore.SIGNAL("setPeakHold(bool)"), ena)

    def setAverage(self, ena):
        self.average = ena
        self.emit(QtCore.SIGNAL("setAverage(bool)"), ena)

    def setAvgAlpha(self, alpha):
        value = int(alpha * self.ui.horizontalSlider_avg.maximum())
        self.setSliderValue(value)
        self.valueChangedFrac(value)

    def setSliderValue(self, val):
        self.emit(QtCore.SIGNAL("setSliderValue(int)"), val)

    def valueChangedFrac(self, val):
        frac = val / (1.0 * self.ui.horizontalSlider_avg.maximum())
        self.avg_alpha = frac
        self.displayLcdNumberAvgValue(frac)

    def displayLcdNumberAvgValue(self, val):
        self.emit(QtCore.SIGNAL("displayLcdNumberAvgValue(double)"), val)

    def buttonHoldClicked(self, ena):
        if self.ui.pushButton_hold.text() == "Stop":
            self.setButtonHoldText("Run")
            self.hold = True
        else:
            self.setButtonHoldText("Stop")
            self.hold = False

    def setButtonHoldText(self, text):
        txt = QtCore.QString(text)
        self.ui.pushButton_hold.setText(txt)
        # Q PushButton doesn't have a setText slot. Thus we can't set its text like this.
        #self.emit(QtCore.SIGNAL("setButtonHoldText(QString)"), txt)

    def activateAverage(self, ena):
        self.average = ena

    def activatePeakHold(self, ena):
        self.peak_hold = ena

    def setValue(self, val):
        self.setValueText(val)
        if self.type == complex:
            self.setRealBar(val.real)
            self.setImagBar(val.imag)
        else:
            self.setRealBar(val)

    def formatValueString(self, val):
        if self.type == complex:
            text = "{0:+." + str(self.decimal_places) + "f}{1:+." + str(self.decimal_places) + "f} " + self.units
            text = text.format(val.real, val.imag)
        else:
            text = "{0:+." + str(self.decimal_places) + "f} " + self.units
            text = text.format(val)
        return QtCore.QString(text)

    def setValueText(self, val):
        text = self.formatValueString(val)
        self.emit(QtCore.SIGNAL("setValueText(QString)"), text)

    def setRealBar(self, val):
        self.emit(QtCore.SIGNAL("setRealBar(int)"), int(val * self.bar_expand))

    def setImagBar(self, val):
        self.emit(QtCore.SIGNAL("setImagBar(int)"), int(val * self.bar_expand))

    def work(self, input_items, output_items):
        in0 = input_items[0]
        for i in range(len(in0)):
            time = gr.high_res_timer_now()
            value = self.expand_factor(in0[i])
            value = self.adjust_ref_level(value)
            value = self.calculate_average(value)
            value = self.find_peak(value)
            if not self.hold:
                if time > self.last_update + self.update_res:
                    self.last_update = gr.high_res_timer_now()
                    self.setValue(value)

        return len(input_items[0])

    def expand_factor(self, val):
        return val * self.factor

    def adjust_ref_level(self, val):
        return val + self.ref_level

    def calculate_average(self, val):
        if not self.average:
            return val
        else:
            self.avgval = (self.avgval * (1 - self.avg_alpha)) + (val * self.avg_alpha)
            return self.avgval

    def find_peak(self, val):
        if self.peak_hold:
            self.peakval = max(val, self.peakval)
            return self.peakval
        else:
            self.peakval = 0
            return val

    def set_samp_rate(self, rate):
        self.samp_rate = rate
        self.update_samps = int(self.samp_rate/self.number_rate)

    def set_number_rate(self, rate):
        self.number_rate = rate
        self.update_samps = int(self.samp_rate/self.number_rate)
