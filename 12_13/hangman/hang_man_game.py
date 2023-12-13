from hangman_pics import final_hangman_pics

hangman_pics = final_hangman_pics


class HangManGame:
    MAX_INDEX = 7

    def __init__(self, word: str):
        length = len(word)
        self.answer: str = word
        self.current_my_word = '_' * length
        self.index = 0
        self.is_success = False

    def attempt(self, char: str) -> None:
        if not len(char) == 1:
            print('문자는 꼭 한 글자를 입력해 주세요. 다시 실행 합니다.')
            raise

        if self.__yes_or_no(char):
            self.__print_current_my_word()
            if self.__is_same(self.current_my_word):
                self.index = 7
        else:
            self.__print_all()

    def solve(self, word: str):
        if not self.__is_same(word):
            self.index += 1
            self.__print_all()
            return self

        self.index = self.MAX_INDEX

    def start(self) -> None:
        print('게임을 시작 합니다.')
        self.__print_all()

    def __print_all(self) -> None:
        self.print_hangman_status()
        self.__print_current_my_word()

    def print_hangman_status(self) -> None:
        print(hangman_pics[self.index])

    def __print_current_my_word(self) -> None:
        print(f'현재 까지 맞춘 단어 : {self.current_my_word}')

    def __is_same(self, word: str) -> bool:
        self.is_success = word.lower() == self.answer.lower()
        return self.is_success

    def __yes_or_no(self, char: str) -> bool:
        if char in self.answer:
            index_list = self.__get_index(char)
            self.current_my_word = self.__converting_my_word(index_list, char)
            return True

        self.index += 1
        return False

    def __get_index(self, char: str) -> list:
        result = []
        for i, c in enumerate(self.answer):
            if c == char:
                result.append(i)

        return result

    def __converting_my_word(self, idx_list: list, char: str) -> str:
        result = ''
        for i in range(len(self.answer)):
            if i in idx_list:
                result += char
            else:
                result += self.current_my_word[i]

        return result


def hangman_game_play():
    game = HangManGame("hangman")
    game.start()
    print(f'맞춰야 하는 단어는 {len(game.answer)} 글자 입니다.')
    while game.index < game.MAX_INDEX:
        challenge = input(f'문자를 입력 하세요. 정답을 알 것 같으면 숫자 {0}, 현재 Hangman의 상태를 보고 싶으면 {1} 을 입력해 주세요 : ')
        if challenge == '0':
            word = input('정답이라고 생각 하는 단어를 입력해 주세요. : ')
            game.solve(word)
        elif challenge == '1':
            game.print_hangman_status()
        else:
            try:
                game.attempt(challenge)
            except:
                continue

    if game.is_success:
        print('정답입니다.\n성공을 축하 합니다. 게임이 종료 됩니다.')
    else:
        print('실패입니다.\nhangman이 죽었습니다. 게임이 종료 됩니다.')


hangman_game_play()
