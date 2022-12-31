import pyautogui as events
import time
import ftfy as text_corrector
import keyboard

### Config ###
isEnglish = True  # If it is not English that means it is German
seperator = " - "
card_file_name = "english_file.txt" if isEnglish else "german_file.txt"
card_file = open(card_file_name, "r")
word_array = []
word_part_range = 2  # how many seperator are there? if x, you should write x + 1 here
# At least 1. If computer can't catch bot's speed, try to increase this.
delay = 1

## Find Meaning Config ##
custom_word_file_px = [1061, 123]
first_word_px = [1262, 96]
chatGPT_chat_px = [823, 825]
chatGPT_answer_px = [775, 836]
current_word_px = [1262, 110]

## Deck Config ##
front_field_px = [893, 154]
back_field_px = [867, 226]
add_field_px = [671, 1054]
set_color_px = [285, 87]
choose_color_px = [269, 87]
color_red_px = [242, 638]
color_green_px = [269, 638]
color_blue_px = [301, 638]
color_ok_button_px = [611, 730]


time.sleep(3)
print(events.position())
time.sleep(10)

### Word Array Preparing ###
for card in card_file:
    splitted_array = card.split(seperator)
    if isEnglish:
        last_one_corrected_splitted_array = [
            text_corrector.fix_text(splitted_array[0]), text_corrector.fix_text(splitted_array[1].rsplit("\n")[0])]
    else:
        last_one_corrected_splitted_array = [
            text_corrector.fix_text(splitted_array[0]),
            text_corrector.fix_text(splitted_array[1]),
            text_corrector.fix_text(splitted_array[2].rsplit("\n")[0])]
    word_array.append(last_one_corrected_splitted_array)

# To check word_array
# print(word_array)
# time.sleep(5)

### Deck Writer Bot ###

## Functions ##

# Common Functions #

# def findingMeaning(word):


def setFrontWord(word, isGermanNoun):
    events.click(front_field_px[0], front_field_px[1])
    keyboard.write(word)
    if isEnglish == False and isGermanNoun:
        setWordColor()


def writeMeaning(word):
    events.click(back_field_px[0], back_field_px[1])
    keyboard.write('{}, '.format(word))

# German Spesific Functions #


def setWordColor():
    events.hotkey('ctrl', 'a')
    events.click(choose_color_px[0], choose_color_px[1])


def setCurrentColor(type):
    events.click(set_color_px[0], set_color_px[1])
    time.sleep(1)
    if type == 'der ':
        events.click(color_blue_px[0], color_blue_px[1])
    if type == 'das ':
        events.click(color_green_px[0], color_green_px[1])
    if type == 'die ':
        events.click(color_red_px[0], color_red_px[1])
    time.sleep(1)
    events.click(color_ok_button_px[0], color_ok_button_px[1])


for word in word_array:
    for index in range(word_part_range):
        current_word = word[index]
        isGermanNoun = isEnglish == False and (
            'der ' == current_word[:4] or 'die ' == current_word[:4] or 'das ' == current_word[:4])
        if index == 0:
            if isGermanNoun:
                setCurrentColor(current_word[:4])
            setFrontWord(current_word, isGermanNoun)
            time.sleep(1)
            continue
        writeMeaning(current_word)
        time.sleep(1)
    events.click(add_field_px[0], add_field_px[1])


# events.click(color_field_px[0], color_field_px[1])
# events.write(deck_name)
# events.click(ok_button_px[0], ok_button_px[1])
