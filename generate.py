import random as rn

def WeightedChoice(d):
	weights = d.values()
	strings = d.keys()
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
        'suffix': locale,
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


compass = {'north':1,
		   'south':1,
		   'east':0.5,
		   'west':0.5}

position = {'upper':1,
			'lower':1}

name = {'garfield':1,
		 'morgan':0.5,
		 'pullman':0.6,
		 'beverly':0.6,
		 'rogers':0.8,
		 'wright':0.4,
		 'chester':0.3,
		 'austin':0.4,
		 'sheridan':0.6,
		 'roscoe':0.8,
		 'pulaski':0.4,
		 'wicker':0.7,
		 'lincoln':1,
		 'irving':0.8,
		 'hyde':0.7,
		 'humboldt':0.6,
		 'grand':0.5}

prefix = {'lake':10,
		  'wood':1,
		  'wild':0.3,
		  'river':0.8,
		  'ken':0.3,
		  'green':0.6,
		  'engle':0.6,
		  'edge':0.7,
		  'buck':0.7,
		  'bronze':0.3}

locale = {'park':1,
		  'ridge':0.8,
		  'heights':0.8,
		  'shore':0.7,
		  'side':0.2,
		  'village':0.8,
		  'gardens':0.6,
		  'green':0.7,
		  'glen':0.4,
		  'woods':0.3}

suffix = {'ville':0.8,
		  'land':1,
		  'field':1,
		  'town':1,
		  'lawn':1,
		  'dale':1,
		  'hill':1,
		  'view':1,
		  'coast':1,
		  'water':1,
		  'brook':1,
		  'burn':1,
		  'ham':1}

mod = {'old':1,
	   'new':0.5}

templates = {'compass prefix_suffix':1,
			 'compass name locale':1,
			 'position prefix_suffix':0.1,
			 'position name locale':0.1,
			 'compass locale':0.05,
			 'mod compass prefix_suffix':0.1,
			 'mod name locale':0.1,
			 'name locale':0.8,
			 'mod name locale':0.1}

print ParseTemplate(WeightedChoice(templates)).title();