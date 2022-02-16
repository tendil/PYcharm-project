class Method():
    @classmethod
    def skills_access(cls, self):
        pass

    @classmethod
    def job_access(cls, Name):
        if Name._job == cls.__name__:
            return True
        else: 
            return False


class Person:
    # * - все параметры по правую сторону будут исключительно именнованными
    def __init__(self,
                 *, 
                 growth: float = 160.0,
                 wight: float = 60.0,
                 hair_color: str = 'brown',
                 race: str = 'white',
                 saving: int = 500
                 ):
        
        self._growth = growth                           # Рост
        self._wight = wight                             # Вес
        self._hair_color = hair_color                   # Цвет глаз
        self._satiety = 100                             # Сытость
        self._thirsty = 0                               # Жажда
        self._race = race                               # Человек True or Black
        self._saving = saving                           # Сбережения
        self._job = None                                # Должность
    def who_i_am(self):                                 # Кто я такой?
        if self._race == 'black':
            print('Ты просто нигга.')
        else:
            print(f'Рост {self._growth}, вес {self._wight}, раса {self._race}, цвет волос {self._hair_color}.')

    def my_job(self):
        return f'Я {self._job}'

    def phis_stats(self):
        return f'Жажда: {self._thirsty},  голод: {self._satiety}'

    def get_eating(self):
        self._satiety += 25
        print('*Кушает*')

    def have_a_drinking(self):
        self._thirsty -= 25
        print('*Пьёт*')

    def to_tolking(self):
        print('Разговаривает')

    @property
    def saving(self):
        return f'У меня в копилке: ${self._saving}'


class Cleaning_Master(Method):
    def __init__(self):
        pass

    def clean_up(self):             # Убраться
        print('*Вытираю лужу*')


class Technician(Method):
    def __init__(self):
        pass

    def to_repair(self):
        if Technician.job_access(self):
            print('*Чиню поломку*')
        else:
            print('Фу, я ведь не чёрный, чтобы это делать(!')

    def washing(self):
        if Technician.job_access(self):
            print('Смываю грязь, оттираю мазуту')
        else:
            print('Фу, я ведь не чёрный, чтобы это делать!(')


class Cook(Method):
    def __init__(self):
        pass

    def cooking(self):
        print('*Готовлю суп*')

    def cleaning_workplace(self):                       # уборка рабочего места
        if Cook.job_access(self):
            print('*Привожу рабочее место в порядок*')
        else:
            print('Почему я? Я ведь даже не повар...')

    def cake(self):
        if Cook.job_access(self):
            print('*Готовлю торт к выдаче*')
        else:
            print('Почему я? Я ведь даже не повар...')


class Sales_Manager(Method):
    def __init__(self):
        pass

    def sell_ivent(self):
        if Sales_Manager.job_access(self):
            print('*Почти продал человеку мероприятие!*')
        else:
            print('Я не занимаю нужную должность')

    def base_clients(self):
        if Sales_Manager.job_access(self):
            print('*Обновляю базу клиентов*')
        else:
            print('Я не занимаю нужную должность')

    def compiling_a_report(self):
        if Sales_Manager.job_access(self):
            print('*Составляю отчёт по итогу мероприятия*')
        else:
            print('Я не занимаю нужную должность')

    def selection_of_premises(self):
        if Sales_Manager.job_access(self):
            print('*Подбираю крутую локацию для бомбического мероприятия*')
        else:
            print('Я не занимаю нужную должность')


class Event_Manager(Method):
    def __init__(self):
        pass

    def recruitment(self):
        if Event_Manager.job_access(self):
            print('*Набираю персонал для мероприятия*')
        else:
            print('Но я ведь не работаю как Event Manager')


class Directory(Method):
    def __init__(self):
        pass

    def pay_a_salary(self):
        if Directory.job_access(self):
            print('*Выдаю зарплату за февраль месяц*')
        else:
            print('*Нет, не буду это делать, я за эту работу плачу людям деньги!!!*')


class Creachars(Person, Directory, Event_Manager, Sales_Manager, Cook, Technician, Cleaning_Master):
    def __init__(self):
        Person.__init__(self)

    def get_skils(self, NameSkils):
        NameSkils.__init__(self)

    def get_work(self, NameJob : str):
        self._job = NameJob













