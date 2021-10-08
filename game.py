from models import Player, Enemy, GameOver, EnemyDown
from settings import ENEMY_LEVEL, ENEMY_LIVES, TOP

final_result = player = None


def play():
    """
    Check validity of name input.
    In the cycle calls player's attack/defence methods.
    When EnemyDown exception risen - +5 points and creates enemy with increased level by one.
    When GameOver exception risen - makes scores global and raises GameOver exception again.

    """
    while True:
        name_input = input('Your nickname: ')
        print()
        if name_input.isdigit():
            print('Name can\'t consist only numeric symbols!\n')
        elif not 2 < len(name_input) < 32:
            print('Please, change your name.\n')
        else:
            break

    global player
    player = Player(name_input)
    enemy = Enemy(ENEMY_LIVES, ENEMY_LEVEL)
    level = 1
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown:
            player.score += 5
            enemy = Enemy(ENEMY_LIVES + level, ENEMY_LEVEL + level)
            level += 1
            print('You have killed the opponent. +5 points!')
            print('-' * 14 + f'\nScore: {player.score}\n')
        except GameOver:
            global final_result
            final_result = player.score
            raise GameOver


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        pass
    except GameOver:
        if len(GameOver.check_lines()) < TOP:
            GameOver.append_lines(str(final_result))
        else:
            GameOver.write_lines(str(final_result))
        GameOver.sort_lines()
    finally:
        player.get_score()
        print('Good bye!')
