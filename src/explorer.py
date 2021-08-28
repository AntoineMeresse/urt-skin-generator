from os import listdir, getcwd
from os.path import isdir, sep

class FileExplorer:

    def __init__(self) -> None:
        path_sep = getcwd() + sep + 'images'+ sep
        self.path_blade = path_sep+"blade"
        self.path_hand = path_sep+"hand"
        self.path_handle = path_sep+"handle"
        self.path_tint = path_sep+"tint"
        
        self.blades = listdir(self.path_blade) if isdir(self.path_blade) else None
        self.handles = listdir(self.path_hand) if isdir(self.path_hand) else None
        self.hands = listdir(self.path_handle) if isdir(self.path_handle) else None
        self.tints = listdir(self.path_tint) if isdir(self.path_tint) else None

    def get_blades(self) -> list:
        return self.blades

    def get_handles(self) -> list:
        return self.handles

    def get_hands(self) -> list:
        return self.hands

    def get_tints(self) -> list:
        return self.tints

    def to_string(self):
        print("Blades : {}\nHandles : {}\nHands : {}\nTints : {}".format(self.blades, self.handles, self.hands, self.tints))
