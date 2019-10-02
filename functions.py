import numpy as np #linear algebra
import pandas as pd #data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pylab as plt
import seaborn as sns

#
#class ( L, M , H ) by nationality ,place of bith , topic , gender , stage , semester
#ca donne les grades des etudiants par ses axes
#

def classparnationality():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    data['numeric_class'] = [1 if data.loc[i,'Class'] == 'L' else 2 if data.loc[i,'Class'] == 'M' else 3 for i in range(len(data))]
    # Now lets look at nationality
    nation = data.NationalITy.unique()
    nation_grades_ave = [sum(data[data.NationalITy == i].numeric_class)/float(len(data[data.NationalITy == i])) for i in nation]
    ax = sns.barplot(x=nation, y=nation_grades_ave)
    jordan_ave = sum(data[data.NationalITy == 'TN'].numeric_class)/float(len(data[data.NationalITy == 'TN']))
    print('\n\n\n\n\n\n\n\n\n')
    print('Tunisia average: '+str(jordan_ave))
    print('\n\n\n\n\n\n\n\n\n')
    plt.xticks(rotation=90)
    plt.title('Moyenne General des Etudiants')    
    plt.show()
    
def classparplaceofbirth():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    data['numeric_class'] = [1 if data.loc[i,'Class'] == 'L' else 2 if data.loc[i,'Class'] == 'M' else 3 for i in range(len(data))]
    # Now lets look at nationality
    nation = data.PlaceofBirth.unique()
    nation_grades_ave = [sum(data[data.PlaceofBirth == i].numeric_class)/float(len(data[data.PlaceofBirth == i])) for i in nation]
    ax = sns.barplot(x=nation, y=nation_grades_ave)
    for i in nation :
        print(i+' : '+str(sum(data[data.PlaceofBirth == i].numeric_class)/float(len(data[data.PlaceofBirth == i]))))
    plt.xticks(rotation=90)
    plt.title('Moyenne des etudiants par gouvernorat')
    plt.show()

def classpartopic():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    data['numeric_class'] = [1 if data.loc[i,'Class'] == 'L' else 2 if data.loc[i,'Class'] == 'M' else 3 for i in range(len(data))]
    lessons = data.Topic.unique()
    lessons_grade_ave=[sum(data[data.Topic == i].numeric_class)/float(len(data[data.Topic == i])) for i in lessons]
    ax = sns.barplot(x=lessons, y=lessons_grade_ave)
    for i in lessons :
        print(i+' : '+str(sum(data[data.Topic == i].numeric_class)/float(len(data[data.Topic == i]))))
    print('\n\n\n\n\n\n\n\n\n')
    plt.title('Moyenne des etudiants par matieres')
    plt.xticks(rotation=90)
    plt.show()

def classpargender():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    data['numeric_class'] = [1 if data.loc[i,'Class'] == 'L' else 2 if data.loc[i,'Class'] == 'M' else 3 for i in range(len(data))]
    genders = data.gender.unique()
    genders_grade_ave=[sum(data[data.gender == i].numeric_class)/float(len(data[data.gender == i])) for i in genders]
    ax = sns.barplot(x=genders, y=genders_grade_ave)
    plt.title('Moyenne des etudiants par sex')
    for i in genders :
        print(i+' : '+str(sum(data[data.gender == i].numeric_class)/float(len(data[data.gender == i]))))
    print('\n\n\n\n\n\n\n\n\n')
    plt.show()

def classparstage():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    data['numeric_class'] = [1 if data.loc[i,'Class'] == 'L' else 2 if data.loc[i,'Class'] == 'M' else 3 for i in range(len(data))]
    genders = data.StageID.unique()
    genders_grade_ave=[sum(data[data.StageID == i].numeric_class)/float(len(data[data.StageID == i])) for i in genders]
    ax = sns.barplot(x=genders, y=genders_grade_ave)
    plt.title('Moyenne des etudiants par niveau D''étude')
    for i in genders :
        print(i+' : '+str(sum(data[data.StageID == i].numeric_class)/float(len(data[data.StageID == i]))))
    print('\n\n\n\n\n\n\n\n\n')
    plt.show()

