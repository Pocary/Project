# 장성진 제작

# 파이게임 모듈을 불러온다.
import pygame
import sys

# 초기화 시킨다.
pygame.init()
width, height = 1024, 576
screen = pygame.display.set_mode((width, height))

# 타이틀 설정
pygame.display.set_caption("lock minigame test")

# 이미지를 가져온다
lock = pygame.image.load("resources/images/lock.png")
first = pygame.image.load("resources/images/first.png")
second = pygame.image.load("resources/images/second.png")
third = pygame.image.load("resources/images/third.png")
fourth = pygame.image.load("resources/images/fourth.png")
fifth = pygame.image.load("resources/images/fifth.png")
sixth = pygame.image.load("resources/images/sixth.png")
seventh = pygame.image.load("resources/images/seventh.png")

# 이미지 크기 조정
lock = pygame.transform.scale(lock, (width, height))
first = pygame.transform.scale(first, (46, 230))
second = pygame.transform.scale(second, (46, 230))
third = pygame.transform.scale(third, (46, 230))
fourth = pygame.transform.scale(fourth, (46, 230))
fifth = pygame.transform.scale(fifth, (46, 230))
sixth = pygame.transform.scale(sixth, (46, 230))
seventh = pygame.transform.scale(seventh, (46, 230))

# 이미지 위치 초기화
lock_x, lock_y = 0, 0
first_x, first_y = 600, 110
second_x, second_y = 650, 110
third_x, third_y = 700, 110
fourth_x, fourth_y = 750, 110
fifth_x, fifth_y = 800, 110
sixth_x, sixth_y = 850, 110
seventh_x, seventh_y = 900, 110

# 클릭 확인 변수
is_first_clicked = False
is_second_clicked = False
is_third_clicked = False
is_fourth_clicked = False
is_fifth_clicked = False
is_sixth_clicked = False
is_seventh_clicked = False
first_offset_x, first_offset_y = 0, 0
second_offset_x, second_offset_y = 0, 0
third_offset_x, third_offset_y = 0, 0
fourth_offset_x, fourth_offset_y = 0, 0
fifth_offset_x, fifth_offset_y = 0, 0
sixth_offset_x, sixth_offset_y = 0, 0
seventh_offset_x, seventh_offset_y = 0, 0

while True:
    screen.fill((0, 0, 0))

    # 모든 요소를 다시 그린다
    screen.blit(lock, (lock_x, lock_y))
    screen.blit(first, (first_x, first_y))
    screen.blit(second, (second_x, second_y))
    screen.blit(third, (third_x, third_y))
    screen.blit(fourth, (fourth_x, fourth_y))
    screen.blit(fifth, (fifth_x, fifth_y))
    screen.blit(sixth, (sixth_x, sixth_y))
    screen.blit(seventh, (seventh_x, seventh_y))

    pygame.display.flip()

    for event in pygame.event.get():
        # X누르면 게임종료
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                first_rect = first.get_rect(topleft=(first_x, first_y))
                second_rect = second.get_rect(topleft=(second_x, second_y))
                third_rect = third.get_rect(topleft=(third_x, third_y))
                fourth_rect = fourth.get_rect(topleft=(fourth_x, fourth_y))
                fifth_rect = fifth.get_rect(topleft=(fifth_x, fifth_y))
                sixth_rect = sixth.get_rect(topleft=(sixth_x, sixth_y))
                seventh_rect = seventh.get_rect(topleft=(seventh_x, seventh_y))

                # 각 이미지 클릭 여부 확인
                if first_rect.collidepoint(event.pos):
                    is_first_clicked = True
                    first_offset_x, first_offset_y = event.pos[0] - first_x, event.pos[1] - first_y
                elif second_rect.collidepoint(event.pos):
                    is_second_clicked = True
                    second_offset_x, second_offset_y = event.pos[0] - second_x, event.pos[1] - second_y
                elif third_rect.collidepoint(event.pos):
                    is_third_clicked = True
                    third_offset_x, third_offset_y = event.pos[0] - third_x, event.pos[1] - third_y
                elif fourth_rect.collidepoint(event.pos):
                    is_fourth_clicked = True
                    fourth_offset_x, fourth_offset_y = event.pos[0] - fourth_x, event.pos[1] - fourth_y
                elif fifth_rect.collidepoint(event.pos):
                    is_fifth_clicked = True
                    fifth_offset_x, fifth_offset_y = event.pos[0] - fifth_x, event.pos[1] - fifth_y
                elif sixth_rect.collidepoint(event.pos):
                    is_sixth_clicked = True
                    sixth_offset_x, sixth_offset_y = event.pos[0] - sixth_x, event.pos[1] - sixth_y
                elif seventh_rect.collidepoint(event.pos):
                    is_seventh_clicked = True
                    seventh_offset_x, seventh_offset_y = event.pos[0] - seventh_x, event.pos[1] - seventh_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                is_first_clicked = False
                is_second_clicked = False
                is_third_clicked = False
                is_fourth_clicked = False
                is_fifth_clicked = False
                is_sixth_clicked = False
                is_seventh_clicked = False

    # 각 막대기를 클릭해서 움직이는 용도
    if is_first_clicked:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        first_y = mouse_y - first_offset_y

    if is_second_clicked:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        second_y = mouse_y - second_offset_y

    if is_third_clicked:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        third_y = mouse_y - third_offset_y

    if is_fourth_clicked:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        fourth_y = mouse_y - fourth_offset_y

    if is_fifth_clicked:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        fifth_y = mouse_y - fifth_offset_y

    if is_sixth_clicked:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        sixth_y = mouse_y - sixth_offset_y

    if is_seventh_clicked:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        seventh_y = mouse_y - seventh_offset_y

    # 변수들을 딕셔너리로 묶음
    data = {
        "first_y": first_y,
        "second_y": second_y,
        "third_y": third_y,
        "fourth_y": fourth_y,
        "fifth_y": fifth_y,
        "sixth_y": sixth_y,
        "seventh_y": seventh_y
    }

    # 조건을 정의한 딕셔너리
    conditions = {
        "clear1": (97 < data["first_y"] < 103),
        "clear2": (102 < data["second_y"] < 108),
        "clear3": (92 < data["third_y"] < 98),
        "clear4": (99 < data["fourth_y"] < 105),
        "clear5": (103 < data["fifth_y"] < 109),
        "clear6": (94 < data["sixth_y"] < 100),
        "clear7": (97 < data["seventh_y"] < 103)
    }

    # 각 변수에 조건 결과를 할당
    clear1 = conditions["clear1"]
    clear2 = conditions["clear2"]
    clear3 = conditions["clear3"]
    clear4 = conditions["clear4"]
    clear5 = conditions["clear5"]
    clear6 = conditions["clear6"]
    clear7 = conditions["clear7"]

    results = [clear1, clear2, clear3, clear4, clear5, clear6, clear7]

    if all(results):
        pygame.quit()
        sys.exit(0)
