# creating a chatbot
print("This is Alexia Chat Bot")
def askq():
    print("Enter any prompt here or press enter to exit")
    prompt = input()
    prompt = prompt.lower()


    q1 = ["what is ai", "what is ai?",  "define ai", "define ai?"]
    q2 = ["what is capital of pakistan", "capital of pakistan", "capital city of pakistan"]
    q3 = ["who is president of pakistan", "president of pakistan"]
    q4 = ["largest country in the world", "biggest country in the world?",
          "what is the world's largest country by area?", "what is Earth's biggest country?"]
    q5 = ["highest mountain in the world", "what's the tallest mountain?", "tallest mountain peak on Earth?",
          "which mountain is the highest?"]
    q6 = ["when was the Great Wall of China built?", "how old is the Great Wall of China?",
          "Great Wall of China construction period?", "when did the building of the Great Wall begin?"]
    q7 = ["most populous city in the world", "what city has the most people?",
          "which is the most populated city globally?", "largest city in terms of population?"]
    q8 = ["oldest civilization in the world", "what is the oldest human civilization?",
          "which civilization is considered the oldest?", "origins of the earliest known civilization?"]
    q9 = ["who invented the light bulb?", "light bulb inventor?", "when was the light bulb invented?",
          "discovery of the light bulb?"]
    q10 = ["first person on the moon", "who walked on the moon first?", "when was the first moon landing?",
           "moon landing astronauts?"]
    q11 = ["when was the internet invented?", "internet invention year?", "origins of the internet?",
           "who created the internet?"]
    q12 = ["most viewed sports globally", "most viewed sports in earth", "most famous sports", "most popular sports"]
    q13 = ["how many continents are there?", "what are the seven continents?",
           "how many landmasses considered continents?"]
    q14 = ["which is the world's largest ocean?", "what is the biggest ocean on Earth?", "most expansive ocean?"]
    q15 = ["what is the longest river in the world?", "which river flows the farthest distance?",
           "longest river globally?"]
    q16 = ["what is the most spoken language?", "languages with the most native speakers?",
           "most common language globally?"]
    q17 = ["which is the world's largest religion?", "most followed religion globally?",
           "religion with the highest number of adherents?"]
    q18 = ["what is the tallest building in the world?", "which building holds the current height record?",
           "tallest skyscraper globally?"]
    q19 = ["when was the first airplane invented?", "first successful flight of an airplane?",
           "which year did airplanes first fly?"]
    q20 = ["what is the largest planet in our solar system?", "which planet has the biggest diameter?",
           "giant planet with the most mass?"]
    q21 = ["what is the current population of Earth?", "how many people live on Earth right now?",
           "estimated global population today?"]
    q22 = ["what is the world's largest island?", "which island is the biggest?",
           "biggest island by size?", "largest island on Earth?"]
    q23 = ["highest waterfall in the world", "world's tallest waterfall?", "which waterfall is the highest?",
           "what is the tallest waterfall on Earth?"]
    q24 = ["what is the deepest ocean trench?", "deepest point in the ocean?", "where is the deepest trench located?",
           "which trench is the deepest in the ocean?"]
    q25 = ["what is the largest desert in the world?", "biggest desert on Earth?", "which desert is the largest?",
           "what is the world's largest desert by area?"]
    q26 = ["what is the hottest place on Earth?", "highest recorded temperature location?",
           "where is the highest temperature ever recorded?", "hottest spot on the planet?"]
    q27 = ["what is the largest animal on Earth?", "biggest creature in the world?",
           "which animal holds the record for size?", "largest living organism on the planet?"]
    q28 = ["what is the longest reigning monarch?", "monarch with the longest reign in history?",
           "who holds the record for the longest time as a monarch?", "longest ruling king or queen?"]
    q29 = ["what is the fastest land animal?", "which animal is the quickest on land?",
           "fastest mammal on Earth?", "what is the top speed of the fastest land creature?"]
    q30 = ["what is the tallest mammal on Earth?", "which animal holds the record for height?",
           "tallest land animal species?", "what is the tallest creature in the world?"]

    if prompt == "":
        print("Exiting")
        exit()
    elif prompt in q1:
        print("AI is a digital mimicry of human thought. It trains programs to learn, reason, and understand language, just like us. Imagine chess-playing \nrobots that learn, not just follow rules. Two types exist: one thrives on specific tasks, while the other chases human-level understanding. This \nevolving intelligence impacts the digital world, pushing boundaries and raising ethical questions. Think of it as intelligence blooming outside \nbiology, reshaping what technology can achieve.")
        print()
        return askq()
    elif prompt in q2:
        print("Islamabad is the capital of Pakistan.")
        print()
        return askq()
    elif prompt in q3:
        print("Arif Alvi is the president of Pakistan")
        print()
        return askq()
    elif prompt in q4:
        print("The largest country in the world by area is Russia, with a total land area of approximately 16.38 million square kilometers (6.3 million square \nmiles). This is equivalent to roughly 11% of the world's total landmass!")
        print()
        return askq()
    elif prompt in q5:
        print("Mount Everest is the tallest mountain on Earth.")
        print()
        return askq()
    elif prompt in q6:
        print("While construction began as early as the 7th century BC, the majority of the Great Wall visible today was built during the Ming Dynasty (1368-1644 \nAD). So, roughly speaking, you can say the Great Wall was built around 600 years ago.")
        print()
        return askq()
    elif prompt in q7:
        print("As of today (February 19, 2024), the most populous city in the world is Tokyo, Japan, with a population of around 37.4 million people. This makes \nit about twice as populated as New York City, the second largest city!")
        print()
        return askq()
    elif prompt in q8:
        print("The oldest known civilization, Mesopotamia, flourished in present-day Iraq, Kuwait, and Syria between 4000-3500 BCE. This region birthed \ninfluential societies like Sumer, Akkad, and Babylon, leaving behind lasting legacies in agriculture, writing, law, and urban planning.")
        print()
        return askq()
    elif prompt in q9:
        print("Though Thomas Edison is usually credited as the man who invented the lightbulb, the famous American inventor wasn't the only one who contributed \nto the development of this revolutionary technology.\n Alessandro Volta, Humphrey Davy and Joseph Swan played a critical role in the development of \nthis technology. ")
        print()
        return askq()
    elif prompt in q10:
        print("The first person to walk on the moon was Neil Armstrong on July 20, 1969, as part of the Apollo 11 mission. His famous first words after stepping \nonto the lunar surface were: 'That's one small step for a man, one giant leap for mankind.'")
        print()
        return askq()
    elif prompt in q11:
        print("The internet's origins aren't a single point, but two key stages:\n1960s: ARPANET, a communication network, laid the foundation for connecting computers.\nEarly 1990s: The user-friendly World Wide Web made the internet accessible to the public through browsers.")
    elif prompt in q12:
        print("Football is the most viewed sports, with an estimated 3.5 billion fans worldwide, football is the undisputed king of global sports. Its simple \nrules, minimal equipment requirements, and fast-paced action make it accessible and enjoyable for people of all ages and backgrounds. Whether you're \ncheering on your favorite team in a packed stadium or playing a casual kickabout with friends, soccer offers a unique blend of competition, \ncamaraderie, and excitement. ")
        print()
        return askq()
    elif prompt in q13:
        print("The world consists of seven continents: Africa, Antarctica, Asia, Europe, North America, South America, and Australia (sometimes referred to as \nOceania). Each continent has its own unique geographical features, ecosystems, and cultural diversity. From the vast landscapes of Asia to the \nbiodiversity of South America, and the icy expanses of Antarctica, each continent contributes to the rich tapestry of our planet's diversity.")
        print()
        return askq()
    elif prompt in q14:
        print("The world's largest ocean is the Pacific Ocean. It covers an area of approximately 63 million square miles (165 million square kilometers), making \nit larger than all the Earth's landmasses combined. The Pacific Ocean stretches from the Arctic in the north to the Southern Ocean in the south, and \nit spans the distance between the Americas in the east and Asia and Australia in the west. Its vast expanse is home to numerous islands, diverse \nmarine life, and important ecosystems.")
        print()
        return askq()
    elif prompt in q15:
        print("The longest river in the world is the Nile River, stretching over 6,650 kilometers (4,130 miles) in northeastern Africa.")
        print()
        return askq()
    elif prompt in q16:
        print("The most spoken language in the world, in terms of the number of native speakers, is Mandarin Chinese. It's the official language of China and is \nspoken by over a billion people globally.")
        print()
        return askq()
    elif prompt in q17:
        print("The world's largest religion is Christianity. With over 2.3 billion adherents, Christianity comprises various denominations and traditions, \nincluding Catholicism, Protestantism, and Eastern Orthodoxy. It is based on the teachings of Jesus Christ and has a significant presence across the \nglobe, particularly in the Americas, Europe, Africa, and parts of Asia.")
        print()
        return askq()
    elif prompt in q18:
        print("The tallest building on Earth is the Burj Khalifa in Dubai, United Arab Emirates, standing at a height of 828 meters (2,717 feet).")
        print()
        return askq()
    elif prompt in q19:
        print("The first successful powered airplane was invented and flown by the Wright brothers, Orville and Wilbur Wright. Their historic flight took place \non December 17, 1903, near Kitty Hawk, North Carolina, United States. This event marked a significant milestone in aviation history, \nas it demonstrated controlled, sustained flight with a powered aircraft.")
        print()
        return askq()
    elif prompt in q20:
        print("The largest planet in our solar system is Jupiter. It has a diameter of about 139,822 kilometers (86,881 miles) at its equator, making it more \nthan 11 times wider than Earth. Jupiter is a gas giant composed mostly of hydrogen and helium, and it's known for its prominent bands of clouds and \nthe Great Red Spot, a persistent storm larger than Earth.")
        print()
        return askq()
    elif prompt in q21:
        print("The estimated population of Earth is currently around 7.9 billion people. However, please note that population figures are continually changing due to factors such as births, deaths, and migration. For the most current population estimate, you may want to refer to reliable sources such as the United Nations or the World Bank.")
        print()
        return askq()
    elif prompt in q22:
        print("The world's largest island is Greenland, known for its vast ice sheet and stunning landscapes. Covering approximately 2.2 million square \nkilometers, it's larger than any other island on Earth.")
        print()
        return askq()
    elif prompt in q23:
        print("The highest waterfall in the world is Angel Falls in Venezuela, plunging an impressive 979 meters (3,212 feet). It's a breathtaking natural wonder \nnestled within the lush landscape of Canaima National Park.")
        print()
        return askq()
    elif prompt in q24:
        print("The Mariana Trench in the western Pacific Ocean is the deepest ocean trench, reaching a staggering depth of about 11,034 meters (36,201 feet) at \nits lowest point, known as the Challenger Deep.")
        print()
        return askq()
    elif prompt in q25:
        print("The Sahara Desert is the largest desert in the world, spanning over 9 million square kilometers across northern Africa. Its vast expanse of sand \ndunes and rocky plains makes it an iconic symbol of desert landscapes.")
        print()
        return askq()
    elif prompt in q26:
        print("The hottest place on Earth is the Lut Desert in Iran, where temperatures have been recorded as high as 70.7°C (159.3°F). This barren landscape \nexperiences extreme heat due to its low elevation and lack of vegetation.")
        print()
        return askq()
    elif prompt in q27:
        print("The blue whale holds the title for the largest animal on Earth, growing up to 30 meters (98 feet) in length and weighing as much as 200 tons. \nThese magnificent creatures roam the oceans, feeding on krill with their massive mouths.")
        print()
        return askq()
    elif prompt in q28:
        print("Queen Elizabeth II of the United Kingdom holds the record for the longest-reigning monarch in British history, surpassing more than 70 years on the throne. Her reign began on February 6, 1952, following the death of her father, King George VI.")
        print()
        return askq()
    elif prompt in q29:
        print("The cheetah is the fastest land animal, capable of sprinting at speeds up to 100 kilometers per hour (62 miles per hour) in short bursts. This \nsleek predator relies on its speed and agility to chase down prey on the African savannah.")
        print()
        return askq()
    elif prompt in q30:
        print("The giraffe is the tallest mammal on Earth, with males reaching heights of up to 5.5 meters (18 feet) and females slightly shorter. Their long \nnecks and legs allow them to browse leaves from tall trees in their African habitats.")
        print()
        return askq()
    else:
        print("Sorry, I won't be able to answer that!")
        print()
        return askq()

askq()