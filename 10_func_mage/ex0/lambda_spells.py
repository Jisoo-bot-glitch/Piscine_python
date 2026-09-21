# function simple, power numver reverse sorted
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


# it returns only respect the rule, filter choose only True
def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


# map changes all elements
def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": round(sum(m["power"] for m in mages) / len(mages), 2),
    }


def main() -> None:
    artifacts = [
            {"name": "Crystal Orb", "power": 85, "type": "orb"},
            {"name": "Fire Staff", "power": 92, "type": "staff"}
        ]
    print("Testing artifact sorter...")
    result = artifact_sorter(artifacts)
    print(
        f"{result[0]['name']} ({result[0]['power']} power) "
        f"comes before {result[1]['name']} ({result[1]['power']} power)"
    )
    print()
    print("Testing spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(" ".join(transformed))
    print()
    print("Testing power filter...")
    mages = [
            {"name": "Jeremie", "power": 80, "element": "fire"},
            {"name": "Chataigne", "power": 45, "element": "earth"},
            {"name": "Alex", "power": 95, "element": "water"},
        ]
    strong = power_filter(mages, 50)
    print(f"Mages with power >= 50: {len(strong)}")
    print()
    print("Testing mages stats")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Avg power: {stats['avg_power']}")


if __name__ == "__main__":
    main()
