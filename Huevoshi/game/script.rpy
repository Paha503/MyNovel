﻿# Вы можете расположить сценарий своей игры в этом файле.
init:
    $ d = 0 #число смертей
# Определение персонажей игры.
define null_konst = Character('Галлюцинационный Конст', color="#ff0000")
define null_konst_name = Character('Галя', color="#ff0000")
define hero = Character('[player_name]', color="#008080")
define security = Character('Охранница', color="#0000ae")
define bar_kat = Character('Барменша', color="#9400d3")
define director_paha = Character('Директор', color="#2f4f4f")
define artemy = Character('Тьома', color="#8B0000")


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    play music "music/silence.mp3" fadeout 1
    "Вы стоите в полной пустоте, полной неизведанности."
    "Наверное вы должны сделать что-то вроде : \"*ВЫБЕРИ СВОЮ СУДЬБУ*\""
    null_konst "{color=#f00}Ну привет, игрок!{/color}"
    null_konst "{color=#f00}Давай познакомимся!\nМеня зовут Галюцинационный Конст, но ты можешь звать меня Галя!{/color}"
    null_konst_name "{color=#f00}А как тебя зовут?{/color}"
    $ player_name = renpy.input("{color=#f00}Назовите имя павшего ангела:{/color}")
    if player_name == "Конст":
        null_konst_name "{color=#f00}ТЫ НЕ МОЖЕШЬ.{/color}"
        $ player_name = "Идиот"
        "{color=#f00}G A M E  O V E R .{/color}"
        jump gameover
    null_konst "{color=#f00}Я НАДЕЮСЬ МЫ БОЛЬШЕ НЕ УВИДИМСЯ, [player_name]!{/color}"

    play music "music/fakelove.mp3" fadeout 1
    scene start

    "Вы стоите в темнеющем переулке, единственным источником света в котором является небольшая неоновая вывеска кафе с необычным названием - \"Хуевощи\"."

    "Ваши друзья рассказывали про это место и, Вы должны признаться, что без их совета данное кафе было тяжело найти."

    scene downstairs

    "Перед Вами была маленькая, потрепанная и уже облезающая металлическая спусковая лестница, которая уходила глубоко вниз. На стенах рядом красовались пара десяток граффити, содержащие в себе нецензурную брань"

    "Собравшись с мыслями, Вы решаете всё-таки спуститься вниз."

    scene door

    "Пройдя несколько ступенек Вы сталкиваетесь с металлической дверью уже бурого, выцветшего цвета"

    "Ручка двери не поддавалась, поэтому Вам пришлось постучать. Небольшое отверстие сверху разъезжается и на вас смотрит пара глаз"

    "???" "Чего тебе?\n(голос звучит агрессивно и не располагает к общению.)"

    "Вас предупреждали о \"подобной\" проверке."

    menu:
        "Я к вам на работу пришел устраиваться, пустите, а то на улице холодно пиздец":
            jump v1
        "Я хочу устроиться мыть полы.":
            jump v2
        "*Харкнуть в отверстие*":
            "MISSON FAILED\nТы гребаный долбоеб."
            jump gameover
    label gameover:
        $ d += 1
        if d == 1:
            label first_death:
                hero "{color=#008080}Что со мной случилось?\nПочему я снова в этом странном месте?{/color}"
                null_konst_name "{color=#f00}Похоже, что ты умер!{/color}"
                null_konst_name "{color=#f00}Как же ты все таки жалок!{/color}"
                null_konst_name "{color=#f00}А теперь перестань быть ленивой жопой и возродись в самом начале!\n=){/color}"
                jump start
        if d <=15:
            label standart_death:
                null_konst_name "{color=#f00}ТЫ СНОВА ОПОДЛИВИЛСЯ!{/color}"
                null_konst_name "{color=#f00}Ты умер уже [d] раз!{/color}"
                null_konst_name "{color=#f00}Удачи, [player_name]!\n=){/color}"
                jump start
        if d > 15:
            label ustoppable_determination_never_death:
                null_konst_name "{color=#f00}Умерев [d] раз ты так и не сдался?{/color}"
                null_konst_name "{color=#f00}Интересно, очень интересно, [player_name]!\n=){/color}"
                jump start
    label v1:
        "???" "Чего сразу не постучал, яйца на морозе мял, дебил. Заходи."
        jump after_start
    label v2:
        "???" "Нам только посудомойки нужны, но проходи."
        jump after_start
    label after_start:
        scene blackhole
        "Как только вы проходите внутрь, то лицом к лицу сталкиваетесь с девушкой в форме охранника."
        menu:
            "Представиться":
                hero "{color=#008080}Меня зовут [player_name]. Надеюсь в будущем мы станем коллегами{/color}"
                security "{color=#0000ae}Как скажешь.{/color}"
            "Молча пройти мимо":
                "Вы прошли мимо охранницы."
        scene strip
        play music "music/club.mp3" fadeout 1
        "Вы входите в наполненный шумной музыкой клуб. На сцене какой-то юный панк брынчит что-то современное на своей электро-гитаре. У бара, на стульях сидит уже храпящая клиентура. В середине огромного зала на сцене кто-то флексит."
        "Вы решаете подойти к барменше, неторопливо перемешивающей очередной коктейль."
        scene stripbar
        "Она мычала про себя песню и не особо концентрировала внимание на Вас."
        menu:
            "Перебить и задать вопрос: где найти начальника.":
                jump next
            "Продолжить слушать, в конце сделать комплимент.\n(Барменша(???))":
                jump notfull_kotya
        label notfull_kotya:
            "Она смущается и отводит взгляд в сторону, тихо хмыкая \"Спасибо\""
            bar_kat "{color=#9400d3}Вы кто?{/color}"
            hero "{color=#008080}Я [player_name], пришел на собеседование.{/color}"
            "Она выдавливает из себя улыбку и кивает Вам в сторону коридора."
            "Вы благодарите и уходите."
            jump after_after_start
        label next:
            "Вы громко откашливаетесь, заставляя девушку вздрогнуть. Она роняет свой миксер в раковину и переводит взгляд на Вас."
            bar_kat "{color=#9400d3}Вы к директору на собеседование?{/color}"
            hero "{color=#008080}Да.{/color}"
            "Девушка заправляет прядь волос за ухо и указывает на коридор справа от себя."
            bar_kat "{color=#9400d3}Иди вперёд, не ошибёшься.{/color}"
            "Вы благодарите и уходите."
            jump after_after_start
        label after_after_start:
            play music "music/office.mp3" fadeout 1
            scene hall
            "Вы идете вдоль короткого коридора, осматривая небольшие картины некого мужчины...\nКоторый постоянно на них светился."
            "Вы делаете вывод, что это сам директор."
            scene dirdoor
            "Подходя к концу, впереди красовалась стальная дверь с инкрустированными в неё алмазами, которые формировали собой слово \"директор\""
            scene office
            "Не долго думая, Вы открываете дверь и осматриваете стильную большую комнату с большими бежевыми диванами, столом из красного дерева и куда больше картин с молодым человеком, который сейчас сидел за столом и уставился в монитор."
            "На столе стоит табличка, похоже, золотого отлива, где было написано \"Павел Вильсон\".\nВы итак уже понимали, что мужчина перед вами - начальник, но это развеяло все сомнения."
            menu:
                "Выйти и зайти заново":
                    jump aasv1
                "Как-нибудь иначе привлечь его внимание":
                    jump aasv2
            label aasv1:
                "Он продолжает вас не замечать."
                menu:
                    "Продолжить выходить и заходить, пока он вас не заметит.":
                        "Вы сломали дверь, но у вас не было денег оплатить ремонт, потому что вы так и не устроились на работу."
                        "Может, на Нарах вам больше повезет."
                        "MISSON FAILED\nТы гребаный долбоеб."
                        jump gameover
                    "Откашляться, привлекая внимание.":
                        jump aasv2
            label aasv2:
                "Вы стучите костяшками по полуприкрытой двери сзади и парень переводит свой взгляд с экрана на вас с задумчивым видом."
                menu:
                    "Вы уверенно представляетсь.":  ###8б-1
                        director_paha "{color=#2f4f4f}Нам как раз нужны работники!{/color}"
                        "Он протягивает Вам контракт. Вы хотите спросить о собеседовании, но решаете, что лучше не испытывать судьбу."
                        jump ch9
                    "Вы продолжаете молчать.":      ###8б-2
                        director_paha "{color=#2f4f4f}Вы на собеседование?{/color}"
                        hero "{color=#008080}Да.{/color}"
                        jump ch9
            label ch9:
                "Директор проводит с вами небольшое собеседование"
                menu:
                    "Отвечать на вопросы не задумываясь.": ###9а
                        "Вы отвечали на вопросы так, будто находились под действием каких-то препаратов, что смутило его."
                        "MISSON FAILED\nТы гребаный долбоеб."
                        jump gameover
                    "Подумать перед ответом":
                        "Директор внимательно слушал ваши ответы."
                        "Он довольно кивнул и выдал Вам документы для подписи."
                        "Вы официально приняты на работу"
                        jump firstday
                    "На неудобных вопросах чаще молчать":
                        "Директор заметил Ваше нежелание тщательно вести беседу."
                        "Он не стал пытаться вас разговорить и протянул вам документы для трудоустройства."
                        jump firstday
            label firstday:
                "Тут будет первый день"
    return
