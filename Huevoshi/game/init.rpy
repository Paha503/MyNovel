init python:
    def stats_frame(name, level, hp, maxhp, **properties):

        ui.frame(xfill=False, yminimum=None, **properties)

        ui.hbox() # (name, "HP", bar) из (level, hp, maxhp)
        ui.vbox() # name из ("HP", bar)

        ui.text(name, size=20)

        ui.hbox() # "HP" из bar
        ui.text("HP", size=20)
        ui.bar(maxhp, hp,
                xmaximum=150,
                left_bar=Frame("rrslider_full.png", 12, 0),
                right_bar=Frame("rrslider_empty.png", 12, 0),
                thumb=None,
                thumb_shadow=None)

        ui.close()
        ui.close()

        ui.vbox() # level из (hp/maxhp)

        ui.text("Lv. %d" % level, xalign=0.5, size=20)
        ui.text("%d/%d" % (hp, maxhp), xalign=0.5, size=20)

        ui.close()
        ui.close()
