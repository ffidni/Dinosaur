from main import *

class Dino:

    def __init__(self):
        #Generating attributes/properties.
        self.DINO_IMG = "@"
        self.OBSTACLE_IMG = "|"
        self.SPEEDS = {
            300:(0.06, 3),
            500:(0.05, 4),
            1000:(0.04, 5),
            5000:(0.03, 6)
        }
        self.speed_count = 0.07
        self.obstacle_count = 2
        self.score = 0
        try:
            self.highscore = pickle.load(open('Assets/highscore.pkl', 'rb'))
        except EOFError:
            self.highscore = 0
        #Generate a road with a length of 80.
        self.road = ['_' for _ in range(80)]
        self.flag = True

    def screen_display(self, type=None):
        #Displaying jump, dead, and normal scene to the screen.
        CLEAR()
        road_display = ''.join(self.road[:50])
        tab_score = '\t'*2
        tab_road = '\t'*1
        line_score = '\n'*10
        line_road = '\n'*4
        print(f'{line_score}{tab_score}    High Score: {self.highscore} Current: {self.score}')
        if type == 'jump':
            print(f'{line_road}\t    @\n{tab_road}  {road_display}')
        elif type == 'dead':
            print(f'\n\n\t\t\t     Game Over! \n\n\n  {tab_road}  {road_display}')
        else:
            print(f'\n\n\n\n\n  {tab_road}  {road_display}')

    def jump_handler(self):
        #If the dinosaur jump, we're gonna fill the current position to a line
        #And put the dinosaur on the top
        self.road[1] = '_'
        self.screen_display('jump')

    def speed_obstacle_handler(self):
        #Check if the current score matching up new speed and obstacle count.
        #If it's true, we're gonna add up the number of speed and obstacles.
        try:
            self.speed_count = self.SPEEDS[self.score][0]
            self.obstacle_count = self.SPEEDS[self.score][1]
        except:
            pass
                
    def obstacle_generator(self):
        #Generate obstacles in range 40 to 80 with 6 steps.
        for _ in range(self.obstacle_count):
            random_obstacle = choice([i for i in range(40,80,6)])
            self.road[random_obstacle] = self.OBSTACLE_IMG

    def score_handler(self):
        #Adding up current score by 1 every 0.01 seconds.
        sleep(0.01)
        self.score += 1

    def death_handler(self):
        #If the current score greater than the highscore, change the highscore.
        if self.score > self.highscore:
            pickle.dump(self.score, open('Assets/highscore.pkl', 'wb'))
        
        #Printing dead scene to the screen.
        self.screen_display('dead')

    def obstacle_handler(self):
        obstacles_indices = [index for index,obs in enumerate(self.road) if obs == self.OBSTACLE_IMG]
        if len(obstacles_indices):
            for i in obstacles_indices:
                #Check if the next element in the road is not a cactus.
                if self.road[i-1] != self.DINO_IMG:
                    #Deleting a cactus that reaches the end of the road.
                    if self.road[0] == self.OBSTACLE_IMG:
                        del obstacles_indices[0]
                        self.road[0] = '_'
                    #Otherwise we're gonna fill it with road and generate new cactuses.
                    else:
                        self.road[i] = '_'
                        self.road[i-1] = self.OBSTACLE_IMG
                #If the next element is a cactus, the game is over. Otherwise, fill it with new road.
                else:
                    if self.road[1] == self.DINO_IMG: 
                        self.death_handler()
                        self.flag = False
                    else:
                        self.road[i] = '_'
        else:
            self.obstacle_generator()

    def reset_entity(self):
        #Reseting all game's entity to it's default value.
        self.flag = True
        self.speed_count = 0.07
        self.obstacle_count = 2
        self.score = 0
        self.highscore = pickle.load(open('Assets/highscore.pkl', 'rb'))
        self.road = ['_' for _ in range(80)]

    def start(self):
        while self.flag:
            self.road[1] = self.DINO_IMG

            #Handling dinosaur's movement with keyboard.
            if is_pressed('up') or is_pressed('space'):
                self.jump_handler()
            else:
                self.screen_display()

            #Handling obstacles, speed, and score.
            self.obstacle_handler() 
            self.speed_obstacle_handler() 
            self.score_handler()
            sleep(self.speed_count)

        #Check if user wants to play again.
        user_input = input("\n\t\t\t Play Again? (y/n): ").lower()
        if 'y' in user_input:
            self.reset_entity()
            self.start()