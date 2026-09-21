from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count
    return increment


# persistent state: it remembers the modified value and returns it
def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accumulate(add: int) -> int:
        nonlocal power
        power += add
        return power
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchant(item_name: str) -> str:
        return enchantment_type + " " + item_name
    return enchant


# vault["store"]("secret", 42) calls the store function with a key and a value
# The return value contains the store and recall functions
def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> int | str:
        if key not in memory:
            return "Memory not found"
        else:
            return memory[key]
    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("Testing mage counter...")
    call_a = mage_counter()
    call_b = mage_counter()
    print("counter_a call 1: ", call_a())
    print("counter_a call 2: ", call_a())
    print("counter_b call 1: ", call_b())
    print()

    print("Testing spell accumulator...")
    accum1 = spell_accumulator(100)
    print("Base 100, add 20:", accum1(20))
    print("Base 100, add 30:", accum1(30))
    print()

    print("Testing enchantment factory...")
    first = enchantment_factory("Flaming")
    second = enchantment_factory("Frozen")
    print(first("Sword"))
    print(second("Shield"))
    print()

    print("Testing memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print("Recall 'secret':", vault["recall"]("secret"))
    print("Recall 'unknown':", vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
