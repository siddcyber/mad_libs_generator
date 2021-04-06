from tkinter import *

my_entries = []

main = Tk()


def button_hover(e):
    button1["bg"] = "#FFF2BA"
    return


def button_hover1(e):
    button2["bg"] = "#FFF2BA"
    return


def button_hover2(e):
    button3["bg"] = "#FFF2BA"
    return


def button_hover3(e):
    button4["bg"] = "#FFF2BA"
    return


def button_hover4(e):
    button5["bg"] = "#FFF2BA"
    return


def button_hover_leave(e):
    button1["bg"] = "#F0FFFF"
    return


def button_hover1_leave(e):
    button2["bg"] = "#F0FFFF"
    return


def button_hover2_leave(e):
    button3["bg"] = "#F0FFFF"
    return


def button_hover3_leave(e):
    button4["bg"] = "#F0FFFF"
    return


def button_hover4_leave(e):
    button5["bg"] = "#F0FFFF"
    return


def button_exit_hover_leave(e):
    button_exit["bg"] = "#F0FFFF"
    return


def button_exit_hover(e):
    button_exit["bg"] = "#FFF2BA"
    return


def button_submit_hover_leave(e):
    submit["bg"] = "#F0FFFF"
    return


def button_submit_hover(e):
    submit["bg"] = "#FFF2BA"
    return


def disable():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)


def bookish():
    disable()

    frame = LabelFrame(main, bg="#F0FFFF", bd=0)
    frame.grid(row=3, column=0, columnspan=5)

    llist = "Enter an Adjective:", "Enter a Noun:", "Enter a Plural Noun:", "Enter a Person Name:", "Enter an Adjective:", \
            "Enter any article of Clothing:", "Enter a Noun:", "Enter a City:", "Enter a Plural Noun:", "Enter an Adjective:", \
            "Enter a Part of body:", "Enter an Alphabet:", "Enter a Celebrity:", "Enter a Plural Noun:", "Enter an Adjective:", \
            "Enter a Place:", "Enter a Part of Body:", "Enter an Adjective:", "Enter an Adjective:", "Enter a Verb:", \
            "Enter a Plural Noun:", "Enter a Number:"
    nrow = 3

    for i in range(len(llist)):
        label = Label(frame, text=llist[i], bg="#F0FFFF")
        label.grid(row=nrow, column=0, columnspan=3)

        my_entry = Entry(frame, width=40, borderwidth=5)
        my_entry.grid(row=nrow, column=3, columnspan=2)
        my_entries.append(my_entry)

        nrow += 1



    def mainbook():
        frame.grid_forget()

        submit.grid_forget()

        answer_list = [None] * len(my_entries)
        x = 0
        for entries in my_entries:
            answer_list[x] = entries.get()
            x += 1

        ans = "There are many " + str(answer_list[0]) + " ways to choose a\\an " + str(answer_list[1]) + \
              " to \nread. First, you could ask for recommendations from your friends and\n " + str(answer_list[2]) + \
              ". Just don\'t ask Aunt " + str(answer_list[3]) + " she only \nreads " + str(answer_list[4]) + \
              " books with " + str(answer_list[5]) + \
              " ripping goddess \non cover. If your friends and family are no help, try checking out the \n" + \
              str(answer_list[6]) + " Review in the " + str(answer_list[7]) + " Times. If the \n" + str(answer_list[8]) + \
              " Featured are too " + str(answer_list[9]) + " for your taste, try something a little\n more low-" + \
              str(answer_list[10]) + ", like " + str(answer_list[11]) + " : the " + str(answer_list[12]) + "\nMagazine, or " + \
              str(answer_list[13]) + " Magazine. You could also choose a book the\n" + str(answer_list[14]) + \
              "-fashioned way. Head to your local libaray or " + str(answer_list[15]) + \
              "\nand browse the shelves until something catches your " + str(answer_list[16]) + \
              ".\nOr, you could save yourself a whole lot of " + str(answer_list[17]) + \
              " trouble and log on \n to WWW.BOOKISH.COM, the " + str(answer_list[18]) + " new website to " + str(answer_list[19]) \
              + " for\n books! With all the time you\'ll save not having to search for " + str(answer_list[20]) + \
              ",\n you can read " + str(answer_list[21]) + " more books!"

        button_exit.grid(row=26, column=0, columnspan=5)
        frame2 = LabelFrame(main, bg="#F0FFFF", bd=0)
        frame2.grid(row=3, column=0, columnspan=5, rowspan=10)

        tab = Label(frame2, text=ans, bg="#F0FFFF")
        tab.grid(row=0, column=0, columnspan=5, rowspan=10)

    submit.config(command=mainbook)
    submit.grid(row=26, column=0, columnspan=5)


