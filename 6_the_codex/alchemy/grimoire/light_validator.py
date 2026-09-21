def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    results = light_spell_allowed_ingredients()
    for result in results:
        if result in ingredients.lower():
            return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
