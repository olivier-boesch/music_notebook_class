# music_notebook_class
Music class for jupyter notebooks

----
Help on module music:

NAME
    music

CLASSES
    builtins.Exception(builtins.BaseException)
        MusicError
    builtins.object
        Music
    
    class Music(builtins.object)
     |  Music(frequency=440, duration=3, volume=1.0, framerate=44100, generate=True)
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
     |  __init__(self, frequency=440, duration=3, volume=1.0, framerate=44100, generate=True)
     |      Music: General class for audio data creation and play
     |      parameters:
     |          frequency: frequency in Hertz of the given note. - defaults to 440Hz
     |              When storing a melody, the value is 0.
     |              When storing a complex sound, the value is the lowest frequency used.
     |          duration: duration in seconds of the note or the melody - defaults to 3s
     |          volume: volume (amplitude) of the note (0.0->nothing, 1.0-> full volume) - defaults to 1.0
     |              when storing a melody or a complex sound, the value is always 1.0
     |          framerate: framerate of the data in hertz - defaults to 44100Hz
     |          generate: should the data be generated automatically (internal use only) - defaults to True
     |  
     |  generate_data(self)
     |      generate_data: generate sound data from parameters (frequency, duration, framerate and volume
     |  
     |  play(self)
     |      play: display of the sound reader
     |  
     |  plot(self, periods=None)
     |      plot: plot the data using matplotlib
     |      parameters:
     |          periods: number of periods to display. - defaults to None
     |              when the value is None, displays the entire data set
     |  
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  content = None
     |  
     |  data = None
    
    class MusicError(builtins.Exception)
     |  MusicError: Exceptions for the Music class

