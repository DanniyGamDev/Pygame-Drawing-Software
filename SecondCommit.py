import pygame


pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()



# -- MISC --

#drawing mechanics


has_selected_line = False
start_drawing_line = False


has_selected_rectangle = False
start_drawing_rectangle = False


has_selected_triangle = False
start_drawing_triangle = False


has_selected_circle = False
start_drawing_circle = False


has_selected_fill = False

last_mouse_pos = None
current_mouse_pos = [0 ,0]
options_selected = 0

# -- GRAPHICS --

#main canvas
canvas_surface = pygame.image.load("Assets/Graphics/canvas.png").convert()
canvas_rect = canvas_surface.get_rect(center = (640, 360))

#save icon
save_icon_surface = pygame.image.load("Assets/Graphics/save_icon.png").convert_alpha()
save_icon_width = save_icon_surface.get_width()
save_icon_height = save_icon_surface.get_height()

save_icon_surface_2 = pygame.transform.scale(save_icon_surface, (save_icon_width * 2, save_icon_height * 2))

save_icon_rect = save_icon_surface_2.get_rect(topleft = (1100, 0))

#background
bg_surface = pygame.image.load("Assets/Graphics/bg.png").convert()
bg_height = bg_surface.get_height()
bg_width = bg_surface.get_height()

screen_ratio_width = 1280 / 16
screen_ratio_height = 720 / 9 

bg_surface_2 = pygame.transform.scale(bg_surface, (bg_width * 200, bg_height * 100))

bg_rect = bg_surface_2.get_rect(center = (640, 360))





#line
line_surface = pygame.image.load("Assets/Graphics/line_icon.png").convert_alpha()
line_width = line_surface.get_width()
line_height = line_surface.get_height()

line_surface_2 = pygame.transform.scale(line_surface, (line_width * 7, line_height * 7))

line_rect = line_surface_2.get_rect(center = (100, 125))

line_selected_surface = pygame.image.load("Assets/Graphics/line_icon_selected.png").convert_alpha()
line_selected_width = line_selected_surface.get_width()
line_selected_height = line_selected_surface.get_height()
line_selected_surface_2 = pygame.transform.scale(line_selected_surface, (line_selected_width * 7, line_selected_height * 7))


line_rect_selcted = line_selected_surface_2.get_rect(center = (100, 125))






#triangle
triangle_surface = pygame.image.load("Assets/Graphics/triangle_icon.png").convert_alpha()
triangle_width = triangle_surface.get_width()
triangle_height = triangle_surface.get_height()

triangle_surface_2 = pygame.transform.scale(triangle_surface, (triangle_width * 7, triangle_height * 7))

triangle_rect = triangle_surface_2.get_rect(center = (100, 275))


triangle_selected_surface = pygame.image.load("Assets/Graphics/triangle_icon_selected.png").convert_alpha()
triangle_selected_width = triangle_selected_surface.get_width()
triangle_selected_height = triangle_selected_surface.get_height()
triangle_selected_surface_2 = pygame.transform.scale(triangle_selected_surface, (triangle_selected_width * 7, triangle_selected_height * 7))


traingle_rect_selcted = triangle_selected_surface_2.get_rect(center = (100, 275))





#rectangle
rectangle_surface = pygame.image.load("Assets/Graphics/rectangle_icon.png").convert_alpha()
rectangle_width = rectangle_surface.get_width()
rectangle_height = rectangle_surface.get_height()

rectangle_surface_2 = pygame.transform.scale(rectangle_surface, (rectangle_width * 7, rectangle_height * 7))

rectangle_rect = rectangle_surface_2.get_rect(center = (100, 425))


rectangle_selected_surface = pygame.image.load("Assets/Graphics/rectangle_icon_selected.png").convert_alpha()
rectangle_selected_width = rectangle_selected_surface.get_width()
rectangle_selected_height = rectangle_selected_surface.get_height()
rectangle_selected_surface_2 = pygame.transform.scale(rectangle_selected_surface, (rectangle_selected_width * 7, rectangle_selected_height * 7))


rectangle_rect_selcted = rectangle_selected_surface_2.get_rect(center = (100, 425))






#circle
circle_surface = pygame.image.load("Assets/Graphics/circle_icon.png").convert_alpha()
circle_width = circle_surface.get_width()
circle_height = circle_surface.get_height()

circle_surface_2 = pygame.transform.scale(circle_surface, (circle_width * 7, circle_height * 7))

