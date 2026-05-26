@namespace
class SpriteKind:
    Portal = SpriteKind.create()

def on_on_overlap(sprite2, otherSprite2):
    tiles.set_current_tilemap(tilemap("""
        level5
        """))
    tiles.place_on_tile(Prinsess_Peach, tiles.get_tile_location(0, 0))
sprites.on_overlap(SpriteKind.player, SpriteKind.Portal, on_on_overlap)

def on_up_pressed():
    if True:
        Prinsess_Peach.vy = -200
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_overlap2(sprite, otherSprite):
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    global Dude, Donutfabrik
    info.change_life_by(1)
    sprites.destroy(otherSprite3, effects.confetti, 500)
    if 20 == info.life():
        Dude = sprites.create(img("""
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
                8 9 6 6 6 6 6 9 9 6 6 6 9 8 9 8
                8 9 9 9 9 9 9 9 9 8 8 8 8 9 9 8
                8 8 8 8 8 8 8 8 9 9 9 9 9 8 8 8
                8 6 6 6 9 9 9 6 6 6 6 8 8 8 6 8
                8 9 8 8 8 9 8 9 8 8 8 9 9 9 9 8
                8 9 9 9 6 9 8 9 8 6 9 9 8 6 6 8
                8 6 6 6 6 9 9 9 9 9 6 6 6 8 8 8
                8 8 8 8 8 8 9 8 8 9 8 8 8 9 9 8
                8 9 6 6 9 9 9 6 6 9 6 6 9 6 9 8
                8 6 8 8 9 6 8 8 8 6 8 8 8 8 6 8
                8 6 6 6 9 6 6 9 9 9 9 9 9 6 6 8
                8 8 8 8 8 6 9 6 6 9 8 8 8 8 8 8
                8 9 9 9 6 6 8 8 6 8 6 9 9 9 9 8
                8 6 6 6 9 9 9 6 9 6 9 9 6 6 6 8
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
                """),
            SpriteKind.Portal)
        Donutfabrik = 1
        tiles.place_on_random_tile(Dude, assets.tile("""
            transparency16
            """))
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap3)

mad: Sprite = None
Dude: Sprite = None
Prinsess_Peach: Sprite = None
Donutfabrik = 0
tiles.set_current_tilemap(tilemap("""
    level0
    """))
Donutfabrik = 0
Prinsess_Peach = sprites.create(img("""
        . . . . . . 5 . 5 . . . . . . .
        . . . . . f 5 5 5 f f . . . . .
        . . . . f 1 5 2 5 1 6 f . . . .
        . . . f 1 6 6 6 6 6 1 6 f . . .
        . . . f 6 6 f f f f 6 1 f . . .
        . . . f 6 f f d d f f 6 f . . .
        . . f 6 f d f d d f d f 6 f . .
        . . f 6 f d 3 d d 3 d f 6 f . .
        . . f 6 6 f d 2 2 d f 6 6 f . .
        . f 6 6 f 3 f f f f 3 f 6 6 f .
        . . f f d 3 5 3 3 5 3 d f f . .
        . . f d d f 3 5 5 3 f d d f . .
        . . . f f 3 3 3 3 3 3 f f . . .
        . . . f 3 3 5 3 3 5 3 3 f . . .
        . . . f f f f f f f f f f . . .
        . . . . . 3 3 . . 3 3 . . . . .
        """),
    SpriteKind.player)
tiles.place_on_tile(Prinsess_Peach, tiles.get_tile_location(1, 14))
scene.camera_follow_sprite(Prinsess_Peach)
controller.move_sprite(Prinsess_Peach, 100, 0)
Prinsess_Peach.ay = 300

def on_on_update():
    if tiles.tile_at_location_equals(Prinsess_Peach.tilemap_location(),
        sprites.dungeon.collectible_red_crystal):
        music.play(music.create_song(hex("""
                00a0000408020405001c000f0a006400f4010a0000040000000000000000000000000000000002060020002400012007001c00020a006400f401640000040000000000000000000000000000000003060028002c00012208001c000e050046006603320000040a002d00000064001400013200020100022c0000000400012708000c00012410001400012718001c0002242720002400012530003400012438003c0002242709010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c8000600280029000108
                """)),
            music.PlaybackMode.UNTIL_DONE)
        game.set_game_over_message(True, "Win Win!")
        game.game_over(True)
    if tiles.tile_at_location_equals(Prinsess_Peach.tilemap_location(),
        sprites.dungeon.collectible_blue_crystal):
        game.set_game_over_message(False, "Booo!")
        game.game_over(False)
game.on_update(on_on_update)

def on_update_interval():
    global mad
    if Donutfabrik == 0:
        mad = sprites.create(img("""
                ..............bbbbbbb...........
                ...........bb66663333baa........
                .........bb3367776333663aa......
                ........b33333888333389633aa....
                .......b3333333333333389633aa...
                ......b34443333333333338633bae..
                .....b3455433333333334443333ae..
                ....b33322333dddd3333455233daee.
                ...b3d333333dd3bbbb33322333dabe.
                ..b3d333333d3bb33bb33333333da4e.
                ..bd33333333b33aab3333333223a4ee
                .b3d3663333b33aab33366332442b4ee
                .bd3b983333a3aa3333387633ee3b4ee
                .bd6983333baaa333333387633bb4bee
                b3d6833333bba333333333863ba44ebe
                bdd3333333bb3333333333333a44bebe
                add666633333322333366333ba44bbbe
                ad67776333332442336983d3a444b4e.
                add888b333333ee3369833d3a44b44e.
                add333333333333336833d3a444b4e..
                a3dd3333344433333dddd3a444b44e..
                ab33ddd325543333dd33aa444b44e...
                .eabb3dd32233333baaa4444b44e....
                .ebabb3d333d33baa444443b44e.....
                ..ebaab3ddd3aaa4444433b44e......
                ..eebbaab33a44444333b444e.......
                ...3eebbaab444b333b4444e........
                ....ebeeebbbbbbbb4444ee.........
                .....eebbbb44444444ee...........
                .......eeebbb444eee.............
                ..........eeeeee................
                ................................
                """),
            SpriteKind.food)
        tiles.place_on_random_tile(mad, assets.tile("""
            transparency16
            """))
game.on_update_interval(5000, on_update_interval)
