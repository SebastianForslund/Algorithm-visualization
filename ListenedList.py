class ListenedList(list):

    def __init__(self, gui, args=None):
        self.gui = gui
        super()

    def __setitem__(self, key, value):
        # normal list, just call the sort_event() on each change.
        self.gui.list_sort_event()
        super(ListenedList, self).__setitem__(key, value)