circle_rect = circle_surface_2.get_rect(center = (100, 575)) 


circle_selected_surface = pygame.image.load("Assets/Graphics/circle_icon_selected.png").convert_alpha()
circle_selected_width = circle_selected_surface.get_width()
circle_selected_height = circle_selected_surface.get_height()
circle_selected_surface_2 = pygame.transform.scale(circle_selected_surface, (circle_selected_width * 7, circle_selected_height * 7))


circle_rect_selcted = circle_selected_surface_2.get_rect(center = (100, 575))


#lines and shapes already made
items_list = []



running = True
while running:
    current_mouse_pos = pygame.mouse.get_pos()

    #fill screen with a colour
    screen.blit(bg_surface_2, bg_rect)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Main code for selecting options
        if event.type == pygame.MOUSEBUTTONDOWN:


            if start_drawing_line:
                start_drawing_line = False


           
            #line logic
            if line_rect.collidepoint(event.pos):
                if has_selected_line:
                    has_selected_line = False
                else:
                    has_selected_line = True
                    has_selected_triangle = False
                    has_selected_rectangle = False
                    has_selected_circle = False
                    has_selected_fill = False


            #triangle logic
            if triangle_rect.collidepoint(event.pos):
                if has_selected_triangle:
                    has_selected_triangle = False
                else:
                    has_selected_triangle = True
                    has_selected_line = False
                    has_selected_rectangle = False
                    has_selected_circle = False
                    has_selected_fill = False


            #rectangle logic
            if rectangle_rect.collidepoint(event.pos):
                if has_selected_rectangle:
                    has_selected_rectangle = False
                else:
                    has_selected_rectangle = True
                    has_selected_line = False
                    has_selected_triangle = False   
                    has_selected_circle = False
                    has_selected_fill = False


            #circle logic
            if circle_rect.collidepoint(event.pos):
                if has_selected_circle:
                    has_selected_circle = False
                else:
                    has_selected_circle = True
                    has_selected_line = False
                    has_selected_triangle = False
                    has_selected_rectangle = False
                    has_selected_fill = False

        if has_selected_line and event.type == pygame.MOUSEBUTTONDOWN:
            last_mouse_pos = event.pos
            start_drawing_line = True


        # -- DRAWING MECHANICS --
        
        if has_selected_line:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_mouse_pos = event.pos
                print(last_mouse_pos)
                start_drawing_line = True

        
    
    if has_selected_line:
        screen.blit(line_selected_surface_2, line_rect_selcted)


    
    """
    if has_selected_line:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_mouse_pos = event.pos
                print(last_mouse_pos)
                start_drawing_line = True
    """

    """       
    if start_drawing_line:
        pygame.draw.line(screen, "#1CC51C", last_mouse_pos, current_mouse_pos, 10) 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                line_drawn = pygame.draw.line(screen, "#000000", last_mouse_pos, event.pos, 10)  #stop drawing
                start_drawing_line = False
    if has_selected_line:
        screen.blit(line_selected_surface_2, line_rect_selcted)
    """


    if has_selected_triangle:
        screen.blit(triangle_selected_surface_2, traingle_rect_selcted)

    if has_selected_rectangle:
        screen.blit(rectangle_selected_surface_2, rectangle_rect_selcted)

    #if has_selected_fill:
         #   screen.blit(fill_selected_surface_2, fill_rect_selcted)

    if has_selected_circle:
        screen.blit(circle_selected_surface_2, circle_rect_selcted)
    #fills screen with a colour
    

    #draws main graphics

    #line icon
    screen.blit(line_surface_2, line_rect)
    #triangle icon
    screen.blit(triangle_surface_2, triangle_rect)
    #rectangle icon
    screen.blit(rectangle_surface_2, rectangle_rect)
    #circle icon
    screen.blit(circle_surface_2, circle_rect)

    #Canvas
    #print(canvas_rect.topleft)
    screen.blit(canvas_surface, canvas_rect)




    #Drawing Mechanics



    #Save icon
    screen.blit(save_icon_surface_2, save_icon_rect)

    if start_drawing_line:
        pygame.draw.line(screen, "#000C00", last_mouse_pos, current_mouse_pos, 10)

    clock.tick(60)  # limits FPS to 60



   


    #updates screen
    pygame.display.flip()
pygame.quit()



def clear_screen():
    pass





def get_current_mouse_pos():
    current_mouse_pos = pygame.mouse.get_pos() 
