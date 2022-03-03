# music_notebook_class
Music class for jupyter notebooks

as notebook or python module (use as hidden lib in capytale)

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
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  index_plot_figure = 0
     |      index_plot_figure: class variable to ensure each plot is made in a different figure (internal use only)
    
    class MusicError(builtins.Exception)
     |  MusicError: Exceptions for the Music class
     |  
     |  Method resolution order:
     |      MusicError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args

FILE
    music.py
~~~
