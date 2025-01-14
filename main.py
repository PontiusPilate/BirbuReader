from kivy_deps import sdl2, glew
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from bs4 import BeautifulSoup
import requests

# Window.size = (480, 853)

class CommonHeader(AnchorLayout):
    header_text = StringProperty('Главное меню')

class MainScreen(Screen):
    header_text = StringProperty("Главное меню")

class FifthFScreen(Screen):
    header_text = StringProperty("Лит-ра 5-го класса")

class SixthFScreen(Screen):
    header_text = StringProperty("Лит-ра 6-го класса")

class SeventhFScreen(Screen):
    header_text = StringProperty("Лит-ра 7-го класса")

class EighthFScreen(Screen):
    header_text = StringProperty("Лит-ра 8-го класса")

class NinthFScreen(Screen):
    header_text = StringProperty("Лит-ра 9-го класса")

class TenthFScreen(Screen):
    header_text = StringProperty("Лит-ра 10-го класса")

class EleventhFScreen(Screen):
    header_text = StringProperty("Лит-ра 11-го класса")

class ScrollableLabel(ScrollView):
    pass

class Reader(Screen):
    work_text = StringProperty("")

class Config(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

class MyApp(MDApp):
    work = ''
    name = ''
    class_ = ''

    urls = {
        'Гомер, "Одиссея"': 'https://www.litres.ru/book/gomer/odisseya-146616/chitat-onlayn/',
        '"Царевна-лягушка"': 'https://www.litres.ru/book/narodnoe-tvorchestvo/carevna-lyagushka-4743072/chitat-onlayn/',
        '"Падчерица"': 'https://nukadeti.ru/skazki/doch_i_padcherica',
        'Эзоп, басни': 'https://www.litres.ru/book/ezop/basni-145542/chitat-onlayn/',
        'М. Ю Лермонтов, "Бородино"': 'https://www.culture.ru/poems/36608/borodino',
        'И. С. Тургенев, "Муму"': 'https://ilibrary.ru/text/1250/p.1/index.html',
        'Л. Н. Толстой, "Кавказский пленник"': 'https://ilibrary.ru/text/1846/p.1/index.html',

        'А. С. Пушкин, "Повести Белкина"': 'https://www.litres.ru/book/aleksandr-pushkin/povesti-belkina-171969/chitat-onlayn/',
        'Н. В. Гоголь, "Тарас Бульба"': 'https://www.litres.ru/book/nikolay-gogol/taras-bulba-19429600/chitat-onlayn/',
        'И. А. Крылов, "Ворона и Лисица"': 'https://deti-online.com/basni/basni-krylova/vorona-i-lisica/',
        'В. М. Шукшин, "Срезал"': 'https://azbyka.ru/fiction/srezal-sbornik-rasskazov/',
        'А. П. Чехов, "Каштанка"': 'https://www.litres.ru/book/anton-chehov/kashtanka-172108/chitat-onlayn/',
        'М. Твен, "Приключения Тома Сойера"': 'https://www.litres.ru/book/mark-twain/priklucheniya-toma-soyera-49789078/chitat-onlayn/',
        'Д. Дефо, "Робинзон Крузо"': 'https://www.litres.ru/book/daniel-defo/robinzon-kruzo-136433/chitat-onlayn/',

        'Н. В. Гоголь, "Шинель"': 'litres.ru/book/nikolay-gogol/shinel-173495/chitat-onlayn/',
        'А. С. Пушкин, "Полтава"': 'https://www.litres.ru/book/aleksandr-pushkin/poltava-171970/chitat-onlayn/',
        'Д. И. Фонвизин, "Недоросль"': 'https://www.litres.ru/book/denis-fonvizin/nedorosl-176530/chitat-onlayn/',
        'И. С. Тургенев, "Записки охотника"': 'https://knijky.ru/books/zapiski-ohotnika',
        'А. П. Чехов, "Хамелеон"': 'https://www.litres.ru/book/anton-chehov/hameleon-172167/chitat-onlayn/',
        'В. А. Жуковский, "Светлана"': 'https://www.litres.ru/book/vasiliy-andreevich-zhukovskiy/svetlana-21119198/chitat-onlayn/',
        'Д. Лондон, "Белый Клык"': 'https://www.litres.ru/book/dzhek-london/belyy-klyk-6982549/chitat-onlayn/',

        'А. С. Пушкин, "Капитанская дочка"': 'https://www.litres.ru/book/aleksandr-pushkin/kapitanskaya-dochka-171967/chitat-onlayn/',
        'М. Ю. Лермонтов, "Мцыри"': 'https://www.litres.ru/book/mihail-lermontov/mcyri-175922/chitat-onlayn/',
        'И. С. Тургенев, "Ася"': 'https://www.litres.ru/book/ivan-turgenev/asya-172010/chitat-onlayn/',
        'Л. Н. Толстой, "После бала': 'https://www.litres.ru/book/lev-tolstoy/posle-bala-172377/chitat-onlayn/',
        'У. Шекспир, "Ромео и Джульетта"': 'https://www.litres.ru/book/uilyam-shekspir/romeo-i-dzhuletta-25102035/chitat-onlayn/',
        'В. Скотт, "Айвенго"': 'https://www.litres.ru/book/valter-skott/ayvengo-125383/chitat-onlayn/',
        'У. Шекспир, "Гамлет"': 'https://www.litres.ru/book/uilyam-shekspir/gamlet-princ-datskiy-25102038/chitat-onlayn/',

        'Н. М. Карамзин, "Бедная Лиза"': 'https://www.litres.ru/book/nikolay-karamzin/bednaya-liza-7368680/chitat-onlayn/',
        'А. С. Грибоедов, "Горе от ума"': 'https://www.litres.ru/book/aleksandr-griboedov/gore-ot-uma-148277/chitat-onlayn/',
        'А. С. Пушкин, "Евгений Онегин"': 'https://www.litres.ru/book/aleksandr-pushkin/evgeniy-onegin-171966/chitat-onlayn/',
        'М. Ю. Лермонтов, "Герой нашего времени"': 'https://www.litres.ru/book/mihail-lermontov/geroy-nashego-vremeni-172009/chitat-onlayn/',
        'Н. В. Гоголь, "Мёртвые души"': 'https://www.litres.ru/book/nikolay-gogol/mertvye-dushi-171960/chitat-onlayn/',
        'И. С. Тургенев, "Первая любовь"': 'https://www.litres.ru/book/ivan-turgenev/pervaya-lubov-4929843/chitat-onlayn/',
        'М. А. Шолохов, "Судьба человека"': 'https://azbyka.ru/fiction/sudba-cheloveka-mihail-sholohov/',

        'И. А. Гончаров, "Обломов"': 'https://www.litres.ru/book/ivan-goncharov/oblomov-172015/chitat-onlayn/',
        'А. И. Островский, "Гроза"': 'https://www.litres.ru/book/aleksandr-ostrovskiy/groza-172629/chitat-onlayn/',
        'И. С. Тургенев, "Отцы и дети"': 'http://loveread.ec/read_book.php?id=12021&p=1',
        'А. П. Чехов, "Вишнёвый сад': 'https://www.litres.ru/book/anton-chehov/vishnevyy-sad-172106/chitat-onlayn/',
        'Н. А. Некрасов, "Кому на Руси жить хорошо..."': 'https://www.litres.ru/book/nikolay-nekrasov/komu-na-rusi-zhit-horosho-173705/chitat-onlayn/',
        'Ф. М. Достоевский, "Преступление и наказание"': 'https://www.litres.ru/book/fedor-dostoevskiy/prestuplenie-i-nakazanie-139491/chitat-onlayn/',
        'Л. Н. Толстой, "Война и мир"': 'https://mybook.ru/author/lev-tolstoj/vojna-i-mir-3/read/',

        'М. А. Булгаков, "Мастер и Маргарита"': 'http://loveread.ec/read_book.php?id=1527&p=1',
        'М. А. Шолохов, "Тихий Дон" (1 книга)': 'http://loveread.ec/read_book.php?id=14716&p=1',
        'М. А. Шолохов, "Тихий Дон" (2 книга)': 'http://loveread.ec/read_book.php?id=14717&p=1',
        'Б. Л. Пастернак, "Доктор Живаго"': 'http://loveread.ec/read_book.php?id=10611&p=1',
        'А. А. Блок, "Двенадцать"': 'https://www.litres.ru/book/aleksandr-blok/dvenadcat-172337/chitat-onlayn/',
        'А. А. Ахматова, "Реквием"': 'https://www.culture.ru/poems/10174/rekviem',
        'Е. И. Замятин, "Мы"': 'http://loveread.ec/read_book.php?id=13045&p=1',
        'М. Горький, "На дне"': 'https://www.litres.ru/book/maksim-gorkiy/na-dne-172750/chitat-onlayn/?page=1'
    }

    number = 1
    label_text = StringProperty(f'Стр. {number}')

    # button_color = (0.16, 0.48, 0.32, 1)
    # label_color = (0.24, 0.71, 0.48, 1)
    # bg_color = (0.08, 0.25, 0.16, 1)
    # text_color = (1, 1, 1, 1)

    def build(self):
        root = Builder.load_string(open("my.kv", encoding="utf-8").read())
        return root

    # def change_color(self, color):
    #     colors = {
    #         'green': [[0.16, 0.48, 0.32, 1], [0.24, 0.71, 0.48, 1], [0.08, 0.25, 0.16, 1], 'white'],
    #         'blue': [[0.94, 0.42, 0.42, 1], [0.85, 0.18, 0.18, 1], [0.67, 0.16, 0.16, 1], 'white'],
    #         'white': [[0.85, 0.85, 0.91, 1], [0.73, 0.73, 0.79, 1], [1, 1, 1, 1], 'black'],
    #         'black': [[0.23, 0.23, 0.24, 1], [0.32, 0.32, 0.34, 1], [0, 0, 0, 1], 'white']
    #     }
    #
    #     MyApp.button_color = ListProperty(colors.get(color)[0])
    #     MyApp.label_color = ListProperty(colors.get(color)[1])
    #     MyApp.bg_color = ListProperty(colors.get(color)[2])
    #     MyApp.text_color = ListProperty(colors.get(color)[3])
    #
    #     Clock.schedule_once(self.update_ui, 0)
    #
    # def update_ui(self, *args):
    #     self.root.clear_widgets()
    #     self.root.add_widget(Builder.load_string(open("my.kv", encoding="utf-8").read()))

    def get_data(self, work, name, class_):
        self.work = work
        self.name = name
        self.class_ = class_

    def change_screen(self, screen_name):
        self.root.current = screen_name
        current_screen = self.root.get_screen(screen_name)
        if hasattr(current_screen, "header_text"):
            self.root.get_screen(screen_name).ids.common_header.header_text = current_screen.header_text

        MyApp.number = 1
        self.label_text = f'Стр. {MyApp.number}'


    def btn_press(self):
        work = MyApp.work
        name = MyApp.name
        class_ = MyApp.class_

        url = MyApp.urls.get(str(work))
        if not url:
            return

        data = ''

        try:
            request = requests.get(url)
            soup = BeautifulSoup(request.text, "html.parser")

            if class_ == '0':
                elements = soup.find_all(name)
            else:
                elements = soup.find_all(name, class_)

            for element in elements:
                data = element.get_text(separator='\n')

        except Exception as e:
            data = f"Ошибка загрузки: {e}"

        self.root.get_screen('reader').work_text = data

    def next_page(self):
        work = MyApp.work
        name = MyApp.name
        class_ = MyApp.class_

        sc = ScrollableLabel()
        data = ''
        MyApp.number += 1
        self.label_text = f'Стр. {MyApp.number}'

        if class_ == 'MsoNormal':
            url = MyApp.urls.get(work) + f'{MyApp.number}'
        else:
            url = MyApp.urls.get(work) + '?page=' + f'{MyApp.number}'

        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")
        if class_ == '0':
            elements = soup.find_all(name)
        else:
            elements = soup.find_all(name, class_=class_)
        for element in elements:
            data = element.get_text(separator='\n')
        self.root.get_screen('reader').work_text = data

    def previous_page(self):
        work = MyApp.work
        name = MyApp.name
        class_ = MyApp.class_

        data = ''
        if MyApp.number != 1:
            MyApp.number -= 1
        self.label_text = f'Стр. {MyApp.number}'

        if class_ == 'MsoNormal':
            url = MyApp.urls.get(work) + f'{MyApp.number}'
        else:
            url = MyApp.urls.get(work) + '?page=' + f'{MyApp.number}'

        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")
        if class_ == '0':
            elements = soup.find_all(name)
        else:
            elements = soup.find_all(name, class_=class_)
        for element in elements:
            data = element.get_text(separator='\n')

        self.root.get_screen('reader').work_text = data

if __name__ == '__main__':
    MyApp().run()