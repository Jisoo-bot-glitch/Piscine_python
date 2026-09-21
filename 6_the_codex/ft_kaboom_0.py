import alchemy.grimoire

print("=== Kaboom 0 ===")
print("Using grimoire module directly")
name = "Fantasy"
content = "Earth, wind and fire"
print("Testing record light spell: "
      f"{alchemy.grimoire.light_spell_record(name, content)}\n")
