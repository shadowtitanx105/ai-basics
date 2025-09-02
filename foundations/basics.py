"""
Foundations: basic Python functions and sanity tests.
Run:  python foundations/basics.py
"""

from typing import List


def hello(name: str = "world") -> str:
    return f"hello, {name}"


def tokens_per_second(text: str, seconds: float) -> float:
    """
    Rough speech pacing proxy: words per second.
    """
    words = text.split()
    return len(words) / seconds if seconds > 0 else 0.0


def count_vowels(s: str) -> int:
    return sum(ch.lower() in "aeiou" for ch in s)


def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs) if xs else 0.0


def median(xs: List[float]) -> float:
    if not xs:
        return 0.0
    ys = sorted(xs)
    n = len(ys)
    mid = n // 2
    if n % 2 == 1:
        return float(ys[mid])
    return (ys[mid - 1] + ys[mid]) / 2.0


def bin_to_dec(bits: str) -> int:
    """
    Convert a binary string like '1011' to decimal 11.
    """
    total = 0
    for b in bits:
        if b not in "01":
            raise ValueError("bits must be '0' or '1'")
        total = total * 2 + int(b)
    return total


# Quick self-tests (simple asserts)
if __name__ == "__main__":
    assert hello("ai") == "hello, ai"
    assert tokens_per_second("one two three four", 2.0) == 2.0
    assert count_vowels("Abhin") == 2
    assert mean([1, 2, 3]) == 2.0
    assert median([3, 1, 2]) == 2.0
    assert median([1, 2, 3, 4]) == 2.5
    assert bin_to_dec("1011") == 11
    print("basics.py ok")
