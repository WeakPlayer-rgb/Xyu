import bs4
import requests

class VkBot:

    def __init__(self, user_id):
        print('\n'+'Я родился')
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)

        self._COMMANDS = ['ПРИВЕТ','ЗАКАЗ']

    def _get_user_name_from_vk_id(self,user_id):
        request  = requests.get('https://vk.com/id'+str(user_id))
        bs = bs4.BeautifulSoup(request.text,'html.parser')

        user_name = self._clean_all_tag_from_str(bs.findAll('title')[0])

        return user_name.split()[0]

    def new_message(self,message):
        if message.upper() == self._COMMANDS[0]:
            return f'Дарова, {self._USERNAME}!'
        elif message.upper() == self._COMMANDS[1]:
            return self.search_sportmaster()
        else:
            return ('Хуй')

    def search_sportmaster(self):
        print("Ну допустим")
        return "Еее, бой"

    def _clean_all_tag_from_str(self,string_line):
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True
    
        return result
