import os

open('formulas.txt', 'w').close()

# values = ['arc*', 'cli*', 'const*', 'contr*', 'oth*', 'prof*', 'stru*', 'subc*', 'sup*']

# values = ['app*', 'cons*', 'eng*', 'health*', 'IT', 'oth*', 'proc*', 'proj*', 'QS', 'Senio*', 'Sit*', 'Trade*']

# values = ['up*', 'bet*', '£10*', 'ov*']

# values = ['und*', '50*', '101*', 'more*']

with open('formulas.txt', 'wt') as output:
    beginning = 3
    end = 11
    sum_range = 'SUM(S{}:S{},U{}:U{},W{}:W{})'.format(beginning, end, beginning, end, beginning, end)
    letter = 'SUW'
    col_range = [beginning, end+1]
    for l in letter:
        for i in range(col_range[0], col_range[1]):
            print('={}{}/{}'.format(l, i, sum_range))
            output.write('={}{}/{}\n'.format(l, i, sum_range))
        output.write('\n')
        print('\n')


# cols = ['ay', 'az', 'ba', 'bb', 'bc', 'bd', 'be', 'bf']
# vals = ['co', 'sk', 'pr', 'oth']
# k_cols = 'hijklmnopqr'
#
# with open('formulas.txt', 'wt') as output:
#     letter = 'af'
#     cell_ref = 'Imported!{}4:{}2000'.format(letter, letter)
#     for k in k_cols:
#         for c in cols:
#             output.write('=COUNTIFS(Imported!{}4:{}2000, "*", Imported!a{}4:a{}2000, "*")\n'.format(c, c, k, k))
#         output.write('\n')

# with open('formulas.txt', 'wt') as output:
#     letter = 'af'
#     cell_ref = 'Imported!{}4:{}2000'.format(letter, letter)
#     for v in vals:
#         for c in cols:
#             output.write('=COUNTIFS(Imported!{}4:{}2000, "*", {}, "{}*")\n'.format(c, c, cell_ref, v))


# with open('formulas.txt', 'wt') as output:
#     letter = 'af'
#     field = '",Imported!{}4:{}2000,'.format(letter, letter)
#     for v in values:
#         output.write("{}{}{}{}\n".format('=COUNTIFS(Imported!bh4:bh2000,"', v, field,'"{}*")'.format("c")))
#     for v in values:
#         output.write("{}{}{}{}\n".format('=COUNTIFS(Imported!bh4:bh2000,"', v, field,'"{}*")'.format("s")))
#     for v in values:
#         output.write("{}{}{}{}\n".format('=COUNTIFS(Imported!bh4:bh2000,"', v, field,'"{}*")'.format("p")))
#     for v in values:
#         output.write("{}{}{}{}\n".format('=COUNTIFS(Imported!bh4:bh2000,"', v, field,'"{}*")'.format("o")))
# with open('formulas.txt', 'wt') as output:
#     # for v in values:
#     #     output.write("{}{}{}\n".format('=COUNTIFS(Imported!AS4:AS2000,"', v, '",Imported!w4:w2000, "All of*")'))
#     refs = ['x', 'y', 'z', 'aa', 'ab', 'ac', 'ad']
#     letter = 'af'
#     field = '",Imported!{}4:{}2000,'.format(letter, letter)
#     for i in refs:
#         print('",Imported!{}4:{}2000,'.format(i, i))
#         field = '",Imported!{}4:{}2000,'.format(i, i)
#         for v in values:
#             output.write("{}{}{}{}\n".format('=COUNTIFS(Imported!bh4:bh2000,"', v, field,'"*")'))
#         output.write('\n')


os.system('start formulas.txt')
