# -*- coding: utf-8 -*-
# CREATED ON DATE: 25.05.15
__author__ = 'mail@pythonic.ninja'

# Polynolmial aprox sum 1091 CORMEN

DEBUG = True
LOG_LEVEL = 2

def log(*args, **kwargs):
    log_level = kwargs.get('log_level', 0)
    if DEBUG and log_level >= LOG_LEVEL:
        print " ".join([str(arg) for arg in args])


def trim(L, r):
    # m = len(L)
    L1 = [L[0]]
    last = L[0]
    for li in L:
        if last < (1 - r) * li:
            L1.append(li)
            last = li
    return L1


log('\ntrim:\t', trim([1, 104], 0.05), log_level=1)

def increase_list(L, value):
    return [entry + value for entry in L]

log('\nincrease_list\t', increase_list([1, 2, 3], 2), log_level=1)

def merge_list(L1, L2):
    result = []
    il, ir = 0, 0
    while il < len(L1) and ir < len(L2):
        log(il, ir)
        if L1[il] < L2[ir]:
            il += 1
            result.append(L1[il-1])
        else:
            ir += 1
            result.append(L2[ir-1])
        log(result)

    log(il, ir)
    log(result, L1, L2, L1[il:], L2[ir:])
    result += L1[il:] + L2[ir:]
    return result

log('\nmerge_list:\t', merge_list([1, 2, 3], [4, 5, 6]), log_level=1)

def approx_subset_sum(S, t, e):
    n = len(S)
    L0 = [[x] for x in range(1)]

    for i in xrange(1, n+1):
        log(i, L0, L0[i-1], S[i-1])
        item = merge_list(L0[i-1], increase_list(L0[i-1], S[i-1]))
        log(item)

        L0.append(item)

        log(i, log_level=2)
        log('Merge:\t', L0[i], log_level=2)
        L0[i] = trim(L0[i], 0.05)
        log('Trim:\t', L0[i], log_level=2)
        L0[i] = [item for item in L0[i] if item < t]
        log('Remove:\t', L0[i], log_level=2)
        log('', log_level=2)

        log(L0, log_level=1)

    return L0[n]

print(approx_subset_sum([104, 102, 201, 101], 308, 0.20))
