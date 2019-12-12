class Dr_Alice():
  def __init__(self, patient, age, depression, anxiety, mental_health):
    self.patient = patient
    self.age = age
    self.depression = depression
    self.anxiety = anxiety
    self.mental_health = mental_health
  def print_mental_health(self):
    print('Hello my name is ' + self.patient + 'and I am ' + self.age + 'I have ' + self.depression + self.anxiety + 'I am looking for some help. Can you help me Dr. Alice?')

# Opening Statment from Patient
need_help = Dr_Alice('Lila ', '22 ', 'depression, ', 'no anxiety. ', 'I need help, can you help me? ')
need_help.print_mental_health()

Alice_respond = 'Dr.A: I see that you need some help, let me ask you a few questions.'
print(Alice_respond)

patient_info = {'patient_age' : 22, 'parent_consent' : 'yes', 'patient_has_depression' : 'yes', 'lack_of_motivation' : 'no', 'large_amount_of_sadness' : 'yes', 'days_a_week_depression' : 5, 'patient_has_anxiety' : 'yes', 'intense_worrying' : 'yes', 'days_a_week_anxiety' : 2, 'exercise' : 'yes', 'healthy_diet' : 'yes' }

# Age and/or Parental Consent
if patient_info['patient_age'] >= 18:
    print('I am above the age of 18')
    print('Dr.A: Since you are above the age 18, you do not need parental consent. What is the main reason you have come in today?')
elif patient_info['patient_age'] < 18:
    print('Dr.A: Since you are under the age of 18, do you have parental consent?')
    print(patient_info['parent_consent'])
    if patient_info['parent_consent'] == 'yes':
        print('Dr.A: Since you have parental consent, you are good to go!')
    elif patient_info['parent_consent'] == 'no':
        print('Dr.A: I am unable to help you without parental consent. Please return when/if you have consent.')

# Depression and Anxiety Questionaire
if patient_info['patient_has_depression'] == 'yes':
    print('I have depression and I want to get help for that')
    print('Dr.A: I see you have depression, let me figure out what your symptoms are by asking some questions. Do you tend to have a lack of motivation?')
    if 'yes' in patient_info['lack_of_motivation']:
        print('I have a lack of motivation.')
        print('Dr.A: I see that you have a lack of motivation. What about general sadness?')
        if 'yes' in patient_info['large_amount_of_sadness']:
            print('I do have a large amount of sadness. It feels hard to get through the day')
            print('Dr.A: I see. How many days a week would you say this occurs?')
            if patient_info['days_a_week_depression'] in range(0,3):
                print(patient_info['days_a_week_depression'])
                print('Dr.A: Since it occurs half the week, let us figure out what else is wrong.')
            elif patient_info['days_a_week_depression'] in range(4,7):
                print('Dr.A: Since it occurs most of the week, I will make a note to emphasize your depression. Let us figure out if there is anything else.')
elif patient_info['patient_has_depression'] =='no':
    print('Dr.A: Since you dont have depression, let us move on to other questions so I can help you.')

if patient_info['patient_has_anxiety'] == 'yes':
    print('Dr.A: I see you have anxiety, let me figure out what your symptoms are by asking some questions. Do you tend have intense worrying you cannot control?')
    if 'yes' in patient_info['intense_worrying']:
        print('I have this feeling inside of me that is nonstop and intense')
        print('Dr.A: I will make note of your generalized anxiety. How many days on average do you have anxiety?')
        if patient_info['days_a_week_anxiety'] in range(0,3):
            print(patient_info['days_a_week_anxiety'])
            print('Dr.A: Since it occurs half the week, I will make a note on your anxiety. That is enough basic information. Let us begin the healing stage.')
        elif patient_info['days_a_week_anxiety'] in range(4,7):
            print(patient_info['days_a_week_anxiety'])
            print('Dr.A: Since it occurs most of the week, I will make a note to emphasize your anxiety. That is enough basic information. Let us continue to healing.')

# Helpful Advice
print('Dr.A: After looking at your information regarding your depression and anxiety. let me offer some advice on how to manage these issues you are currently dealing with. Do you exercise?')
print('Dr.A: Exercise can be good in releasing dopamine which can indirectly lower depression and anxiety')
if patient_info['exercise'] == 'yes':
    print('Yes, I run a lot. I used to be on the cross-country team. It gets boring')
    print('Dr.A: It is good to incorporate exercise! Changing exercises could help make it more exciting. Lets move on, how is your diet?')
elif 'no' in patient_info['exercise']:
    print('I dont really exercise. I dont have the time')
    print('Dr.A: You should look into adding exercise. It should help with the dopamine regulation and can act as a stress relief for your anxiety. Look into some fun exercises! Another thing is diet, how is it? ')

if patient_info['healthy_diet'] == 'yes':
    print('Yes, I try to keep a healthy diet. I eat my greens and a lot of coffee.')
    print('Dr.A: If your diet is healthy, it can help make you better about yourself. A diet that is not healthy can cause mood swings.')
elif 'no' in patient_info['healthy_diet']:
    print('No, I dont really eat healthy. Its too hard to keep up a healthy diet.')
    print('Dr.A: You should look into eating healthier. It will help with mood regulation. Dont worry with proper exercise and mood regulation we will help withy our depression/anxiety. We are in this together.')