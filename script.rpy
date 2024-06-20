
define s = Character("Max")
define n = Character (None)

image mc_nobg_s_scaled = im.Scale("mc_nobg_s.png",1000,1300)
image max_gloomy_scaled = im.Scale("max_gloomy.png",900,800)
#image background_school = im.Scale("background_school.png",1280,720)

transform pop_up_upper:
    xpos 350
    ypos 25

transform max_gloomy_foto:
    xpos 550
    ypos 25


label start:
    scene kelas_bg with fade
    play music "Audio/Music/music_bg.mp3"
    n "Welcome to the wonderfully chaotic world of Max’s, where every step is a new opportunity for disaster! Meet Max, an ordinary student living a far-from-ordinary life."
    n "Before you meet our lovable hero, remember this carefully: \"Milo Murphy's Law says anything that can go wrong, will go wrong—and with him, it definitely will!\""
    n "Please help poor Max make it home in one piece, Let’s go!"
    show mc_nobg_s_scaled at center with dissolve
    n "Meet Max. A good kid with a knack for tripping over his own feet and a magnet for minor mishaps. Today, he's about to embark on the perilous journey from school to home—a task that, for Max, is anything but simple."
    s "Alright, time to make my way home. What could possibly go wrong?"
   
    hide mc_nobg_s_scaled with dissolve
    #  hide background_school
    menu:
        
        "Go through basement gate":
            jump basement_gate

        "Go through front gate":
            jump front_gate

label basement_gate:
    scene pintu_blkng_sklh with dissolve
    show mc_nobg_s_scaled at center with dissolve 
    n "Max decides to take a shortcut through the basement gate."

    n "As he steps into the dimly lit basement, Max's adventurous spirit kicks in."
    
    hide mc_nobg_s_scaled with dissolve

    menu:
        "You brought Motorbike to school":
            jump motorbike_basement

        "You brought Car to school":
            jump car_basement

        "You book a car from app":
            jump app_car_basement

label motorbike_basement:
    show max_naik_motor at pop_up_upper with dissolve
    n "Max hops onto his trusty motorbike."
    play sound "audio/Sound/motor_rev.mp3"
    n "He revs up the engine and sets off towards home."
    hide max_naik_motor with dissolve

    menu:
        "Took the usual way home":
            jump usual_way_home

        "Took a new way to get home":
            jump new_way_home

label car_basement:
    show mobil_max at pop_up_upper with dissolve
    n "Max jumps into his car parked in the basement."
    play sound "audio/Sound/mobil_rev.mp3"
    n "He puts on his seatbelt and starts the engine."
    hide mobil_max with dissolve
    menu:
        "Took the highway":
            jump highway_car

        "Took the toll":
            jump toll_car

label app_car_basement:
    n "Max decides to book a car using a ride-sharing app."
    n "He checks his phone for available drivers."

    menu:
        "Go to mall":
            jump mall_car

        "Go straight home":
            jump straight_home_car

label front_gate:
    scene pintu_depan_sklh with fade
    show mc_nobg_s_scaled with dissolve
    n "Max heads out through the front gate of the school."
    n "He surveys the bustling street outside, contemplating his next move."
    hide mc_nobg_s_scaled with dissolve
    menu:
        "You book a motorbike from app":
            jump app_motorbike_front_gate

        "You want to take public transportation":
            jump public_transportation_front_gate

label app_motorbike_front_gate:
    hide mc_nobg_s_scaled with dissolve
    show motor grab at pop_up_upper with dissolve
    n "Max decides to book a motorbike using a ride-sharing app."
    n "He waits for the motorbike to arrive, eager to get home."
    n "A few minutes later, the Grab motorbike driver arrives and Max gets on the bike."
    scene highway
    play sound "Audio/Sound/highway.mp3"
    show motor_grab_max at pop_up_upper with dissolve
    n "As they navigate through the busy streets, Max enjoys the cool breeze and the speed of the ride."

    jump straight_home_motorbike

