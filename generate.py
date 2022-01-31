import random as rn

def WeightedChoice(d):
	weights = list(d.values())
	strings = list(d.keys())
	totals = []
	running_total = 0
	for w in weights:
		running_total += w
		totals.append(running_total)
	rnd = rn.random() * running_total
	for i, total in enumerate(totals):
		if rnd < total:
			return strings[i]

def WhichArray(s):
	return {
        'compass': compass,
        'position': position,
        'name': name,
        'prefix': prefix,
        'locale': locale,
        'suffix': suffix,
        'mod': mod
    }[s]

def ParseTemplate(template):
	words = template.split(' ')
	final = []
	for word in words:
		if '_' in word:
			part1 = WeightedChoice(WhichArray(word.split('_')[0]))
			part2 = WeightedChoice(WhichArray(word.split('_')[1]))
			final.append(part1+part2)
		elif '_' not in word:
			final.append(WeightedChoice(WhichArray(word)));
	return ' '.join(final)

compass = {
	'north': 1,
	'south': 1,
	'east': 0.5,
	'west': 0.7
}

position = {
	'upper': 1,
	'lower': 1
}

name = {
	'garfield': 1,
	'morgan': 0.5,
	'pullman': 0.6,
	'beverly': 0.6,
	'rogers': 0.8,
	'wright': 0.4,
	'chester': 0.3,
	'austin': 0.4,
	'sheridan': 0.6,
	'roscoe': 0.8,
	'pulaski': 0.4,
	'wicker': 0.7,
	'lincoln': 1,
	'irving': 0.8,
	'hyde': 0.5,
	'humboldt': 0.6,
	'grand': 0.3,
	'grant': 0.7,
	'belmont': 0.9,
	'douglas': 0.5
}

prefix = {
	'lake': 1,
	'wood': 1,
	'river': 0.8,
	'ken': 0.3,
	'green': 0.6,
	'engle': 0.6,
	'edge': 0.7,
	'buck': 0.7,
	'bronze': 0.3
}

locale = {
	'park': 1,
	'ridge': 0.8,
	'heights': 0.8,
	'shore': 0.7,
	'side': 0.2,
	'village': 0.8,
	'gardens': 0.6,
	'green': 0.7,
	'glen': 0.4,
	'woods': 0.3
}

suffix = {
	'ville': 0.7,
	'land': 0.3,
	'field': 0.4,
	'town': 0.5,
	'lawn': 0.7,
	'dale': 0.8,
	'hill': 0.5,
	'view': 0.6,
	'coast': 0.2,
	'water': 0.8,
	'brook': 0.7,
	'burn': 0.7,
	'ham': 0.7,
	'port': 0.4
}

mod = {
	'old': 1,
	'new': 0.5
}

templates = {
	'compass prefix_suffix': 0.6,
	'compass name locale': 0.6,
	'position prefix_suffix': 0.1,
	'position name locale': 0.2,
	'compass locale': 0.1,
	'mod compass prefix_suffix': 0.1,
	'mod name locale': 0.1,
	'name locale': 0.8,
	'mod name locale': 0.1
}

print(ParseTemplate(WeightedChoice(templates)).title())