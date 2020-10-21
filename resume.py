from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
# Text Variables
Header = '>>>This resume was generated entirely in Python. For full sourcecode, view my portfolio.'
# Setting style for bar graphs
import matplotlib.pyplot as plt
# %matplotlib inline
# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'
fig, ax = plt.subplots(figsize=(8.5, 11))
# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)
# set background color
ax.set_facecolor('white')
# remove axes
plt.axis('off')
# add text
plt.annotate(Header, (.02,.98), weight='regular', fontsize=8, alpha=.75)
plt.savefig('resumeexample.png', dpi=300, bbox_inches='tight')