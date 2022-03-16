def numberToWords(num: int):
    if num == 0:
        return 'Zero'
    string = str(num)[::-1]
    size = len(string)
    triplets = []
    counter = 0
    for n in range(size):
        if counter < size - 1:
            triplets.append(string[counter:counter + 3][::-1])
        counter += 3
    remain = size % 3
    if remain and remain != 2:
        triplets += [string[remain * -1:]]
    triplets.reverse()
    thou = ['', 'thousand ', 'million ', 'billion ']
    to_19 = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six',
             '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven',
             '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen',
             '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
    dozens = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy',
              '8': 'eighty', '9': 'ninety'}
    all_words = []
    word = ''
    for i in triplets:
        if len(i) == 3:
            if i[0] != '0':
                word += f'{to_19[i[0]]} hundred '
            if i[1] == '1':
                word += f'{to_19[i[1:3]]} '
            elif i[1] == '0':
                word += f'{to_19[i[2:3]]} '
            else:
                word += f'{dozens[i[1]]} '
                if i[2] != '0':
                    word += f'{to_19[i[2]]} '
        elif len(i) == 2:
            if i[0] in ['1', '0']:
                word += f'{to_19[i]} '
            else:
                word += f'{dozens[i[0]]} '
                if i[1] != '0':
                    word += f'{to_19[i[1]]} '
        elif len(i) == 1:
            word = f'{to_19[i]} '
        all_words += [word]
        word = ''
    final = []
    counter = 0
    s = len(all_words) - 1
    last = 0
    for i in range(len(all_words)):
        if all_words[counter] == ' ':
            last += 1
        else:
            last = 0
        if last < 1:
            final += [f'{all_words[counter].strip()} {thou[s].strip()} ']
        s -= 1
        counter += 1
    final = (''.join(final)).strip()
    return final.title()

# https://leetcode.com/problems/integer-to-english-words/
# Mais de 2 horas aqui, finalmente consegui, meuamigo essa foi pancada, o código está mal organizado e longo, porém...
# ...cumpre a função e por incrível que pareça está mais rápido que 92% das submissions no leetcode
# 1 mês e 2 dias estudando programação
