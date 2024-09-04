from sys import stdin
import typing as tp


def subsets(lst: tp.List[int]):
    for i in range(2 ** len(lst)):
        current = []
        for bit_idx in range(len(lst)):
            bit = (i >> bit_idx) & 1
            if bit:
                current.append(lst[bit_idx])
        yield current


exec("\n".join(stdin))
