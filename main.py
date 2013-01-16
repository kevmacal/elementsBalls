# -*- coding: cp1252 -*-

import pygame
import random
import pelota
import obstaculo

#Class


                    
class meta(object):
    def __init__(self):
        self.rec=pygame.Rect(0,0,100,40)
        self.posX=120
        self.sound1=pygame.mixer.Sound("resources\sounds\\left.wav")
        self.sound2=pygame.mixer.Sound("resources\sounds\\centre.wav")
        self.sound3=pygame.mixer.Sound("resources\sounds\\rigth.wav")     
    
    def crearMeta(self):
        
        self.direccion=random.randrange(0,6)
        self.rec.move_ip(self.direccion*self.posX, 0)
        if self.direccion<2:
            self.sound1.play()
        if self.direccion>1 and self.direccion<4:
            self.sound2.play()
        if self.direccion>3:
            self.sound3.play()            
        
    def pintar(self,screen):
        pygame.draw.rect(screen, (140,121,65), self.rec)
        #pygame.draw.rect(screen, (255,255,255), self.rec)
        
    def collide(self,ball):
        if self.rec.colliderect(ball):
            return True


#Main


def main():
    pygame.init()
    pygame.display.set_icon(pygame.image.load("ico.jpg"))
    screen=pygame.display.set_mode([700,600])
    pygame.display.set_caption("Elements_Balls")
    mainBackground=pygame.image.load("newMain.jpg")
    standByBackground=pygame.image.load("standBy.jpg")
    gameEnd=pygame.image.load("gameEnd.jpg")
    fuente1=pygame.font.SysFont("Lucida Handwriting", 50, False, True)
    fuente2=pygame.font.SysFont("Times New Roman", 50, False,False)
    fuenteFinal=pygame.font.SysFont("Times New Roman", 30, False,False)
    fuenteFinal2=pygame.font.SysFont("Lucida Handwriting", 12, False,False)
    fin1=fuente1.render("Juego", 0, (2,2,3))
    fin2=fuente1.render("Terminado", 0, (2,2,3))
    obst=obstaculo.obstaculo()
    llegada=meta()
    gameBackground=standByBackground
    fps=pygame.time.Clock()    
    soundMain=0
    soundsCaso2=0
    stateAnother=False
    play=False
    inicia=0
    nivel=1
    control=0
    phaseMov=1
    numAyuda=0
    caso=0
    tipoPelota=1
    ejecutar=True
    ballGame=pelota.pelota()
    velX,velY=0,0
    movementX,movementY=0,5
    acabaTiempo=0
    
    while ejecutar:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                ejecutar=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN and stateAnother==False and play==False:
                    pygame.mixer.quit()
                    pygame.mixer.init()
                    stateAnother=True
                    ballGame.rect.left=305
                    ballGame.rect.top=510
                    movementX,movementY=0,5
                    phaseMov=1                   
                    caso=1
                    inicia=1
                if event.key==pygame.K_a and stateAnother==False:
                    soundsCaso2=1
                    stateAnother=True
                    caso=2
                if event.key==pygame.K_q and stateAnother==False:
                    ejecutar=False
                if event.key==pygame.K_RETURN and stateAnother and caso==2:
                    soundsCaso2=0
                    soundMain=260
                    stateAnother=False
                    caso=0
                if event.key==pygame.K_RETURN and stateAnother and play and caso==1 and control>100:
                    acabaTiempo=0
                    soundMain=260
                    stateAnother=False
                    play=False
                    control=0
                    nivel=1
                    tipoPelota=1
                    obst=obstaculo.obstaculo()
                    llegada=meta()
                    caso=0
                if event.key==pygame.K_SPACE and stateAnother and play and caso==1 and phaseMov==1:
                    phaseMov=0                    
                    velY=-movementY
                    ballGame.nVelX=movementX
                    ballGame.nVelY=velY
                if event.key==pygame.K_RIGHT and phaseMov==1:
                    velX=7                    
                if event.key==pygame.K_LEFT and phaseMov==1:
                    velX=-7
                if event.key==pygame.K_f and phaseMov==1 and play:
                    ballGame.choose=0
                    movementY=5
                    tipoPelota=1                    
                if event.key==pygame.K_d and phaseMov==1and play:
                    ballGame.choose=0
                    movementY=5
                    tipoPelota=2
                if event.key==pygame.K_t and phaseMov==1 and play:
                    ballGame.choose=0
                    movementY=7
                    tipoPelota=3
                if event.key==pygame.K_e and phaseMov==1 and play:
                    ballGame.choose=0
                    movementY=4
                    tipoPelota=4
                if event.key==pygame.K_g and phaseMov==1 and play:
                    ballGame.choose=0
                    movementY=5
                    tipoPelota=5
                if event.key==pygame.K_r and phaseMov==1 and play:
                    ballGame.choose=0
                    movementY=3
                    tipoPelota=6
                if event.key==pygame.K_f and phaseMov==1 and caso==2:
                    numAyuda=2                 
                if event.key==pygame.K_d and phaseMov==1and caso==2:
                    numAyuda=1
                if event.key==pygame.K_t and phaseMov==1 and caso==2:
                    numAyuda=6
                if event.key==pygame.K_e and phaseMov==1 and caso==2:
                    numAyuda=4
                if event.key==pygame.K_g and phaseMov==1 and caso==2:
                    numAyuda=3
                if event.key==pygame.K_r and phaseMov==1 and caso==2:
                    numAyuda=5
                if event.key==pygame.K_DOWN and phaseMov==1:
                    if movementX>-8:
                        movementX-=1
                    if movementX<-3:
                        if movementX<-6 and movementY>2:
                            movementY-=2
                        elif movementY>1: movementY-=1                                            
                if event.key==pygame.K_UP and phaseMov==1:
                    if movementX<8:
                        movementX+=1
                    if movementX>3:
                        if movementX>6 and movementY>2:
                            movementY-=2
                        elif movementY>1: movementY-=1  
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    velX=0
                if event.key==pygame.K_LEFT:
                    velX=0
                    
        #Pantalla Principal
        
        if caso==0:
            screen.blit(mainBackground,(0,0))                
            pygame.display.update()
            if soundMain==0:                
                pygame.mixer.music.load("resources\sounds\soundMainI.mp3")
                pygame.mixer.music.play()
            soundMain+=1
            if soundMain>260 and soundMain<300:
                if soundMain==261:
                    pygame.mixer.quit()
                    pygame.mixer.init()
                    pygame.mixer.music.load("resources\sounds\mainSound.mp3")
                    pygame.mixer.music.play()
        #Jugando
                                
        if caso==1:
            acabaTiempo+=1
            if acabaTiempo==50:
                pygame.mixer.quit()
                pygame.mixer.init()
                pygame.mixer.music.load("resources\sounds\mainSound.mp3")
                pygame.mixer.music.play()
            if phaseMov==0 and llegada.collide(ballGame):
                tipoPelota=1
                ballGame.cambiarTipo(tipoPelota)
                phaseMov=1
                velX,velY=0,0
                movementX,movementY=0,5
                ballGame.rect.left=305
                ballGame.rect.top=510
                inicia+=1
                obst=obstaculo.obstaculo()
                llegada=meta()
            if inicia==nivel:
                obst.crearObstaculos(nivel)
                llegada.crearMeta()
                nivel+=1
            if control<200:
                control+=1
            play=True
            screen.blit(gameBackground,(0,0))
            if(phaseMov==1 and ballGame.rect.left<600 and ballGame.rect.left>0):
                ballGame.update(screen,velX,0,tipoPelota)
            else: 
                ballGame.update(screen,0,0,tipoPelota)
                if ballGame.rect.left>600 and phaseMov==1:
                    ballGame.rect.left=1
                    ballGame.recs[0].left=16
                    ballGame.recs[1].left=36
                if ballGame.rect.left<0 and phaseMov==1:
                    ballGame.rect.left=599
                    ballGame.recs[0].left=614
                    ballGame.recs[1].left=634
            if phaseMov==0:
                obst.tratarCollision(ballGame,movementX,velY)
                if ballGame.rect.top<0 or ballGame.rect.top>550:
                    tipoPelota=1
                    ballGame.cambiarTipo(tipoPelota)
                    phaseMov=1
                    velX,velY=0,0
                    movementX,movementY=0,5
                    ballGame.nVelX,ballGame.nVelY=0,0
                    ballGame.rect.left=305
                    ballGame.rect.top=510
                if ballGame.rect.left>600 and phaseMov==0:
                    movementX=-movementX
                    ballGame.nVelX,ballGame.nVelY=movementX,velY
                if ballGame.rect.left<0 and phaseMov==0:
                    movementX=-movementX
                    ballGame.nVelX,ballGame.nVelY=movementX,velY                
                movementX=ballGame.nVelX
                velY=ballGame.nVelY
                tipoPelota=ballGame.tipo                                
                ballGame.update(screen,movementX,velY,tipoPelota)
            
                
            obst.pintar(screen)
            llegada.pintar(screen)
            if acabaTiempo==2475:
                caso=3
            
        #Ayuda
                     
        if caso==2:
            if soundsCaso2==1:
                pygame.mixer.quit()
                pygame.mixer.init()
                pygame.mixer.music.load("resources\sounds\objPr.mp3")
                pygame.mixer.music.play()
                screen.blit(standByBackground,(0,0))
                screen.blit(fuente2.render("Leaf (E)", 0, (15,162,9)),(50,200))
                screen.blit(fuente2.render("Earth (R)", 0, (176,127,22)),(260,200))
                screen.blit(fuente2.render("Water (T)", 0, (2,2,194)),(460,200))
                screen.blit(fuente2.render("Dark (D)", 0, (18,0,46)),(50,500))
                screen.blit(fuente2.render("Fire (F)", 0, (193,7,12)),(260,500))
                screen.blit(fuente2.render("Ligth (G)", 0, (224,233,150)),(460,500))
                screen.blit(pygame.image.load("LeafBall1.jpg"),(60,100))
                screen.blit(pygame.image.load("EarthBall1.jpg"),(270,100))
                screen.blit(pygame.image.load("WaterBall1.jpg"),(470,100))
                screen.blit(pygame.image.load("DarkBall1.jpg"),(60,350))
                screen.blit(pygame.image.load("FireBall1.jpg"),(270,350))
                screen.blit(pygame.image.load("LigthBall1.jpg"),(470,350))
                soundsCaso2+=1
            if soundsCaso2==2:
                if numAyuda==1:
                    pygame.mixer.quit()
                    pygame.mixer.init()
                    pygame.mixer.music.load("resources\sounds\hDark.mp3")
                    pygame.mixer.music.play()
                    numAyuda=0
                if numAyuda==2:
                    pygame.mixer.quit()
                    pygame.mixer.init()
                    pygame.mixer.music.load("resources\sounds\hFire.mp3")
                    pygame.mixer.music.play()                    
                    numAyuda=0
                if numAyuda==3:
                    pygame.mixer.quit()
                    pygame.mixer.init()
                    pygame.mixer.music.load("resources\sounds\hLigth.mp3")
                    pygame.mixer.music.play()
                    numAyuda=0
                if numAyuda==4:
                    pygame.mixer.quit()
                    pygame.mixer.init()
                    pygame.mixer.music.load("resources\sounds\hLeaf.mp3")
                    pygame.mixer.music.play()
                    numAyuda=0
                if numAyuda==5:
                    pygame.mixer.quit()
                    pygame.mixer.init()
                    pygame.mixer.music.load("resources\sounds\hEarth.mp3")
                    pygame.mixer.music.play()
                    numAyuda=0
                if numAyuda==6:
                    pygame.mixer.quit()
                    pygame.mixer.init()
                    pygame.mixer.music.load("resources\sounds\hWater.mp3")
                    pygame.mixer.music.play()
                    numAyuda=0               
        
        #Cuando acaba el tiempo
                
        if caso==3:
            if acabaTiempo==2475:
                sound=pygame.mixer.Sound("resources\sounds\endTime.wav")
                sound.play()
            acabaTiempo+=1
            screen.blit(gameEnd,(0,0))
            if acabaTiempo<2800:
                screen.blit(fin1,(260,150))
                screen.blit(fin2,(180,230))
                niv=str(nivel-1)
                screen.blit(fuente1.render("al Nivel: "+niv, 0, (200,10,40)),(190,300))
                if acabaTiempo==2799:
                    soundMain=260
                    stateAnother=False
                    play=False
                    control=0
                    nivel=1
                    tipoPelota=1
                    obst=obstaculo.obstaculo()
                    llegada=meta()
                    caso=0
                    acabaTiempo=0
                
            
        fps.tick(40)
        
        pygame.display.update()
        
    dialogoSalida=0
    
    #Cierre del juego
       
    while dialogoSalida<90:
        fps.tick(40)
        screen.blit(gameEnd,(0,0))
        screen.blit(fuenteFinal.render("Elements",0, (2,2,3)),(290,150))
        screen.blit(fuenteFinal.render("Balls",0, (2,2,3)),(310,200))
        screen.blit(fuenteFinal2.render("Idea Original y desarrollo al año 2013-2014 por: ",0, (2,2,3)),(185,390))
        screen.blit(fuenteFinal2.render("Kevin M. Calderón B.",0, (2,2,3)),(275,410))
        pygame.display.update()
        dialogoSalida+=1     
        
        
        
    pygame.quit()
    
    
       
main()