def dinner():

    disable()

    frame = LabelFrame(main, bg="#F0FFFF", bd=0)
    frame.grid(row=3, column=0, columnspan=5)

    llist = "Enter a Noun:", "Enter a Person\'s name:", "Enter a Verb:","Enter a Part of body:","Enter an Adjective:",\
            "Enter a Noun:","Enter a Noun:","Enter a Plural Noun:","Enter a Type of Liquid:","Enter an Adjective:",\
            "Enter a Noun:","Enter a Noun:","Enter a Noun:","Enter a Plural Noun:","Enter Name of person:",\
            "Enter a Noun:","Enter a Part of Body:",

    nrow = 3

    for i in range(len(llist)):
        label = Label(frame, text=llist[i], bg="#F0FFFF")
        label.grid(row=nrow, column=0, columnspan=3)

        my_entry = Entry(frame, width=40, borderwidth=5)
        my_entry.grid(row=nrow, column=3, columnspan=2)
        my_entries.append(my_entry)

        nrow += 1


    def mainbook():
        frame.grid_forget()

        submit.grid_forget()

        answer_list = [None] * len(my_entries)
        x = 0
        for entries in my_entries:
            answer_list[x] = entries.get()
            x += 1

        ans = "It was Thanksgiving, and the scent of succulent roast " + str(answer_list[0]) + \
              "\nwafted through my house. \"" + str(answer_list[1]) + ", it\'s time to\n" + str(answer_list[2]) + \
              "!\" my mother called. I couldn\'t wait to get my \n" + str(answer_list[3]) + \
              " on that " + str(answer_list[4]) + " Thanksgiving meal.\nMy family sat around the dining-room " + \
              str(answer_list[5]) + ". The table\n was laid out with every kind of " + str(answer_list[6]) + \
              " imaginable. There was\n a basket of hot buttered " + str(answer_list[7]) + \
              " and glasses of sparkling\n " + str(answer_list[8]) + ". The " + str(answer_list[9]) + \
              " turkey sat, steaming, \n next to a tureen of " + str(answer_list[10]) + \
              " gravy. A bowl of ruby-red\n " + str(answer_list[11]) + " sauce, a sweet-" + str(answer_list[12]) + \
              " casserole, and a dish of \n mashed " + str(answer_list[13]) + " tempted my taste buds. But the dish" \
              " i \nlooked forward to most was Grandma " +str(answer_list[14]) + "\'s\n famous " + str(answer_list[15]) + \
              " pie. Thanksgiving is my favourite holiday,\n" + str(answer_list[16]) + " down."

        frame2 = LabelFrame(main, bg="#F0FFFF", bd=0)
        frame2.grid(row=3, column=0, columnspan=5, rowspan=10)
        button_exit.grid(row=24, column=0, columnspan=5)

        tab = Label(frame2, text=ans, bg="#F0FFFF")
        tab.grid(row=0, column=0, columnspan=5, rowspan=10)

    submit.config(command=mainbook)
    submit.grid(row=24, column=0, columnspan=5)


def november():
    disable()

    frame = LabelFrame(main, bg="#F0FFFF", bd=0)
    frame.grid(row=3, column=0, columnspan=5)

    llist = "Enter an Adjective:", "Enter an Adjective:", "Enter type of Bird:", "Enter Room in House:", \
            "Enter a Verb(paste tense):", "Enter a Verb:", "Enter a Name:", "Enter a Noun:", "Enter any Liquid:", \
            "Enter a Verb(ending -ing):", "Enter any Parts of Body:", "Enter a Plural Noun:", \
            "Enter a Verb(ending -ing):", "Enter a Noun:",

    nrow = 3

    for i in range(len(llist)):
        label = Label(frame, text=llist[i], bg="#F0FFFF")
        label.grid(row=nrow, column=0, columnspan=3)

        my_entry = Entry(frame, width=40, borderwidth=5)
        my_entry.grid(row=nrow, column=3, columnspan=2)
        my_entries.append(my_entry)

        nrow += 1

    def mainbook():
        frame.grid_forget()

        submit.grid_forget()

        answer_list = [None] * len(my_entries)
        x = 0
        for entries in my_entries:
            answer_list[x] = entries.get()
            x += 1

        ans = "It was a " + str(answer_list[0]) + ", cold November day. I\nwoke up to the " + str(answer_list[1]) \
              + " smell of " + str(answer_list[2]) + "\n roasting in the " + str(answer_list[3]) + \
              " downstairs. I\n" + str(answer_list[4]) + " down the stairs to see if i could\n help " + \
              str(answer_list[5]) + " the dinner. My mom said,\n\"See if " + str(answer_list[6]) + " needs a fresh " + \
              str(answer_list[7]) + ".\" So i\n carried a tray of glasses full of " + str(answer_list[8]) + \
              " into\n the " + str(answer_list[9]) + " room. When i got there, i\n couldn\'t believe my " + \
              str(answer_list[10]) + "! There were\n " + str(answer_list[11]) + " " + str(answer_list[12]) +\
              " on the " + str(answer_list[13]) + "!"

        button_exit.grid(row=24, column=0, columnspan=5)
        button_exit.bind("<Enter>", button_exit_hover)
        button_exit.bind("<Leave>", button_exit_hover_leave)

        frame2 = LabelFrame(main, bg="#F0FFFF", bd=0)
        frame2.grid(row=3, column=0, columnspan=5, rowspan=10)

        tab = Label(frame2, text=ans, bg="#F0FFFF")
        tab.grid(row=0, column=0, columnspan=5, rowspan=10)

    submit.config(command=mainbook)
    submit.grid(row=24, column=0, columnspan=5)
    submit.bind("<Enter>", button_submit_hover)
    submit.bind("<Leave>", button_submit_hover_leave)


