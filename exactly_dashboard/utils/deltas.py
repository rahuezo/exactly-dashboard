import matplotlib as mpl
import matplotlib.cm as cm 
import numpy as np

custom_cmap = mpl.colors.LinearSegmentedColormap.from_list("", ["#f41d1d","#0033e5","#1bd14d"])


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
    if len(history) == 1 or history[-1] - history[0] <= 0: 
        return 0
    return (history[-1] - history[-i]) / i / float(history[-1] - history[0])


def get_delta_history(history): 
    delta_history = []
    history_copy = history[:]

    for i in xrange(len(history)): 
        current = get_delta_percent(history_copy[:i + 1])
        delta_history.append(current)
    return delta_history

    

def scale_color_map(delta_percent, map_type, scale_shift=0.2): 
    if map_type == "lead": 
        if delta_percent <= 0.9: 
            return 0 + scale_shift
        elif 0.9 < delta_percent <= 1.0:
            return (delta_percent - 0.9)*5 + scale_shift
        elif delta_percent < 1.5: 
            return delta_percent - 0.5 + scale_shift
        else: 
            return 1 + scale_shift
    else: 
        return (delta_percent**0.4)* (1 - scale_shift) + scale_shift



def delta_to_color(delta_percent, map_type="operations", raw=False, color_map=custom_cmap, scale_shift=0.2):
    norm = mpl.colors.Normalize(vmin=0, vmax=1)
    mapper = cm.ScalarMappable(norm=norm, cmap=color_map if color_map else cm.winter)

    rgba = [val for val in mapper.to_rgba(scale_color_map(delta_percent, map_type, scale_shift))]
    if not raw: 
        return delta_percent, 'rgb({}, {}, {})'.format(int(255*rgba[0]), int(255*rgba[1]), int(255*rgba[2]))
    return int(255*rgba[0]), int(255*rgba[1]), int(255*rgba[2])






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