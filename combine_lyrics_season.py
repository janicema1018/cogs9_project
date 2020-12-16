import os
import codecs

for root, dirs, files in os.walk(r"/Users/janice/Desktop/cogs 9/sheldon_lyrics_scrape"):
    for dir in dirs:
        if dir.startswith("Series"):
            inner_path = os.path.join("/Users/janice/Desktop/cogs 9/sheldon_lyrics_scrape", dir)
            for root, dirs, files in os.walk(inner_path):
                for file in files:
                    if file.startswith("Series"):
                        print(file)
                        with codecs.open(os.path.join(inner_path, file), "r", "utf-8") as fr:
                            with codecs.open(os.path.join(inner_path, "combined_series_" + dir), "a", "utf-8") as fw:
                                for line in fr:
                                    fw.write(line)

