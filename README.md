# music_notebook_class
Music class for jupyter notebooks

python module (use as hidden lib in capytale)
and test notebook

----

Documentation:

~~~
Help on module music:

NAME
    music

DESCRIPTION
    Music making helping class for jupyter notebooks
        Olivier Boesch (c) 2022

CLASSES
    builtins.Exception(builtins.BaseException)
        MusicError
    builtins.object
        Music

    class Music(builtins.object)
     |  Music(f=440, d=None, v=1.0, framerate=None, generate=True)
     |
     |  Music: General class for audio data creation and play
     |  Uses Ipython.display.Audio for display and numpy to handle data
     |
     |  Methods defined here:
     |
     |  __add__(self, other)
     |      __add__ : use of add operator (+) to concatenate notes and create melodies
     |
     |  __and__(self, other)
     |      __and__ : use of bitwise and operator (&) to merge notes and create complex sounds
     |
     |  __init__(self, f=440, d=None, v=1.0, framerate=None, generate=True)
     |      Music: General class for audio data creation and play
     |      parameters:
     |          f: frequency in Hertz of the given note. - defaults to 440Hz
     |          d: duration in seconds of the note or the melody - defaults to 3s
     |          v: volume (amplitude) of the note (0.0->nothing, 1.0-> full volume) - defaults to 1.0
     |              when storing a melody or a complex sound, the value is always 1.0
     |          framerate: framerate of the data in hertz - defaults to 44100Hz
     |          generate: should the data be generated automatically (internal use only) - defaults to True
     |
     |  __mul__(self, other)
     |      __mult__ : use of multiplication operator (*) to multiply the frequency by a certain amount
     |
     |  __rmul__(self, other)
     |      __rmul__: identical to __mul__ (* operator)
     |
     |  generate_data(self)
     |      generate_data: generate sound data from parameters (frequency, duration, framerate and volume)
     |
     |  play(self, autoplay=True)
     |      play: display of the sound reader using IPython.display.Audio
     |
     |  plot(self, periods=None)
     |      plot: plot the data using matplotlib
     |      parameters:
     |          periods: number of periods to display. - defaults to None
     |              when the value is None, displays the entire data set
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  default_duration = 3
     |
     |  default_framerate = 44100
     |
     |  index_plot_figure = 0

    class MusicError(builtins.Exception)
     |  MusicError: Exceptions for the Music class

FUNCTIONS
    test_mul()

FILE
    music.py
~~~
