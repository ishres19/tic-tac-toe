from tkinter import *
from tkinter import messagebox

def click_button(button):
    """ writes 'x' or 'o' in the boxes"""
    global clicked, num_clicks
    if button["text"] == " " and clicked == True: 
        button["text"] = 'X'						#writes x on the button if the player has clicked on it
        clicked = False								#changes clicked to false. so that the next turn will be of O
        num_clicks = num_clicks + 1						#counts the number of times the button is clicked
        check_win()									#calls the check_win() function to see if anyone has won yet

    if button["text"] == " " and clicked == False:  
        button["text"] = "O"						#writes o on the button if the clicked is false. 
        clicked = True								#changes click to true. So that the next turn will be of X
        num_clicks = num_clicks + 1 
        check_win()									#calls the check_win() function to see if anyone has won yet

def disable_all_buttons():
    """ disables all the buttons """
    all_buttons = [B1, B2, B3, B4, B5, B6, B7, B8, B9]
    for button in all_buttons: 			
        button.config(state = DISABLED)				#disables all the buttons

def check_win():
    """ checks the winner of the game or checks if the game is a tie"""
    global win
    win = False
    winning_combinations = [[B1, B2, B3], [B1, B4, B7], [B2, B5, B8], [B3, B6, B9],    
         [B4, B5, B6], [B7, B8, B9], [B1, B5, B9], [B3, B5, B7] ]			#the combinations a player a needs to win

    for triples in winning_combinations:   													#goes through each list inside the winning_combination list 
        if triples[0]['text'] == 'X' and triples[1]['text'] == 'X' and triples[2]['text'] == 'X':   #checks the elements of the nested list.
            win = True                    													#if all the elements of the nested list are X then win is declared true
# 		    print (win)
            for button in triples:	
                button.config(bg = "light sky blue")											#changes the color of the winning row/column/diagonal buttons.
            messagebox.showinfo("Tic Tac Toe", "Congratulations X won!")					#gives a message showing who won
            disable_all_buttons()															#the buttons are disabled 
        elif triples[0]['text'] == 'O' and triples[1]['text'] == 'O' and triples[2]['text'] == 'O':		 #checks the elements of the nested list.	
            win = True																					#if all the elements of the nested list are X then win is declared true
            for button in triples:
                button.config(bg = "pink")																#changes the color of the winning row/column/diagonal buttons.
            messagebox.showinfo("Tic Tac Toe", "Congratulations O won!")								#gives a message showing who won
            disable_all_buttons()																		#the buttons are disabled 	

    if win == False and num_clicks == 9:														# checks if the count is 9 and win is still false. 
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!")									#shows a message saying its a tie
        disable_all_buttons()																#the buttons are disabled

def how_to_play():
    """ adds a how to play message """
    messagebox.showinfo("Tic Tac Toe","The first player to click the box will be an X and the second player will be an O. The player who succeeds in placing three of their marks in a diagonal, horizontal or vertical will win the game")

def close_game():
    """ exits from the game"""
    root.destroy ()				#destroys the root. exits the game

def menu_bar():
    """ adds menu bar """
    my_menu = Menu(root)				#initializes a menu
    root.config(menu = my_menu) 
    
    options_menu = Menu(my_menu, tearoff = 0, activebackground= 'steel blue')		#adds an Option button in the menu bar, the cascade menu will turn steel blue if the cursor touches it
    my_menu.add_cascade(label = "Options", menu = options_menu, command = reset_or_create_buttons)  # creates a hierarchical menu, making option_menu the parent menu
    options_menu.add_command(label = "Restart", command = reset_or_create_buttons)		#adds a menu item to the option_menu and calls the reset or create function 
    options_menu.add_separator()														#adds a separator between restart and exit menu item
    options_menu.add_command(label = "Exit", command = close_game)						#adds Exit to the Options menu

    help_menu = Menu(my_menu, tearoff = 0, activebackground= 'steel blue')     #adds help button in the menu bar
    my_menu.add_cascade(label = "Help", menu = help_menu)
    help_menu.add_command(label = "how to play", command = how_to_play)


def reset_or_create_buttons(): 
    """ creates or resets the the buttons"""
    global B1, B2, B3, B4, B5, B6, B7, B8, B9    #so that every time this function is called it a fresh button, so that it can be used to reset the board. Global because it needs to be used outside of this function
    global clicked, num_clicks
    clicked = True
    num_clicks = 0   
    #creating 9 buttons, for the 9 boxes of the tic_tac_toe board, each button calls the click_button function.
    
    B1 = Button(root, text = " ", bg = 'lavender blush', activebackground = 'lavender',  
        font = ("Times", 20, 'bold'), height = 5, width = 9, command = lambda: click_button(B1))
    B1.grid(row =0, column = 0)

    B2 = Button(root, text = " ", bg = 'lavender blush', activebackground = 'lavender', 
        font = ("Times", 20, 'bold'), height = 5, width = 9, command = lambda: click_button(B2))
    B2.grid(row =0, column = 1)

    B3 = Button(root, text = " ", bg = 'lavender blush', activebackground = 'lavender', 
        font = ("Times", 20, 'bold'), height = 5, width = 9, command = lambda: click_button(B3))
    B3.grid(row =0, column = 2)

    B4 = Button(root, text = " ", bg = 'lavender blush', activebackground = 'lavender', 
        font = ("Times", 20, 'bold'), height = 5, width = 9, command = lambda: click_button(B4))
    B4.grid(row =1, column = 0)

    B5 = Button(root, text = " ", bg = 'lavender blush', activebackground = 'lavender', 
        font = ("Times", 20, 'bold'), height = 5, width = 9, command = lambda: click_button(B5))
    B5.grid(row =1, column = 1)

    B6 = Button(root, text = " ", bg = 'lavender blush', activebackground = 'lavender', 
        font = ("Times", 20, 'bold'), height = 5, width = 9, command = lambda: click_button(B6))
    B6.grid(row =1, column = 2)

    B7 = Button(root, text = " ", bg = 'lavender blush', activebackground = 'lavender', 
        font = ("Times", 20, 'bold'), height = 5, width = 9, command = lambda: click_button(B7))
    B7.grid(row =2, column = 0)

    B8 = Button(root, text = " ", bg = 'lavender blush', activebackground = 'lavender', 
        font = ("Times", 20, 'bold'), height = 5, width = 9, command = lambda: click_button(B8))
    B8.grid(row =2, column = 1)

    B9 = Button(root, text = " ", bg = 'lavender blush', activebackground = 'lavender', 
        font = ("Times", 20, 'bold'), height = 5, width = 9, command = lambda: click_button(B9))
    B9.grid(row =2, column = 2)
	
	
if __name__ == '__main__':
    root = Tk()
    root.title('Tic-Tac-Toe')
    reset_or_create_buttons()
    menu_bar()
root.mainloop()
