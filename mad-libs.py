#Team members: Kiddee, Kent
#Life of Po

#Introduction part
print('----- Wellcome to "Life of Po" story-----')
print('------ Head of Story by Kiddee ----- Head of Code by Kent ------')

#Enter to begin the story
print('-----please enjoy the story!!!-----')

import random

#word list
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
name1 = ['Alblana','Liopadia', 'Kikpa','Jogar','Pimamono','Highho','Fraruk','Namamoni']
name2 = ['Central Plaza','castel','hotel','school','supermarket','stadium','market','garage']
verb1 = ['kill', 'run', 'kick', 'slap', 'play', 'jump','bang gang', 'WWE']
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
thing = ['fish', 'bear', 'bottle', 'apple', 'banana', 'cow', 'jacket', 'plate']


#Random
adj1 = random.choice(adjective1)
adj2 = random.choice(adjective2)
adj3 = random.choice(adjective3)
adj4 = random.choice(adjective4)
adj5 = random.choice(adjective5)
adj6 = random.choice(adjective6)
shp = random.choice(shape)
col = random.choice(colour)
pl1 = random.choice(place1)
pl2 = random.choice(place2)
pl3 = random.choice(place3)
pl4 = random.choice(place4)
pl5 = random.choice(place5)
nm1 = random.choice(name1)
nm2 = random.choice(name2)
v1 = random.choice(verb1)
v2 = random.choice(verb2)
v3 = random.choice(verb3)
seq1 = random.choice(sequence1)
seq2 = random.choice(sequence2)
rshp1 = random.choice(relationship1)
rshp2 = random.choice(relationship2)
restrnt = random.choice(restaurant_name)
wrd_expr = random.choice(word_expression)
t_expr = random.choice(time_expression)
jb = random.choice(job)
thg = random.choice(thing)

#Mad lib outcome
mad_lib = f''' Hi, my name is Po. I am  {adj1},  {adj2},  {adj3}  and  {adj4} boy. 
I live in the {adj5} {shp} {col} {pl1} named {nm1}. 
My father is the {jb} who {v1} a {thg} to {nm2}'s {pl2}.
Today is my {seq1} {t_expr} to go to {pl3} since I {v2} the old {pl4}. 
I {v3} with Katty, my {adj6} {rshp1} who said to me “Don’t be worried about your smartphone and TV spying on you. Your vacuum cleaner has been gathering dirt on you for years”. 
Finally this is my {seq2} dinner at {restrnt} with my {rshp2} after that I have to go to {pl5}.
{wrd_expr}, Po!!! '''

#print the story session

import cowsay

cowsay.milk (mad_lib)

