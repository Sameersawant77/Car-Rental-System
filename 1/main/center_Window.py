
def center_window(w, h, ws, hs):
    # get screen width and height
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    return ('%dx%d+%d+%d' % (w, h, x, y))
