# -*- coding: utf-8 -*-
# CREATED ON DATE: 25.05.15
__author__ = 'mail@pythonic.ninja'

# Polynolmial aprox sum 1091 CORMEN

DEBUG = True
LOG_LEVEL = 1

def log(*args, **kwargs):
    log_level = kwargs.get('log_level', 0)
    if DEBUG and log_level >= LOG_LEVEL:
        print " ".join([str(arg) for arg in args])


def trim(L, r):
    L1 = [L[0]]
    last = L1[-1]
    for yi in L:
        if last < (1 - r) * yi:
            L1.append(yi)
            last = yi
    return L1


log('\ntrim:\t', trim([0, 102, 201, 302, 303, 407], 0.05), log_level=1)


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
    L = [[0]]

    for i in xrange(1, n+1):
        log(i, L, L[i-1], S[i-1])
        item = merge_list(L[i-1], [item + S[i-1] for item in L[i-1]])
        log(item)

        L.append(item)

        log(i, log_level=2)
        log('Merge:\t', L[i], log_level=2)
        L[i] = trim(L[i], e/n)
        log('Trim:\t', L[i], log_level=2)
        L[i] = [item for item in L[i] if item < t]
        log('Remove:\t', L[i], log_level=2)
        log('', log_level=2)

        log(L, log_level=1)

    return L[-1][-1], L[-1][1:-1]

suma, choices = approx_subset_sum([104, 102, 201, 101], 308, 0.20)

print
print('Sigma    = %s = %s' % (suma, "+".join([str(choice) for choice in choices])))
print('Optiomal = %s = %s' % (307, "+".join([str(choice) for choice in [104, 102, 101]])))

