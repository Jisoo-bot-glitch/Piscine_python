import operator
from typing import Any
from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        result = reduce(operator.add, spells)
    elif operation == "multiply":
        result = reduce(operator.mul, spells)
    elif operation == "min":
        result = reduce(min, spells)
    elif operation == "max":
        result = reduce(max, spells)
    else:
        raise ValueError("Operation is not correct")
    return result


# helper func for partial_enchanter()
def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment ({power} power) on {target}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchantment = partial(
        base_enchantment,
        power=50,
        element="Fire"
    )

    ice_enchantment = partial(
        base_enchantment,
        power=50,
        element="Ice"
    )

    lightning_enchantment = partial(
        base_enchantment,
        power=50,
        element="Lightning"
    )

    spells: dict[str, Callable] = {
        "fire": fire_enchantment,
        "ice": ice_enchantment,
        "lightning": lightning_enchantment
    }
    return spells


# lru_cache() is used to cache the results of function calls
@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    # the base version used when the arg'type doesn't match anything registered
    @singledispatch
    def cast(spell: Any) -> str:
        return "unknown spell type"

    @cast.register
    def _(spell: int) -> str:
        return f"{spell} damage"

    @cast.register
    def _(spell: str) -> str:
        return spell

    @cast.register
    def _(spell: list) -> str:
        return f"{len(spell)} spells"
    return cast


def main() -> None:
    print()
    print("Testing spell reducer...")
    print("Sum:", spell_reducer([20, 50, 30], "add"))
    print("Product:", spell_reducer([120000, 2], "multiply"))
    print("Max:", spell_reducer([40, 0, -5, 28], "max"))
    print()

    print("Testing memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
    print()
    dispatcher = spell_dispatcher()
    print("Testing spell dispatcher...")
    print("Damage spell:", dispatcher(42))
    print("Enchantment:", dispatcher("fireball"))
    print("Multi-cast:", dispatcher([1, 2, 3]))
    print(dispatcher(3.15))
    print()
    print("Testing partial enchanter...")
    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire"](target="Sword"))
    print(enchanters["ice"](target="Shield"))
    print(enchanters["lightning"](target="Staff"))
    print()


if __name__ == "__main__":
    main()
