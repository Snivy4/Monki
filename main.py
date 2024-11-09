namespace SpriteKind {
    export const whathtehel = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.vy == 0) {
        mySprite.vy = -150
    }
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (dash > 0) {
        pauseUntil(() => dash < 0)
    } else {
        if (mySprite.vy < -1) {
            mySprite.y += -25
            dash = 1
        } else {
        	
        }
        if (mySprite.vx > 1) {
            mySprite.x += 25
            dash = 1
        } else {
            if (mySprite.vx < -1) {
                mySprite.x += -25
                dash = 1
            } else {
            	
            }
        }
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.vy == 0) {
        mySprite.vy = -150
    }
})
let dash = 0
let mySprite: Sprite = null
mySprite = sprites.create(img`
    . . . . f f f f f . . . . . . . 
    . . . f e e e e e f . . . . . . 
    . . f d d d d e e e f . . . . . 
    . c d f d d f d e e f f . . . . 
    . c d f d d f d e e d d f . . . 
    c d e e d d d d e e b d c . . . 
    c d d d d c d d e e b d c . f f 
    c c c c c d d d e e f c . f e f 
    . f d d d d d e e f f . . f e f 
    . . f f f f f e e e e f . f e f 
    . . . . f e e e e e e e f f e f 
    . . . f e f f e f e e e e f f . 
    . . . f e f f e f e e e e f . . 
    . . . f d b f d b f f e f . . . 
    . . . f d d c d d b b d f . . . 
    . . . . f f f f f f f f f . . . 
    `, SpriteKind.Player)
let mySprite2 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    . . . . . . . . . . . . . . . . 
    `, SpriteKind.whathtehel)
mySprite2.follow(mySprite, 150)
scene.cameraFollowSprite(mySprite2)
mySprite.setPosition(10, 101)
tiles.setCurrentTilemap(tilemap`level2`)
controller.moveSprite(mySprite, 100, 0)
mySprite.ay = 400
mySprite.setStayInScreen(true)
game.onUpdate(function () {
    if (mySprite.vy == 0) {
        dash = 0
    }
})
