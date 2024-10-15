# Chapter 6/Cities.py


cities = {
    'chongqing': {
        'country': 'china',
        'population': 32000000,
        'descriptions': 'Chongqing, reputed as Little Hong Kong, has become the world\'s fastest-growing tourism city in recent years with both enthralling urban cityscape and traditional cultural elements. Positioned alongside the upper Yangtze River in Southwest China, this sprawling metropolis is the launching point for scenic relaxing cruise down the Yangtze River through Three Gorges and the Three Gorges Dam. As one of the four major municipalities of China (the other three are Beijing, Shanghai, Tianjin), Chongqing is bordered with Sichuan in the west, Hubei and Hunan in the east, Shaanxi in the north, linked by numerous high speed trains and flights with many domestic cities of China.',
        },
    'ha noi': {
        'country': 'viet nam',
        'population': 8587000,
        'descriptions': 'Founded along the Red River, Ha Noi was named Thang Long (soaring dragon) by Emperor Ly Thai To in 1010. Over a thousand years of war, natural disasters and new administrations, the city grew from swamplands into the charismatic capital it is today. Take in details of the ancient architecture, battle the barrage of millennials on motorbikes and drink fresh bia hơi in the Old Quarter. Here are 11 must-see stops in Hanoi.',
        },
    'siem reap': {
        'country': 'cambodia',
        'population': 1003285,
        'descriptions': 'Siem Reap has French-colonial and Chinese-style architecture in the Old French Quarter and around the Old Market. In and around the city there are museums, traditional Apsara dance performances, a Cambodian cultural village, souvenir and handicraft shops, silk farms, rice paddies in the countryside, fishing villages and a bird sanctuary near Tonlé Sap, and a cosmopolitan drinking and dining scene. Siem Reap city, home to the famous Angkor Wat temples, was named the ASEAN City of Culture for the period 2021–2022 at the 9th Meeting of the ASEAN Ministers Responsible for Culture and Arts (AMCA) organised on Oct 22, 2020',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    scenery = city_info['descriptions']

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print(scenery)