import pygame

def reproducir_audio():
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load("meditacion.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  
            
    except pygame.error as e:
        print("Error al reproducir el audio:", e)

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()

reproducir_audio()