def pizza():
    disable()

    frame = LabelFrame(main, bg="#F0FFFF", bd=0)
    frame.grid(row=3, column=0, columnspan=5)

    llist = "Enter an Adjective:", "Enter a Nationality:", "Enter a Person Name:", \
            "Enter a Noun::", "Enter an Adjective:", "Enter a Noun:", "Enter an Adjective:", "Enter an Adjective:", \
            "Enter a Plural Noun:", "Enter a Noun:", "Enter a Number:", "Enter a Shape:", "Enter a Food:", "Enter a Food:", \
            "Enter a Number:"
    nrow = 3

    for i in range(len(llist)):
        label = Label(frame, text=llist[i], bg="#F0FFFF")
        label.grid(row=nrow, column=0, columnspan=3)

        my_entry = Entry(frame, width=40, borderwidth=5)
        my_entry.grid(row=nrow, column=3, columnspan=2)
        my_entries.append(my_entry)

        nrow += 1

    def mainbook():
        frame.grid_forget()

        submit.grid_forget()

        answer_list = [None] * len(my_entries)
        x = 0
        for entries in my_entries:
            answer_list[x] = entries.get()
            x += 1

        ans = "Pizza was invented by a " + str(answer_list[0]) + " " + str(answer_list[1]) + "\n chef named " \
              + str(answer_list[2]) + ".  To make a pizza, you need\n to take a lump of " + str(answer_list[3]) \
              + ", and make a thin, round\n" + str(answer_list[4]) + " " + str(
            answer_list[5]) + ". Then you cover it with\n" \
              + str(answer_list[6]) + " sauce, " + str(answer_list[7]) + " cheese, and fresh\n chopped " + str(
            answer_list[8]) \
              + ". Next you have to bake it in a very\n hot " + str(answer_list[9]) + ". When it is done, cut it into " \
              + str(answer_list[10]) + "\n" + str(answer_list[11]) + ". Some kids like " + str(answer_list[12]) \
              + " pizza the\n best, but my favorite is the " + str(answer_list[13]) + \
              " pizza. If i could, i\n would eat pizza " + str(answer_list[14]) + " times a day!"

        button_exit.grid(row=24, column=0, columnspan=5)

        frame2 = LabelFrame(main, bg="#F0FFFF", bd=0)
        frame2.grid(row=3, column=0, columnspan=5, rowspan=10)

        tab = Label(frame2, text=ans, bg="#F0FFFF")
        tab.grid(row=0, column=0, columnspan=5, rowspan=10)

    submit.config(command=mainbook)
    submit.grid(row=24, column=0, columnspan=5)


