from django.shortcuts import render
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse
from io import StringIO
from steps.models import Member, Know, Connect, Grow, Change

# Create your views here.


def index(request):
    circle_graph = return_circle_graph()
    bar_graph = return_bar_graph()

    members = Member.objects.all()
    num_members = len(members)

    know = Know.objects.filter(attend_worship_service=True)
    num_know = 0
    for k in know:
        num_know += 1

    


    return render(request, 'index.html', {'circle_graph':circle_graph, 'bar_graph': bar_graph, 'members':num_members, 'know':know})



def know(request):

    members = len(Member.objects.all())
    attend_service = len(Know.objects.filter(attend_worship_service=True))
    attend_percent = get_percent(attend_service, members)
    attend = 'Attend Worship Service'
    

    starting_point = len(Know.objects.filter(starting_point=True))
    starting_point_percent = get_percent(starting_point, members)
    starting = 'Starting Point'

    commit = len(Know.objects.filter(commit_life_to_christ=True))
    commit_percent = get_percent(commit, members)
    commitment = 'Commit Life To Christ'

    recommit = len(Know.objects.filter(recommit_life_to_christ=True))
    recommit_percent = get_percent(recommit, members)
    recommitment = "Re-Commit Life To Christ"

    baptism = len(Know.objects.filter(baptism=True))
    baptism_percent = get_percent(baptism, members)
    baptisms = 'Baptism'

    join = len(Know.objects.filter(join_the_church=True))
    join_percent = get_percent(join, members)
    joining = 'Join the Church'

    steps = Know.objects.all()

    context = {
        'attend_service': attend_service,
        'attend_percent': attend_percent,
        'attend': attend,
        'starting_point': starting_point,
        'starting_point_percent': starting_point_percent,
        'starting': starting,
        'commit': commit,
        'commitment':commitment,
        'commit_percent': commit_percent,
        'recommit': recommit,
        'recommitment':recommitment,
        'recommit_percent': recommit_percent,
        'baptism': baptism,
        'baptisms': baptisms,
        'baptism_percent': baptism_percent,
        'join': join,
        'joining':joining, 
        'join_percent': join_percent, 
        'steps':steps,

    }
    
    return render(request, 'know.html', context)


def connect(request):

    members = len(Member.objects.all())
    complete_card = len(Connect.objects.filter(complete_a_connect_card=True))
    complete_card_percent = get_percent(complete_card, members)
    connect = 'Connect a Connect Card'

    life_group = len(Connect.objects.filter(attend_life_group=True))
    life_group_percent = get_percent(life_group, members)
    life = 'Attend Life Group'

    attend_gathering = len(Connect.objects.filter(attend_community_gathering=True))
    attend_gathering_percent = get_percent(attend_gathering, members)
    community = 'Attend Community Gathering'

    attend_event = len(Connect.objects.filter(attend_a_mens_or_womens_event=True))
    attend_event_percent = get_percent(attend_event, members)
    event = "Attend a Men's or Women's Event"

    participate = len(Connect.objects.filter(participate_in_an_Age_Graded_Ministry=True))
    participate_percent = get_percent(participate, members)
    ministry = 'Participate in an Age-Graded Ministry'

    join = len(Connect.objects.filter(join_our_mailing_list_or_notification_list=True))
    join_percent = get_percent(join, members)
    mail = 'Join our Mailing List or Notification List'

    context = {
        'complete_card': complete_card,
        'complete_card_percent': complete_card_percent,
        'connect': connect,
        'life_group': life_group,
        'life_group_percent': life_group_percent,
        'life':life,
        'attend_gathering': attend_gathering,
        'attend_gathering_percent': attend_gathering_percent,
        'community':community,
        'attend_event': attend_event,
        'attend_event_percent': attend_event_percent,
        'event':event,
        'participate': participate,
        'participate_percent': participate_percent,
        'ministry':ministry,
        'join': join,
        'join_percent': join_percent,
        'mail':mail,

    }
    return render(request, 'connect.html', context)


def grow(request):

    members = len(Member.objects.all())
    read_the_Bible = len(Grow.objects.filter(read_the_Bible=True))
    read_the_Bible_percent = get_percent(read_the_Bible, members)
    read = 'Read the Bible'

    journaling = len(Grow.objects.filter(engage_in_Gods_word_through_journaling=True))
    journaling_percent = get_percent(journaling, members)
    engage = "Engage in God's Word through Journaling"

    memorize = len(Grow.objects.filter(memorize_scripture=True))
    memorize_percent = get_percent(memorize, members)
    scripture = 'Memorize Scripture'

    join_D = len(Grow.objects.filter(join_a_D_group=True))
    join_D_percent = get_percent(join_D, members)
    d_group = 'Join a D-group'

    lead_D = len(Grow.objects.filter(lead_a_d_group=True))
    lead_D_percent = get_percent(lead_D, members)
    d_lead = 'Lead a D-Group'

    attend_study = len(Grow.objects.filter(attend_a_mid_week_study=True))
    attend_study_percent = get_percent(attend_study, members)
    study = 'Attend a Mid-Week Study'

    fast_pray = len(Grow.objects.filter(fast_and_pray=True))
    fast_pray_percent = get_percent(fast_pray, members)
    fast = 'Fast & Pray'

    context = {
        'read_the_Bible': read_the_Bible,
        'read_the_Bible_percent': read_the_Bible_percent,
        'read':read,
        'journaling': journaling,
        'journaling_percent': journaling_percent,
        'engage':engage,
        'memorize': memorize,
        'memorize_percent': memorize_percent,
        'scripture':scripture,
        'join_D': join_D,
        'join_D_percent': join_D_percent,
        'd_group':d_group,
        'lead_D': lead_D,
        'lead_D_percent': lead_D_percent,
        'd_lead':d_lead,
        'attend_study': attend_study,
        'attend_study_percent': attend_study_percent,
        'study':study,
        'fast_pray': fast_pray,
        'fast_pray_percent': fast_pray_percent,
        'fast':fast,
    }


    return render(request, 'grow.html', context)


def change(request):

    members = len(Member.objects.all())
    invite = len(Change.objects.filter(invite_someone_to_church=True))
    invite_percent = get_percent(invite, members)
    invite_someone = 'Invite Someone to Church'

    bring = len(Change.objects.filter(bring_a_guest_to_church=True))
    bring_percent = get_percent(bring, members)
    guest = 'Bring a Guest to Church'

    conversation = len(Change.objects.filter(have_a_gospel_conversation=True))
    conversation_percent = get_percent(conversation, members)
    gospel = 'Have a Gospel Conversation'

    serving_team = len(Change.objects.filter(join_a_serving_team=True))
    serving_team_percent = get_percent(serving_team, members)
    serving = 'Join a Serving Team'

    give = len(Change.objects.filter(give_for_the_first_time=True))
    give_percent = get_percent(give, members)
    first = 'Give For the First Time'

    repeat_giver = len(Change.objects.filter(become_a_repeat_giver=True))
    repeat_giver_percent = get_percent(repeat_giver, members)
    repeat = 'Become a Repeat Giver'

    regular_giver = len(Change.objects.filter(become_a_regular_giver=True))
    regular_giver_percent = get_percent(regular_giver, members)
    regular = 'Become a Regular Giver'

    mission_trip = len(Change.objects.filter(go_on_a_mission_trip=True))
    mission_trip_percent = get_percent(mission_trip, members)
    mission = 'Go On a Mission Trip'

    mission_project = len(Change.objects.filter(lead_a_neighborhood_mission_project=True))
    mission_project_percent = get_percent(mission_project, members)
    project = 'Lead a Neighborhood Mission Project'

    spiritual_gifts = len(Change.objects.filter(take_a_spiritual_gifts_inventory=True))
    spiritual_gifts_percent = get_percent(spiritual_gifts, members)
    inventory = 'Take a Spiritual Gifts Inventory'

    social_media = len(Change.objects.filter(share_church_content_on_social_media=True))
    social_media_percent = get_percent(social_media, members)
    media = 'Share Church Content on Social Media'

    context = {
        'invite': invite,
        'invite_percent': invite_percent,
        'invite_someone': invite_someone,
        'bring': bring,
        'bring_percent': bring_percent,
        'guest':guest,
        'conversation': conversation,
        'conversation_percent': conversation_percent,
        'gospel':gospel,
        'serving_team': serving_team,
        'serving_team_percent': serving_team_percent,
        'serving': serving,
        'give': give,
        'give_percent': give_percent,
        'first':first,
        'repeat_giver': repeat_giver,
        'repeat_giver_percent': regular_giver_percent,
        'repeat':repeat,
        'regular_giver': regular_giver,
        'regular_giver_percent': regular_giver_percent,
        'regular':regular,
        'mission_trip': mission_trip,
        'mission_trip_percent': mission_trip_percent,
        'mission':mission,
        'mission_project': mission_project,
        'mission_project_percent': mission_project_percent,
        'project':project,
        'spiritual_gifts': spiritual_gifts,
        'spiritual_gifts_percent': spiritual_gifts_percent,
        'inventory':inventory,
        'social_media': social_media,
        'social_media_percent': social_media_percent,
        'media':media,
    }

    return render(request, 'change.html', context)


def person(request):

    members = Member.objects.all()
    member_id = [id['id'] for id in Member.objects.all().values()]
    member_list = zip(members,member_id)
    member_know = Know.objects.filter(attend_worship_service=True)

    return render(request, 'person.html', {'members':members, 'member_know': member_know, 'member_id': member_id, 'member_list': member_list})


def progress(request, person, id):

   
    name = person.upper()
    member_know = Know.objects.filter(member=id).values()
    member_connect = Connect.objects.filter(member=id).values()
    member_grow = Grow.objects.filter(member=id).values()
    member_change = Change.objects.filter(member=id).values()
    

    context = {
        'name':name,
        'member_know':member_know,
        'member_connect': member_connect,
        'member_grow': member_grow,
        'member_change': member_change,
       
    }

    return render(request, 'progress.html', context)


def completed(request, step):

    
    members = " "
    if step == 'Attend Worship Service':
        members = Know.objects.filter(attend_worship_service=True)
    elif step == 'Starting Point':
        members = Know.objects.filter(starting_point=True)
    elif step == 'Commit Life To Christ':
        members = Know.objects.filter(commit_life_to_christ=True)
    elif step == 'Re-Commit Life To Christ':
        members = Know.objects.filter(recommit_life_to_christ=True)
    elif step == 'Baptism':
        members = Know.objects.filter(baptism=True)
    elif step == 'Join the Church':
        members = Know.objects.filter(join_the_church=True)
    elif step == 'Connect a Connect Card':
        members = Connect.objects.filter(complete_a_connect_card=True)
    elif step == 'Attend Life Group':
        members = Connect.objects.filter(attend_life_group=True)
    elif step == 'Attend Community Gathering':
        members = Connect.objects.filter(attend_community_gathering=True)
    elif step == "Attend a Men's or Women's Event":
        members = Connect.objects.filter(attend_a_mens_or_womens_event=True)
    elif step == 'Participate in an Age-Graded Ministry':
        members = Connect.objects.filter(participate_in_an_Age_Graded_Ministry=True)
    elif step == 'Join our Mailing List or Notification List':
        members = Connect.objects.filter(join_our_mailing_list_or_notification_list=True)
    elif step == 'Read the Bible':
        members = Grow.objects.filter(read_the_Bible=True)
    elif step == "Engage in God's Word through Journaling":
        members = Grow.objects.filter(engage_in_Gods_word_through_journaling=True)
    elif step == 'Memorize Scripture':
        members = Grow.objects.filter(memorize_scripture=True)
    elif step == 'Join a D-group':
        members = Grow.objects.filter(join_a_D_group=True)
    elif step == 'Lead a D-Group':
        members = Grow.objects.filter(lead_a_d_group=True)
    elif step == 'Attend a Mid-Week Study':
        members = Grow.objects.filter(attend_a_mid_week_study=True)
    elif step == 'Fast & Pray':
        members = Grow.objects.filter(fast_and_pray=True)
    elif step == 'Invite Someone to Church':
        members = Change.objects.filter(invite_someone_to_church=True)
    elif step == 'Bring a Guest to Church':
        members = Change.objects.filter(bring_a_guest_to_church=True)
    elif step == 'Have a Gospel Conversation':
        members = Change.objects.filter(have_a_gospel_conversation=True)
    elif step == 'Join a Serving Team':
        members = Change.objects.filter(join_a_serving_team=True)
    elif step == 'Give For the First Time':
        members = Change.objects.filter(give_for_the_first_time=True)
    elif step == 'Become a Regular Giver':
        members = Change.objects.filter(become_a_regular_giver=True)
    elif step == 'Become a Repeat Giver':
        members = Change.objects.filter(become_a_repeat_giver=True)
    elif step == 'Go On a Mission Trip':
        members = Change.objects.filter(go_on_a_mission_trip=True)
    elif step == 'Lead a Neighborhood Mission Project':
        members = Change.objects.filter(lead_a_neighborhood_mission_project=True)
    elif step == 'Take a Spiritual Gifts Inventory':
        members = Change.objects.filter(take_a_spiritual_gifts_inventory=True)
    elif step == 'Share Church Content on Social Media':
        members = Change.objects.filter(share_church_content_on_social_media=True)



    return render(request, 'completed.html', {'step':step, 'members':members})


def return_circle_graph():

    
    y = np.array([32,25,25,15])

    fig = plt.figure()
    plt.pie(y)
    plt.title('Percent of People')

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


def return_bar_graph():

    x = [5,10,15,20]
    y = [5,10,15,20]

    fig = plt.figure()
    plt.bar(x,y, color='blue', width=2)
    plt.title('Number of People')

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


def get_percent(num, total):
    percent = round((num/total) * 100, 2)
    return percent