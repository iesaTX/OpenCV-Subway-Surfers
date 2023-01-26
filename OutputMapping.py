# Check if the person has jumped.

if posture == 'Jumping' and y_pos_index == 1:

    # Press the up arrow key

    pyautogui.press('up')

    # Update the veritcal position index of  the character.

    y_pos_index += 1



# Check if the person has crouched.

elif posture == 'Crouching' and y_pos_index == 1:

    # Press the down arrow key

    pyautogui.press('down')