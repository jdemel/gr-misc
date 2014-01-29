#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Wed Jan 29 13:46:59 2014
##################################################

execfile("/home/johannes/.grc_gnuradio/xlate_interleave.py")
from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import PyQt4.Qwt5 as Qwt
import math
import misc
import sip
import sys

class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 7.5e6
        self.decim = decim = 150
        self.xlate_bw = xlate_bw = 25e3
        self.usrp_gain = usrp_gain = 33
        self.rx_antenna = rx_antenna = "RX2"
        self.port = port = 47110
        self.phase = phase = 0
        self.mlen = mlen = 100
        self.keep_plot = keep_plot = 16
        self.keep = keep = 1
        self.ip = ip = "localhost"
        self.freq_offset = freq_offset = 200e3
        self.fire = fire = 0
        self.device_args = device_args = "type=x300, master_clock_rate=150e6"
        self.calib_freq_offset = calib_freq_offset = 2e6
        self.cal_freq = cal_freq = 450e6
        self.baseband_rate = baseband_rate = int(samp_rate/decim)
        self.angular_resolution = angular_resolution = 360
        self.N_keep = N_keep = 1000
        self.N = N = 512
        self.M_keep = M_keep = 100

        ##################################################
        # Blocks
        ##################################################
        self.tabw = Qt.QTabWidget()
        self.tabw_widget_0 = Qt.QWidget()
        self.tabw_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabw_widget_0)
        self.tabw_grid_layout_0 = Qt.QGridLayout()
        self.tabw_layout_0.addLayout(self.tabw_grid_layout_0)
        self.tabw.addTab(self.tabw_widget_0, "Synchronization Setup")
        self.tabw_widget_1 = Qt.QWidget()
        self.tabw_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabw_widget_1)
        self.tabw_grid_layout_1 = Qt.QGridLayout()
        self.tabw_layout_1.addLayout(self.tabw_grid_layout_1)
        self.tabw.addTab(self.tabw_widget_1, "DOA")
        self.top_layout.addWidget(self.tabw)
        self._xlate_bw_layout = Qt.QVBoxLayout()
        self._xlate_bw_tool_bar = Qt.QToolBar(self)
        self._xlate_bw_layout.addWidget(self._xlate_bw_tool_bar)
        self._xlate_bw_tool_bar.addWidget(Qt.QLabel("Xlate Bandwidth"+": "))
        self._xlate_bw_counter = Qwt.QwtCounter()
        self._xlate_bw_counter.setRange(0, baseband_rate, 1)
        self._xlate_bw_counter.setNumButtons(2)
        self._xlate_bw_counter.setValue(self.xlate_bw)
        self._xlate_bw_tool_bar.addWidget(self._xlate_bw_counter)
        self._xlate_bw_counter.valueChanged.connect(self.set_xlate_bw)
        self._xlate_bw_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._xlate_bw_slider.setRange(0, baseband_rate, 1)
        self._xlate_bw_slider.setValue(self.xlate_bw)
        self._xlate_bw_slider.setMinimumWidth(200)
        self._xlate_bw_slider.valueChanged.connect(self.set_xlate_bw)
        self._xlate_bw_layout.addWidget(self._xlate_bw_slider)
        self.tabw_grid_layout_0.addLayout(self._xlate_bw_layout, 0,2,1,1)
        self._phase_layout = Qt.QVBoxLayout()
        self._phase_tool_bar = Qt.QToolBar(self)
        self._phase_layout.addWidget(self._phase_tool_bar)
        self._phase_tool_bar.addWidget(Qt.QLabel("phase"+": "))
        self._phase_counter = Qwt.QwtCounter()
        self._phase_counter.setRange(-3, 3, 0.001)
        self._phase_counter.setNumButtons(2)
        self._phase_counter.setValue(self.phase)
        self._phase_tool_bar.addWidget(self._phase_counter)
        self._phase_counter.valueChanged.connect(self.set_phase)
        self._phase_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._phase_slider.setRange(-3, 3, 0.001)
        self._phase_slider.setValue(self.phase)
        self._phase_slider.setMinimumWidth(200)
        self._phase_slider.valueChanged.connect(self.set_phase)
        self._phase_layout.addWidget(self._phase_slider)
        self.top_layout.addLayout(self._phase_layout)
        self._keep_tool_bar = Qt.QToolBar(self)
        self._keep_tool_bar.addWidget(Qt.QLabel("Keep input vectors"+": "))
        self._keep_line_edit = Qt.QLineEdit(str(self.keep))
        self._keep_tool_bar.addWidget(self._keep_line_edit)
        self._keep_line_edit.returnPressed.connect(
        	lambda: self.set_keep(int(self._keep_line_edit.text().toAscii())))
        self.tabw_grid_layout_1.addWidget(self._keep_tool_bar, 2,1,1,1)
        self._freq_offset_layout = Qt.QVBoxLayout()
        self._freq_offset_tool_bar = Qt.QToolBar(self)
        self._freq_offset_layout.addWidget(self._freq_offset_tool_bar)
        self._freq_offset_tool_bar.addWidget(Qt.QLabel("Xlate Freq. Offset"+": "))
        self._freq_offset_counter = Qwt.QwtCounter()
        self._freq_offset_counter.setRange(-samp_rate/2, samp_rate/2, 1)
        self._freq_offset_counter.setNumButtons(2)
        self._freq_offset_counter.setValue(self.freq_offset)
        self._freq_offset_tool_bar.addWidget(self._freq_offset_counter)
        self._freq_offset_counter.valueChanged.connect(self.set_freq_offset)
        self._freq_offset_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._freq_offset_slider.setRange(-samp_rate/2, samp_rate/2, 1)
        self._freq_offset_slider.setValue(self.freq_offset)
        self._freq_offset_slider.setMinimumWidth(200)
        self._freq_offset_slider.valueChanged.connect(self.set_freq_offset)
        self._freq_offset_layout.addWidget(self._freq_offset_slider)
        self.tabw_grid_layout_0.addLayout(self._freq_offset_layout, 0,1,1,1)
        self.xlate_interleave_0 = xlate_interleave(
            samp_rate=samp_rate,
            decim=decim,
            freq_offset=freq_offset,
            xlate_bw=xlate_bw,
        )
        self._usrp_gain_tool_bar = Qt.QToolBar(self)
        self._usrp_gain_tool_bar.addWidget(Qt.QLabel("USRP RF Gain"+": "))
        self._usrp_gain_line_edit = Qt.QLineEdit(str(self.usrp_gain))
        self._usrp_gain_tool_bar.addWidget(self._usrp_gain_line_edit)
        self._usrp_gain_line_edit.returnPressed.connect(
        	lambda: self.set_usrp_gain(eng_notation.str_to_num(self._usrp_gain_line_edit.text().toAscii())))
        self.tabw_grid_layout_0.addWidget(self._usrp_gain_tool_bar, 0,3,1,1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	angular_resolution, #size
        	1.0/1000.0, #samp_rate
        	"MUSIC Spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-3.0, 20.0)
        self.qtgui_time_sink_x_1.enable_tags(-1, False)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.tabw_grid_layout_1.addWidget(self._qtgui_time_sink_x_1_win, 0,0,2,1)
        self.missile_launcher_0 = misc.async_missile_launcher(azimuth=0.0, elevation=25.0, threshold=0.0, recal_threshold=0.0)
        self.misc_numbersink_0 = misc.numbersink(float, "Angle", "Degrees", samp_rate, 0, 360, 1.0, 10, 0.0, 15, False, 0, "Angle", False, True)
        self._misc_numbersink_0_win = self.misc_numbersink_0.get_pyqwidget()
        self.tabw_grid_layout_1.addWidget(self._misc_numbersink_0_win, 1,1,1,1)
          
        self.misc_music_doa_1 = misc.music_doa_helper(m=2, n=1, nsamples=N, angular_resolution=angular_resolution, frequency=cal_freq, array_spacing=0.132, antenna_array=[[0,0],[1,0]], output_spectrum=True)
        self.misc_compass_0 = misc.compass(False, "nice", "simple", 15)
        self._misc_compass_0_win = self.misc_compass_0.get_pyqwidget()
        self.tabw_grid_layout_1.addWidget(self._misc_compass_0_win, 0,1,1,1)
        self._fire_tool_bar = Qt.QToolBar(self)
        self._fire_tool_bar.addWidget(Qt.QLabel("FIRE!"+": "))
        self._fire_line_edit = Qt.QLineEdit(str(self.fire))
        self._fire_tool_bar.addWidget(self._fire_line_edit)
        self._fire_line_edit.returnPressed.connect(
        	lambda: self.set_fire(int(self._fire_line_edit.text().toAscii())))
        self.tabw_grid_layout_1.addWidget(self._fire_tool_bar, 2,0,1,1)
        self._calib_freq_offset_layout = Qt.QVBoxLayout()
        self._calib_freq_offset_tool_bar = Qt.QToolBar(self)
        self._calib_freq_offset_layout.addWidget(self._calib_freq_offset_tool_bar)
        self._calib_freq_offset_tool_bar.addWidget(Qt.QLabel("Calibration Tone Offset"+": "))
        self._calib_freq_offset_counter = Qwt.QwtCounter()
        self._calib_freq_offset_counter.setRange(-samp_rate/2, samp_rate/2, 1)
        self._calib_freq_offset_counter.setNumButtons(2)
        self._calib_freq_offset_counter.setValue(self.calib_freq_offset)
        self._calib_freq_offset_tool_bar.addWidget(self._calib_freq_offset_counter)
        self._calib_freq_offset_counter.valueChanged.connect(self.set_calib_freq_offset)
        self._calib_freq_offset_slider = Qwt.QwtSlider(None, Qt.Qt.Horizontal, Qwt.QwtSlider.BottomScale, Qwt.QwtSlider.BgSlot)
        self._calib_freq_offset_slider.setRange(-samp_rate/2, samp_rate/2, 1)
        self._calib_freq_offset_slider.setValue(self.calib_freq_offset)
        self._calib_freq_offset_slider.setMinimumWidth(200)
        self._calib_freq_offset_slider.valueChanged.connect(self.set_calib_freq_offset)
        self._calib_freq_offset_layout.addWidget(self._calib_freq_offset_slider)
        self.tabw_grid_layout_0.addLayout(self._calib_freq_offset_layout, 0,0,1,1)
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, angular_resolution)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, N)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, angular_resolution, 0)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((math.e**(1.0j*phase), ))
        self.blocks_keep_one_in_n_1 = blocks.keep_one_in_n(gr.sizeof_float*angular_resolution, keep_plot)
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_gr_complex*N, keep)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((0, ))
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 200e3, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.misc_music_doa_1, 0))
        self.connect((self.misc_music_doa_1, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.xlate_interleave_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.xlate_interleave_0, 0))
        self.connect((self.xlate_interleave_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.misc_numbersink_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.missile_launcher_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.misc_compass_0, 0))
        self.connect((self.misc_music_doa_1, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_keep_one_in_n_1, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_vector_to_stream_0_0, 0))
        self.connect((self.misc_music_doa_1, 2), (self.blocks_keep_one_in_n_1, 0))
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.qtgui_time_sink_x_1, 0))


