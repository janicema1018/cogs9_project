import codecs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


class Sheldon(object):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('window-size=1920x3000')
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=chrome_options)

    def run(self):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('window-size=1920x3000')
        inner_driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=chrome_options)

        parent_dir = "/Users/janice/Desktop/cogs 9/sheldon_lyrics_scrape"

        episodes = self.driver.find_elements_by_xpath('//div[@id="pages-2"]//li/a')
        episodes = [episode.get_attribute('href') for episode in episodes]
        episodes.remove("https://bigbangtrans.wordpress.com/about/")
        for episode in episodes:
            inner_driver.get(episode)

            filename = inner_driver.find_element_by_xpath('//div[@id="content"]//h2').text
            if "/" in filename:
                filename = filename.replace("/", "")

            if filename.startswith("Series 01"):
                directory = "Series 01"
            if filename.startswith("Series 02"):
                directory = "Series 02"
            if filename.startswith("Series 03"):
                directory = "Series 03"
            if filename.startswith("Series 04"):
                directory = "Series 04"
            if filename.startswith("Series 05"):
                directory = "Series 05"
            if filename.startswith("Series 06"):
                directory = "Series 06"
            if filename.startswith("Series 07"):
                directory = "Series 07"
            if filename.startswith("Series 08"):
                directory = "Series 08"
            if filename.startswith("Series 09"):
                directory = "Series 09"
            if filename.startswith("Series 10"):
                directory = "Series 10"
            path = os.path.join(parent_dir, directory)
            if not os.path.exists(path):
                os.mkdir(path)
            os.chdir(path)

            file = codecs.open(filename + ".txt", "a", "utf-8")
            lines = inner_driver.find_elements_by_xpath('//div[@class="entrytext"]//p')
            for line in lines:
                line = line.text
                if line.startswith("Sheldon"):
                    line = line.split(": ")[-1]

                    file.write(line + "\n")

        inner_driver.close()
        self.driver.close()


if __name__ == '__main__':
    new_spider = Sheldon()
    url = "https://bigbangtrans.wordpress.com/series-1-episode-1-pilot-episode/"
    new_spider.driver.get(url)
    new_spider.run()