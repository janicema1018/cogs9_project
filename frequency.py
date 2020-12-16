from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


# Read the whole text.
text = open("/Users/janice/Desktop/cogs 9/sheldon_lyrics_scrape/Series 01/combined_series_Series 01").read()

# read the mask / color image
sheldon_coloring = np.array(Image.open("sheldon_mask.jpg"))
stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=sheldon_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)
# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(sheldon_coloring)

# show
# fig, axes = plt.subplots(1, 3)
# axes[0].imshow(wc, interpolation="bilinear")
# # recolor wordcloud and show
# # we could also give color_func=image_colors directly in the constructor
# axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
# axes[2].imshow(sheldon_coloring, cmap=plt.cm.gray, interpolation="bilinear")
# for ax in axes:
#     ax.set_axis_off()
# plt.show()

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()