# QT sink close method reimplementation
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_baseband_rate(int(self.samp_rate/self.decim))
        self.xlate_interleave_0.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.misc_numbersink_0.set_samp_rate(self.samp_rate)

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_baseband_rate(int(self.samp_rate/self.decim))
        self.xlate_interleave_0.set_decim(self.decim)

    def get_xlate_bw(self):
        return self.xlate_bw

    def set_xlate_bw(self, xlate_bw):
        self.xlate_bw = xlate_bw
        self.xlate_interleave_0.set_xlate_bw(self.xlate_bw)
        self._xlate_bw_counter.setValue(self.xlate_bw)
        self._xlate_bw_slider.setValue(self.xlate_bw)

    def get_usrp_gain(self):
        return self.usrp_gain

    def set_usrp_gain(self, usrp_gain):
        self.usrp_gain = usrp_gain
        self._usrp_gain_line_edit.setText(eng_notation.num_to_str(self.usrp_gain))

    def get_rx_antenna(self):
        return self.rx_antenna

    def set_rx_antenna(self, rx_antenna):
        self.rx_antenna = rx_antenna

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port

    def get_phase(self):
        return self.phase

    def set_phase(self, phase):
        self.phase = phase
        self.blocks_multiply_const_vxx_1.set_k((math.e**(1.0j*self.phase), ))
        self._phase_counter.setValue(self.phase)
        self._phase_slider.setValue(self.phase)

    def get_mlen(self):
        return self.mlen

    def set_mlen(self, mlen):
        self.mlen = mlen

    def get_keep_plot(self):
        return self.keep_plot

    def set_keep_plot(self, keep_plot):
        self.keep_plot = keep_plot
        self.blocks_keep_one_in_n_1.set_n(self.keep_plot)

    def get_keep(self):
        return self.keep

    def set_keep(self, keep):
        self.keep = keep
        self.blocks_keep_one_in_n_0.set_n(self.keep)
        self._keep_line_edit.setText(str(self.keep))

    def get_ip(self):
        return self.ip

    def set_ip(self, ip):
        self.ip = ip

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.xlate_interleave_0.set_freq_offset(self.freq_offset)
        self._freq_offset_counter.setValue(self.freq_offset)
        self._freq_offset_slider.setValue(self.freq_offset)

    def get_fire(self):
        return self.fire

    def set_fire(self, fire):
        self.fire = fire
        self.missile_launcher_0.launch(self.fire, False)
        self._fire_line_edit.setText(str(self.fire))

    def get_device_args(self):
        return self.device_args

    def set_device_args(self, device_args):
        self.device_args = device_args

    def get_calib_freq_offset(self):
        return self.calib_freq_offset

    def set_calib_freq_offset(self, calib_freq_offset):
        self.calib_freq_offset = calib_freq_offset
        self._calib_freq_offset_counter.setValue(self.calib_freq_offset)
        self._calib_freq_offset_slider.setValue(self.calib_freq_offset)

    def get_cal_freq(self):
        return self.cal_freq

    def set_cal_freq(self, cal_freq):
        self.cal_freq = cal_freq
        self.misc_music_doa_1.set_frequency(self.cal_freq)

    def get_baseband_rate(self):
        return self.baseband_rate

    def set_baseband_rate(self, baseband_rate):
        self.baseband_rate = baseband_rate

    def get_angular_resolution(self):
        return self.angular_resolution

    def set_angular_resolution(self, angular_resolution):
        self.angular_resolution = angular_resolution

    def get_N_keep(self):
        return self.N_keep

    def set_N_keep(self, N_keep):
        self.N_keep = N_keep

    def get_N(self):
        return self.N

    def set_N(self, N):
        self.N = N

    def get_M_keep(self):
        return self.M_keep

    def set_M_keep(self, M_keep):
        self.M_keep = M_keep

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    qapp = Qt.QApplication(sys.argv)
    tb = top_block()
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets

