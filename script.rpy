#testing change

define j = Character("Jamie")
define a = Character("Alex")

label start:

    "Alex, a close MBBS peer, recently failed the summative exam. He has been avoiding your messages for two days."
    "You decide to visit Alex’s dorm room."
    scene bg dorm
    show giveaway box 
    "Jamie finds him packing a suitcase and dumping his expensive medical textbooks in a 'giveaway' box."
    hide giveaway box 
    show a sad at right 
    with fade
    "He stares at his pile of handwritten notes, and without hesitation, rips them up and throws them in the trash."
    show trash can top at left with fade
    "He takes a deep breath and sits down on his bed, looking defeated."
    hide trash can top
    show a sad with fade
    "You pop your head into his room."
    show a shocked at right 
    show jamie curious at left 
    with fade
    "Alex notices your concerned expression, and tries to downplay his situation."
    "He puts on a fake smile."
    show a happy at right
    a "Hey Jamie! Here to visit me?"
    show jamie calm at left
    with fade
    j "Yeah, I was worried about you. I haven't heard from you in a couple of days."
    a "Oh! Sorry about that!"
    show a awkward at right
    with fade
    a "I was just... busy lately."
    show a happy 
    with fade
    a "I'm just doing some cleaning out, nothing to worry!"
    show giveaway box books
    with fade
    "Alex pushes the 'giveaway' box aside."
    "You notice the textbooks in the box."
    hide giveaway box books 
    show jamie curious 
    with fade
    j "Alex, I noticed you're giving away your textbooks and packing."

label m0:
    show jamie curious at left
    show a happy at right
    menu:
        "Focus on Alex's feelings":
            show jamie worried at left
            with fade
            j "Combined with you not answering texts, I'm really worried about you. Is everything alright?"
            hide jamie worried with fade
            "Correct! This opens the door allows Alex to express his feelings and concerns. Hits the 'A' (Asking and Approaching) in ALGEE."
            jump continue
        "Focus on the price of the textbooks":
            show jamie shocked with fade
            j "Don't you know those books are really expensive? Are you sure you want to give them away? What a waste!!"
            hide jamie shocked with fade
            "Incorrect! This guilt trips Alex and triggers shame and embarrassment. It does not address the concerning behavior."
            "Try Again."
            jump m0

label continue:

    show a sad with fade
    a "There's no point anymore. I'm an embarrassment to my family."
    a "Honestly, I feel like everyone would be better off if I wasn't here."
    show jamie worried at left
    with fade
    j "I'm really concerned about you and I'm here for you. Can we talk about what's going on?"
    hide jamie worried
    show a sad
    with fade
    a "I just feel like a failure. How did I fail so badly? I studied so hard, but I just can't seem to get it right."
    a "But that's ok. Nothing will matter after tonight."
    "Alex's voice trembles as he speaks, and tears well up in his eyes."
    show a crying 
    with fade
    "You notice Alex's distress, and is concerned about the meaning of 'after tonight'."

label m1:
    show jamie worried at left
    show a crying at right
    menu:
        "Directly question Alex":
            j "When you say nothing will matter after tonight, are you thinking about suicide?"
            "Correct! Hits the 'A' (Assessing suicidal risk) in ALGEE. Asks the terrifying but necessary question directly and unambiguously."
            a "I don't have a plan or anything... I just want everything to stop."
            a "I can't face the disappointment in my parents' eyes. I just feel so trapped."
            jump m2
        "Avoid the topic":
            show jamie sweat at left
            j "Don't say that! You're a great friend and your family loves you." 
            j "You want to go grab some food and get your mind off things?"
            "Incorrect! Fails to assess Alex's suicidal risk and tries to distract the person from their distress."
            # altpath Alex withdraws further, realizing Jamie is not a safe person to share his darkest thoughts with."
            show a worried
            a "No thanks..."
            a "I really shouldn't have brought this up with you...sorry for making you worry..."
            show jamie worried
            j "(Oh no...it seems Alex doesn't feel comfortable sharing his darkest thoughts with me...)"
            j "(Maybe I should say something to make him open up again...)"
            "Try Again."
            jump m1b

label m1b:
    show a sad at right
    show jamie worried at left
    menu:
        "Reassure him":
            j "You don't have to feel sorry. You can talk to me about anything."
            "Alex's expression softens. There's something he wants to say, but he can't get the words out."
            a "To be honest, I..."
            jump m1
        "Blame him for not telling you":
            show jamie mad at left
            j "Why won't you just tell me directly? You're just making everything harder..."
            "Incorrect! Give Alex some space to process his feelings. Don't make him feel pressured."
            show a crying
            a "I'm sorry, I'm sorry...I know I'm just a burden who can't do anything right."
            hide a crying
            "Sobbing, Alex runs and slams the door behind him."
            "Try Again."
            jump m1b

label m2:
    show a sad at right
    show jamie no emotion at left
    menu:
        "I can see that you're really upset.":
            show jamie worried at left
            j "It makes sense that you feel this way after failing the exam."
            "Correct! This validates Alex's feelings and acknowledges his situation."
            jump m3
        "Be dismissive":
            show jamie happy at left
            j "Whoa, don't pack up! You can just retake the exam next semester."
            j "It's not the end of the world. Everyone fails at something."
            "Incorrect! This minimizes Alex's pain and rushes to fix the situation."
            "Try Again."
            jump m2

    label m3:
        show jamie worried at left
        show a sad at right
        menu:
            "Validate and hold space for him.":
                show jamie happy
                j "Thank you for trusting me with this. It makes complete sense that you feel trapped and overwhelmed right now given how much pressure you've been under."
                "Correct! Hits the 'L' and 'G' in ALGEE. Normalizes the emotion without agreeing with the suicidal ideation."
                show a sad
                a "I'm just so exhausted. I don't know what to do next. I feel completely empty."
                jump m4
            "Interrogate him.":
                show jamie worried
                j "Have you talked to the academic advisor yet? Maybe they can help you draft an email to your parents to explain what happened."
                "Incorrect! Jumps to logistical solutions while the person is still in an acute emotional crisis."
                "Try Again."
                jump m3

    label m4:
        show jamie calm at left
        show a sad at right
        menu:
            "Bridge to care":
                show jamie calm at left
                j "You don't have to figure it all out tonight. But because I care about you, I want to make sure you're safe."
                j "Can we call the university 24-hour support line together right now?"
                show a relaxed
                "Correct! Hits the 'E' in ALGEE. Shares the burden and actively facilitates the hand-off to professional care."
                "===SIMULATION SUCCESS!==="
            "Take sole responsibility":
                show jamie sweat
                j "Okay, just promise me you won't do anything tonight. Try to get some sleep and I will come check on you first thing in the morning."
                "Incorrect. The first aider takes on the full burden of keeping the person safe without looping in professionals. This is dangerous for both parties."
                "Try Again."
                jump m4

    return

# a emotions: shocked, sad, mad, crying, happy
# j emotions: calm, worried, sweat, mad