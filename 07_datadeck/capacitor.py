from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
    HealCapability,
    TransformCapability
)


def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal("itself"))
    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal("itself"))
    print()


def test_creature(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.revert())
    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.revert())


if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    test_healing(healing_factory)
    print()
    creature_factory = TransformCreatureFactory()
    test_creature(creature_factory)
