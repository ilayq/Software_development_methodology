from abc import ABC
import random
import math


class UserInterfaceManager(ABC):

    name = None
    ask_name_str = "Welcome to the Brain Games!\nMay I have your name?"

    def greet(self) -> None:
        raise NotImplementedError

    def success(self) -> None:
        raise NotImplementedError

    def mistake(self, player_answer: str, correct_answer: str) -> None:
        raise NotImplementedError

    def question(self) -> None:
        raise NotImplementedError

    def your_answer(self) -> str:
        raise NotImplementedError


class UserCLIInterface(UserInterfaceManager):

    def greet(self) -> None:
        self.name = input(self.ask_name_str)
        print("Hello,", self.name)

    @staticmethod
    def print_str(*args, **kwargs) -> None:
        print(*args, **kwargs)

    def success(self) -> None:
        self.print_str("Correct!")
        congrats_string = f"Congratulations, {self.name}"
        self.print_str(congrats_string)

    def mistake(self, player_answer: str, correct_answer: str) -> None:
        self.print_str(f"{player_answer} is wrong answer;(. Correct answer was {correct_answer}")
        self.print_str("Let's try again,", self.name)

    def question(self, qs_string: str) -> None:
        self.print_str(f"Question: {qs_string}")

    def your_answer(self) -> str:
        ans = input("Your answer:")
        return ans


class Game(ABC):

    game_name: str = ''
    user_interface_manager_cls: UserInterfaceManager = UserInterfaceManager
    user_interface_manager: UserInterfaceManager = None
    num_games: int = 1
    infinite_num_games: bool = False

    def get_user_interface_manager(self) -> UserInterfaceManager:
        if self.user_interface_manager is None:
            self.user_interface_manager = self.user_interface_manager_cls()
        return self.user_interface_manager

    def do_try(self) -> bool:
        raise NotImplementedError

    def run(self):
        self.get_user_interface_manager().greet()
        self.get_user_interface_manager().print_str(f"{self.game_name}")
        game_num = 0
        while self.infinite_num_games or game_num < self.num_games:
            result = self.do_try()
            if result:
                game_num += 1
            else:
                break


class LCMGame(Game):
    game_name = "Find the smallest common multiple of given numbers."
    user_interface_manager_cls = UserCLIInterface
    infinite_num_games = True

    @staticmethod
    def lcm(a, b):
        """Функция для нахождения наименьшего общего кратного двух чисел."""
        return abs(a * b) // math.gcd(a, b)

    @staticmethod
    def lcm_of_three(a, b, c):
        """Функция для нахождения НОК трех чисел."""
        return LCMGame.lcm(LCMGame.lcm(a, b), c)

    def do_try(self) -> bool:
        numbers = [random.randint(1, 100) for _ in range(3)]
        correct_answer = self.lcm_of_three(*numbers)

        manager = self.get_user_interface_manager()
        manager.question(f"{numbers[0]} {numbers[1]} {numbers[2]}")
        user_answer = manager.your_answer()

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            manager.success() 
            return True
        else:
            manager.mistake(user_answer, str(correct_answer))
            return False


class GeomProgression(Game):
    game_name = "Геометрическая прогрессия"
    user_interface_manager_cls = UserCLIInterface
    infinite_num_games = True

    @staticmethod
    def geometric_progression():
        length = random.randint(5, 10)
        first_term = random.randint(1, 10)
        ratio = random.randint(2, 5)
        progression = [first_term * (ratio ** i) for i in range(length)]

        hidden_index = random.randint(0, length - 1)
        correct_answer = progression[hidden_index]
        progression[hidden_index] = ".."

        return progression, correct_answer

    def do_try(self) -> bool:
        manager = self.get_user_interface_manager()
        progression, correct_ans = self.geometric_progression()
        manager.question(str(progression))
        user_answer = manager.your_answer()

        if user_answer.isdigit() and int(user_answer) == correct_ans:
            manager.success() 
            return True
        else:
            manager.mistake(user_answer, str(correct_ans))
            return False

