#-------------------------------------------------------------------------------------------------------------------------------------
import customtkinter as ctk
import random
from PIL import Image
import pygame
#-------------------------------------------------------------------------------------------------------------------------------------
        #apariencia
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

#------------------------------------------------------------------------------------------------------------------------------------- 
        #aplicacion
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        pygame.mixer.init()
#-------------------------------------------------------------------------------------------------------------------------------------
        #ventana
        self.after(201, lambda :self.iconbitmap("big.ico"))
        

        self.title("Steve Vs Warden")
        self.attributes("-fullscreen",True)
        self.resizable(False, False)
        #imagen del player
#-------------------------------------------------------------------------------------------------------------------------------------
        #Variables importantes
        self.muerte = 0
        self.ganar = 0
        self.rondas = 1
        self.vicst = 0
        self.vicwar = 0
        self.value1 = "nada"
        self.numero_aleatorio = "nada"
#-------------------------------------------------------------------------------------------------------------------------------------
        #imagen del waren
        wardenst = ctk.CTkImage(light_image=Image.open("warde.jpg"),
                              dark_image=Image.open("warde.jpg"),
                              size= (1980,1200))
        self.backgr = ctk.CTkLabel(self,image= wardenst, text="")
        self.backgr.place(x= 0, y= 0)  
#-------------------------------------------------------------------------------------------------------------------------------------          
#sistemas de eleccion
        def version1():
                vacio1 = ctk.CTkImage(light_image=Image.open("roca2.png"),
                            dark_image=Image.open("roca2.png"),
                            size= (120,120))
                self.eleccion.configure(image = vacio1)
                self.value1 = "Piedra1"
               
        def version2():
                vacio2 = ctk.CTkImage(light_image=Image.open("papel.png"),
                            dark_image=Image.open("papel.png"),
                            size= (120,120))    
                self.eleccion.configure(image = vacio2)
                self.value1 = "Papel1"
                
        def version3():
                
                vacio3 = ctk.CTkImage(light_image=Image.open("tijerass.png"),
                            dark_image=Image.open("tijerass.png"),
                            size= (120,120)) 
                self.eleccion.configure(image = vacio3)     
                self.value1 = "Tijeras1"   
#-------------------------------------------------------------------------------------------------------------------------------------                
        def luchar():
                self.numero_aleatorio = random.choice(["Piedra","Papel","Tijeras"])   
                aletoriedad()  
#-------------------------------------------------------------------------------------------------------------------------------------              
        #boton de roca
        roca = ctk.CTkImage(light_image=Image.open("roca2.png"),
                            dark_image=Image.open("roca2.png"),
                            size= (120,120))
        self.roca = ctk.CTkButton(self,image= roca,text="",command=version1,
                                  fg_color="transparent")
        self.roca.place(x= 1600, y= 380)
#-------------------------------------------------------------------------------------------------------------------------------------        
        #boton de roca
        papel = ctk.CTkImage(light_image=Image.open("papel.png"),
                            dark_image=Image.open("papel.png"),
                            size= (120,120))
        self.papel = ctk.CTkButton(self,image= papel,text="",command=version2,
                                   fg_color="transparent")
        self.papel.place(x= 1600, y= 580)
#-------------------------------------------------------------------------------------------------------------------------------------       
         #boton de tijeras
        tijeras = ctk.CTkImage(light_image=Image.open("tijerass.png"),
                            dark_image=Image.open("tijerass.png"),
                            size= (120,120))
        self.tijeras = ctk.CTkButton(self,image= tijeras,text="",command= version3,
                                     fg_color="transparent")
        self.tijeras.place(x= 1600, y= 780)
#-------------------------------------------------------------------------------------------------------------------------------------
        #boton warnen        
        normal = ctk.CTkImage(light_image=Image.open("nono.png"),
                            dark_image=Image.open("nono.png"),
                            size= (120,120))
        self.vacio = ctk.CTkButton(self,image= normal,text="",fg_color="transparent")
        self.vacio.place(x= 800, y= 380)
#-------------------------------------------------------------------------------------------------------------------------------------       
        #vida
        self.vidasteve = ctk.CTkProgressBar(self,height= 40, orientation= "horizont", width= 640, 
                                            fg_color="green",
                                            progress_color="red",determinate_speed=0,corner_radius=0)
        self.vidasteve.place(x=1103,y=100)
        self.vidasteve.set(0)
        
        self.vidawar = ctk.CTkProgressBar(self,height= 40, orientation= "horizont", width= 640, 
                                          fg_color="darkblue",
                                          progress_color="red",determinate_speed=0,corner_radius=0)
        self.vidawar.place(x=200,y=100)
        self.vidawar.set(0)
