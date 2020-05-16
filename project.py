from tkinter import *
import random
import time

   
tk = Tk()               
canvas = Canvas(tk, width=1109,height=648)
canvas.pack()

road_image = PhotoImage(file='road.gif')
road_id = canvas.create_image(0,0,
                              anchor =NW, image=road_image)


##########################################################################################
####################################### BAll #############################################
##########################################################################################

class Ball:
    def __init__(self,canvas):
        self.canvas=canvas
        self.image=PhotoImage(file='ball.gif')
        self.x=500
        self.y=500
        self.vx=0
        self.vy=0
        self.ball_id = canvas.create_image(self.x,self.y,anchor=SW,image=self.image)
    def move(self):
        self.canvas.move(self.ball_id,self.vx,self.vy)
        self.x+=self.vx
        self.y+=self.vy
        self.vx=0
        self.vy=0
        if self.x<0:
            self.vx=0
        elif self.x+100>1000:
            self.vx=0
        if self.y-100 < 300:
            self.y = 300


def move_ball(event):
    if event.keysym=='Left':
        ball.vx= -160
    elif event.keysym=='Right':
        ball.vx= 160

canvas.bind_all('<KeyPress-Left>',move_ball)
canvas.bind_all('<KeyPress-Right>',move_ball)


##########################################################################################
####################################### Car ##############################################
##########################################################################################

class Car:
    def __init__(self,canvas,vy):
        self.canvas=canvas
        self.x = random.choice([20,180,350,510,670,820,980])#เปลี่ยนรถที่สุ่ม
        self.y = 0
        self.vy = vy
        self.vx = 0
        image = random.choice(['carnew001.gif','carnew002.gif','carnew003.gif','carnew004.gif','carnew005.gif','carnew006.gif','carnew007.gif'])
        self.image = PhotoImage(file=image)
        self.car_id = canvas.create_image(self.x,0,anchor =SW, image=self.image)
    def move(self):
        self.canvas.move(self.car_id,self.vx,self.vy)
        self.y+=self.vy
        
cars=[]
t = 0 #เวลาในการสร้างรถ
t2 = 18 # เวลาในการสร้างรถ ทำให้เร็วขึ้น ยิ่งน้อยเร็วขึ้น
n = 1
end = 0
vy = 15 #ความเร็วรถเริ่มต้น
ball=Ball(canvas)
while True:
    if t%t2==0:#ระยะเวลาการสร้างรถ สัมพันธ์กับเวลา t
        if n % 10 == 0 : #เพิ่มความเร็วรถ  ใช้จากรถที่ถูกลบไป
            vy += 2 #เพิ่มความเร็ว 
            if vy >= 61:
                vy = 60
            t2 -=1 #ลดตัวหาร เพื่อให้สร้างรถเร็วขึ้น 
            if t2==0:
                t2 = 1
        i = Car(canvas,vy)
        cars.append(i)
    for car in cars:
        car.move()
        if car.y>600:
            canvas.delete(car.car_id)
            cars.remove(car)
            n+=1 #นับรถที่ลบออกไป
        elif ball.x+50>=car.x and ball.x+50<=car.x+100 and ball.y-50 <= car.y:
            end += 1
            canvas.delete(car.car_id)
            cars.remove(car)
            break
        elif ball.x+80>=car.x and ball.x+80<=car.x+100 and ball.y-50 <= car.y:
            end += 1
            canvas.delete(car.car_id)
            cars.remove(car)
            break
        
##########################################################################################
####################################### SCORE ############################################
##########################################################################################
        
    label2 = Label(tk, text = 'Life : '+str(3-end), font = 40)
    label2.place(x=10,y=10)    
    if end ==3:
        break
    ball.move()
    tk.update()
    time.sleep(0.03)
    t += 1
    label = Label(tk, text = 'score : '+str(n), font = 40)
    label.place(x=900,y=10)

print(n)#### นับจำนวนรถที่ถูกลบ 




##########################################################################################
####################################### end ##############################################
##########################################################################################

car101_image = PhotoImage(file='car101.gif')
car101_id = canvas.create_image(1000,110,anchor =SW, image=car101_image)

car201_image = PhotoImage(file='car201.gif')
car201_id = canvas.create_image(1000,240,anchor =SW, image=car201_image)


car102_image = PhotoImage(file='car102.gif')
car102_id = canvas.create_image(1000,370,anchor =SW, image=car102_image)

car202_image = PhotoImage(file='car202.gif')
car202_id = canvas.create_image(1000,500,anchor =SW, image=car202_image)


car103_image = PhotoImage(file='car101.gif')
car103_id = canvas.create_image(1000,630,anchor =SW, image=car103_image)

car203_image = PhotoImage(file='car201.gif')
car203_id = canvas.create_image(1000,760,anchor =SW, image=car203_image)


for i in range(200): #200ชิดขอบ 
    canvas.move(car101_id,-5,0)
    canvas.move(car201_id,-5,0)
    
    canvas.move(car102_id,-5,0)
    canvas.move(car202_id,-5,0)
    
    canvas.move(car103_id,-5,0)
    canvas.move(car203_id,-5,0)
    tk.update()
    time.sleep(0.02)

gameover_image = PhotoImage(file='gameover.gif')
gameover = canvas.create_image(0,0,anchor =NW, image=gameover_image)
tk.update()







            
