import turtle


# msgr font is Roboto

# draw rounded corner
def corner(tess):
    for i in range(15):
        tess.right(6)
        tess.forward(2)


# draw rounded, filled rectangle of around (40+h)*(40+w) dimensions
def round_rec(tess, h, w):
    tess.pd()
    tess.begin_fill()
    tess.seth(0)
    for i in [w, h, w, h]:
        tess.forward(i)
        corner(tess)
    tess.end_fill()


# write out a message with a set width
def write_block(tess, text, w):
    tess.pu()
    x = tess.xcor()
    y = tess.ycor()
    line = 0
    font_h = 16
    for i in range(len(text)):
        if tess.xcor() - x >= w - 3:
            line += 1
            tess.goto(x, (y - line * (font_h + 7)))
        tess.write(text[i], True, font=("Roboto", font_h, "normal"))
    # tess.seth(0)
    # tess.forward(2)


# draw one text bubble for the input text at the predefined width
def bubble(tess, text, w, x_i, y_i, bubble_color="blue", text_color="white"):
    tess.pu()
    tess.goto(x_i, y_i)
    # write out everything to see how tall it should be
    write_block(tess, text, w)
    h = abs(tess.ycor() - y_i) + 5
    tess.goto(x_i, y_i + 30)
    tess.pencolor(bubble_color)
    tess.fillcolor(bubble_color)
    # fill in bubble
    round_rec(tess, h, w)
    tess.pu()
    tess.seth(270)
    tess.forward(32)
    tess.pencolor(text_color)
    # rewrite everything bc the rectangle filled in over it
    # yes it is horribly inefficient yes there's probably a better way
    # oh well
    write_block(tess, text, w)
    return h


# draw a full conversation from messages
def draw_conversation(messages, w):
    # basic set up and such
    wn = turtle.Screen()
    wn.bgcolor("white")
    wh = wn.window_height() / 2 - 50
    ww = wn.window_width() / 2 - 50
    y = wh
    them_x = -ww
    you_x = them_x + 0.7 * w

    tess = turtle.Turtle()
    tess.pensize(3)
    tess.pu()

    # draw appropriate bubble in appropriate location depending on whose msg
    prior = True
    for sender, text in messages:
        if prior != sender:
            y -= 7
        if sender:
            y -= bubble(tess, text, w, you_x, y) + 45
        else:
            y -= bubble(tess, text, w, them_x, y, "lightgrey", "black") + 45
        prior = sender

    wn.exitonclick()


# Example usage
text0 = """Yo what's up dawwwwg?"""
text1 = """It's somewhat of a saga, my friend, I fear I'd bore you to tears"""
text2 = """Nah man come on tell me some, you know I'm one for the gossip :D"""
text3 = """Okay then, let me tell you the story of Mel. """
text4 = """Back in the Good Old Days, when the term 'software' sounded funny  
and Real Computers were made out of drums and vacuum tubes, 
Real Programmers wrote in machine code. Not FORTRAN.  Not RATFOR.  Not, even,
assembly language. 
Machine Code. Raw, unadorned, inscrutable hexadecimal numbers. Directly."""
text5 = """OMG am I looking forward to the rest of this."""

# True for messages sent by you; False for those sent by someone else.
msgs = [(True, text0), (False, text1), (True, text2),
        (False, text3), (False, text4), (True, text5)]

draw_conversation(msgs, 300)
