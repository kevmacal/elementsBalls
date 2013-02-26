import pygame
import random


class obstaculo(object):
    def __init__(self):
        self.lista=[]
        self.posY=50
        self.change=5
        self.elemento=0      
    
    def crearObstaculos(self,nivel): 
        for x in range(nivel+1):
            leftRand=random.randrange(0,600)
            topRand=random.randrange(self.posY,self.posY+self.change)
            obstNum=random.randrange(1,5)
            if obstNum==1:
                width=50
                heigth=20
            if obstNum==2:
                width=70
                heigth=20
            if obstNum==3:
                width=120
                heigth=20
            if obstNum==4:
                width=90
                heigth=30            
            self.elemento=random.randrange(1,7)
            self.lista.append(obsElemento(self.elemento,pygame.Rect(leftRand,topRand,width,heigth),obstNum))
            self.posY+=10
            self.change+=10       
    
    def tratarCollision(self,pelota,velX,velY):
        for rect in self.lista:
            if rect.Rect.colliderect(pelota.recs[0]):
                if pelota.tipo==7:
                    if rect.elemento!=1:
                        sound=pygame.mixer.Sound("resources\sounds\\boing.wav")                        
                        sound.play()
                        pelota.nVelX=-velX
                        pelota.nVelY=-velY
                if pelota.tipo==1:
                    if rect.elemento==pelota.tipo:
                        pass
                    if rect.elemento==3:
                        sound=pygame.mixer.Sound("resources\sounds\\boing.wav")
                        sound.play()
                        pelota.tipo=7
                        pelota.nVelX=-velX
                        pelota.nVelY=-velY                        
                    if rect.elemento!=3 and rect.elemento!=1:
                        sound=pygame.mixer.Sound("resources\sounds\\fire.wav")
                        sound.play()
                        self.lista.remove(rect)
                        pelota.tipo=7
                if pelota.tipo==2:
                    if rect.elemento==pelota.tipo or pelota.tipo==3:
                        pass
                    if rect.elemento==6:
                        sound=pygame.mixer.Sound("resources\sounds\\nD.wav")
                        sound.play()
                        self.lista.remove(rect)                        
                    if rect.elemento!=6 and rect.elemento!=3 and rect.elemento!=pelota.tipo:
                        sound=pygame.mixer.Sound("resources\sounds\\boing.wav")
                        sound.play()
                        pelota.nVelX=-velX
                        pelota.nVelY=-velY
                if pelota.tipo==3:
                    if rect.elemento==pelota.tipo:
                        pass
                    if rect.elemento==1:
                        sound=pygame.mixer.Sound("resources\sounds\\nD.wav")
                        sound.play()
                        self.lista.remove(rect)
                    if rect.elemento!=1 and rect.elemento!=3:
                        sound=pygame.mixer.Sound("resources\sounds\\boing.wav")
                        sound.play()
                        pelota.nVelX=-velX
                        pelota.nVelY=-velY
                if pelota.tipo==4:
                    if rect.elemento==pelota.tipo or rect.elemento==2:
                        pass         
                    if rect.elemento==3:
                        sound=pygame.mixer.Sound("resources\sounds\\leafD.wav")
                        sound.set_volume(0.5)
                        sound.play()
                        self.lista.remove(rect)
                    if rect.elemento<2 or rect.elemento>4 and rect.elemento!=7:
                        sound=pygame.mixer.Sound("resources\sounds\\boing.wav")
                        sound.play()
                        pelota.nVelX=-velX
                        pelota.nVelY=-velY
                if pelota.tipo==5:
                    if rect.elemento==pelota.tipo or rect.elemento==1:
                        pass
                    if rect.elemento==4:
                        sound=pygame.mixer.Sound("resources\sounds\\nD.wav")
                        sound.play()
                        self.lista.remove(rect)
                        pelota.nVelX=-velX
                        #pelota.nVelY=-velY
                    if rect.elemento!=1 and rect.elemento!=4 and rect.elemento!=5:
                        sound=pygame.mixer.Sound("resources\sounds\\boing.wav")
                        sound.play()
                        pelota.nVelX=-velX
                        pelota.nVelY=-velY
                if pelota.tipo==6:
                    if rect.elemento==pelota.tipo:
                        pass
                    if rect.elemento!=6 and rect.elemento!=5:
                        sound=pygame.mixer.Sound("resources\sounds\\earthD.wav")
                        sound.set_volume(0.5)
                        sound.play()
                        self.lista.remove(rect)
                    if rect.elemento==5:
                        sound=pygame.mixer.Sound("resources\sounds\\boing.wav")
                        sound.play()
                        pelota.nVelX=-velX
                        pelota.nVelY=-velY
                        
                        
            if rect.Rect.colliderect(pelota.recs[1]):
                if pelota.tipo==7:
                    if rect.elemento!=1:
                        sound=pygame.mixer.Sound("resources\sounds\\boing.wav")
                        sound.play()
                        pelota.nVelX=velX
                        pelota.nVelY=-velY
                if pelota.tipo==1:
                    if rect.elemento==pelota.tipo:
                        pass
                    if rect.elemento==3:
                        sound=pygame.mixer.Sound("resources\sounds\\boing.wav")
                        sound.play()
                        pelota.tipo=7
                        pelota.nVelX=velX
                        pelota.nVelY=-velY
                    if rect.elemento!=3 and rect.elemento!=1:
                        sound=pygame.mixer.Sound("resources\sounds\\fire.wav")
                        sound.play()
                        self.lista.remove(rect)
                        pelota.tipo=7
                if pelota.tipo==2:
                    if rect.elemento==pelota.tipo or pelota.tipo==3:
                        pass
                    if rect.elemento==6:
                        sound=pygame.mixer.Sound("resources\sounds\\nD.wav")
                        sound.play()
                        self.lista.remove(rect)                        
                    if rect.elemento!=6 and rect.elemento!=3 and rect.elemento!=pelota.tipo:
                        sound=pygame.mixer.Sound("resources\sounds\\boing.wav")
                        sound.play()
                        pelota.nVelX=velX
                        pelota.nVelY=-velY
                if pelota.tipo==3:
                    if rect.elemento==pelota.tipo:
                        pass
                    if rect.elemento==1:
                        sound=pygame.mixer.Sound("resources\sounds\\nD.wav")
                        sound.play()
                        self.lista.remove(rect)
                    if rect.elemento!=1 and rect.elemento!=3:
                        sound=pygame.mixer.Sound("resources\sounds\\boing.wav")
                        sound.play()
                        pelota.nVelX=velX
                        pelota.nVelY=-velY
                if pelota.tipo==4:
                    if rect.elemento==pelota.tipo or rect.elemento==2:
                        pass         
                    if rect.elemento==3:
                        sound=pygame.mixer.Sound("resources\sounds\\leafD.wav")
                        sound.set_volume(0.5)
                        sound.play()
                        self.lista.remove(rect)
                    if rect.elemento<2 or rect.elemento>4 and rect.elemento!=7:
                        sound=pygame.mixer.Sound("resources\sounds\\boing.wav")
                        sound.play()
                        pelota.nVelX=velX
                        pelota.nVelY=-velY                        
                if pelota.tipo==5:
                    if rect.elemento==pelota.tipo or rect.elemento==1:
                        pass
                    if rect.elemento==4:
                        sound=pygame.mixer.Sound("resources\sounds\\boing.wav")
                        sound.play()
                        self.lista.remove(rect)
                        pelota.nVelX=velX
                    if rect.elemento!=1 and rect.elemento!=4 and rect.elemento!=5:
                        sound=pygame.mixer.Sound("resources\sounds\\boing.wav")
                        sound.play()
                        pelota.nVelX=velX
                        pelota.nVelY=-velY
                if pelota.tipo==6:
                    if rect.elemento==pelota.tipo:
                        pass
                    if rect.elemento!=6 and rect.elemento!=5:
                        sound=pygame.mixer.Sound("resources\sounds\\earthD.wav")
                        sound.set_volume(0.5)
                        sound.play()
                        self.lista.remove(rect)
                    if rect.elemento==5:
                        sound=pygame.mixer.Sound("resources\sounds\\boing.wav")
                        sound.play()
                        pelota.nVelX=velX
                        pelota.nVelY=-velY
                        
    def pintar(self,screen):
        for rect in self.lista:
            rect.pintar(screen)


