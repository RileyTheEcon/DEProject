# -*- coding: utf-8 -*-
"""
Created on Sat May  8 19:33:19 2021

@author: RC
"""
# = LIBRARIES AND GLOBALS =================================================== #
from pandas import DataFrame 
from random import sample
# =========================================================================== #



# = FUNCTIONS =============================================================== #
def get_titles() :
    ltTitles = [('Analyst',          'Logic',   'Intellect'),
                ('Pure Rationalist', 'Logic',   'Intellect'),
                ('Logician',         'Logic',   'Intellect'),
                
                ('Thinker',     'Encyclopedia',   'Intellect'),
                ('Historian',   'Encyclopedia',   'Intellect'),
                ('Trivia Freak','Encyclopedia',   'Intellect'),
                
                ('Ideologue',           'Rhetoric',   'Intellect'),
                ('Conversationalist',   'Rhetoric',   'Intellect'),
                ('Would-Be-Politician', 'Rhetoric',   'Intellect'),
                
                ('Undercover Cop', 'Drama',   'Intellect'),
                ('Thespian',       'Drama',   'Intellect'),
                ('Psychopath',     'Drama',   'Intellect'),
                
                ('Creative',            'Conceptualization',   'Intellect'),
                ('Psychedelic Fancier', 'Conceptualization',   'Intellect'),
                ('Art Critic',          'Conceptualization',   'Intellect'),
                
                ('Forensic Scientist', 'Visual Calculus',   'Intellect'),
                ('Tactical Fighter',   'Visual Calculus',   'Intellect'),
                ('Math-Minded Person', 'Visual Calculus',   'Intellect'),
                
                ('Sane',              'Violition',   'Psyche'),
                ('Well-Adjusted Cop', 'Violition',   'Psyche'),
                ('Non-Suicidal',      'Violition',   'Psyche'),
                
                ('Dreamer',                   'Inland Empire',   'Psyche'),
                ('Para-Natural Investigator', 'Inland Empire',   'Psyche'),
                ('Mental Creator',            'Inland Empire',   'Psyche'),
                
                ('Good Judge of Character', 'Empathy',   'Psyche'),
                ('Interviewer',             'Empathy',   'Psyche'),
                ('Interrogator',            'Empathy',   'Psyche'),
                
                ('Leader',                'Authority',   'Psyche'),
                ('Psychological Warrior', 'Authority',   'Psyche'),
                ('Respect Junkie',        'Authority',   'Psyche'),
                
                ('Cop',            'Esprit de Corps',   'Psyche'),
                ('Cop-Aficionado', 'Esprit de Corps',   'Psyche'),
                ('Pretend-Cop',    'Esprit de Corps',   'Psyche'),
                
                ('Diplomat',  'Suggestion',   'Psyche'),
                ('Charmer',   'Suggestion',   'Psyche'),
                ('Sociopath', 'Suggestion',   'Psyche'),
                
                ('Fighter Who Can Take a Hit', 'Endurance', 'Physique'),
                ('Lookout Who Doesn\'t Sleep', 'Endurance', 'Physique'),
                ('Human Battery',              'Endurance', 'Physique'),
                
                ('Unstoppable Fighter', 'Pain Threshold', 'Physique'),
                ('Indestructible',      'Pain Threshold', 'Physique'),
                ('Masochist',           'Pain Threshold', 'Physique'),
                
                ('Muscle Man',           'Physical Instrument', 'Physique'),
                ('Bare Knuckle Brawler', 'Physical Instrument', 'Physique'),
                ('Gym Teacher',          'Physical Instrument', 'Physique'),
                
                ('High-Flier',              'Electro-Chemistry', 'Physique'),
                ('Party Enthusiast',        'Electro-Chemistry', 'Physique'),
                ('Cop Who Needs Lightning', 'Electro-Chemistry', 'Physique'),
                
                ('City Lover',                'Shivers', 'Physique'),
                ('Wisest of the Street Wise', 'Shivers', 'Physique'),
                ('Genuinely Supra-Natural',   'Shivers', 'Physique'),
                
                ('High-Strung Investigator',          'Half Light', 'Physique'),
                ('Shoot-Now-Ask-Questions-Later Cop', 'Half Light', 'Physique'),
                ('Surprise Hater',                    'Half Light', 'Physique'),
                
                ('Trick-Shooter', 'Hand-Eye Coordination',  'Motorics'),
                ('Sniper',        'Hand-Eye Coordination',  'Motorics'),
                ('Juggler',       'Hand-Eye Coordination',  'Motorics'),
                
                ('Fine Detail Detective', 'Perception',  'Motorics'),
                ('Sensualist',            'Perception',  'Motorics'),
                ('Urban Scavenger',       'Perception',  'Motorics'),
                
                ('Shot-Dodger',        'Reaction Speed',  'Motorics'),
                ('Think-On-Your-Feet', 'Reaction Speed',  'Motorics'),
                ('Pinball Head',       'Reaction Speed',  'Motorics'),
                
                ('Acrobat',             'Savoir Faire',  'Motorics'),
                ('Thief',               'Savoir Faire',  'Motorics'),
                ('Unbearable Show-Off', 'Savoir Faire',  'Motorics'),
                
                ('Machinist', 'Interfacing',  'Motorics'),
                ('Tinkerer',  'Interfacing',  'Motorics'),
                ('Musician',  'Interfacing',  'Motorics'),
                
                ('Card Player',        'Composure',  'Motorics'),
                ('Military Fetishist', 'Composure',  'Motorics'),
                ('Cool Person',        'Composure',  'Motorics'),
                ]
    dfStats = DataFrame(ltTitles,columns=['title','skill','attribute'])
    dfStats['assign'] = (sample(range(18),18)+sample(range(18),18)+
                         sample(range(18),18)+sample(range(18),18))
    dfStats['choice'] = 0
    return dfStats
