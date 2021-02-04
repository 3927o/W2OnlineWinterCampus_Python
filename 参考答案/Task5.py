import random


class Friend:
    def __init__(self, name, sex="unknown", age=0, money=0, tel=None, addr=None, edu_level=None):
        self.name = name
        self.sex = sex
        self.__age = age
        self.__money = money
        self.__tel = tel
        self.__addr = addr
        self.__edu_level = edu_level

    def talk(self, sentence):
        print(f"'{sentence}', {self.name} say")

    def buy(self, fee):
        self.__money -= fee

    def setdata(self, attr_name, value):
        setattr(self, attr_name, value)  # setattr()函数的用法请自行百度

    def display(self):
        print(f"""
Name: {self.name},
Sex: {self.sex},
Age: {self.__age},
Money: {self.__money},
Tel: {self.__tel},
Addr: {self.__addr},
EduLevel: {self.__edu_level},
""")


class MaBaoGuo(Friend):
    def talk(self):
        sentences = [
            "经典语录1",
            "经典语录2",
            "经典语录3",
            "经典语录4",
            "经典语录5",
        ]
        index_sentence = random.randint(0, 4)  # 该函数会从0~4之中取一个整数, random库的用法请自行百度
        print(sentences[index_sentence])


my_friend = Friend("lin")
my_friend.display()
my_friend.setdata("sex", "male")
my_friend.display()
my_friend.talk("hello!")
my_friend.buy(123)

保国 = MaBaoGuo("Teacher Ma")
保国.talk()
