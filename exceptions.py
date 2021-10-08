class GameOver(Exception):
    @staticmethod
    def append_lines(my_result):
        """Appends score in file."""
        with open('scores.txt', 'a') as f:
            f.write(my_result+'\n')

    @staticmethod
    def check_lines():
        """Returns stored scores."""
        with open('scores.txt', 'r') as f:
            lines = f.read().splitlines()
            return lines

    @staticmethod
    def write_lines(my_result):
        """
        Writes scores into file.
        If final score is less than minimal score from file - just writes scores.
        If final score is greater than minimal score from file - changes minimal score on the final score.

        """
        file_lines = GameOver.check_lines()
        with open('scores.txt', 'w') as f:
            check_min = min(list(map(int, file_lines)))
            if check_min > int(my_result):
                str(my_result)
                my_return = [line + '\n' for line in file_lines]
                for line in my_return:
                    f.write(line)
            else:
                file_lines[file_lines.index(min(file_lines))] = my_result
                my_return = [line + '\n' for line in file_lines]
                for line in my_return:
                    f.write(line)

    @staticmethod
    def sort_lines():
        """
        Sorts results.
        Used after append_lines write_lines methods.

        """
        file_lines = sorted(GameOver.check_lines(), reverse=True)
        with open('scores.txt', 'w') as f:
            my_return = [line + '\n' for line in file_lines]
            for line in my_return:
                f.write(line)


class EnemyDown(Exception):
    """Raised when enemy is beaten"""
    pass
