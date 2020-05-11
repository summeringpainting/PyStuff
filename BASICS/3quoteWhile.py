REFRAIN = '''
%d bottles of beer on wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!,
%d number of fucks given
'''
bottles_of_beer = 9
while bottles_of_beer > 1:
    print (REFRAIN % (bottles_of_beer, bottles_of_beer,
                      bottles_of_beer - 1, bottles_of_beer - 2))
    bottles_of_beer -= 1
    bottles_of_beer -= 2
