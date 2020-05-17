import pygame



down_pointer = 1
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('car.png')
backImg = pygame.image.load('background.jpg')
twrImg = pygame.image.load('tower.png')


display_width = 800
display_height = 600

x = (display_width * 0.04)
y = (display_height * 0.08)
x_change = 0
car_speed = 0
speed = -3

LEFT = (400 -242 , 270)
RIGHT = (400 + 242 , 270)
TOP = ( 400, 28)
DOWN = ( 400, 512)
CENTER = (400, 270)
center = CENTER
radius = 242

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Simulator")



#rotate(180)

def quit():
    pygame.quit()



class car:

    def __init__(self,coord, platform, angle):
        self.platform = platform
        self.loc = coord
        self.coord = (coord[0] - 30, coord[1] -30)
        self.angle = angle
        cars.append(self)

    def set_coord(self, coord):
        self.coord = (coord[0] - 30, coord[1] -30)

    def draw(self):
        gameDisplay.blit(carImg,self.coord)

class spikes:

    color = blue
    initial = (400, 270)
    def __init__(self,number,  final, angle):
        #self.initial = initial
        self.number = number
        self.final = final
        self.angle = angle
        lines.append(self)

    def draw(self):
        pygame.draw.line(gameDisplay, self.color, spikes.initial, self.final, 10)

class platform:

    def __init__(self, coord, color):
        self.coord = coord
        self.color = color
        platforms.append(self)

    def draw(self):
        pygame.draw.circle(gameDisplay, self.color, self.coord, 45)

cars = []
lines = []
platforms = []

#########################INIT#################






###################################

import math
import time


def update():
    gameDisplay.fill(black)
    gameDisplay.blit(backImg,(0,0))
    gameDisplay.blit(twrImg, (center[0] - 255, center[1]))
    for spike in lines:
        spike.draw()
    for plat in platforms:
        plat.draw()
    for vehicle in cars:
        vehicle.draw()
    pygame.display.update()

def rotate(ang):
    ####ROTATION##########
        #print("called")
        ang_temp = 0
        global down_pointer
        while(ang_temp != ang):
            #print(ang_temp)
            
            gameDisplay.fill(black)
            gameDisplay.blit(backImg,(0,0))
            gameDisplay.blit(twrImg, (center[0] - 255, center[1]))
            j = 0
            for spike in lines:

                r = 242		#Length of the line
                spike.angle += math.fabs(speed)
                x = 400 + int(r * math.sin(math.radians(90 - spike.angle)))
                y = 270 + int(r * math.sin(math.radians(spike.angle)))

                

                spike.final = (x,y)
                #print(spike.number, "\n\n")
                #print(spike.angle)
                
                platforms[j].coord = spike.final
                j += 1
            for vehicle in cars:
                    vehicle.angle += math.fabs(speed)
                    #print(vehicle.angle)
                    x = 400 + int(r * math.sin(math.radians(90 - vehicle.angle)))
                    y = 272 + int(r * math.sin(math.radians(vehicle.angle)))
                    vehicle.set_coord((x,y))
                    update()
            ##################
            #print("\n\n")
            update()
            #i = 0
            #for spike in lines:
                #print(spike)
            #    spike.draw()
            #    platforms[i].draw()
            #    if(len(cars) > i):
            #        cars[i].draw()

                

                

            #    i += 1
            #pygame.display.update()
            #time.sleep(2)
            if(ang_temp + math.fabs(speed) >= ang):
                ang_temp = ang
                #print("YES")
                #print(ang_temp + speed >= ang)
                
            else:
                ang_temp += math.fabs(speed)
                ang_temp = int(ang_temp)
                #print(type(ang), type(ang_temp),ang, ang_temp , ang_temp + speed >= ang)

            if(int(ang_temp) % 90 == 0 and ang_temp != 0):
                down_pointer += 1
                if(down_pointer > 4):
                    down_pointer = 1

    

s1 = spikes(1, DOWN, 90)
p1 = platform(s1.final, white)
#    c1 = car(s1.final)
s2 = spikes(2, RIGHT, 0)
p2 = platform(s2.final, red)
#    c2 = car(s2.final)
s3 = spikes(3, TOP, 270)
p3 = platform(s3.final, green)
#c3 = car(s3.final)
s4 = spikes(4, LEFT, 180)
p4 = platform(s4.final, blue)
#    c4 = car(s4.final)



def add_car():
    
    for vehicle in cars:
        if(vehicle.platform == down_pointer or len(cars) >=4):
            return -1
    #global c
    loc = DOWN
    c = car(loc, down_pointer, lines[down_pointer-1].angle)
    c.draw()
    pygame.display.update()

def remove_car():
    flag = 0
    for vehicle in cars:
        if(vehicle.platform == down_pointer):
            flag = 1
            cars.remove(vehicle)
            update()
    if(flag == 0):
        return -1
    
def down_platform(platform):
    diff = math.fabs(4 - down_pointer + platform)
    if(diff >= 4):
        diff = math.fabs(diff - 4)
    print(diff)
    angle = (diff * 90)
    rotate(angle)

def empty_platform():
    plat = [1,2,3,4]
    for vehicle in cars:
        if vehicle.platform in plat:
            plat.remove(vehicle.platform)
            if(len(plat) <= 0):
                return -1
    #print(plat)
    down_platform(plat[0])
    
rotate(360)
