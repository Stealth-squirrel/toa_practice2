# Ответ: б)изменение порядка следования пары способно улучшить статус партнера женщины. 

def gale_shapley(men_prefs, women_prefs):
    """
    Finds a stable matching using the Gale-Shapley algorithm.

    :param men_prefs: A dictionary where keys are men and values are
                      lists of women in order of preference.
    :param women_prefs: A dictionary where keys are women and values are
                        lists of men in order of preference.
    :return: A dictionary representing the final stable relationships
             (women keyed to their matched man).
    """
    free_men = list(men_prefs.keys())
    relationships = {}  # {woman: man}
    # Create a reverse lookup for women's preference ranking (for faster lookups)
    women_rankings = {w: {m: i for i, m in enumerate(prefs)} for w, prefs in women_prefs.items()}

    while free_men:
        man = free_men.pop(0)
        prefs = men_prefs[man]
        for woman in prefs:
            if woman not in relationships:
                # If woman is free, she accepts the proposal
                relationships[woman] = man
                break
            else:
                # If woman is already engaged, check if the new man is preferred
                current_spouse = relationships[woman]
                # Compare index in woman's preference list: lower index means higher preference
                if women_rankings[woman][man] < women_rankings[woman][current_spouse]:
                    # Woman prefers the new man; she switches partners
                    relationships[woman] = man
                    free_men.append(current_spouse) # Old spouse becomes free
                    break
        # If the man exhausted all options without a match, the loop naturally ends (though this shouldn't happen with equal numbers and complete lists)

    # Convert the relationships to {man: woman} for final output format
    stable_matching = {man: woman for woman, man in relationships.items()}
    return stable_matching

mp = {
    "abe": ["ada", "bea", "cat"],
    "bob": ["ada", "cat", "bea"],
    "cal": ["bea", "ada", "cat"]
}

wp = {
    "ada": ["cal", "abe", "bob"],
    "bea": ["abe", "cal", "bob"],
    "cat": ["cal", "abe", "bob"]
}
print(gale_shapley(mp, wp))


mp = {
    "abe": ["ada", "bea", "cat"],
    "bob": ["ada", "cat", "bea"],
    "cal": ["bea", "ada", "cat"]
}

wp_lie = {
    "ada": ["cal", "bob", "abe"],
    "bea": ["abe", "cal", "bob"],
    "cat": ["cal", "abe", "bob"]
}
print(gale_shapley(mp, wp_lie))