#------------------------------------------------------------------------------------------------------------------------------------- 
        #Cuadro de uestra eleccion ya sea piedra papel o tijera
        normal2 = ctk.CTkImage(light_image=Image.open("nono.png"),
                            dark_image=Image.open("nono.png"),
                            size= (120,120))
        self.eleccion = ctk.CTkButton(self,image=normal2, text= "",fg_color="transparent")
        self.eleccion.place(x= 1100, y= 380)
        self.eleccion == "nada"
#------------------------------------------------------------------------------------------------------------------------------------- 
        #Cuadro de rondas
        self.rondas1 = ctk.CTkLabel(self, text=f"Round {self.rondas}", 
                                    fg_color="transparent",font=('skia', 15),
                                    width=140,height=40)
        self.rondas1.place(x=900, y=100)
#------------------------------------------------------------------------------------------------------------------------------------- 
        #Cuadros de victorios de cada jugador
        self.victoriaste = ctk.CTkLabel(self, text=f"Win {self.vicst}", 
                                        fg_color="transparent",font=('skia', 15),
                                        width=140,height=40)
        self.victoriaste.place(x=1750, y=100) 
        
        self.victoriawar = ctk.CTkLabel(self, text=f"Win {self.vicwar}", 
                                        fg_color="transparent",font=('skia', 15),
                                        width=140,height=40)
        self.victoriawar.place(x=50, y=100) 
#-------------------------------------------------------------------------------------------------------------------------------------
        #luchar con espada        
        sword = ctk.CTkImage(light_image=Image.open("diamond.png"),
                            dark_image=Image.open("diamond.png"),
                            size= (120,120))
        self.lucha = ctk.CTkButton(self,image= sword, text= "", command= luchar,fg_color="transparent")
        self.lucha.place(x=1100 , y= 580)
#-------------------------------------------------------------------------------------------------------------------------------------  
        #Imagenes al ganar o perder
        self.wincreem= ctk.CTkLabel(self, text= "")
        self.wincreem.place(x= 0, y= 0)
        self.deadscreem= ctk.CTkLabel(self,text= "")
        self.deadscreem.place(x= 0, y= 0) 
        
        def ganastes():
                        win = ctk.CTkImage(light_image=Image.open("Youwin.png"),
                            dark_image=Image.open("Youwin.png"),
                            size= (1920,1080))
                        self.wincreem.configure(image = win)
                        self.rondas1.configure(text=f"Round {self.rondas}") 
                        self.victoriaste.configure(text=f"Win {self.vicst}") 
                        sonidito1()
        def temoriste():
                        dead = ctk.CTkImage(light_image=Image.open("youlose.png"),
                            dark_image=Image.open("youlose.png"),
                            size= (1920,1080))
                        self.deadscreem.configure(image = dead)
                        self.rondas1.configure(text=f"Round {self.rondas}")
                        self.victoriawar.configure(text=f"Win {self.vicwar}")      
                        sonidito2()                
#-------------------------------------------------------------------------------------------------------------------------------------  
        #Funcion de aleotoriedad con las condicionales para poder luchar               
        def aletoriedad(): 
#-------------------------------------------------------------------------------------------------------------------------------------
                vacio1 = ctk.CTkImage(light_image=Image.open("roca2.png"),
                            dark_image=Image.open("roca2.png"),
                            size= (120,120))
                vacio2 = ctk.CTkImage(light_image=Image.open("papel.png"),
                            dark_image=Image.open("papel.png"),
                            size= (120,120))
                vacio3= ctk.CTkImage(light_image=Image.open("tijerass.png"),
                            dark_image=Image.open("tijerass.png"),
                            size= (120,120))
#-------------------------------------------------------------------------------------------------------------------------------------               
                if self.numero_aleatorio == "Piedra":
                        self.vacio.configure(image = vacio1)
                elif self.numero_aleatorio == "Papel":
                        self.vacio.configure(image = vacio2)
                elif self.numero_aleatorio == "Tijeras":
                        self.vacio.configure(image =vacio3)           
