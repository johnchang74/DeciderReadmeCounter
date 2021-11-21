import requests
from bs4 import BeautifulSoup


# Extract the first 300 characters from readme file
# output.txt file will be produced at the end of successful run
class DeciderExtractor:
    # initializing html parser object after calling the online readme file
    def __init__(self):
        decider_readme = 'https://github.com/mvoloskov/decider#readme'
        self.readme_content = ''
        try:
            resp = requests.get(decider_readme)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                readme_content = soup.find_all(id='readme')
                self.readme_content = readme_content[0].text.strip()
            else:
                raise ValueError('decider readme file not reachable!')
        except any:
            print(any)

    # return the first 300 characters
    def get_first_three_hundred_chars(self):
        return self.readme_content[0:300]


if __name__ == "__main__":
    extractor = DeciderExtractor()
    print(extractor.get_first_three_hundred_chars())
    f = open('output.txt', 'w')
    try:
        f.write(extractor.get_first_three_hundred_chars())
        f.write('\n')
        f.flush()
    except any:
        print(any)
    finally:
        if f is not None:
            f.close()

