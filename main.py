import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_ESCAPE
pygame.init() # ініціалізує бібліотеку pygame

FPS = pygame.time.Clock() #створює об'єкт класу Clock з модуля pygame.time. 
# Об'єкт Clock використовується для вимірювання часу в грі і контролювання швидкості оновлення кадрів.
screen = width, height = 1400, 800 

BLACK = 0, 0, 0
WHITE = 255, 255, 255 
GREEN = 0, 255, 0
BLUE = 0, 0, 255
RED = 255, 0, 0

font = pygame.font.SysFont('Verdana', 20) # створює об'єкт шрифту 

main_surface = pygame.display.set_mode(screen) # використовується для створення вікна гри 
# або поверхні для відображення графічного вмісту. Перeдаємо аргумент screen

player = pygame.image.load('player.png').convert_alpha() #завантажує зображення гравця з файлу "player.png" 
# і створює об'єкт зображення/ Функція pygame.image.load() використовується для завантаження зображення з файлу. 
# У даному випадку, вказаний файл "player.png" містить зображення гравця. Метод convert_alpha() застосовується до 
# завантаженого зображення для оптимізації його використання в грі з врахуванням альфа-каналу (прозорості). 
# Це дозволяє відображати зображення з правильною прозорістю, якщо воно має прозорий фон або прозорі пікселі.
player_rect = player.get_rect() # цей рядок отримує прямокутник (rect) області, яку займає зображення гравця. 
# Метод get_rect() викликається на об'єкті зображення (player у цьому випадку) і повертає прямокутник, який 
# представляє область зображення. Цей прямокутник містить координати та розміри зображення. 
# Змінна player_rect отримує цей прямокутник, і це дозволяє використовувати його для маніпулювання та 
# позиціонування зображення гравця на екрані гри. Наприклад, ви можете встановити початкову позицію гравця, 
# змінювати його координати, перевіряти перетини з іншими об'єктами гри і т. д.
player_speed = 5 #встановлює значення швидкості гравця у грі. Це значення використовується для керування рухом гравця на екрані гри. 

def create_enemy():

    enemy = pygame.image.load('enemy.png').convert_alpha()
    enemy_rect = pygame.Rect(width, random.randint(0, height), *enemy.get_size()) # створює прямокутник (Rect) для об'єкта ворога у грі.
    #pygame.Rect() є конструктором класу Rect в бібліотеці Pygame і використовується для створення прямокутника 
    # на основі заданих параметрів. 
    # У даному випадку, розміри прямокутника визначаються за допомогою методу get_size() на об'єкті enemy, 
    # який є зображенням або об'єктом ворога. Аргументи width та random.randint(0, height) 
    # встановлюють початкові координати x та y прямокутника відповідно. Значення width вказує на 
    # горизонтальне положення ворога на екрані, тоді як random.randint(0, height) генерує випадкову 
    # вертикальну позицію в межах висоти екрану.
    enemy_speed = random.randint(2, 5) # Функція random.randint(a, b) з модуля random генерує випадкове ціле 
    #число в межах вказаних значень a та b, включаючи обидва кінці. У даному випадку, random.randint(2, 5) 
    # генерує випадкове ціле число між 2 і 5 включно.
    return [enemy, enemy_rect, enemy_speed] # повертає список, що містить об'єкти та значення, пов'язані з ворогом у грі.
#enemy представляє об'єкт ворога. Це може бути, наприклад, зображення або інший об'єкт, що відображає ворога 
# на екрані гри. 
# enemy_rect є прямокутником, що визначає позицію та розміри ворога на екрані гри. 
# Він може використовуватись для взаємодії з ворогом, здійснення колізій або інших операцій.
# enemy_speed вказує швидкість руху ворога. Це значення може використовуватись для керування рухом 
# ворога та зміни його позиції на екрані. 
# Повернення цих значень у вигляді списку дозволяє функції або методу передавати ці 
# значення іншим частинам програми для подальшого використання або обробки.

def create_bonus():

    bonus = pygame.image.load('bonus.png').convert_alpha()
    bonus_rect = pygame.Rect(random.randint(0, width), 0, *bonus.get_size())
    bonus_speed = random.randint(2, 5)
    return [bonus, bonus_rect, bonus_speed]

bg = pygame.transform.scale(pygame.image.load('background.png').convert(), screen) #завантажує зображення 
# фону з файлу "background.png", змінює його розмір до розмірів екрану гри і зберігає результат у змінній bg.
#pygame.image.load('background.png') - цей виклик завантажує зображення фону з файлу "background.png" 
# за допомогою функції pygame.image.load(). Завантажене зображення буде представлено об'єктом surface 
# в бібліотеці Pygame.

