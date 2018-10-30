import numpy as np
import matplotlib.pyplot as plt


def operations_predict(history): 
    fit = np.polyfit(np.arange(len(history)), history, 3)
    fit_fn = np.poly1d(fit)

    prediction = int(fit_fn(len(history)) - fit_fn(len(history) - 1))

    return prediction if prediction > 0 else 0

