input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        `)
    music.playMelody("C5 G C F - A - G ", 120)
    control.waitMicros(1000000)
    basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
        `)
    control.waitMicros(1500000)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("you suck!")
})
input.onButtonPressed(Button.B, function () {
    basic.showString("" + (randint(0, 10)))
    control.waitMicros(2000000)
    basic.clearScreen()
})
