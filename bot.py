# This code is an API for telegram bot of YAMG
# written by: Michael Getu
# Written due: 18/04/2022

# Import Statement
import Constants as keys
from telegram.ext import *
from telegram import update
import Responses as R
import json
import requests
import telegram
import os

PORT = int(os.environ.get('PORT', 5000))

# Global Variables
TOKEN = keys.API_KEY
user_id = -722317705
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
FNAME, LNAME, AGE, PHONE, EMAIL, ADDRESS, CORRECT = 0, 1, 2, 3, 4, 5, 6
first_name = ''
last_name = ' '
uage = 0
uphone = ' '
uemail = ' '
uaddress = ' '
ans = ' '

bot = telegram.Bot(TOKEN)

print("Bot started...")


# Handle for start command
def start_command(update, context):
    update.message.reply_text \
        ("""Hello, I'm YAMG your assist.
        How may I assist you?
        /about - For information about YAMG
        /upcoming - For Upcoming Events
        /register - For registering to YAMG
        /contact - For Contact us
        /help - For help or to view this message""")


# Handle for about command
def about_command(update, context):
    update.message.reply_text(
        'YAMG is a non-profitable organization that works on the mindset and actions of the youth for a better future.\n'
        'It believes that educating youth about issues such as equality, climate change, entrepreneurship, gender empowerment, and leadership will result in a better culture, society, and planet.\n'
        '\nYouth shaping is shaping the future.\n'
        '\nFor More information visit: yamgweb.com')


# Handle for upcoming command
def upcoming_command(update, context):
    update.message.reply_text('There are no recent upcoming events.\n'
                              'You can register and be Notified when there is something.')


def intro(update, context: CallbackContext) -> int:
    update.message.reply_text("""We're glad that you've  decided to join us as a member.
    Please fill the below form""")
    update.message.reply_text('Enter First Name:')

    return FNAME


def fname(update, context: CallbackContext) -> int:
    global first_name
    first_name = update.message.text
    update.message.reply_text('Enter Last Name:')

    return LNAME


def lname(update, context: CallbackContext) -> int:
    global last_name
    last_name = update.message.text
    update.message.reply_text(f'Enter age:')

    return AGE


def age(update, context: CallbackContext) -> int:
    global uage
    uage = int(update.message.text)

    if 0 < uage < 100:
        update.message.reply_text(f'Enter phone number:')

        return PHONE

    else:
        update.message.reply_text('Incorrect Input\n'
                                  'Enter Age:')

        return AGE


def phone(update, context: CallbackContext) -> int:
    global uphone
    uphone = update.message.text
    if len(uphone) >= 10:
        update.message.reply_text(f'Enter E-mail :')

        return EMAIL

    else:
        update.message.reply_text('Incorrect Input\n'
                                  'Enter Phone number (Must be at least 10 digit):')

        return PHONE


def email(update, context: CallbackContext) -> int:
    global uemail
    uemail = update.message.text
    if uemail.find('@') != -1:
        update.message.reply_text(f'Enter Address Example: Betel, Addis Ababa:')

        return ADDRESS

    else:
        update.message.reply_text('Incorrect Input\n'
                                  'Enter Email:')

        return EMAIL


def address(update, context: CallbackContext) -> int:
    global uaddress
    uaddress = update.message.text
    if uaddress.find(',') != -1:
        update.message.reply_text('Check if everything is correct')
        update.message.reply_text(f'Full Name: {first_name} {last_name}\n'
                                  f'Age: {uage}\n'
                                  f'Phone number: {uphone}\n'
                                  f'E-mail: {uemail}\n'
                                  f'Address:{uaddress}')
        update.message.reply_text('Is everything correct (Yes/No): ')

        return CORRECT

    else:
        update.message.reply_text('Incorrect Input')
        update.message.reply_text(f'Enter Address Example: Betel, Addis Ababa:')

        return ADDRESS


def correct(update, context: CallbackContext) -> int:
    global ans
    ans = str(update.message.text)
    temp = ans.lower()
    if temp.find('yes') != -1 or temp.find('y') != -1:
        message = f'Full Name: {first_name} {last_name}\n'\
                  f'Age: {uage}\n'\
                  f'Phone number: {uphone}\n'\
                  f'E-mail: {uemail}\n'\
                  f'Address:{uaddress}'
        method = 'sendMessage'
        requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(TOKEN, method),
            data={'chat_id': user_id, 'text': message}).json()
        update.message.reply_text("CONGRATULATIONS!!\n"
                                  "You've Registered successfully. We will contact you soon here or via E-mail")
        update.message.reply_text \
            ("""Hello, I'm YAMG your assist.
                How may I assist you?
                /about - For information about YAMG
                /upcoming - For Upcoming Events
                /register - For registering to YAMG
                /contact - For Contact us
                /help - For help or to view this message""")

        return ConversationHandler.END
    elif temp.find('no') != -1 or temp.find('n') != -1:
        update.message.reply_text('Fill in the correct answer again')

        return FNAME
    else:
        update.message.reply_text('INVALID INPUT')
        update.message.reply_text(f'Full Name: {first_name} {last_name}\n'
                                  f'Age: {uage}\n'
                                  f'Phone number: {uphone}\n'
                                  f'E-mail: {uemail}\n'
                                  f'Address:{uaddress}')
        update.message.reply_text('Is everything correct (Reply with yes or no): ')

        return CORRECT


def quit(update, context: CallbackContext):
    update.message.reply_text('INVALID INPUT')
    update.message.reply_text \
        ("""Hello, I'm YAMG your assist.
            How may I assist you?
            /about - For information about YAMG
            /upcoming - For Upcoming Events
            /register - For registering to YAMG
            /contact - For Contact us
            /help - For help or to view this message""")
    return ConversationHandler.END


# Handle for contact command
def contact_command(update, context):
    update.message.reply_text('You can contact us via\n'
                              'Phone: +251 93532 1140\n'
                              'Email:\n'
                              'youthawarenessandmindsetgrowth@gmail.com')


# Handle for help command
def help_command(update, context):
    update.message.reply_text \
        ("""Hello, I'm YAMG your assist.
        How may I assist you?
        /about - For information about YAMG
        /upcoming - For Upcoming Events
        /register - For registering to YAMG
        /contact - For Contact us
        /help - For help or to view this message""")


# Handle for users response
def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


# Handle for errors
def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler('register', intro)],
        states={
            FNAME: [MessageHandler(Filters.text, callback=fname)],
            LNAME: [MessageHandler(Filters.text, callback=lname)],
            AGE: [MessageHandler(Filters.text, callback=age)],
            PHONE: [MessageHandler(Filters.text, callback=phone)],
            EMAIL: [MessageHandler(Filters.text, callback=email)],
            ADDRESS: [MessageHandler(Filters.text, callback=address)],
            CORRECT: [MessageHandler(Filters.text, callback=correct)]
        },
        fallbacks=[CommandHandler('quit', quit)]
    ))

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("about", about_command))
    dp.add_handler(CommandHandler("upcoming", upcoming_command))
    dp.add_handler(CommandHandler("contact", contact_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://ancient-castle-08894.herokuapp.com/' + TOKEN)
    updater.idle()


main()
