import pygame

pygame.init()
ekran = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

dzialanie=True
gora=False
skok=False

pozycja=[640,360]
poprzednia_pozycja_y=0
grawitacja=0
kierunek_w_x=0
kierunek_w_y=0

zliczanie_do_grawitacji=30 #wysokosc pierwszego skoku
odbicia=12 #do odbijania pilki

while dzialanie:
    for event in pygame.event.get():
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            dzialanie = False
        if event.type == pygame.QUIT:
            dzialanie= False
    ekran.fill('white')

    pygame.draw.circle(ekran,(0,0,0),(pozycja[0],pozycja[1]),10)
    pozycja[0]=pozycja[0]+kierunek_w_x
    if skok:
        pozycja[1]=pozycja[1]+((kierunek_w_y)*(1-(grawitacja/zliczanie_do_grawitacji)))
    if grawitacja>=zliczanie_do_grawitacji:
        grawitacja=grawitacja-4#bez zawisu w gornym punkcie
        skok=False #przestaje dodawac do skoku
        gora=True #znacznik pozycji gornej
        #ss
    if gora: #opadanie
        pozycja[1]=pozycja[1]-((kierunek_w_y)*(1-(grawitacja/zliczanie_do_grawitacji)))
        if pozycja[1]>poprzednia_pozycja_y:
            pozycja[1]=poprzednia_pozycja_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        kierunek_w_x=10
    if keys[pygame.K_a]:
        kierunek_w_x=-10
    elif not keys[pygame.K_d]:
        kierunek_w_x=0
    if keys[pygame.K_w] and grawitacja==0 and odbicia==12:
        poprzednia_pozycja_y=pozycja[1]
        kierunek_w_y=-33#zalezny od ilosci odbic i aktualizacji wartosci kierunku w y
        skok=True
    #od razu po wcisnieciu przycisku robi skok=True wiec pierwszy cykl od razu wyzej mnozy przez stala grawitacji

    pygame.display.update()
    deltaT=clock.tick(20)
    if skok:
        grawitacja=grawitacja+4
    #test
    #if grawitacja >= zliczanie_do_grawitacji:
        #print(pozycja[1])
    if gora: #zaczyna odejmowac
        grawitacja=grawitacja-4

        if grawitacja<=0: #kiedy odejmie do zera

            gora=False #wylacz odejmowanie
            #wkierunek_w_y=0 #reset kierunku w y zeby pilka pozostala w spoczynku (po przerobce wywalic bo patrz 3 linie nizej)
            if odbicia>0:
                skok=True
                #************
                grawitacja=grawitacja+4 #rozwiazanie problemu z pozostawaniem pilki wyzej po odbiciu. w pierwszym
                #cyklu po wcisnieciu W grawitacja od razu sie dodawala. w kolejnych cyklach grawitacja sie zerowala
                #a skok byl dalej True wiec pierwszy skok w nowym cyklu pilka wykonywala na pelna wysokosc kierunek_w_y
                kierunek_w_y = kierunek_w_y+3#nowa predkosc po odbiciud
            odbicia=odbicia-1
            zliczanie_do_grawitacji=((odbicia*2.2))#+(6-odbicia))-3 #wielokrotnosci
            #pozycja[1]=poprzednia_pozycja_y
            if odbicia==0: #jak dojdzie do zera z odbiciami to zresetuj
                odbicia=12
                zliczanie_do_grawitacji=30
                skok=False
                grawitacja=0

    #test notatki:
    #odbija wyzej bo odejmuje do innej niz skoczyla
    #print("poz", pozycja[1])
    #print(kierunek_w_y)
    #print(poprzednia_pozycja_y)
    #print('zliczanie',zliczanie_do_grawitacji)
    #print('graw',grawitacja)
    #print(odbicia)
pygame.quit()