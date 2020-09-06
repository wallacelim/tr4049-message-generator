import signal
import sys
import pyperclip

user_id = input("Please select your name (C for Chloe, N for Nicholas, P for Pengfei, W for Wallace: ").casefold()

# 1. Determine user name
user_name = None
if user_id == 'c':
    user_name = 'Chloe'
elif user_id == 'n':
    user_name = 'Nicholas'
elif user_id == 'p':
    user_name = 'Pengfei'
elif user_id == 'w':
    user_name = 'Wallace'
else:
    raise Exception('Begone, imposter!')

print(' -------------------------------------------------------- \n')
print(f'  Hello, {user_name}!\n')
print(' ---------------- Press Ctrl + C to exit ---------------- \n')

message_count = 0


while True:
    # 2. Determine message type
    message_type = None
    try: 
        message_type = int(input("Enter message type (1 for email, 2 for mobile): "))
        assert(message_type == 1 or message_type == 2)
    except:
        print(f"\nINVALID MESSAGE TYPE: {message_type}")    
        continue

    # 3. Determine job poster's name (optional)
    job_poster_name = input("Enter the job poster's name: ")
    message_greeting = None
    if job_poster_name:
        message_greeting = f'Hello {job_poster_name},'
    else:
        message_greeting = 'Hello,'

    # 4. Determine job title (optional)
    job_title = input("Enter the job title: ")

    # 5. Determine job platform
    job_platform = None
    while True:
        job_platform = input("Enter the job platform: ")
        try:    
            assert(job_platform)
            break
        except:
            print('Please input a job platform')

    background_sentence = None
    if job_platform and not job_title: 
        background_sentence = f'I came across your contact on {job_platform}.'
    else:
        background_sentence = f'I came across your post for {job_title} on {job_platform}.'

    message = None
    if message_type == 2:
        message = f'''\
{message_greeting}

My name is {user_name}. {background_sentence}

My friends and I are students who are currently validating our start-up idea to help job posters like yourself find on-demand labour quickly and with ease. 

We were hoping to learn more about the market from you, as well as tap on your experience in the sector.

If you would be so kind, I'd love to have a 15-20 mins call with you. If you are too busy, we can shorten the call further.

Looking forward to hearing from you soon :)
'''
        print(f'''
----------------------------------------------------------------------------------------------------------

{message}

------------------------- THE ABOVE MESSAGE HAS BEEN COPIED TO YOUR CLIPBOARD -------------------------
''')
    elif message_type == 1:
        message = f'''
{message_greeting}

I hope this email finds you well. {background_sentence}

My friends and I are undergraduate students who are currently validating our start-up idea to help job posters like yourself find on-demand labour quickly with ease. 

As an initial step, we were hoping to learn more about the market from you, as well as tap on your experience in the sector.

If you would be so kind as to speak with us, we’d love to schedule a 15-20 mins video call with you. The video call could be even shorter if you’d like, we want to be respectful of your time. 

Looking forward to hearing from you soon :)

Yours sincerely,

{user_name}
'''
        print(f'''\
----------------------------------------------------------------------------------------------------------

Subject: A sincere request for your help

----------------------------------------------------------------------------------------------------------

{message}

------------------------- THE ABOVE MESSAGE HAS BEEN COPIED TO YOUR CLIPBOARD -------------------------
        ''')
    pyperclip.copy(message)
    

    message_count += 1
    print(f'\nYOU HAVE PRINTED {message_count} MESSAGES SO FAR\n')