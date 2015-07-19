import math

class EightPuzzleGameState(object):
    """A state of an 8 puzzle game contains all the properties of state itself.
    """

    __slots__ = {'_data', '__puzzle_pieces', '_representation', '_blank_position'}

    def __init__(self, game_state_as_array):
        self._data = game_state_as_array
        self._representation = ''
        self.__puzzle_pieces = 8

        # Parse through the puzzle pieces to change the x to a blank space
        # and represent the state as a string
        for index, puzzle_piece in enumerate(self._data):
            if puzzle_piece == 'x':
                self._representation += ' '
                self._blank_position = index
            else:
                self._representation += self._data[index]
            # if (index + 1) % int(math.sqrt(self.__puzzle_pieces+1)) == 0:
            #     self._board_representation += '\n'
            # else:
            #     self._board_representation += ' '
    
    @property
    def data(self):
        """Get the data of the eight puzzle game board.
        """
        return self._data

    @data.setter
    def data(self, some_data):
        """Sets the data of the GameState.
        """
        self._data = some_data

    @property
    def blank_position(self):
        """Get the blank space index.
        """
        return self._blank_position

    @property
    def representation(self):
        """Get the representation as string.
        """
        return self._representation

    def __repr__(self):
        return self._representation

    __str__ = __repr__