####
def run_questions (dfStats) :
    iCounter = 1
    for i in range(18) :
        dictChoice = {}
        jCounter = 1
        
        for j in sample(list(dfStats[dfStats['assign']==i].index),4) :
            dictChoice[jCounter] = j
            jCounter+=1
        #   endfor
        
        print('\n\n\n['+str(iCounter)+' / 18] '+
              'Which description most applies to you '+
              '(or the cop you want to play as)?\n\n'+
              '1: '+dfStats.iloc[dictChoice[1]]['title']+'\n'+
              '2: '+dfStats.iloc[dictChoice[2]]['title']+'\n'+
              '3: '+dfStats.iloc[dictChoice[3]]['title']+'\n'+
              '4: '+dfStats.iloc[dictChoice[4]]['title']
              )
        
        strIn = None
        while type(strIn)!=int :
            strIn = input('In: ')
            
            if strIn in ['1','2','3','4'] :
                strIn = int(strIn)
            else :
                print('Please enter 1, 2, 3 or 4')
        #   endwhile
        dfStats.loc[dictChoice[strIn],'choice'] = 1
        iCounter+=1
    #   endfor
    return dfStats
####
def get_attr (dfStats) :
    ### ATTRIBUTES
    # dfStats.groupby(['attribute'])['choice'].sum().sort_values()
    dfAttr = DataFrame(dfStats.groupby(['attribute']
                                       )['choice'].sum().sort_values())
    dfAttr['choice'] = dfAttr['choice'].apply(lambda x : 1+round((4/9)*x))
    while not ((dfAttr['choice'].sum()==12)&
               (dfAttr['choice'].max()<=6)&
               (dfAttr['choice'].min()>=1)) : 
        # Apply max/min
        dfAttr['choice'] = dfAttr['choice'].apply(lambda x : 6 if x>6 else x)
        dfAttr['choice'] = dfAttr['choice'].apply(lambda x : 1 if x<1 else x)
        
        # Apply b caps
        dfAttr['capped'] = 0
        dfAttr['capped'] = dfAttr['choice'].apply(lambda x : 1 if x==6 else 0)
        
        # Get Unassigned Points, Open Skills, Check Comparison
        intPoints = 12 - dfAttr['choice'].sum()
        listAttr = list(dfAttr[dfAttr['capped']==0].index)
        
        # For too many points:
        if intPoints>=len(listAttr) : 
            dfAttr['choice'] = dfAttr.apply(lambda x : x['choice']+1 
                                            if x.name in listAttr
                                            else x['choice'], axis=1
                                            )
            
        # For too few points:
        else :
            # Get user input
            print(str(intPoints)+' unassigned attribute point'+
                  's'*int(intPoints>1)+' found. '+
                  '(S)elect or assign by (R)andom.')
            strIn = input('[Select/Random]: ')
            
            # Boost user selected
            if strIn in ['s','S','select','Select'] :
                i = 0
                listI = []
                while i < len(listAttr) :
                    print(str(i+1)+': '+listAttr[i])
                    i+=1
                    listI.append(str(i))
                #   endwhile
                strIn = input('Input int index: ')
                if strIn in listI :
                    strAttr = listAttr[int(strIn)-1]
                    dfAttr['choice'] = dfAttr.apply(lambda x : x['choice']+1 
                                                    if x.name==strAttr
                                                    else x['choice'], axis=1
                                                    )
                    
                else : print('Please enter integer from table shown')
            
            # Randomly assign points
            elif strIn in ['r','R','random','Random']:
                strAttr = listAttr[sample(range(len(listAttr)),1)[0]]
                dfAttr['choice'] = dfAttr.apply(lambda x : x['choice']+1 
                                                if x.name==strAttr
                                                else x['choice'], axis=1
                                                )
                
            else : print("Please input 'S', 'select', 'R' or 'random'")
        #   endif
        
    #   endwhile
    return dfAttr
