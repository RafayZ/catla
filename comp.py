#Dictionary for all the comps possible 
def dcomp(name):
    print('Please note that high level rare comps can also be used backwards.')
    comps = {
        'Ranpo' : ["For Sr,Ur max & rare 1000-2200: Arde, Ikumi, Ikumi (all Sr) or Senku, Jiraiya/Loke, Dio/Gasai (all Sr)"],
        'Nico' : ["For Sr,Ur max & rare 1000-2200: Izumo, Mukuro, Iris (2 UR)"],
        'Iz' : ["For Sr,Ur max & rare 1000-2200: Ranpo, Motoyasu, Dio (1 UR)"],
        'Machi' : ["For Sr,Ur max: Doppo, Koshi, Shion (all SR) or Josuke, Doppo, Shion (all Sr)", "For rare 1800-2200: Doppo, Koshi, Shion (1 UR)"],
        'Sora' : ["For Sr,Ur max & rare 1000-2200: Kenma, Shoto, Fuyumi (all Sr"],
        'Hinawa' : ["For Sr,Ur max & rare 1000-1800: Shoto, Gowther, Fuyumi (all Sr)", "For rare 1800-2100: Jonathan, Iz, Elma (1 Ur)"],
        'Izumo' : ["For Sr,Ur max & rare 1000-1600: Rize, Doppo/Iz, Nezuko", "For rare 1600+: Nico, Shoto, Gasai (1 Ur min)"],
        'Shoto' : ["For Sr,Ur max & rare 1500-2200: Nishinoya, Iz/Yukina, Killua/Kenpachi (Ur Para is a must, 1-2 Ur)", "For rare 1000-1500: Ranpo, Motoyasu, Dio (1-2 Ur)"],
        'Star' : ["For Sr,Ur max & rare 1000-1600: Doppo, Koshi, Shion (1 Ur for Sr max, 2 Ur for above)", "For rare 1600+ Doppo, Koshi, Gin (2-3 Ur)"]
        }
    for key in comps:
        if key == name.title():
            print(comps[key])

dcomp('hinawa')