class obsElemento(pygame.sprite.Sprite):
    def __init__(self,elemento,Rect,obNum):
        self.imagen=pygame.image.load("resources\images\obs\obF1.jpg")
        self.Rect=Rect
        self.elemento=elemento
        self.obNum=obNum
        
    def pintar(self,screen):
        if self.elemento==1:
            #pygame.draw.rect(screen, (193,7,12), self.Rect)
            if self.obNum==1:
                self.imagen=pygame.image.load("resources\images\obs\obF1.jpg")
            if self.obNum==2:
                self.imagen=pygame.image.load("resources\images\obs\obF2.jpg")
            if self.obNum==3:
                self.imagen=pygame.image.load("resources\images\obs\obF3.jpg")
            if self.obNum==4:
                self.imagen=pygame.image.load("resources\images\obs\obF4.jpg")
            screen.blit(self.imagen,self.Rect)
        if self.elemento==2:
            #pygame.draw.rect(screen, (18,0,46), self.Rect)
            if self.obNum==1:
                self.imagen=pygame.image.load("resources\images\obs\obD1.jpg")
            if self.obNum==2:
                self.imagen=pygame.image.load("resources\images\obs\obD2.jpg")
            if self.obNum==3:
                self.imagen=pygame.image.load("resources\images\obs\obD3.jpg")
            if self.obNum==4:
                self.imagen=pygame.image.load("resources\images\obs\obD4.jpg")
            screen.blit(self.imagen,self.Rect)
        if self.elemento==3:
            #pygame.draw.rect(screen, (2,2,194), self.Rect)
            if self.obNum==1:
                self.imagen=pygame.image.load("resources\images\obs\obT1.jpg")
            if self.obNum==2:
                self.imagen=pygame.image.load("resources\images\obs\obT2.jpg")
            if self.obNum==3:
                self.imagen=pygame.image.load("resources\images\obs\obT3.jpg")
            if self.obNum==4:
                self.imagen=pygame.image.load("resources\images\obs\obT4.jpg")
            screen.blit(self.imagen,self.Rect)
        if self.elemento==4:
            #pygame.draw.rect(screen, (15,162,9), self.Rect)
            if self.obNum==1:
                self.imagen=pygame.image.load("resources\images\obs\obE1.jpg")
            if self.obNum==2:
                self.imagen=pygame.image.load("resources\images\obs\obE2.jpg")
            if self.obNum==3:
                self.imagen=pygame.image.load("resources\images\obs\obE3.jpg")
            if self.obNum==4:
                self.imagen=pygame.image.load("resources\images\obs\obE4.jpg")
            screen.blit(self.imagen,self.Rect)
        if self.elemento==5:
            #pygame.draw.rect(screen, (224,233,150), self.Rect)
            if self.obNum==1:
                self.imagen=pygame.image.load("resources\images\obs\obG1.jpg")
            if self.obNum==2:
                self.imagen=pygame.image.load("resources\images\obs\obG2.jpg")
            if self.obNum==3:
                self.imagen=pygame.image.load("resources\images\obs\obG3.jpg")
            if self.obNum==4:
                self.imagen=pygame.image.load("resources\images\obs\obG4.jpg")
            screen.blit(self.imagen,self.Rect)
        if self.elemento==6:
            #pygame.draw.rect(screen, (176,127,22), self.Rect)
            if self.obNum==1:
                self.imagen=pygame.image.load("resources\images\obs\obR1.jpg")
            if self.obNum==2:
                self.imagen=pygame.image.load("resources\images\obs\obR2.jpg")
            if self.obNum==3:
                self.imagen=pygame.image.load("resources\images\obs\obR3.jpg")
            if self.obNum==4:
                self.imagen=pygame.image.load("resources\images\obs\obR4.jpg")
            screen.blit(self.imagen,self.Rect)