#.convert() - цей метод викликається на завантаженому зображенні і конвертує його у внутрішній формат, 
# що прискорює подальше відображення зображення.

#pygame.transform.scale(..., screen) - цей виклик змінює розмір зображення до розмірів екрану гри 
# (screen). Він застосовується до об'єкту зображення, отриманого з попередніх кроків.

#bg = ... - отримане зображення зміненого розміру присвоюється змінній bg. Тепер bg містить змінене 
# зображення фону, яке готове для відображення на екрані гри.
bgX = 0
bgX2 = bg.get_width()
bg_speed = 3

CREATE_ENEMY = pygame.USEREVENT + 1 # встановлює значення константи CREATE_ENEMY для події 
#користувача у бібліотеці Pygame.
 # Рядок CREATE_ENEMY = pygame.USEREVENT + 1 встановлює нову константу 
#CREATE_ENEMY, яка має значення, що на одиницю більше, ніж базова константа pygame.USEREVENT. 
# Це дає змогу використовувати цю константу для ідентифікації спеціальної події, наприклад, 
# створення нового ворога у грі.
pygame.time.set_timer(CREATE_ENEMY, 1500) # встановлює таймер для генерації події CREATE_ENEMY 
#з інтервалом 1500 мілісекунд (1.5 секунди).
CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 1500) 

enemies = []
bonuses = []

connections = 0

is_working = True

while is_working:

    FPS.tick(60) #абезпечить, що гра оновлюється не більше, ніж з частотою 60 кадрів в секунду 
    #(FPS - frames per second). Якщо обробка кадрів гри займає менше часу, ніж цей обмежувальний 
    #інтервал, то об'єкт Clock автоматично затримує виконання на необхідний час, щоб забезпечити 
    # стабільну швидкість оновлення.
    for event in pygame.event.get(): #У бібліотеці Pygame функція pygame.event.get() 
        #використовується для отримання всіх активних подій, що виникли в системі, 
        # таких як події клавіатури, миші, вікон та інших. Вона повертає список об'єктів Event, 
        # кожен з яких представляє окрему подію.
        if event.type == QUIT:
            is_working = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
   
    pressed_keys = pygame.key.get_pressed() #повертає стан усіх клавіш на клавіатурі у вигляді булевих значень.

#У бібліотеці Pygame функція pygame.key.get_pressed() використовується для отримання стану 
# всіх клавіш на клавіатурі у данний момент. Вона повертає список, де кожен елемент представляє стан 
# однієї клавіші. Якщо клавіша натиснута, відповідний елемент у списку має значення True, в іншому випадку - False.
    
    # Копіювання фонового зображення на головну поверхню main_surface відбувається 
    #кожну ітерацію основного циклу гри, щоб показувати статичний фон або фон, що рухається, 
    # як у цьому випадку зі змінною bgX.
    bgX -= bg_speed # Цей рядок зменшує значення змінних bgX і bgX2 на величину bg_speed.  ці змінні зазвичай використовуються 
    #для руху фонового зображення (переднього та заднього планів) відповідно. Швидкість руху фону визначається значенням bg_speed.
    # Зменшення значень bgX та bgX2 на bg_speed кожну ітерацію основного циклу гри приводить до зміщення фонового зображення вліво. 
    # Це може створювати ефект руху фону зліва направо, якщо значення bg_speed відповідає бажаній швидкості руху.
    bgX2 -= bg_speed

    if bgX < - bg.get_width():
       bgX = bg.get_width()
#Цей рядок перевіряє, чи фонове зображення bg виходить за межі вікна гри зліва, і якщо так, 
# то переміщує його в кінцеву позицію зправа.
# Умова bgX < -bg.get_width() перевіряє, чи координата bgX фонового зображення bg вийшла за 
# межі вікна гри зліва. bg.get_width() повертає ширину фонового зображення. Це може використовуватися 
# для створення ефекту безкінечного руху фону гри.
    if bgX2 < - bg.get_width():
       bgX2 = bg.get_width()

    main_surface.blit(bg, (bgX, 0)) # У бібліотеці Pygame функція blit() використовується для копіювання зображення 
    #з однієї поверхні на іншу. Вона приймає два параметри: перше - зображення, яке потрібно скопіювати, 
    # і друге - позицію на цільовій поверхні, де буде розміщено копію зображення.
    main_surface.blit(bg, (bgX2, 0))

    main_surface.blit(font.render("Сигналів: " + str(connections), True, WHITE), (width-150, 0)) #створити текстовий рядок, який містить 
    #інформацію про кількість сигналів connections, і потім намалювати цей рядок на головній поверхні.
    main_surface.blit(player, player_rect)
    #Функція blit() в бібліотеці Pygame використовується для копіювання зображень з однієї поверхні на іншу. 
    # У даному випадку, main_surface.blit(player, player_rect) копіює зображення player (зображення гравця) на 
    # головну поверхню гри main_surface. Копіювання відбувається в позиції, яка визначена прямокутником player_rect. 
    # Прямокутник player_rect визначає положення та розміри гравця на головній поверхні. 
    # Цей рядок зазвичай використовується для малювання гравця на екрані гри. Копіювання зображення гравця на 
    # головну поверхню main_surface відбувається кожну ітерацію основного циклу гри, щоб оновлювати відображення 
    # гравця під час руху або зміни стану гри.
    for enemy in enemies:
        enemy[1]= enemy[1].move(-enemy[2], 0)
