import time
from functools import wraps
from collections.abc import Callable
from typing import Any


# decorator should cover all functions so it uses *args, **kwargs
def spell_timer(func: Callable) -> Callable:

    # keep func's name and content
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")

        return result
    return wrapper


def power_validator(min_power: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = args[-1]
            # -1 means "last element"
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for i in range(1, max_attempts + 1):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    if not i == max_attempts:
                        print("Spell failed, retrying..."
                              f" (attempt {i}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not len(name) >= 3:
            return False
        for i in range(len(name)):
            if not name[i] == " " and not name[i].isalpha():
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Fireball cast!"


@retry_spell(3)
def spell(i: int) -> str:
    if i == 1:
        return "Waaaaaaagh spelled !"
    else:
        raise ValueError


def main() -> None:
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")
    print()
    print("Testing retrying spell...")
    print(spell(0))
    print(spell(1))
    print()
    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("SFP"))
    print(MageGuild.validate_mage_name("32"))
    light = MageGuild()
    print(light.cast_spell("Lightning", 15))
    print(light.cast_spell("Lightning", 9))
    print()


if __name__ == "__main__":
    main()