#-------------------------------------------------------------------------------------------------------------------------------------                    
                if self.numero_aleatorio == "Tijeras" and self.value1 == "Piedra1":
       
                    
                    self.vidawar.configure(determinate_speed = 5)
                    self.vidawar.step()
                    self.ganar += 10
                    warda.play()
                elif self.numero_aleatorio == "Piedra" and self.value1 == "Papel1":
                  
                    
                    self.vidawar.configure(determinate_speed = 5)
                    self.vidawar.step()
                    self.ganar += 10
                    warda.play()
                elif self.numero_aleatorio == "Papel" and self.value1 == "Tijeras1":
                
                    
                    self.vidawar.configure(determinate_speed = 5)
                    self.vidawar.step()
                    self.ganar += 10
                    warda.play()
#-------------------------------------------------------------------------------------------------------------------------------------            
                elif self.numero_aleatorio == self.value1:
                                
                                self.vidawar.step()
                                self.vidawar.configure(determinate_speed = 0)
                elif self.numero_aleatorio == "Tijeras" and self.value1 == "Papel1":
                                
                                
                                self.vidasteve.configure(determinate_speed = 5)
                                self.vidasteve.step()
                                self.muerte += 10
                                steveda.play()  
                elif self.numero_aleatorio == "Piedra" and self.value1 == "Tijeras1":
                               
                                
                                self.vidasteve.configure(determinate_speed = 5)
                                self.vidasteve.step()
                                self.muerte += 10
                                steveda.play()  
                elif self.numero_aleatorio == "Papel" and self.value1 == "Piedra1":
                                
                                
                                self.vidasteve.configure(determinate_speed = 5)
                                self.vidasteve.step()
                                self.muerte += 10
                                steveda.play()  
#-------------------------------------------------------------------------------------------------------------------------------------
        #Cuando sacar las imagenes de muerte y de ganar
                if self.ganar == 100:
                        print(self.ganar)
                        self.rondas += 1  
                        self.vicst += 1
                        ganastes()
                                                      
                if self.muerte == 100:
                        print(self.muerte)
                        self.rondas += 1
                        self.vicwar += 1    
                        temoriste() 
#-------------------------------------------------------------------------------------------------------------------------------------
        #Sonidos al golpear steve o warden               
        steveda = pygame.mixer.Sound(r"C:\Users\randy\OneDrive\Documents\Python\.vscode\oof.mp3")
                           
        warda =  pygame.mixer.Sound(r"C:\Users\randy\OneDrive\Documents\Python\.vscode\warden.mp3") 
        
        def sonidito1():
                pygame.mixer.music.load(r"C:\Users\randy\OneDrive\Documents\Python\.vscode\xp.mp3")  
                pygame.mixer.music.play(0)
                
        def sonidito2():
                pygame.mixer.music.load(r"C:\Users\randy\OneDrive\Documents\Python\.vscode\stxp.mp3")  
                pygame.mixer.music.play(0)
                
        pygame.mixer.music.load(r"C:\Users\randy\OneDrive\Documents\Python\.vscode\Ancestry.mp3") 
                
        pygame.mixer.music.play(-1)
#-------------------------------------------------------------------------------------------------------------------------------------                     
        
        

        #cerrar y reiniciar
        def cerrar():
                self.destroy()
                
        def reiniciar():
                self.ganar = 0
                self.muerte = 0
                self.vidawar.set(0)
                self.vidasteve.set(0)
                self.vidasteve.configure(determinate_speed = 0)
                self.vidawar.configure(determinate_speed = 0)
                self.wincreem.configure(image = "")
                self.deadscreem.configure(image = "")
                self.numero_aleatorio = "q"
                self.value1 = "q"
                self.eleccion.configure(image = normal)
                self.vacio.configure(image = normal)
                
                pygame.mixer.music.load(r"C:\Users\randy\OneDrive\Documents\Python\.vscode\Ancestry.mp3") 
                pygame.mixer.music.play(-1)
        
        exit_button1 = ctk.CTkButton(self, text="Salir", command=cerrar, 
                                     fg_color="transparent",font=('skia', 15),
                                     width=140,height=50)
        exit_button1.place(x=1600, y=1000)

        self.reset_button1 = ctk.CTkButton(self, text="Reiniciar", command=reiniciar, 
                                           fg_color="transparent",font=('skia', 15),
                                           width=140,height=50)
        self.reset_button1.place(x=1450, y=1000)    
#-------------------------------------------------------------------------------------------------------------------------------------          
if __name__ == "__main__":
    app = App()
    app.mainloop()