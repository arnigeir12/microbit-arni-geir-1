def on_button_pressed_a():
    basic.show_leds("""
        . # . # .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
    music.play_melody("C5 G C F - A - G ", 120)
    control.wait_micros(1000000)
    basic.show_leds("""
        . # . # .
                . # . # .
                . . . . .
                . # # # .
                # . . . #
    """)
    control.wait_micros(1500000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("you suck!")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("" + str((randint(0, 10))))
    control.wait_micros(2000000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
