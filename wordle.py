#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys

# ANSI escape codes for colors
GREEN = '\033[32m'  # Changed from 92m to 32m for better compatibility
YELLOW = '\033[33m'  # Changed from 93m to 33m for better compatibility
RED = '\033[31m'    # Changed from 91m to 31m for better compatibility
RESET = '\033[0m'

WORD_CLUES = {
    'about': 'Concerning a subject',
    'above': 'Higher than something',
    'abuse': 'Misuse or mistreat',
    'actor': 'Performs in plays',
    'acute': 'Sharp or severe',
    'admit': 'Accept as true',
    'adopt': 'Take as own',
    'adult': 'Grown up person',
    'after': 'Following in time',
    'again': 'One more time',
    'agent': 'Acts for another',
    'agree': 'Share same opinion',
    'ahead': 'In the front',
    'alarm': 'Warning of danger',
    'alert': 'Watchful and ready',
    'alike': 'Similar to another',
    'alive': 'Living not dead',
    'allow': 'Permit to happen',
    'alone': 'By oneself only',
    'along': 'Moving forward beside',
    'ALTER': 'Change or modify',
    'AMONG': 'Surrounded by others',
    'ANGER': 'Strong displeasure feeling',
    'ANGLE': 'Point where lines meet',
    'ANGRY': 'Feeling strong displeasure',
    'APART': 'Separated from others',
    'APPLE': 'Round sweet fruit',
    'APPLY': 'Put into action',
    'ARENA': 'Place of contest',
    'ARGUE': 'Dispute with others',
    'ARISE': 'Get up, emerge',
    'ARRAY': 'Ordered series arrangement',
    'ASIDE': 'To the side',
    'ASSET': 'Valuable thing owned',
    'AUDIO': 'Related to sound',
    'AUDIT': 'Official financial examination',
    'AVOID': 'Stay away from',
    'AWARD': 'Prize or honor',
    'AWARE': 'Having knowledge of',
    'BASIC': 'Simple and fundamental',
    'BEACH': 'Sandy ocean shore',
    'BEGIN': 'Start something new',
    'BELOW': 'Lower than something',
    'BENCH': 'Long sitting seat',
    'BIRTH': 'Beginning of life',
    'BLACK': 'Darkest color possible',
    'BLAME': 'Assign fault to',
    'BLIND': 'Unable to see',
    'BLOCK': 'Solid rectangular piece',
    'BLOOD': 'Red body fluid',
    'BOARD': 'Flat wooden surface',
    'BOOST': 'Increase or enhance',
    'BOOTH': 'Small enclosed space',
    'BOUND': 'Leap or jump',
    'BRAIN': 'Thinking organ inside',
    'BRAND': 'Product maker name',
    'BRAVE': 'Showing no fear',
    'BREAD': 'Baked wheat food',
    'BREAK': 'Separate into pieces',
    'BREED': 'Reproduce animals',
    'BRIEF': 'Short in duration',
    'BRING': 'Carry something here',
    'BROAD': 'Wide in scope',
    'BRUSH': 'Clean with bristles',
    'BUNCH': 'Group of things',
    'BURST': 'Suddenly break open',
    'BUYER': 'Person who purchases',
    'CABLE': 'Strong thick wire',
    'CARRY': 'Transport while holding',
    'CATCH': 'Grab moving object',
    'CAUSE': 'Make something happen',
    'CHAIN': 'Connected metal links',
    'CHAIR': 'Seat with back',
    'CHART': 'Information display graph',
    'CHASE': 'Run after something',
    'CHEAP': 'Low in price',
    'CHECK': 'Verify or examine',
    'CHEST': 'Upper torso part',
    'CHIEF': 'Leader in charge',
    'CHILD': 'Young human being',
    'CHINA': 'Asian country name',
    'CLAIM': 'State as true',
    'CLASS': 'Group of students',
    'CLEAN': 'Free from dirt',
    'CLEAR': 'Easy to see',
    'CLOCK': 'Time telling device',
    'CLOSE': 'Shut or near',
    'COACH': 'Sports team leader',
    'COAST': 'Land near ocean',
    'COUNT': 'Add up numbers',
    'COURT': 'Legal judgment place',
    'COVER': 'Put something over',
    'CRACK': 'Break without separating',
    'CRAFT': 'Skill in making',
    'CRASH': 'Collide with force',
    'CREAM': 'Rich dairy product',
    'CRIME': 'Against the law',
    'CROSS': 'Go across something',
    'CROWD': 'Large group gathered',
    'CROWN': 'Royal head covering',
    'CURVE': 'Bent or rounded',
    'CYCLE': 'Repeat in sequence',
    'DAILY': 'Happening every day',
    'DANCE': 'Move to music',
    'DEATH': 'End of life',
    'DELAY': 'Make happen later',
    'DEPTH': 'Distance down below',
    'DOUBT': 'Feeling of uncertainty',
    'DRAFT': 'Preliminary version',
    'DRAMA': 'Theatrical entertainment',
    'DREAM': 'Images during sleep',
    'DRESS': 'Clothing for women',
    'DRILL': 'Make holes in',
    'DRINK': 'Consume liquid beverage',
    'DRIVE': 'Control moving vehicle',
    'EAGER': 'Very enthusiastic',
    'EARLY': 'Before usual time',
    'EARTH': 'Planet we inhabit',
    'EIGHT': 'Number after seven',
    'ELITE': 'Best of group',
    'EMPTY': 'Containing nothing inside',
    'ENEMY': 'Opposed to another',
    'ENJOY': 'Find pleasure in',
    'ENTER': 'Go into place',
    'ENTRY': 'Point of going in',
    'EQUAL': 'Same as another',
    'ERROR': 'Mistake or wrong',
    'ESSAY': 'Written composition piece',
    'EVENT': 'Something that happens',
    'EXACT': 'Precisely correct',
    'EXIST': 'Have real being',
    'EXTRA': 'Additional amount more',
    'FAITH': 'Strong belief in',
    'FALSE': 'Not true',
    'FAULT': 'Mistake or flaw',
    'FIBER': 'Thread like material',
    'FIELD': 'Open grassy area',
    'FIFTH': 'Number after fourth',
    'FIGHT': 'Struggle against something',
    'FINAL': 'Last in sequence',
    'FIRST': 'Before all others',
    'FIXED': 'Firmly in place',
    'FLASH': 'Sudden bright light',
    'FLEET': 'Group of ships',
    'FLOOR': 'Bottom room surface',
    'FLUID': 'Liquid or gas',
    'FOCUS': 'Center of attention',
    'FORCE': 'Strong physical power',
    'FORTH': 'Forward in place',
    'FOUND': 'Discovered something new',
    'FRAME': 'Border around picture',
    'FRANK': 'Honest and direct',
    'FRAUD': 'Intentional deception',
    'FRESH': 'Recently made',
    'FRONT': 'Forward facing part',
    'FRUIT': 'Sweet plant food',
    'FULLY': 'Completely and entirely',
    'FUNNY': 'Causing to laugh',
    'GIANT': 'Very large size',
    'GLASS': 'Clear solid material',
    'GLOBE': 'Sphere of earth',
    'GRADE': 'Level of quality',
    'GRAND': 'Impressive and large',
    'GRANT': 'Give permission to',
    'GRASS': 'Green lawn plant',
    'GREAT': 'Large or excellent',
    'GREEN': 'Color of grass',
    'GROSS': 'Disgusting or total',
    'GROUP': 'Collection of things',
    'GUARD': 'Watch and protect',
    'GUESS': 'Try to answer',
    'GUEST': 'Visitor in place',
    'GUIDE': 'Show the way',
    'HAPPY': 'Feeling joy',
    'HEART': 'Blood pumping organ',
    'HEAVY': 'Great in weight',
    'HENCE': 'For this reason',
    'HORSE': 'Large riding animal',
    'HOTEL': 'Temporary sleeping place',
    'HOUSE': 'Living dwelling place',
    'HUMAN': 'Person not animal',
    'IDEAL': 'Perfect example of',
    'IMAGE': 'Visual representation of',
    'INDEX': 'Alphabetical listing',
    'INNER': 'Inside part of',
    'INPUT': 'What goes in',
    'ISSUE': 'Problem or concern',
    'JOINT': 'Where things connect',
    'JUDGE': 'Decide about something',
    'KNIFE': 'Sharp cutting tool',
    'KNOWN': 'Already discovered',
    'LABEL': 'Name tag attached',
    'LARGE': 'Big in size',
    'LASER': 'Focused light beam',
    'LATER': 'After some time',
    'LAUGH': 'Show joy sound',
    'LAYER': 'Single thickness level',
    'LEARN': 'Gain new knowledge',
    'LEASE': 'Rent for time',
    'LEAST': 'Smallest in amount',
    'LEAVE': 'Go away from',
    'LEGAL': 'According to law',
    'LEVEL': 'Flat horizontal surface',
    'LIGHT': 'Opposite of dark',
    'LIMIT': 'Boundary or maximum',
    'LOCAL': 'From this area',
    'LODGE': 'Place to stay',
    'LOGIC': 'Reasonable thought process',
    'LOOSE': 'Not tight fitting',
    'LOWER': 'Move something down',
    'LUCKY': 'Having good fortune',
    'LUNCH': 'Midday meal time',
    'MAGIC': 'Mysterious supernatural power',
    'MAJOR': 'Greater in importance',
    'MAKER': 'One who creates',
    'MARCH': 'Walk in step',
    'MATCH': 'Find equal pair',
    'METAL': 'Strong solid material',
    'MINOR': 'Lesser in importance',
    'MIXED': 'Combined together',
    'MODEL': 'Example to copy',
    'MONEY': 'Medium of exchange',
    'MONTH': 'Part of year',
    'MORAL': 'Right and wrong',
    'MOTOR': 'Engine that moves',
    'MOUNT': 'Climb up something',
    'MOUSE': 'Small rodent animal',
    'MOUTH': 'Opening for eating',
    'MOVIE': 'Motion picture film',
    'MUSIC': 'Organized sound art',
    'NEEDS': 'Required things',
    'NEVER': 'Not at anytime',
    'NIGHT': 'Dark evening time',
    'NOISE': 'Unwanted sound',
    'NORTH': 'Compass direction up',
    'NOTED': 'Well known',
    'NOVEL': 'Long fiction book',
    'NURSE': 'Medical care provider',
    'OCEAN': 'Large salt water',
    'OFFER': 'Present for acceptance',
    'ORDER': 'Arranged sequence',
    'OTHER': 'Different from this',
    'OUTER': 'External part of',
    'OWNER': 'One who possesses',
    'PAINT': 'Colored coating liquid',
    'PANEL': 'Flat surface section',
    'PAPER': 'Thin writing material',
    'PARTY': 'Social gathering celebration',
    'PEACE': 'Freedom from conflict',
    'PHASE': 'Stage of development',
    'PHONE': 'Voice communication device',
    'PHOTO': 'Picture from camera',
    'PIECE': 'Part of whole',
    'PILOT': 'Aircraft controller',
    'PITCH': 'Throw ball forward',
    'PLACE': 'Location or spot',
    'PLAIN': 'Simple not fancy',
    'PLANE': 'Flying transport vehicle',
    'PLANT': 'Living growing organism',
    'PLATE': 'Flat dish surface',
    'POINT': 'Sharp end tip',
    'POUND': 'Unit of weight',
    'POWER': 'Ability to act',
    'PRESS': 'Push with force',
    'PRICE': 'Cost in money',
    'PRIDE': 'Self respect feeling',
    'PRIME': 'First in importance',
    'PRINT': 'Make paper copy',
    'PRIOR': 'Coming before',
    'PRIZE': 'Reward for winning',
    'PROOF': 'Evidence of truth',
    'PROUD': 'Feeling self respect',
    'PROVE': 'Show to be true',
    'QUEEN': 'Female royal ruler',
    'QUICK': 'Fast in motion',
    'QUIET': 'Free from noise',
    'QUITE': 'Very or completely',
    'RADIO': 'Sound broadcast device',
    'RAISE': 'Lift up higher',
    'RANGE': 'Extent or scope',
    'RAPID': 'Very fast moving',
    'RATIO': 'Numerical relationship',
    'REACH': 'Extend to touch',
    'READY': 'Prepared for use',
    'REFER': 'Direct attention to',
    'RIGHT': 'Correct or proper',
    'RIVAL': 'Competing opponent',
    'RIVER': 'Flowing water stream',
    'ROBOT': 'Mechanical person',
    'ROUGH': 'Not smooth surface',
    'ROUND': 'Circular in shape',
    'ROUTE': 'Way to destination',
    'ROYAL': 'Related to king',
    'RURAL': 'Country not city',
    'SCALE': 'Size or proportion',
    'SCENE': 'Place of action',
    'SCOPE': 'Range of view',
    'SCORE': 'Number of points',
    'SENSE': 'Faculty of perception',
    'SERVE': 'Help or assist',
    'SEVEN': 'Number after six',
    'SHADE': 'Away from light',
    'SHAKE': 'Move back forth',
    'SHALL': 'Will do something',
    'SHAPE': 'Form or figure',
    'SHARE': 'Give part to',
    'SHARP': 'Having fine edge',
    'SHEET': 'Flat thin material',
    'SHELF': 'Flat storage surface',
    'SHELL': 'Hard outer covering',
    'SHIFT': 'Change position of',
    'SHIRT': 'Upper body garment',
    'SHOCK': 'Sudden disturbing effect',
    'SHOOT': 'Fire or launch',
    'SHORT': 'Not very long',
    'SHOWN': 'Displayed or exhibited',
    'SIGHT': 'Ability to see',
    'SINCE': 'From time past',
    'SIXTH': 'Number after fifth',
    'SKILL': 'Ability to do',
    'SLEEP': 'Rest with eyes closed',
    'SLIDE': 'Glide smoothly along',
    'SMALL': 'Not large size',
    'SMART': 'Intelligent or clever',
    'SMILE': 'Happy facial expression',
    'SMOKE': 'Grey gas from fire',
    'SOLID': 'Firm not liquid',
    'SOLVE': 'Find answer to',
    'SOUND': 'What we hear',
    'SOUTH': 'Opposite of north',
    'SPACE': 'Empty area between',
    'SPARE': 'Extra or additional',
    'SPEAK': 'Say words aloud',
    'SPEED': 'Rate of motion',
    'SPEND': 'Use up money',
    'SPLIT': 'Divide into parts',
    'SPORT': 'Athletic competition game',
    'STAFF': 'Group of workers',
    'STAGE': 'Platform for performance',
    'STAKE': 'Risk in venture',
    'STAND': 'Be upright position',
    'START': 'Begin doing something',
    'STATE': 'Condition or nation',
    'STEAM': 'Hot water vapor',
    'STEEL': 'Strong metal alloy',
    'STICK': 'Long thin piece',
    'STILL': 'Not moving yet',
    'STOCK': 'Available supply goods',
    'STONE': 'Hard rock material',
    'STORE': 'Shop selling goods',
    'STORM': 'Bad weather event',
    'STORY': 'Tale or account',
    'STRIP': 'Long narrow piece',
    'STUDY': 'Learn about subject',
    'STYLE': 'Manner of doing',
    'SUGAR': 'Sweet white crystal',
    'SUITE': 'Set of rooms',
    'SUPER': 'Excellent or superior',
    'SWEET': 'Tasting like sugar',
    'TABLE': 'Flat surface furniture',
    'TAKEN': 'Picked up something',
    'TASTE': 'Flavor in mouth',
    'TAXES': 'Government money requirement',
    'TEACH': 'Help others learn',
    'THEME': 'Main subject idea',
    'THERE': 'In that place',
    'THESE': 'Plural of this',
    'THICK': 'Not thin measurement',
    'THING': 'Object or item',
    'THINK': 'Use your mind',
    'THIRD': 'After second number',
    'THOSE': 'Plural of that',
    'THREE': 'Number after two',
    'THROW': 'Propel through air',
    'THUMB': 'First finger digit',
    'TIGHT': 'Firmly fastened',
    'TITLE': 'Name of something',
    'TODAY': 'This present day',
    'TOPIC': 'Subject under discussion',
    'TOTAL': 'Complete sum amount',
    'TOUCH': 'Make contact with',
    'TOUGH': 'Strong and durable',
    'TOWER': 'Tall building structure',
    'TRACK': 'Path to follow',
    'TRADE': 'Exchange for value',
    'TRAIN': 'Connected railway cars',
    'TREAT': 'Something special given',
    'TREND': 'Current popular style',
    'TRIAL': 'Test of something',
    'TRIED': 'Attempted to do',
    'TRIES': 'Makes an attempt',
    'TRUCK': 'Large road vehicle',
    'TRULY': 'Really and sincerely',
    'TRUST': 'Have confidence in',
    'TRUTH': 'What is real',
    'UNITY': 'State of oneness',
    'world': 'Earth and inhabitants',
    'wound': 'Injury to body',
    'write': 'Make marks communicate',
    'wrong': 'Not correct thing',
    'yield': 'Give way to',
    'young': 'Early in life',
    'youth': 'Time of being young'
    }

