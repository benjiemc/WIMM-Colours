# WIMM-Colours
Theme for plotting libraries following WIMM branding colour scheme.

Clone the repository and then run `python install.py` to download the colour schemes.

## Examples

Matplotlib:

```python
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('wimm')

x = np.linspace(-10, 10)
y = x ** 2

plt.plot(x, y)
plt.show()
```
