""" Models """
from exceptions import EnemyDown, GameOver
from random import randrange
from settings import *


def print_score(func):
    """Decorator that prints function name before the func and score after."""

    def wrapper(self, enemy_obj):
        print('=' * 13 + func.__name__.capitalize() + '=' * 13)
        res = func(self, enemy_obj)
        print('-' * 14 + f'\nScore: {self.score}\n')
        return res

    return wrapper


class Enemy:
    """Model of enemy. Used for stone/scissors/paper game concept"""

    @staticmethod
    def select_attack() -> int:
        """Random choice of attack/defence."""
        return randrange(1, 4)

    def __init__(self, level: int, enemy_lives: int):
        self.level = level
        self.lives = enemy_lives

    def decrease_lives(self):
        """
        Called after successful attack from player.
        Decrease lives and raise EnemyDown exception when lives == 0.

        """
        self.lives -= 1
        print('Enemy`s HP: ', self.lives)
        if self.lives == 0:
            raise EnemyDown


class Player:
    """Model of player. Used for stone/scissors/paper game concept"""

    def __init__(self, name: str):
        self.name = name
        self.player_lives = PLAYER_LIVES
        self.score = SCORE

    @staticmethod
    def fight(attack, defence) -> int:
        """
        Takes two parameters (attack, defence)
        Compares who has won.

        """
        if attack in ALLOWED_MOVES and defence in ALLOWED_MOVES:
            if attack == defence:
                return 0
            elif attack - defence == -1 or attack - defence == 2:
                return 1
            else:
                return -1
        else:
            print('Not Valid input!')

    @print_score
    def attack(self, enemy_obj):
        """
        Takes player's move (attack) and enemy's move (defence)
        Checks user input validity, after calls fight method.
        Shows fight result.

        """
        while True:
            try:
                user_input = int(input())
                if user_input in ALLOWED_MOVES:
                    break
            except ValueError:
                pass
            print(f'Please, insert valid symbol! {list(ALLOWED_MOVES)}\n')

        match_res = Player.fight(user_input, enemy_obj.select_attack())
        if match_res == 0:
            print('It\'s a draw!')
        elif match_res == 1:
            self.score += 1
            Enemy.decrease_lives(enemy_obj)
            print('You attacked successfully! +1 point!')
        elif match_res == -1:
            print('You missed...')

    @print_score
    def defence(self, enemy_obj):
        """
        Takes player's move (defence) and enemy's move (attack)
        Checks user input validity, after calls fight method.
        Shows fight result.

        """
        while True:
            try:
                user_input = int(input())
                if user_input in ALLOWED_MOVES:
                    break
            except ValueError:
                pass
            print(f'Please, insert valid symbol! {list(ALLOWED_MOVES)}\n')

        match_res = Player.fight(enemy_obj.select_attack(), user_input)
        if match_res == 0:
            print('It\'s a draw!')
        elif match_res == 1:
            Player.decrease_lives(self)
            print('Opponent attacked successfully...')
        elif match_res == -1:
            print('Opponent missed!')

    def decrease_lives(self):
        """
        Called after successful attack from enemy.
        Decrease lives and raise GameOver exception when lives = 0.

        """
        self.player_lives -= 1
        if self.player_lives == 0:
            print(f'{self.name} died!\n')
            raise GameOver
        print('Player`s HP: ', self.player_lives)

    def get_score(self):
        """
        Shows top scores.
        If you in the table - you will see your scores next to your name.

        """
        flag = True
        while True:
            print(f'Do you want to get final top-{TOP} scores? (y ; n) \n')
            user_input = input()
            if user_input == 'y':
                print(f'Top-{TOP}:')
                for score in GameOver.check_lines():
                    if int(score) == self.score and flag:
                        print(f'{score} - {self.name}')
                        flag = False
                        continue
                    print(score)
            elif user_input != 'n':
                continue
            break
        print(f'\nThanks for playing, {self.name}!')