#Цей код зміщує позицію ворога, збережену у другому елементі списку enemy, на величину -enemy[2] по горизонталі.
#У цьому коді enemy є списком, де елемент з індексом 1 містить прямокутник enemy_rect, що представляє позицію 
# та розміри ворога на головній поверхні гри. enemy[2] є третім елементом списку enemy і містить значення 
# швидкості ворога.
#Рядок enemy[1] = enemy[1].move(-enemy[2], 0) виконує зміщення прямокутника enemy_rect на -enemy[2] 
# пікселів по горизонталі. Значення -enemy[2] вказує на зсув вліво, оскільки від'ємне значення 
# віднімається від поточної позиції.
#Отже, цей рядок зазвичай використовується для руху ворогів в грі. Зміщення позиції ворога на величину 
# -enemy[2] кожну ітерацію основного циклу гри дозволяє переміщати ворогів вліво з заданою швидкістю enemy[2].
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left<0:
            enemies.pop(enemies.index(enemy))
# Цей код перевіряє, чи ліва границя (значення left) прямокутника ворога enemy_rect вийшла за межі 
# лівого краю екрану гри (тобто, чи ворог перетнув ліву межу екрану). Якщо умова виконується, тобто 
# ворог вийшов за межі лівого краю, то він видаляється зі списку ворогів enemies.
        
#Конкретно, рядок if enemy[1].left<0: перевіряє, чи значення left (ліва границя) прямокутника enemy_rect 
# менше нуля, що означає, що ворог вийшов за межі лівого краю екрану.
#Якщо умова виконується, то рядок enemies.pop(enemies.index(enemy)) видаляє ворога зі списку enemies. 
# Функція enemies.index(enemy) знаходить індекс ворога enemy в списку enemies, а потім функція enemies.pop(index) 
# видаляє елемент зі списку за вказаним індексом.

        if player_rect.colliderect(enemy[1]):
            is_working = False
#Цей код перевіряє, чи відбувається зіткнення (колізія) між прямокутником гравця player_rect і 
# прямокутником ворога enemy_rect. Якщо зіткнення відбувається, то змінна is_working встановлюється на значення False.
#Умова player_rect.colliderect(enemy[1]) визначає, чи перетинаються два прямокутники, 
# тобто чи відбувається зіткнення між гравцем і ворогом. Якщо ця умова виконується, то означає, що 
# гравець стикається з ворогом.
#Якщо зіткнення відбувається, то рядок is_working = False встановлює змінну is_working на 
# значення False. Це може використовуватися для зупинки або припинення роботи гри, коли гравець 
# зіткнувся з ворогом. Наприклад, змінна is_working може використовуватися як прапор для контролю стану гри, 
# і коли вона має значення False, гра може припинити свою роботу або виконати певні дії відповідно до логіки гри.
    for bonus in bonuses:
        bonus[1]= bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])

        if bonus[1].bottom>height:
            bonuses.pop(bonuses.index(bonus))

        if player_rect.colliderect(bonus[1]):
            bonuses.pop(bonuses.index(bonus))
            connections += 1
                
    if pressed_keys[K_DOWN] and not player_rect.bottom >= height:
        player_rect = player_rect.move((0, player_speed))
    
    if pressed_keys[K_UP] and player_rect.top >= 0:
        player_rect = player_rect.move((0, -player_speed))

    if pressed_keys[K_RIGHT] and not player_rect.right >= width:
        player_rect = player_rect.move((player_speed, 0))

    if pressed_keys[K_LEFT] and player_rect.left >= 0:
        player_rect = player_rect.move((-player_speed, 0))

    if pressed_keys[K_ESCAPE]:
        is_working = False

    pygame.display.flip() #  оновлює вікно гри, відображаючи зміни, які були зроблені під час останнього циклу гри.