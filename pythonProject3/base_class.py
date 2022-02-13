from random import choice


class Person:
    # * - все параметры по правую сторону будут исключительно именнованными
    def __init__(self, *,
                 growth: float = 160.0,
                 wight: float = 60,
                 hair_color: str = "brown",
                 race: str = 'white',
                 saving: int = 500
                 ):
        self._growth = growth  # Рост
        self._wight = wight  # Вес
        self._hair_color = hair_color  # Цвет глаз
        self._satiety = 100  # Сытость
        self._thirsty = 0  # Жажда
        self._race = race  # Человек True or Black
        self._saving = saving
        self._saving = 0
        self._job = None

    def who_i_am(self):
        if self._race == 'black':
            print('Ты просто нигга.')
        else:
            print(f'Рост {self._growth},'
                  f'вес {self._wight},'
                  f'раса {self._race},'
                  f'цвет волос {self._hair_color},'
                  f'сбережения {self._saving}.'
                  )
    def my_job(self):
        print(f'Я {self._job}')
    def phis_stats(self):
        print(f'Жажда: {self._thirsty},  голод: {self._satiety}')

    def get_eating(self):
        self._satiety += 25
        print('*Кушает*')

    def have_a_drinking(self):
        self._thirsty -= 25
        print('*Пьёт*')

    def to_tolking(self):
        print('Разговаривает')

    def give_up_my_job(self):
        self = 0
        # self = Person()

    @property
    def saving(self):
        print(f'У меня в копилке: ${self._saving}')
        return


class Cleaning_Master(Person):
    def __init__(self):
        Person.__init__(self)
        self._race = 'black'
        self._saving = -(choice(range(300, 500)))
        self._job = 'Cleaning Master'

    def clean_up(self):  # Убраться
        print('*Вытираю лужу*')


class Technician(Person):
    def __init__(self):
        Person.__init__(self)
        self._race = choice(['black', 'white'])
        self._job = 'Technican'

    def to_repair(self):
        print('*Чиню поломку*')

    def washing(self):
        print('Смываю грязь, оттираю мазуту')


class Cook(Person):
    def __init__(self):
        Person.__init__(self)
        self._satiety = 200
        self._job = 'Cook'

    def cooking(self):
        print('*Готовлю суп*')

    def cleaning_workplace(self):  # уборка рабочего места
        print('*Привожу рабочее место в порядок*')

    def cake(self):
        print('*Готовлю торт к выдаче*')


class Sales_Manager(Person):
    def __init__(self):
        Person.__init__(self)
        self._saving = choice(range(1000, 2000))
        self._job = 'Sales Manager'

    def sell_ivent(self):
        print('*Почти продал человеку мероприятие!*')

    def base_clients(self):
        print('*Обновляю базу клиентов*')

    def compiling_a_report(self):
        print('*Составляю отчёт по итогу мероприятия*')

    def selection_of_premises(self):
        print('*Подбираю крутую локацию для бомбического мероприятия*')


class Event_Manager(Person):
    def __init__(self):
        Person.__init__(self)
        self._saving = choice(range(1500, 3000))
        self._job = 'Event Manager'

    def recruitment(self):
        print('*Набираю персонал для мероприятия*')


class Directory(Event_Manager, Sales_Manager):
    def __init__(self):
        Person.__init__(self)
        self._saving = choice(range(2000, 40000))
        self._job = 'Director'

    def person_get_up(self, person):
        del person
