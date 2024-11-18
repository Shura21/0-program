#Задача "Ошибка эволюции":
#Замечали, что некоторые животные в нашем мире обладают странными и, порой,
# несовместимыми друг с другом свойствами? Например, утконос... Вроде есть клюв, но не птица. Вроде милый,
# а есть шипы на задних лапах. А ещё он откладывает яйца... Опустим факт о том,
# что они потеют молоком и попробуем не эволюционным способом создать нашего утконоса.
#Необходимо написать 5 классов:
#Animal - класс описывающий животных.
#Класс обладает следующими атрибутами:
#live = True
#sound = None - звук (изначально отсутствует)
#_DEGREE_OF_DANGER = 0 - степень опасности существа
#Объект этого класса обладает следующими атрибутами:
#_cords = [0, 0, 0] - координаты в пространстве.
#speed = ... - скорость передвижения существа (определяется при создании объекта)
#И методами:
#move(self, dx, dy, dz), который должен менять соответствующие кооординаты
# в _cords на dx, dy и dz в том же порядке, где множетелем будет являтся speed.
# Если при попытке изменения координаты z в _cords значение будет меньше 0,
# то выводить сообщение "It's too deep, i can't dive :(") , при этом изменения не вносяться.
#get_cords(self), который выводит координаты в формате:
# "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
#attack(self), который выводит "Sorry, i'm peaceful :)",
# если степень опасности меньше 5 и "Be careful, i'm attacking you 0_0" , если равно или больше.
#speak(self), который выводит строку со звуком sound.
#Bird - класс описывающий птиц. Наследуется от Animal.
#Должен обладать атрибутом:
#beak = True - наличие клюва
#И методом:
#lay_eggs(self), который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
#AquaticAnimal - класс описывающий плавающего животного. Наследуется от Animal.
#В этом классе атрибут _DEGREE_OF_DANGER = 3.
#Должен обладать методом:
#dive_in(self, dz) - где dz изменение координаты z в _cords.
# Должен изменять в отрицательную сторону координату z уменьшенную в 2 раза с учётом скорости.
# С каким бы знаком не был передан параметр dz, внутри метода используйте его значение по модулю (функция abs).
#PoisonousAnimal - класс описывающий ядовитых животных. Наследуется от Animal.
#В этом классе атрибут _DEGREE_OF_DANGER = 8.
#Duckbill - класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal,
# PoisonousAnimal. Порядок наследования определите сами, опираясь на ниже приведённые примеры выполнения кода.
#Объект этого класса должен обладать одним дополнительным атрибутом:
#sound = "Click-click-click" - звук, который издаёт утконос
#Пример результата выполнения программы:
#Пример работы программы:
#db = Duckbill(10)
#print(db.live)
#print(db.beak)
#db.speak()
#db.attack()
#db.move(1, 2, 3)
#db.get_cords()
#db.dive_in(6)
#db.get_cords()
#db.lay_eggs()
#Вывод на консоль:
#True
#True
#Click-click-click
#Be careful, i'm attacking you 0_0
#X: 10 Y: 20 Z: 30
#X: 10 Y: 20 Z: 0
#Here are(is) 3 eggs for you # Число может быть другим (1-4)
#По итогу мы должны получить живого утконоса с клювом, атакующего и издающего странные звуки.
#После чего утконос совершает манёвры и ныряет.
#Теперь утконос в безопасности, он откладывает яйца для будущего потомства.
#Примечания:
#Будьте внимательней, когда вызываете методы классов родителей в классе наследнике при множественном наследовании:
# при обращении через super() методы будут искаться сначала в первом, потом во втором и т.д. классах по mro().
#При определении порядка наследования обратите внимание на то, что утконос атакует "Be careful, i'm attacking you 0_0"
import random
class Animal:
    def __init__(self, speed):
        self.live = True
        self.sound = None
        self._DEGREE_OF_DANGER = 0
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [new_x, new_y, new_z]

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        num_eggs = random.randint(1,4)
        print(f"Here are(is) {num_eggs} eggs for you")

class AquaticAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        # Корректировка координаты z
        z_change = abs(dz) * self.speed / 2
        new_z = self._cords[2] - z_change
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = new_z

class PoisonousAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        Bird.__init__(self, speed)
        AquaticAnimal.__init__(self, speed)
        PoisonousAnimal.__init__(self, speed)
        self.sound = "Click-click-click"
db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()