label public_transportation_front_gate:
    n "Max opts for public transportation to get home."
    n "Max ponders which public transportation to take."

    menu:
        "Bus":
            jump bus_public_transportation

        "Train":
            jump train_public_transportation

label usual_way_home:
    play sound "Audio/Sound/highway.mp3"
    scene highway with fade
    n "Max takes his usual route home, navigating the familiar streets with ease."
    scene home with fade
    show mc_nobg_s_scaled with dissolve
    n "He arrives home safely, another day's adventure behind him."

    return

label new_way_home:
    scene jln nyasar with fade
    play sound "Audio/Sound/rain.mp3"
    n "Max decides to take a different route home, hoping for a change of scenery."
    show max_gloomy_scaled at max_gloomy_foto with dissolve

    n "However, he quickly realizes he's lost and spends hours wandering aimlessly."

    return

label highway_car:
    play sound "Audio/Sound/highway.mp3"
    scene highway with fade
    n "Max chooses the highway, hoping for a speedy journey home."
    scene protes with fade
    n "But he gets stuck in a traffic jam caused by a protest, his frustration mounting by the minute."

    return

label toll_car:
    scene jalan tol with fade
    play sound "Audio/Sound/highway.mp3"
    n "Max opts for the toll road, expecting a smooth ride home."

    n "To his relief, the road is clear and he makes it home in record time."

    return

label mall_car:
    scene mall with fade
    show mobil_max_grab at pop_up_upper with dissolve

    n "Max decides to make a pit stop at the mall before heading home."

    n "He wanders around, browsing through shops and treating himself to a little retail therapy."
    hide mobil_max_grab with dissolve
    menu:
        "Bought something":
            jump bought_something

        "Play around":
            jump play_around

label straight_home_car:
    scene home with fade
    show mc_nobg_s_scaled with dissolve
    n "Max chooses to head straight home, eager to relax after a long day at school."

    return

label straight_home_motorbike:
    scene home with fade
    show mc_nobg_s_scaled with dissolve
    n "Max heads straight home on the motorbike, the wind rushing past him as he speeds along the familiar streets."

    n "He arrives home feeling exhilarated, another adventure conquered."

    return

label bus_public_transportation:
    play sound "Audio/Sound/bus.mp3"
    scene bus stop with fade
    n "Max boards the bus, settling into a seat as it sets off towards his neighborhood."
    n "He stays awake, keeping an eye on the passing scenery as the bus makes its way through the city streets."

    menu:
        "Stay awake":
            jump stay_awake

        "Fall asleep":
            jump fall_asleep

label train_public_transportation:
    scene stasiun kereta_kereta with fade
    play sound "Audio/Sound/kereta.mp3"
    n "Max squeezes onto the crowded train, the rush hour crowd pressing in around him."
    scene rush hour with fade
    n "He struggles to keep his balance as the train lurches forward, the crush of bodies making it hard to breathe."

    return

label bought_something:
    scene bought item with fade
    n "Max indulges in a bit of retail therapy, picking up a few items before remembering he still needs to get home."

    n "He quickly books a car using his ride-sharing app, eager to finally relax in the comfort of his own home."

    return

label play_around:
    scene bought item with fade
    n "Max gets distracted by the attractions at the mall, losing track of time as he enjoys the various activities."

    n "By the time he remembers he needs to head home, it's already late and he's too tired to do anything but catch a ride straight there."

    return

label stay_awake:
    n "Max manages to stay awake for the entire bus journey, keeping himself entertained by people-watching and listening to music."
    scene home with fade
    show mc_nobg_s_scaled with dissolve
    n "He gets off at the right stop, and got home,feeling proud of himself for staying focused."

    return

label fall_asleep:
    scene jln nyasar with fade
    show max_gloomy_scaled at max_gloomy_foto with dissolve
    play sound "Audio/Sound/rain.mp3"
    n "Max can't fight off his exhaustion and ends up dozing off on the bus."
    n "He wakes up to find himself at the end of the line, far from his intended destination."

    return
