import time
import random
def generate_code():
    return f"{random.randint(1000, 9999)}"
def print_slow(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
def main():
    print_slow("Я решил провести выходные на природе с друзьями.")
    print_slow("На обратном пути домой я почувствовал себя усталым и немного потерял бдительность.")
    print_slow("Внезапно я получил удар по голове и потерял сознание.")
    print_slow("Когда я пришел в себя, я обнаружил, что нахожусь в заброшенном доме.")
    print_slow("Сначала я не придал этому значения, но вскоре понял, что оказался в ловушке.")
    print_slow("В этом доме были жуткие улики, указывающие на то, что здесь жил маньяк.")
    print_slow("Теперь мне нужно выбраться из этого страшного места до того, как он вернется!")
    time.sleep(2)

    rooms = {
        "спальня": ("Спальня", "Вы находитесь в темной спальне."),
        "кухня": ("Кухня", "Вы находитесь на кухне."),
        "коридор": ("Коридор", "Вы находитесь в коридоре."),
        "окровавленная комната": (
            "Окровавленная комната", "Вы видите окровавленную комнату. Оттуда доносятся странные звуки."),
        "железная дверь": ("Комната с железной дверью", "Перед вами железная дверь. Она заперта."),
        "гардеробная": ("Гардеробная", "Вы вошли в темную гардеробную. Здесь много одежды и обуви.")
    }
    current_room = "спальня"
    inventory = set()
    searched_rooms = set()
    visited_hallway = False
    door_code = None
    ghost_encountered = False
    move_count = 0
    note_found = False
    flashlight_found = False
    encountered_maniac = False
    while True:
        room_name, room_description = rooms[current_room]
        print_slow(f"\n{room_description}")
        actions = ["1) Пойти в другую комнату", "2) Обыскать комнату"]
        if current_room == "спальня":
            if note_found:
                actions.append("3) Обыскать камин")
                actions.append("4) Обыскать кладовую")
        if current_room == "коридор":
            actions = ["1) Пойти в другую комнату", "2) Обыскать коридор"]
        action = input(f"Что вы хотите сделать? ({', '.join(actions)}): ")
        if action == "1":
            available_rooms = [room for room in rooms.keys() if room != current_room]
            if not visited_hallway:
                available_rooms = [room for room in available_rooms if
                                   room not in ["окровавленная комната", "железная дверь"]]
            print_slow("Доступные комнаты: " + ", ".join(rooms[room][0] for room in available_rooms))
            move_action = input(f"Куда вы хотите пойти? ({', '.join(available_rooms)}): ")
            if move_action in rooms:
                current_room = move_action
                move_count += 1
                if current_room == "коридор" and not encountered_maniac and "Мешочек со стеклянными камушками" in inventory:
                    encountered_maniac = True
                    print_slow("\nВы заходите в коридор и внезапно сталкиваетесь с маньяком!")
                    print_slow("Он слепой, но очень опасен. У вас есть два выбора:")
                    print_slow("1) Отвлечь маньяка камушками и побежать к окровавленной двери.")
                    print_slow("2) Отвлечь маньяка камушками и побежать к железной двери.")
                    choice = input("Какой выбор вы сделаете? (1 или 2): ")
                    if choice == "1":
                        print_slow("\nВы бросаете камушки в сторону окровавленной двери.")
                        print_slow("Маньяк отвлекается, и вы успеваете добежать до окровавленной двери!")
                        print_slow("Это комната пыток со множеством инструментов и холодного оружия. В ней есть окно.")
                        print_slow("\nУ вас есть два варианта действий:")
                        print_slow("1) Подобрать ближайшее оружие и вступить в схватку с маньяком.")
                        print_slow("2) Прыгнуть в окно.")
                        action_choice = input("Какой выбор вы сделаете? (1 или 2): ")
                        if action_choice == "1":
                            luck = random.choice([True, False])  # 50% шанс на победу
                            if luck:
                                print_slow("\nВы успешно одолели маньяка и выбрались из комнаты пыток!")
                                break
                            else:
                                print_slow("\nК сожалению, маньяк оказался сильнее. Вы погибли...")
                                break
                        elif action_choice == "2":
                            jump_outcome = random.choice(["minor_injury", "broken_leg"])
                            if jump_outcome == "minor_injury":
                                print_slow("\nВы прыгнули в окно и приземлились с незначительным ушибом.")
                                print_slow("Вы успели убежать и спаслись!")
                                break
                            else:
                                print_slow("\nПрыжок был слишком высок, и вы сломали ногу.")
                                print_slow("Маньяк догнал вас и убил...")
                                break
                    elif choice == "2":
                        print_slow("\nВы бросаете камушки в сторону железной двери.")
                        print_slow("Маньяк отвлекается, и вы успеваете добежать до железной двери!")
                        if ghost_encountered and door_code:
                            entered_code = input("Введите четырехзначный код от железной двери: ")
                            if entered_code == door_code:
                                print_slow("Код верный! Вы вспоминаете встречу с призраком и тихо выбираетесь из дома!")
                                print_slow("Вы сбегаете в лес и спасаетесь!")
                                break
                            else:
                                print_slow("Неверный код. Дверь остается запертой.")
                                continue
                        else:
                            print_slow("На двери оказался замок от которого вы не знали пароля; маньяк догоняет вас...")
                            print_slow("К сожалению, вы погибли...")
                            break
                if not ghost_encountered and random.random() < 0.2:  # 20% шанс
                    door_code = generate_code()
                    ghost_encountered = True
                    print_slow(
                        f"\nВы встретили призрака прошлой жертвы! Он нацарапал код от железной двери: {door_code}")
                if move_count > 3 and current_room != "спальня" and not ghost_encountered:
                    print_slow("\nВ спальне что-то разбилось!")
                    print_slow("Когда вы вернетесь в спальню, вы обязательно встретите призрака.")
                if current_room == "коридор":
                    visited_hallway = True
                    print(
                        "\nВы видите две двери: одна с железной дверью, другая окровавленная с доносящимися странными звуками.")
                elif current_room == "окровавленная комната":
                    if "Кухонный нож" in inventory:
                        print_slow("\nВы столкнулись с маньяком!")
                        luck = random.choice([True, False])
                        if luck:
                            print_slow("Вам повезло! Вы убили маньяка и нашли ключи от выхода!")
                            break
                        else:
                            print_slow("К сожалению, маньяк оказался сильнее. Вы погибли...")
                            break
                    else:
                        print_slow("\nВы столкнулись с маньяком и не успели защититься. Вы погибли...")
                        break
                elif current_room == "железная дверь":
                    if door_code:
                        entered_code = input("Введите четырехзначный код от железной двери: ")
                        if entered_code == door_code:
                            print_slow("Код верный! Вы тихо выбираетесь из дома и сбегаете!")
                            break
                        else:
                            print_slow("Неверный код. Дверь остается запертой.")
                elif current_room == "гардеробная":
                    pass

            else:
                print("Неверный выбор. Попробуйте снова.")
        elif action == "2":
            if current_room == "спальня":
                if not note_found:
                    note_found = True
                    inventory.add("Записка о скрытом проходе")
                    print_slow("Вы нашли записку! В ней говорится, что за камином есть скрытый проход.")
                    print_slow("Также упоминается, что за шкафом есть кладовая.")
                else:
                    print_slow("Вы уже нашли записку.")
            elif current_room == "кухня":
                if current_room not in searched_rooms:
                    searched_rooms.add(current_room)
                    inventory.add("Кухонный нож")  # Используем множество для уникальных предметов
                    print_slow("Вы обыскали кухню и нашли кухонный нож!")
                else:
                    print_slow("Вы уже обыскали кухню и ничего нового не нашли.")
            elif current_room == "железная дверь":
                print_slow("Здесь нет ничего интересного для поиска.")
            elif current_room == "гардеробная":
                if current_room not in searched_rooms:
                    searched_rooms.add(current_room)
                    inventory.add("Мешочек со стеклянными камушками")  # Используем множество для уникальных предметов
                    inventory.add("Записка о слепом маньяке")  # Используем множество для уникальных предметов
                    print_slow("Вы обыскали гардеробную и нашли мешочек со стеклянными камушками!")
                    print_slow(
                        "Также вы нашли записку: 'Я была его жертвой... Он слепой, но очень опасен! Будьте осторожны и тихими. Если он услышит вас, у вас не будет шансов!'")
                else:
                    print_slow("Вы уже обыскали гардеробную и ничего нового не нашли.")
            elif current_room == "коридор":
                print_slow("Вы обыскали коридор. Он очень пуст, и вряд ли здесь что-то есть.")
        elif action == "3" and current_room == 'спальня':
            if note_found:
                print_slow("Вы проверяете камин и находите скрытый проход!")
                if flashlight_found:
                    print(
                        "С фонариком вам удается пролезть дальше через канализационную трубу и выбраться к реке на улицу!")
                    break
                else:
                    print("Без фонарика вы теряетесь в темноте и никогда не выбираетесь из пещеры...")
                    break
            else:
                print("Сначала вам нужно найти записку о скрытом проходе.")
        elif action == '4' and current_room == 'спальня':
            if not flashlight_found:
                flashlight_found = True
                inventory.add("Фонарик")
                print_slow("Вы обыскиваете кладовую и находите фонарик!")
            else:
                print_slow("Вы уже обыскали кладовую и нашли фонарик.")
        else:
            print_slow("Неверный выбор. Попробуйте снова.")
if __name__ == "__main__":
    main()
