import matplotlib as mpl
import matplotlib.cm as cm 
import numpy as np


def get_delta_percent_archive(history): 
    if len(history) == 1: 
        return 0

    latest_delta = history[-1] - history[-2]

    if latest_delta > 0: 
        if len(history) > 2: 
            change = float(history[-1] - history[-3])
        else:
            change = float(history[-1] - history[-2])
        return latest_delta / change
    return 0

def get_delta_percent(history): 
    i = 2
    if len(history) > 2: i = 3
    if len(history) == 1 or history[-1] - history[0] == 0: 
        return 0
    a = (history[-1] - history[-i]) / i / float(history[-1] - history[0])
    return a


def get_delta_history(history): 
    delta_history = []
    history_copy = history[:]

    for i in xrange(len(history)): 
        current = get_delta_percent(history_copy[:i + 1])
        delta_history.append(current)
    return delta_history

    


def delta_to_color(delta_percent, raw=False, color_map=None, scale_shift=0.2):
    norm = mpl.colors.Normalize(vmin=0, vmax=1)
    mapper = cm.ScalarMappable(norm=norm, cmap=color_map if color_map else cm.winter)
    rgba = [val for val in mapper.to_rgba((delta_percent**0.4)* (1 - scale_shift) + scale_shift)]
    if not raw: 
        return delta_percent, 'rgb({}, {}, {})'.format(int(255*rgba[0]), int(255*rgba[1]), int(255*rgba[2]))
    return int(255*rgba[0]), int(255*rgba[1]), int(255*rgba[2])


def make_color_scale(): 
    code = """
    <div class="my-0" style="width: 20px; height: 220px; background: red; background: linear-gradient({})"></div>
    """
    return code.format(','.join(['#{0:02x}{1:02x}{2:02x}'.format(*delta_to_color(i, raw=True)) for i in np.linspace(1, 0, 10)]))
        
        
        
        #['#{0:02x}{1:02x}{2:02x}'.format(*delta_to_color(i, raw=True)) for i in np.linspace(0, 1, 10)]






# UNUSED FUNCTIONS 

# COLOR_BASE = 120

# def delta_to_color(delta_percent, red=COLOR_BASE, blue=COLOR_BASE):
#     green = int(red + (255 - red)*delta_percent)
#     return 'rgb({},{},{})'.format(red, green, blue)

# def interpolate_color(color1, color2, factor=0.5): 
#     result = color1[:]

#     for i in xrange(3): 
#         result[i] = round(result[i] + factor * (color2[i] - color1[i]))
#     return result

# def interpolate_colors(color1, color2, steps): 
#     step_factor = 1.0 / (steps - 1)
#     interpolated_colors = []

#     for i in xrange(steps): 
#         interpolated_colors.append(interpolate_color(color1, color2, step_factor*i))
#     return interpolated_colors