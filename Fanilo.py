print("Hello world")
if 5 > 2 : 
	print ( '5 est effectivement plus grand que 2')
else : 
	"5 n'est pas plus grand que 2"

name = 'Fanilo'
if name == 'Ola' :
	print ('Hey Ola!')
elif name == 'Fanilo':
	print ('Hey Fanilo!')
else :
	print ('Hey Anonymous!')

volume = 57
if volume < 20:
	print("C'est plutôt calme.")
elif 20 <= volume < 40:
	print("Une jolie musique de fond.")
elif 40 <= volume < 60:
	print("Parfait, je peux entendre tous les détails du morceau.")
elif 60 <= volume < 80:
	print("Parfait pour faire la fête !")
elif 80 <= volume < 100:
	print("Un peu trop fort !")
	
def hi():
	print ('hi there!')
	print ('how are you?')
hi()

def hi(name):
	if name == 'Fanilo':
		print ('hi Fanilo!')
	elif name == 'Bozy':
		print ('hey Bozy!')
	else :
		print ('hey Anonymous')
hi('Fanilo')

hi ('Fanilo')

hi ('fa')

def hi(name):
	print ('hi' +'name'+'!')

girls = ['Fanilo', 'Bozy','Fa', 'You'] 
for name in girls:
	hi(name)
	print('Next girl')