class WordleGame(object):
    def __init__(self):
        # Convert all dictionary keys to lowercase during initialization
        self.words = [word.lower() for word in WORD_CLUES.keys()]
        self.clues = {k.lower(): v for k, v in WORD_CLUES.items()}
        self.max_attempts = 6

    def get_guess_feedback(self, guess, target):
        """Compare guess with target word and return color-coded feedback."""
        if len(guess) != len(target):
            return None

        result = []
        guess = guess.lower()
        target = target.lower()

        # Convert strings to lists for letter counting
        target_letters = list(target)
        guess_letters = list(guess)

        # First pass: mark correct letters
        for i in range(len(guess)):
            if guess[i] == target[i]:
                result.append(f"{GREEN}{guess[i]}{RESET}")
                target_letters[i] = '*'
                guess_letters[i] = '*'
            else:
                result.append(guess[i])

        # Second pass: mark misplaced letters
        for i in range(len(guess)):
            if result[i] == guess[i] and guess_letters[i] in target_letters:
                result[i] = f"{YELLOW}{guess[i]}{RESET}"
                target_letters[target_letters.index(guess_letters[i])] = '*'

        return ''.join(result)

    def get_input(self, prompt):
        """Get input in a way that works in both Python 2 and 3."""
        if sys.version_info[0] >= 3:
            return input(prompt)
        return raw_input(prompt)

    def play(self):
        """Main game loop."""
        print("\nWelcome to Offline Wordle!")
        print("Try to guess the 5-letter word. You have 6 attempts.")
        print(f"{GREEN}Green{RESET} letters are in the correct position.")
        print(f"{YELLOW}Yellow{RESET} letters are in the word but wrong position.")
        print("Good luck!\n")

        target_word = random.choice(self.words).lower()
        clue = self.clues[target_word]
        attempts = []

        print("CLUE: %s" % clue)

        while len(attempts) < self.max_attempts:
            guess = self.get_input("\nEnter guess #%d: " % (len(attempts) + 1)).lower()

            if len(guess) != 5:
                print("Please enter a 5-letter word!")
                continue

            if not guess.isalpha():
                print("Please use letters only!")
                continue

            feedback = self.get_guess_feedback(guess, target_word)
            attempts.append((guess, feedback))

            # Display all attempts
            print("\nYour guesses:")
            for i, (g, f) in enumerate(attempts, 1):
                print("%d. %s" % (i, f))

            if guess == target_word:
                print(f"\n{GREEN}Congratulations! You won in {len(attempts)} attempts!{RESET}")
                return True

        print(f"\n{RED}Game Over!{RESET} The word was: {GREEN}{target_word}{RESET}")
        return False

    def play_again(self):
        """Ask if player wants to play another game."""
        response = self.get_input("\nWould you like to play again? (y/n): ").lower()
        return response.startswith('y')

def main():
    game = WordleGame()
    while True:
        game.play()
        if not game.play_again():
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