def classparsemester():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    data['numeric_class'] = [1 if data.loc[i,'Class'] == 'L' else 2 if data.loc[i,'Class'] == 'M' else 3 for i in range(len(data))]
    genders = data.Semester.unique()
    genders_grade_ave=[sum(data[data.Semester == i].numeric_class)/float(len(data[data.Semester == i])) for i in genders]
    ax = sns.barplot(x=genders, y=genders_grade_ave)
    plt.title('Moyenne des etudiants par semestre')
    for i in genders :
        print(i+' : '+str(sum(data[data.Semester == i].numeric_class)/float(len(data[data.Semester == i]))))
    print('\n\n\n\n\n\n\n\n\n')
    plt.show()


#
#absenses by nationality , topic , gender , stage , semester
#ca donne les effets des absenses
#

def abscenceperday():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    data['numeric_class'] = [1 if data.loc[i,'Class'] == 'L' else 2 if data.loc[i,'Class'] == 'M' else 3 for i in range(len(data))]
    absence_day = data.StudentAbsenceDays.unique()
    absense_day_ave = [sum(data[data.StudentAbsenceDays == i].numeric_class)/float(len(data[data.StudentAbsenceDays == i])) for i in absence_day]
    ax = sns.barplot(x=absence_day, y=absense_day_ave)
    plt.title('Effet des absences sur le succes des étudiants')
    plt.show()
    


def abscenceperdayparsemester():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    data['numeric_class'] = [10 if data.loc[i,'StudentAbsenceDays'] == 'Under-7' else 5 if data.loc[i,'StudentAbsenceDays'] == 'Above-7' else 0 for i in range(len(data))]
    absenses = data.Semester.unique()
    absenses_grade_ave=[sum(data[data.Semester == i].numeric_class) for i in absenses]
    ax = sns.barplot(x=absenses, y=absenses_grade_ave)
    plt.title('nombre des absences en jours par semetre')
    for i in absenses :
        print(i+' : moyenne des absenses = '+str(sum(data[data.Semester == i].numeric_class)/float(len(data[data.Semester == i])))+'\nnombre des absnses = '+str(sum(data[data.Semester == i].numeric_class)))
    print('\n\n\n\n\n\n\n\n\n')
    plt.show()


def abscenceperdaypartopic():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    data['numeric_class'] = [10 if data.loc[i,'StudentAbsenceDays'] == 'Under-7' else 5 if data.loc[i,'StudentAbsenceDays'] == 'Above-7' else 0 for i in range(len(data))]
    absenses = data.Topic.unique()
    absenses_grade_ave=[sum(data[data.Topic == i].numeric_class) for i in absenses]
    ax = sns.barplot(x=absenses, y=absenses_grade_ave)
    plt.title('nombre des absences en jours par matieres')
    for i in absenses :
        print(i+' : moyenne des absenses = '+str(sum(data[data.Topic == i].numeric_class)/float(len(data[data.Topic == i])))+'\nnombre des absnses = '+str(sum(data[data.Topic == i].numeric_class)))
    print('\n\n\n\n\n\n\n\n\n')
    plt.xticks(rotation=90)
    plt.show()


def abscenceperdaypargender():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    data['numeric_class'] = [10 if data.loc[i,'StudentAbsenceDays'] == 'Under-7' else 5 if data.loc[i,'StudentAbsenceDays'] == 'Above-7' else 0 for i in range(len(data))]
    absenses = data.gender.unique()
    absenses_grade_ave=[sum(data[data.gender == i].numeric_class) for i in absenses]
    ax = sns.barplot(x=absenses, y=absenses_grade_ave)
    plt.title('nombre des absences en jours par sex')
    for i in absenses :
        print(i+' : moyenne des absenses = '+str(sum(data[data.gender == i].numeric_class)/float(len(data[data.gender == i])))+'\nnombre des absnses = '+str(sum(data[data.gender == i].numeric_class)))
    print('\n\n\n\n\n\n\n\n\n')
    plt.show()