####
def get_skills (dfStats) :
    #### SKILLS
    # dfStats.groupby(['skill'])['choice'].sum().sort_values()
    dfSkill = DataFrame(dfStats.groupby(['skill']
                                        )['choice'].sum().sort_values())
    listSkill = list(dfSkill[dfSkill['choice']==dfSkill['choice'].max()].index)
    if len(listSkill)==1 : strSkill = listSkill[0]
    else:
        print(str(len(listSkill))+' possible signature skills found. '+
              '(S)elect or assign by (R)andom.')
        strIn = input('[Select/Random]: ')
        
        if strIn in ['s','S','select','Select'] :
            i = 0
            listI = []
            while i < len(listSkill) :
                print(str(i+1)+': '+listSkill[i])
                i+=1
                listI.append(str(i))
            #   endwhile
            strIn = input('Input int index: ')
            if strIn in listI : strSkill = listSkill[int(strIn)-1]
            else : print('Please enter integer from table shown')
                
        elif strIn in ['r','R','random','Random']:
            strSkill = listSkill[sample(range(len(listSkill)),1)[0]]
        else : print("Please input 'S', 'select', 'R' or 'random'")
    #   endif
    return strSkill
####
def print_results (dfAttr,strSkill) :
    print('RESULTS\n\n'+
          'Intellect: '+str(dfAttr.loc['Intellect'][0])+'\n'+
          'Psyche:    '+str(dfAttr.loc['Psyche'][0])+'\n'+
          'Physique:  '+str(dfAttr.loc['Physique'][0])+'\n'+
          'Motorics:  '+str(dfAttr.loc['Motorics'][0])+'\n\n'+
          'Signature Skill: '+strSkill
          )
####
# =========================================================================== #


# = MAIN ==================================================================== #
print('WELCOME TO THE DISCO ELYSIUM CHARACTER GENERATOR!!!\n\n'+
      'This program will generate a character build based on your answers '+
      'to a series of 18 questions.\n'+
      'If there are any ties in deciding the allocation of attribute points '+
      'or the choice of signature skill, you will be prompted to either '+
      'manually choose or allow a random process to decide.\n'+
      'Due to the randomized nature of how the questions are generated, '+
      'outcomes will vary. For best results, complete three (or more) times, '+
      'and select the best from the generated characters.\n'
      )
strIn = input('Start character generator? [Y/N]: ')
if strIn in ['y','Y','yes','Yes','run','Run','r','R','1'] : bRun=1

while bRun==1 :
    print('\n'*30)
    
    #   Get titles data
    dfStats = get_titles()
    
    #   Ask questions
    dfStats = run_questions(dfStats)
    print('\n'*30)
    
    #   Process attribute scores
    dfAttr = get_attr(dfStats)
    print('\n'*30)
    
    #   Process skill scores
    strSkill = get_skills(dfStats)
    print('\n'*30)
    
    #   Print results
    print_results(dfAttr,strSkill)
    
    #   Prompt repeat
    strIn = input('Run again? [Y/N]: ')
    if strIn in ['n','N','no','No','0','exit','Exit','end','End'] : bRun=0
    print('\n'*30)
    
#   endwhile
# =========================================================================== #
