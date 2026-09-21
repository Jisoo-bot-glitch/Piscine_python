from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:
    results = dark_spell_allowed_ingredients()
    for result in results:
        if result in ingredients.lower():
            return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
