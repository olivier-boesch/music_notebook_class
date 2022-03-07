"""

Music making helping class for jupyter notebooks
    Olivier Boesch (c) 2022

"""

import numpy as np
from matplotlib import pyplot as plt


class MusicError(Exception):
    """MusicError: Exceptions for the Music class"""
    pass


class Music:
    """Music: General class for audio data creation and play
    Uses Ipython.display.Audio for display and numpy to handle data"""
    """__index_plot_figure: class variable to ensure each plot is made in a different figure"""
    __index_plot_figure = 0
    default_duration = 3
    default_framerate = 44100

    def __init__(self, f=440, d=None, v=1.0, rate=None, generate=True):
        """Music: General class for audio data creation and play
        parameters:
            f: frequency in Hertz of the given note. - defaults to 440Hz
            d: duration in seconds of the note or the melody - defaults to 3s
            v: volume (amplitude) of the note (0.0->nothing, 1.0-> full volume) - defaults to 1.0
                when storing a melody or a complex sound, the value is always 1.0
            rate: framerate of the data in hertz - defaults to 44100Hz
            generate: should the data be generated automatically (internal use only) - defaults to True"""
        self.__data = None
        self.__complex_sound = False
        self.__melody = False
        self.__frequency = f
        if d is not None:
            self.__duration = d
        else:
            self.__duration = Music.default_duration
        self.__volume = v
        if rate is not None:
            self.__rate = rate
        else:
            self.__rate = Music.default_framerate
        if generate:
            self._generate_data()

    def _generate_data(self):
        """_generate_data: generate sound data from parameters (frequency, duration, framerate and volume)"""
        t = np.linspace(0., self.__duration, int(self.__rate * self.__duration))
        self.__data = self.__volume * np.sin(2 * np.pi * self.__frequency * t)

    def copy(self):
        """copy: returns a copy of the object"""
        new_music = Music(generate=False)
        new_music.__frequency = self.__frequency
        new_music.__complex_sound = self.__complex_sound
        new_music.__melody = self.__melody
        new_music.__duration = self.__duration
        new_music.__volume = self.__volume
        new_music.__rate = self.__rate
        new_music.__data = np.copy(self.__data)
        return new_music

    def note(self, duration):
        if self.melody or self.complex:
            raise MusicError("note function works only for simple sound")
        new_music = self.copy()
        new_music.__duration = duration
        new_music._generate_data()
        return new_music

    @property
    def rate(self):
        """rate: read only property that returns the framerate of the data"""
        return self.__rate

    @property
    def frequency(self):
        return self.__frequency

    @frequency.setter
    def frequency(self, value):
        if value < 0:
            raise MusicError("Frequency must be positive")
        if self.__complex_sound:
            raise MusicError("Can't change the frequency of a complex sound")
        if self.__melody:
            raise MusicError("Can't change the frequency of a melody")
        self.__frequency = value
        self._generate_data()

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if value < 0:
            raise MusicError("duration must be positive")
        if self.__complex_sound:
            raise MusicError("Can't change the duration of a complex sound")
        if self.__melody:
            raise MusicError("Can't change the frequency of a melody")
        self.__duration = value
        self._generate_data()

    @property
    def volume(self):
        return self.__duration

    @volume.setter
    def volume(self, value):
        if value < 0:
            raise MusicError("duration must be positive")
        self.__data = self.__data / self.__volume
        self.__volume = value
        self.__data = self.__data * self.__volume

    @property
    def melody(self):
        """melody: read only property set if the sound is a melody"""
        return self.__melody

    @property
    def complex(self):
        """complex: read only property set if the sound is complex (several frequencies)"""
        return self.__complex_sound

    def play(self, autoplay=True):
        """play: display of the sound reader using IPython.display.Audio"""
        from IPython.display import Audio  # import only when needed
        return Audio(self.__data, rate=self.__rate, autoplay=autoplay)

    def plot(self, periods=None):
        """plot: plot the data using matplotlib
        parameters:
            periods: number of periods to display. - defaults to None
                when the value is None, displays the entire data set"""
        if self.__melody:  # if this is a melody, we don't display melodies as it makes no sense
            raise MusicError("Can't plot melodies")
        t = np.linspace(0., self.__duration, int(self.__rate * self.__duration))  # recreate array for time
        if periods is not None:
            # find the right index to slice data
            T = (1 / self.__frequency) * periods
            index_t = (np.abs(t - T)).argmin()
        else:
            index_t = len(t)  # we take all data in this case
        # increment the figure index for the new plot to ensure it is plotted in a new graph
        Music.__index_plot_figure += 1
        plt.figure(Music.__index_plot_figure)
        plt.title("Data Display")
        plt.xlabel("time (s)")
        plt.ylabel("Amplitude")
        plt.plot(t[:index_t], self.__data[:index_t])
        plt.show()

    def plot_fft(self):
        """plot_fft: plot the amplitudes for each frequencies found in the sound
        doc : https://gist.github.com/jedludlow/3919130
        """
        fft_data = np.fft.fft(self.__data)
        n_fft_data = len(fft_data)
        fft_freq = np.fft.fftfreq(n_fft_data, 1 / self.__rate)
        half_n = int(np.ceil(n_fft_data / 2.0))
        half_fft_data = (2.0 / n_fft_data) * fft_data[:half_n]
        half_fft_freq = fft_freq[:half_n]
        Music.__index_plot_figure += 1
        plt.figure(Music.__index_plot_figure)
        plt.title("FFT Display")
        plt.xlabel("frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.xscale("log")
        plt.plot(half_fft_freq, np.abs(half_fft_data))
        plt.show()

    def __and__(self, other):
        """__and__ : use of bitwise and operator (&) to merge notes and create complex sounds"""
        if type(other) != Music:
            raise MusicError('This object is NOT a Music Object')
        if self.__melody:
            raise MusicError("Can't create complex sound for a melody ")
        if self.__rate != other.__rate or self.__duration != other.__duration:
            raise MusicError('Can only merge notes with the same framerate and duration')
        # we take for frequency the lowest one of the two
        new_music = Music(f=min(self.__frequency, other.__frequency),
                          rate=self.__rate,
                          d=self.__duration,
                          generate=False)
        new_music.__complex_sound = True
        # we add arrays
        new_music.__data = self.__data + other.__data
        return new_music

    def __add__(self, other):
        """__add__ : use of add operator (+) to concatenate notes and create melodies"""
        if type(other) != Music:
            raise MusicError('This object is NOT a Music Object')
        if self.__rate != other.__rate:
            raise MusicError('Can only concatenate notes with same framerate')
        # melody making: frequency set to 0 and duration set to total duration
        new_music = Music(f=0, rate=self.__rate, d=self.__duration + other.__duration, generate=False)
        new_music.__melody = True
        new_music.__data = np.concatenate((self.__data, other.__data))
        return new_music

    def __mul__(self, other):
        """__mult__ : use of multiplication operator (*) to multiply the frequency by a certain amount"""
        if self.__melody:
            raise MusicError("Can't change frequency for a melody ")
        if self.__complex_sound:
            raise MusicError("Can't change frequency for a complex sound ")
        if type(other) != int and type(other) != float:
            raise MusicError("Can only use float or int to change frequency")
        new_music = Music(f=self.__frequency * other, d=self.__duration, v=self.__volume, rate=self.__rate)
        return new_music

    def __rmul__(self, other):
        """__rmul__: identical to __mul__ (* operator)"""
        return self.__mul__(other)

    def __truediv__(self, other):
        """__truediv__: use of division operator (/) to divide the frequency by a certain amount"""
        if self.__melody:
            raise MusicError("Can't change frequency for a melody ")
        if self.__complex_sound:
            raise MusicError("Can't change frequency for a complex sound ")
        if type(other) != int and type(other) != float:
            raise MusicError("Can only use float or int to change frequency")
        new_music = Music(f=self.frequency / other, d=self.duration, v=self.volume, rate=self.__rate)
        return new_music


def test_mul():
    from math import isclose
    assert isclose((2.0 * Music(400)).frequency, 800)
    assert (Music(400) * 2).frequency == 800
    assert isclose((3.0 * Music(400)).frequency, 1200.0)
    assert (Music(400) * 3).frequency == 1200
