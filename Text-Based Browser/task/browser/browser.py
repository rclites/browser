import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore


class Browser:
    commands = {'exit', 'back'}
    tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']

    def __init__(self):
        self.folder = sys.argv[1]
        self.history = list()
        self.status = True

    # create a directory
    @staticmethod
    def create_dir(dir_name):
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)

    # exit and back commands
    def user_commands(self, action):
        if action == 'exit':
            self.status = False
        elif action == 'back':
            if len(self.history) > 1:
                self.history.pop()
                data = self.read_data_from_file(self.history[-1])
                print(data)

    # read data from file
    def read_data_from_file(self, file_name):
        path = self.folder + '/' + file_name + '.txt'
        data = open(path, 'r').read()
        return data

    # write data to file
    def write_data_to_tile(self, user_input, data):
        Browser.create_dir(self.folder)
        file_name = '.'.join(user_input.split('.')[:-1])

        self.history.append(file_name)

        path = self.folder + '/' + file_name + '.txt'
        with open(path, 'w') as file:
            file.write(data)

    # read data from URL
    @staticmethod
    def read_data_from_url(user_input):
        url = Browser.url_check(user_input)
        url_data = requests.get(url)
        return url_data.text

    # check/clean the URL
    @staticmethod
    def url_check(user_input):
        url = user_input if user_input.startswith('https://') else 'https://' + user_input
        return url

    # clean URL data
    @staticmethod
    def clean_url_data(url_data):
        soup = BeautifulSoup(url_data, 'html.parser')
        clean_data = '\n'.join([line.get_text().strip() for tag in Browser.tags for line in soup.find_all(tag)])
        return clean_data

    # main program
    def run(self):
        while self.status:
            user_input = input()
            if user_input in Browser.commands:
                self.user_commands(user_input)
                continue
            if user_input in self.history:
                print(self.read_data_from_file(user_input))
                continue
            if user_input not in self.history and user_input.count('.') == 0:
                print('Error Incorrect URL\n')
                continue

            url_data = Browser.read_data_from_url(user_input)
            clean_data = Browser.clean_url_data(url_data)
            print(Fore.BLUE + clean_data)

            if user_input not in self.history:
                self.write_data_to_tile(user_input, clean_data)


if __name__ == '__main__':
    browser = Browser()
    browser.run()
