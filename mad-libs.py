#Team members: Kiddee, Kent
#Life of Po

import random
R = random.randrange(0,8)
def R(Thing):
	Thing[r]

adjective1 = ['fat', 'morbidly obese', 'big', 'wide', 'skinny', 'lean', 'bony']
adjective2 = ['fast', 'slow', 'swift', 'strong', 'weak', 'powerful', 'light', 'nice']
adjective3 = ['slimy', 'loud', 'round', 'furry', 'evil', 'idiotic', 'bald', 'immense']
adjective4 = ['nifty', 'homeless', 'serious', 'swanky', 'scrawny', 'ugly', 'hissing', 'wary', 'second-hand', 'jealous']
adjective5 = ['big', 'small', 'smelly', 'trashy', 'sussy', 'bright', 'lovely', 'tiny']
adjective6 = ['big', 'small', 'smelly', 'trashy', 'sussy', 'bright', 'lovely', 'tiny'] 
shape = ['circle', 'square', 'triangle', 'cube', 'hexagon', 'octagon', 'rhombus','decagon'] 
colour = ['red', 'blue', 'yellow', 'white', 'purple', 'rainbow', 'black', 'violet'] 
place1 = ['Toilet', 'House', 'Barn', 'supermarket', 'box', 'hole', 'restaurant', 'school'] 
place2 = ['school', 'restaurant', 'office', 'home', 'stadium', 'cave', 'college', 'hotel']
place3 = ['school', 'restaurant', 'office', 'home', 'stadium', 'cave', 'college', 'hotel'] 
place4 = ['drug store', 'clinic', 'theater', 'bank', 'cinema', 'night Club', 'market', 'night market']
place5 = ['school', 'resturange', 'office', 'home', 'stadium', 'cave', 'college', 'hotel']
name1 = input("Enter a name for your house:\n")
name2 = input("Enter a name of a place:\n")
verb1 = ['kill', 'run', 'kick', 'slap', 'play', 'jump',' bang gang', 'WWE']
verb2 = ['began', 'drank', 'went', 'ate', 'bought', 'built', 'drew', 'burnt']
verb3 = ['began', 'drank', 'went', 'ate', 'bought', 'built', 'drew', 'burnt']
sequence1 = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth']
sequence2 = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth']
relationship1 = ['father', 'mather', 'sister', 'brother', 'grandmother', 'girlfriend', 'grandfather', 'aunt']
relationship2 = ['father', 'mather', 'sister', 'brother', 'grandmother', 'girlfriend', 'grandfather', 'aunt']
restaurant_name = ['big', 'small', 'smelly', 'trashy', 'sussy', 'bright', 'lovely', 'tiny']
word_expression = ['Goodluck', 'Godspeed', 'Bon voyage', 'Goodbye', 'Adios', 'Adieu', 'Cheerio', 'Farewell']
time_expression = ['day', 'week', 'year', '2 weeks', '3 weeks', '3 days', '4 years', '6 years']
job = ['Attorney', 'Architect', 'Receptionist', 'Waiter', 'Tax collector', 'Lab assistant', 'Software developer', 'Doctor']
#thing =
#kiddee do the one above me ok ^
#      		   	       |
#      		  	       |
adj1 = R(adjective1)
adj2 = R(adjective2)
adj3 = R(adjective3)
adj4 = R(adjective4)
adj5 = R(adjective5)
adj6 = R(adjective6)
shp = R(shape)
col = R(colour)
pl1 = R(place1)
pl2 = R(place2)
pl3 = R(place3)
pl4 = R(place4)
pl5 = R(place5)
v1 = R(verb1)
v2 = R(verb2)
v3 = R(verb3)
seq1 = R(sequence1)
seq2 = R(sequence2)
rshp1 = R(relationship1)
rshp2 = R(relationship2)
restrnt = R(restaurant_name)
wrd_expr = R(word_expression)
t_expr = R(time_expression)
jb = R(job)
thg = R(thing)

mad_lib = f''' Hi, my name is Po. I’m  {adj1},  {adj2},  {adj3}  and  {adj4} boy. 
I live in the {adj5} {shp} {col} {pl1} named {name1}. 
My father is the {jb} who {v1} a {thg} to {name2} {pl2}.
Today is my {seq1} {t_expr} to go to {pl3} since I {v2} the old {pl4}. 
I {v3} with Katty, my {adj6} {rshp1} who said to me “Don’t be worried about your smartphone and TV spying on you. 
Your vacuum cleaner has been gathering dirt on you for years”. 
Finally this is my {seq2} dinner at {restrnt} with my {rshp2} after that I have to go to {pl5}.
{wrd_expr}, Po!!! '''

print(mad_lib)