def vacation():
    disable()
    frame = LabelFrame(main, bg="#F0FFFF", bd=0)
    frame.grid(row=3, column=0, columnspan=5)

    llist = "Enter an Adjective:", "Enter an Adjective:", "Enter a Noun:", "Enter a Noun::", "Enter a Plural Noun:", \
            "Enter any Game:", "Enter a Plural Noun:", "Enter a Verb(ending -ing):", "Enter a Verb(ending -ing):", \
            "Enter a Plural Noun:", "Enter a Verb(ending -ing):", "Enter a Noun:", "Enter a Plant:", \
            "Enter a Part of Body:", "Enter a Place:", "Enter a Verb(ending -ing):", "Enter an Adjective:", \
            "Enter a Number:", "Enter a Plural Noun:"

    nrow = 3

    for i in range(len(llist)):
        label = Label(frame, text=llist[i], bg="#F0FFFF")
        label.grid(row=nrow, column=0, columnspan=3)

        my_entry = Entry(frame, width=40, borderwidth=5)
        my_entry.grid(row=nrow, column=3, columnspan=2)
        my_entries.append(my_entry)

        nrow += 1

    def mainbook():

        frame.grid_forget()
        submit.grid_forget()
        answer_list = [None] * len(my_entries)
        x = 0
        for entries in my_entries:
            answer_list[x] = entries.get()
            x += 1

        ans = "A vacation is when you take a tip to some " + str(answer_list[0]) + " place\n with your " \
              + str(answer_list[1]) + " family. Usually you go to some place\n that is near a/an " + \
              str(answer_list[2]) \
              + " or up on a/an " + str(answer_list[3]) + ".\n A good vacation place is one where you can rise " \
              + str(answer_list[4]) + "\n or play " + str(answer_list[5]) + " or go hunting for " + \
              str(answer_list[6]) \
              + ". I like\n to spend my time " + str(answer_list[7]) + " or " + str(answer_list[8]) \
              + ".\n When parents go on a vacation, they spend their time eating\n three " + str(answer_list[9]) \
              + " a day, and fathers play golf, and mothers\n sit around " + str(answer_list[10]) \
              + ". Last summer, my little brother\n fell in a/an " + str(answer_list[11]) + " and got poison " \
              + str(answer_list[12]) + " all\n over his " + str(answer_list[13]) + \
              ". my family is going to go to (the)\n" \
              + str(answer_list[14]) + ", and i will practice " + str(answer_list[15]) \
              + ". Parents\n need vacations more than kids because parents are always very\n " + str(answer_list[16]) \
              + " and because they have to work " + str(answer_list[17]) + \
              "\n hours every day all year making enough " + str(answer_list[18]) + " to pay\n for the vacation."

        frame2 = LabelFrame(main, bg="#F0FFFF", bd=0)
        frame2.grid(row=3, column=0, columnspan=5, rowspan=10)

        tab = Label(frame2, text=ans, bg="#F0FFFF")
        tab.grid(row=0, column=0, columnspan=5, rowspan=10)
        button_exit.grid(row=24, column=0, columnspan=5)

    submit.config(command=mainbook)
    submit.grid(row=24, column=0, columnspan=5)


main.title("MAdLiBs!!!")
main.iconbitmap('logomad.ico')
main.configure(bg="#F0FFFF")

title = Label(main, text="Mad Libs", bg="#F0FFFF").grid(row=0, column=0, columnspan=10)
select = Label(main, text="  select your theme!!  ", bg="#F0FFFF").grid(row=1, column=0, columnspan=10)

button1 = Button(main, text="Bookish", width=16, command=bookish, bg="#F0FFFF", bd=0)
button1.grid(row=2, column=0)
button1.bind("<Enter>", button_hover)
button1.bind("<Leave>", button_hover_leave)

button2 = Button(main, text="What\'s for dinner?", width=16, command=dinner, bg="#F0FFFF", bd=0)
button2.grid(row=2, column=1)
button2.bind("<Enter>", button_hover1)
button2.bind("<Leave>", button_hover1_leave)

button3 = Button(main, text="november morning", width=16, command=november, bg="#F0FFFF", bd=0)
button3.grid(row=2, column=2)
button3.bind("<Enter>", button_hover2)
button3.bind("<Leave>", button_hover2_leave)

button4 = Button(main, text="Pizza!!!", width=16, command=pizza, bg="#F0FFFF", bd=0)
button4.grid(row=2, column=3)
button4.bind("<Enter>", button_hover3)
button4.bind("<Leave>", button_hover3_leave)

button5 = Button(main, text="vacation!!", width=16, command=vacation, bg="#F0FFFF", bd=0)
button5.grid(row=2, column=4)
button5.bind("<Enter>", button_hover4)
button5.bind("<Leave>", button_hover4_leave)

button_exit = Button(main, text="Exit Program", command=main.quit, bg="#F0FFFF")
button_exit.bind("<Enter>", button_exit_hover)
button_exit.bind("<Leave>", button_exit_hover_leave)

submit = Button(main, bg="#F0FFFF", text="SUBMIT")
submit.bind("<Enter>", button_submit_hover)
submit.bind("<Leave>", button_submit_hover_leave)

main.mainloop()
