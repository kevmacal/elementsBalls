import pygame

class pelota(pygame.sprite.Sprite):
    def __init__(self):
        self.imagen=pygame.image.load("FireBall1.jpg")
        self.recs=[pygame.Rect(320,550,65,25),
                   pygame.Rect(340,532,25,65)]
        self.rect=self.imagen.get_rect()
        (self.rect.left,self.rect.top)=(305,510)
        self.tipo=0
        self.choose=0
        self.nVelX=0
        self.nVelY=0
        
    def cambiarImagen(self,tipo):
        if tipo==1:
            if self.choose==0:
                sound=pygame.mixer.Sound("resources\sounds\\choose.wav")
                sound.play()
                self.choose=1
            self.imagen=pygame.image.load("FireBall1.jpg")
            self.tipo=1
        if tipo==2:
            if self.choose==0:
                sound=pygame.mixer.Sound("resources\sounds\\choose.wav")
                sound.play()
                self.choose=1
            self.imagen=pygame.image.load("DarkBall1.jpg")
            self.tipo=2
        if tipo==3:
            if self.choose==0:
                sound=pygame.mixer.Sound("resources\sounds\\choose.wav")
                sound.play()
                self.choose=1
            self.imagen=pygame.image.load("WaterBall1.jpg")
            self.tipo=3
        if tipo==4:
            if self.choose==0:
                sound=pygame.mixer.Sound("resources\sounds\\choose.wav")
                sound.play()
                self.choose=1
            self.imagen=pygame.image.load("LeafBall1.jpg")
            self.tipo=4
        if tipo==5:
            if self.choose==0:
                sound=pygame.mixer.Sound("resources\sounds\\choose.wav")
                sound.play()
                self.choose=1
            self.imagen=pygame.image.load("LigthBall1.jpg")
            self.tipo=5
        if tipo==6:
            if self.choose==0:
                sound=pygame.mixer.Sound("resources\sounds\\choose.wav")
                sound.play()
                self.choose=1
            self.imagen=pygame.image.load("EarthBall1.jpg")
            self.tipo=6
        if tipo==7:
            self.imagen=pygame.image.load("FireBall2.jpg")
            self.tipo=7
    
    def mover(self,velX,velY):
        self.rect.move_ip(velX,velY)
        for rect in self.recs:
            rect.move_ip(velX,velY)
        #print self.rect.left
        
    def cambiarTipo(self,newT):
        self.tipo=newT
    
    def update(self,screen,velX,velY,tipo):
        self.mover(velX, velY)
        self.cambiarImagen(tipo)
        screen.blit(self.imagen,self.rect)
        if self.rect.left==305 and self.rect.top==510:
            self.recs[0].left,self.recs[0].top=320,550
            self.recs[1].left,self.recs[1].top=340,532
        #for rect in self.recs:
            #pygame.draw.rect(screen,(0,0,255),rect)       
        