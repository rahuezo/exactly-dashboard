import numpy as np
import matplotlib.pyplot as plt


def operations_predict(history): 
    fit = np.polyfit(np.arange(len(history)), history, 1)
    fit_fn = np.poly1d(fit)
    predicted = int(fit_fn(len(history)))
    last = history[-1] 
    return predicted - last

