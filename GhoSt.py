import random,os
door = '''

          |---------|   |---------|   |----------|
          |         |   |         |   |          |
          |         |   |         |   |          |
          |       O |   |       O |   |        O |
          |         |   |         |   |          |
          |         |   |         |   |          |
          |         |   |         |   |          |
          |         |   |         |   |          |
          |         |   |         |   |          |
          |---------|   |---------|   |----------|

               ?
             ----
             |@ @| 
               U  
             / | \       
               | 
              / \  
'''
ghost = '''
             ----
             |@ @| 
               -  
             / | \       
               | 
              / \        
                     
'''
def Ghost():
    o='y'
    while o == 'y':
        os.system('cls')
        print('Welcome To The GhoSt Game\n'+door)
        choice=int(input('Enter Your Number (1-3)'))
        x = random.randint(1,3)
        if choice==x:
            print('win')
            print(x)
        else:
            print('Boom  The GhoSt Here')
            print('Lost'+ghost)
        o = input('Replay (y/n?)')
    print('GoodBye')

        
Ghost()
