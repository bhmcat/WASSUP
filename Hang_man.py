import random
hanging = ['''
     -------|
     :      |
     O      |
    /|\     |
    / \     |
            |
            |
            |
===========================''',
'''
     -------|
     :      |
     O      |
    /|\     |
    /       |
            |
            |
            |
===========================''',
'''
     -------|
     :      |
     O      |
    /|\     |
            |
            |
            |
            |
===========================''',
'''
     -------|
     :      |
     O      |
    /|      |
            |
            |
            |
            |
===========================''',
'''
     -------|
     :      |
     O      |
    /       |
            |
            |
            |
            |
===========================''',
'''
     -------|
     :      |
     O      |
            |
            |
            |
            |
            |
===========================''',
'''
     -------|
     :      |
            |
            |
            |
            |
            |
            |
===========================''']


class Hang_man():
    def __init__(self, word_ls):
        self.word_ls = word_ls
        self.game_word = random.choice(word_ls)
        self.guess_word = ['_'] * len(self.game_word)
        self.chance = 6

    def run(self):
        while self.chance != 0:
            print(hanging[self.chance])
            print(' '.join(self.guess_word))
            print(f'남은기회 : {self.chance}')
            guess = input('맞춰봐라').lower()
            
            if len(guess) != 1:
                print('한글자만 입력해라...')
                continue

            if guess in self.game_word:
                print('딩동~')
                for index, data in enumerate(self.game_word):
                    if data == guess:
                        self.guess_word[index] = data
            elif guess not in self.game_word:
                print('땡~')
                self.chance -= 1
            
            if '_' not in self.guess_word:
                print('잘~ 했다~')
                print(f'결과 : {" ".join(self.guess_word)}')
                break
        if '_' in self.guess_word:
            print(hanging[self.chance])
            print('에휴...')
            print(f'결과 : {" ".join(self.guess_word)}\n정답 : {self.game_word} ')


word_ls = ['python', 'wassup', 'apple', 'google']
play = Hang_man(word_ls)
play.run()