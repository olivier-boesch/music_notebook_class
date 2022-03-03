"""

Music making helping class for jupyter notebooks
    Olivier Boesch (c) 2022

"""



import numpy as np

class MusicError(Exception):
    """MusicError: Exceptions for the Music class"""
    pass


class Music:
    """Music: General class for audio data creation and play
    Uses Ipython.display.Audio for display and numpy to handle data"""
    """index_plot_figure: class variable to ensure each plot is made in a different figure"""
    index_plot_figure = 0

    def __init__(self, frequency=440, duration=3, volume=1.0, framerate=44100, generate=True):
        """Music: General class for audio data creation and play
        parameters:
            frequency: frequency in Hertz of the given note. - defaults to 440Hz
                When storing a melody, the value is 0.
                When storing a complex sound, the value is the lowest frequency used.
            duration: duration in seconds of the note or the melody - defaults to 3s
            volume: volume (amplitude) of the note (0.0->nothing, 1.0-> full volume) - defaults to 1.0
                when storing a melody or a complex sound, the value is always 1.0
            framerate: framerate of the data in hertz - defaults to 44100Hz
            generate: should the data be generated automatically (internal use only) - defaults to True"""
        self.data = None
        self.framerate = framerate
        self.frequency = frequency
        self.duration = duration
        self.volume = volume
        if generate:
            self.generate_data()

    def generate_data(self):
        """generate_data: generate sound data from parameters (frequency, duration, framerate and volume)"""
        t = np.linspace(0., self.duration, int(self.framerate * self.duration))
        self.data = self.volume * np.sin(2*np.pi*self.frequency*t)

    def play(self, autoplay=True):
        """play: display of the sound reader using IPython.display.Audio"""
        from IPython.display import Audio  # import only when needed
        return Audio(self.data, rate=self.framerate, autoplay=autoplay)

    def plot(self, periods=None):
        """plot: plot the data using matplotlib
        parameters:
            periods: number of periods to display. - defaults to None
                when the value is None, displays the entire data set"""
        if self.frequency == 0:  # when freq==0, this is a melody. we don't display melodies as it makes no sense
            raise MusicError("Can't plot melodies")
        from matplotlib import pyplot as plt  # import only when needed
        t = np.linspace(0., self.duration, int(self.framerate * self.duration))  # recreate array for time
        if periods is not None:
            # find the right index to slice data
            T = 1 / self.frequency * periods
            idx_T = (np.abs(t - T)).argmin()
        else:
            idx_T = len(t)  # we take all data in this case
        # increment the figure index for the new plot to ensure it is plotted in a new graph
        Music.index_plot_figure += 1
        plt.figure(Music.index_plot_figure)
        plt.title("Data Display")
        plt.xlabel("time (s)")
        plt.ylabel("Amplitude")
        plt.plot(t[:idx_T],self.data[:idx_T])
        plt.show()

    def __and__(self, other):
        """__and__ : use of bitwise and operator (&) to merge notes and create complex sounds"""
        if type(other) != self.__class__:
            raise MusicError('This object is NOT a Music Object')
        if self.framerate != other.framerate or self.duration != other.duration:
            raise MusicError('Can only merge notes with the same framerate and duration')
        # we take for frequency the lowest one of the two
        new_music = Music(frequency=min(self.frequency, other.frequency), framerate=self.framerate, duration=self.duration, generate=False)
        # we add arrays
        new_music.data = self.data + other.data
        return new_music

    def __add__(self, other):
        """__add__ : use of add operator (+) to concatenate notes and create melodies"""
        if type(other) != self.__class__:
            raise MusicError('This object is NOT a Music Object')
        if self.framerate != other.framerate:
            raise MusicError('Can only concatenate notes with same framerate')
        # melody making: frequency set to 0 and duration set to total duration
        new_music = Music(frequency=0, framerate=self.framerate, duration=self.duration + other.duration, generate=False)
        new_music.data = np.concatenate((self.data, other.data))
        return new_music