def abscenceperdayparstage():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    data['numeric_class'] = [10 if data.loc[i,'StudentAbsenceDays'] == 'Under-7' else 5 if data.loc[i,'StudentAbsenceDays'] == 'Above-7' else 0 for i in range(len(data))]
    absenses = data.StageID.unique()
    absenses_grade_ave=[sum(data[data.StageID == i].numeric_class) for i in absenses]
    ax = sns.barplot(x=absenses, y=absenses_grade_ave)
    plt.title('nombre des absences en jours par niveau d''études')
    for i in absenses :
        print(i+' : moyenne des absenses = '+str(sum(data[data.StageID == i].numeric_class)/float(len(data[data.StageID == i])))+'\nnombre des absnses = '+str(sum(data[data.StageID == i].numeric_class)))
    print('\n\n\n\n\n\n\n\n\n')
    plt.show()


#
#dicussion by topic
#

def discussionpartopic():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    absenses = data.Topic.unique()
    absenses_grade_ave=[sum(data[data.Topic == i].Discussion) for i in absenses]
    ax = sns.barplot(x=absenses, y=absenses_grade_ave)
    plt.title('Discussion des Etudiants par matiere')
    for i in absenses :
        print(i+' : moyenne des absenses = '+str(sum(data[data.Topic == i].Discussion)/float(len(data[data.Topic == i])))+'\nnombre des absnses = '+str(sum(data[data.Topic == i].Discussion)))
    print('\n\n\n\n\n\n\n\n\n')
    plt.xticks(rotation=90)
    plt.show()


#
#raisedhands by topic
#

def raisedhandspartopic():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    absenses = data.Topic.unique()
    absenses_grade_ave=[sum(data[data.Topic == i].raisedhands) for i in absenses]
    ax = sns.barplot(x=absenses, y=absenses_grade_ave)
    plt.title('participation des étudiants par matiere')
    for i in absenses :
        print(i+' : moyenne des absenses = '+str(sum(data[data.Topic == i].raisedhands)/float(len(data[data.Topic == i])))+'\nnombre des absnses = '+str(sum(data[data.Topic == i].raisedhands)))
    print('\n\n\n\n\n\n\n\n\n')
    plt.xticks(rotation=90)
    plt.show()

    
def palettedeparticipation():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    melt = pd.melt(data,id_vars='Class',value_vars=['raisedhands'])
    sns.swarmplot(x='variable',y='value',hue='Class' , data=melt,palette={'H':'lime','M':'grey','L':'red'})
    plt.ylabel('Valeurs de zero à 100')
    plt.title('Étudiants de haut, moyen et bas niveau')
    plt.show()

def relationwithfamily():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    data['numeric_class'] = [1 if data.loc[i,'Class'] == 'L' else 2 if data.loc[i,'Class'] == 'M' else 3 for i in range(len(data))]
    relation = data.Relation.unique()
    relation_grade_ave = [sum(data[data.Relation == i].numeric_class)/float(len(data[data.Relation == i])) for i in relation]
    ax = sns.barplot(x=relation, y=relation_grade_ave)
    plt.title('Relation avec le père ou la mère affecte le succès des élèves')
    plt.show()


def discussionparticipation():
    data=pd.read_csv(r'xAPI-Edu-Data.csv')
    data['numeric_class'] = [1 if data.loc[i,'Class'] == 'L' else 2 if data.loc[i,'Class'] == 'M' else 3 for i in range(len(data))]
    discussion = data.Discussion
    discussion_ave = sum(discussion)/len(discussion)
    ave_raisedhands = sum(data['raisedhands'])/len(data['raisedhands'])
    ave_VisITedResources = sum(data['VisITedResources'])/len(data['VisITedResources'])
    ave_AnnouncementsView = sum(data['AnnouncementsView'])/len(data['AnnouncementsView'])
    unsuccess = data.loc[(data['raisedhands'] >= ave_raisedhands) & (data['VisITedResources']>=ave_VisITedResources) & (data['AnnouncementsView']>=ave_AnnouncementsView)  & (data['Class'] == 'L')]
    ax = sns.violinplot(y=discussion,split=True,inner='quart')
    ax = sns.swarmplot(y=discussion,color='black')
    ax = sns.swarmplot(y = unsuccess.Discussion, color='red')
    plt.title('Participation au groupe de discussion')
    plt.show()
