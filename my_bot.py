import random

b_list = ["My gran could do better! And she’s dead!",

"For what we are about to eat, may the Lord make us truly not vomit",

"You’re getting your knickers in a twist! Calm down!",

"This lamb is so undercooked, it’s following Mary to school!",

"This pizza is so disgusting, if you take it to Italy you’ll get arrested",

"There’s enough garlic in here to kill every vampire in Europe",

"This isn’t a pizza, this is a mistake This is an Italian tragedy",

"Why did the chicken cross the road? Because you didn’t f—ing cook it!",

"You put so much ginger in this, it’s a Weasley",

"The problem with Yanks is they are wimps",

"Don't just stand there like a big f—ing muffin!",

"I wouldn’t trust you running a bath let alone a restaurant",

"This fish is so raw, he’s still finding Nemo",

"You added so much salt and pepper I can hear the dish singing ‘Push It’",

"The minute you start compromising for the sake of massaging somebody’s ego, that’s it, game over",

"You are a nutter your self-obsessed, delicate, dainty, insecure little soul, and an absolute psychopath",

"Hey, panini head, are you even listening to me?",

"I’ll get you more pumpkin, I’ll ram it right up your a—",

"Get your s— together!",

"You used so much oil, the US want to invade the f—ing plate",

"You’ve got to kiss arse to get somewhere, to learn Clock-watchers are no good at kissing arse",

"I’ve got nothing to hide",

"I get frustrated and f— off and wound up with idiots quickly, so I get straight to the point Cut the bullsh— That’s healthy",

"My industry, I’m sorry to say, is full of muppets",

"This crab is so undercooked I can still hear it singing ‘Under the Sea!’",

"This soufflé has sunk so badly James Cameron wants to make a film about it",

"There’s enough garlic in here to kill every vampire in Europe",

"I've never, ever, ever, ever, ever met someone I believe in as little as you",

"Why did the chicken cross the road? Because you didn’t f—ing cook it!",

"I’ve been on my arse before, but I have a lot of determination, and I’m not weak",

"Honestly, chimichanga… Chimi-chuck it in the bin!"]

a_list = [
"If I can give you one strong piece of advice, when you go away for that romantic weekend, whatever you do, do not accept or take the upgrade to the honeymoon suite",

"If I relaxed, if I took my foot off the gas, I would probably die",

"I train my chefs completely different to anyone else My young girls and guys, when they come to the kitchen, the first thing they get is a blindfold They get blindfolded and they get sat down at the chef’s table… Unless they can identify what they’re tasting, they don’t get to cook it",

"Stop taking things personally",

 "I’d like to think I’m a great teacher",

 "I am what I am A fighter",

 "If you want to become a great chef, you have to work with great chefs And that's exactly what I did",

 "I don’t like looking back I’m always constantly looking forward I’m not the one to sort of sit and cry over spilt milk I’m too busy looking for the next cow",

 "Initially, let your food do the talking You’ll be surprised how far you go in a short period of time",

 "The minute you start compromising for the sake of massaging somebody’s ego, that’s it, game over",

 "Cooking is about passion, so it may look slightly temperamental in a way that it’s too assertive to the naked eye",

 "Chefs are nutters They’re all self-obsessed, delicate, dainty, insecure little souls, and absolute psychopaths Every last one of them",

 "I act on impulse and I go with my instincts",

 "I think pressure’s healthy, and very few can handle it",

 "You don’t come into cooking to get rich",

 "Hey, panini head, are you even listening to me?",

 "I’m Gordon Ramsay, for goodness sake; people know I’m volatile",

 "Swearing is industry language For as long as we’re alive, it’s not going to change You’ve got to be boisterous to get results",

 "I swim like a fish, and I have an amazing kick",

 "I cook, I create, I'm incredibly excited by what I do, I've still got a lot to achieve",

"As a soccer player, I wanted an FA Cup winner's medal As an actor you want an Oscar As a chef it's three-Michelin's stars, there's no greater than that So pushing yourself to the extreme creates a lot of pressure and a lot of excitement, and more importantly, it shows on the plate",

 "The pressure on young chefs today is far greater than ever before in terms of social skills, marketing skills, cooking skills, personality and, more importantly, delivering on the plate So you need to be strong Physically fit So my chefs get weighed every time they come into the kitchen",

 "I've had a lot of success; I've had failures, so I learn from the failure",

 "You’ve got to kiss arse to get somewhere, to learn Clock-watchers are no good at kissing arse",

 "I suppose your security is your success and your key to success is your fine palate",

 "Kitchens are hard environments and they form incredibly strong characters",

 "Loo doors without a decent, large hook are as infuriating as a lock that doesn’t offer you full protection",

 "When you cook under pressure you trade perfection",

 "I shoot from the hip",

 "It's very hard when you eat out every day for a living, and a new restaurant comes along and you haven't got that same vigour that you had  years ago",

 "There is a level of snobbery and fickleness in LA",

 "I am a grafter",

 "I’ve got nothing to hide",

 "They say cats have nine lives I've had  already and I don't know how many more I'll have",

 "Running started as a way of relaxing It's the only time I have to myself No phones or emails or faxes",

 "I'd like to think I'm a great teacher",

 "I want my kids to see me as Dad, for God's sake, not a television personality",

 "I'm not critic-proof, and I still take it personally, but I take it less personally now",

 "It's vulgar, coming from where I do, to talk about money",

 "I'm not trying to take New York by storm I just want to sneak in there, keep my head down, batten down the hatches and cook",

 "I am the most unselfish chef in Britain today",

 "I act on impulse and I go with my instincts",

 "There's a bond among a kitchen staff, I think You spend more time with your chef in the kitchen than you do with your own family",

 "I don't run restaurants that are out of control We are about establishing phenomenal footholdings with talent",

 "My wife, a schoolteacher, very disciplined If you think I'm tough, trust me, and wait till you see when the children are on the naughty step It's hilarious So we decided that I'm going to work like a donkey and provide amazing support for the family",

 "I still love football, though, and I think cooking is like football It's not a job, it's a passion When you become good at it, it's a dream job and financially you need never to worry Ever",

 "When you're a chef, you graze You never get a chance to sit down and eat They don't actually sit down and eat before you cook So when I finish work, the first thing I'll do, and especially when I'm in New York, I'll go for a run And I'll run  or k on my — and I run to gain my appetite",

 "I am a chef who happens to appear on the telly, that's it",

 "Would I swap what I have achieved as a cook if I could have been as successful as a footballer? Definitely",

 "I won't let people write anything they want to about me",

 "I mean, families are weird",

 "I grew up in a funny way",

 "When I get angry, I’m just being honest, and I don’t think it’s ever going to be any different I, like any good chef, want everything to be perfect",

 "I get frustrated and f— off and wound up with idiots quickly, so I get straight to the point Cut the bullsh— That’s healthy",

 "I can spot within the first  minutes of a young chef in the kitchen whether they’re passionate Cooking with their eyes, their left- and right-hand side, their posture, holding the knife, excitement and developing the palate",

 "What I’ve instilled in the kids, from day one, is a work ethic So, the time we spend together is limited, but it’s quality",

 "My industry, I’m sorry to say, is full of muppets",

 "I’ve never been one for pondering or questioning and thinking Waste of time Dust yourself down and get back up",

 "One lesson to any young chef out there: never mix family with business",

 "If one of my daughters’ boyfriends asked me for a pint in a couple years’ time and said, ‘Hey Mr Ramsay, I’m thinking of setting up this burger chain Would you be interested in investing?’    You can f— right, off With a capital F! And two capital Fs at the end!",

 "That level of frustration is healthy If you don’t give a f— and you’re not cautious about what you’ve just delivered, that tells you a lot about where you’re going to go in this industry, big time",

 "Put your head down and work hard Never wait for things to happen, make them happen for yourself through hard graft and not giving up",

 "Anyone can open a restaurant You just need a dinner party where everyone’s pissed and someone says, ‘Hey Tom, you should open a restaurant, this food’s delicious’",

 "[The kids] don’t sit with us in first class They haven’t worked anywhere near hard enough to afford that At that age, at that size, you’re telling me they need to sit in first class? No, they do not We’re really strict on that",

 "This soufflé has sunk so badly James Cameron wants to make a film about it",

 "My mum doesn’t enjoy sometimes listening to me tell staff off, and I say to my mum, it’s a kitchen, not a hair-dressing salon",

 "That journey of coming back to the very top is better than actually being at the top You find out so much about yourself and who your friends are",

 "Eating out doesn’t have to be a formula Eating out is about having fun I get really frustrated when it’s badly done",

 "I spend more time in the kitchen than I have in the dining room, for obvious reasons, however, I just want to sit and indulge",

 "Triathlons saved my life That put things in perspective in a way I could claw back, valuable, independent time that took me away from the hustle of running production companies to major networks, to the pressure of the Michelin Guide I found that balance and that release, and that’s really important",

 "All four of the children have grown up with that respect, and that, hey, if you want something in your life, you work hard for it",

 "What’s frustrating more than anything is when chefs start to cut corners and believe that they are incognito in the way they send out appetizers, entrees, and they know it’s not  percent, but they think the customers can’t spot it",

 "We had four young kids at one stage, and you have to get them involved with more of the prep as opposed to the cooking Sooner or later, they’re gonna have to use a knife They’re gonna learn how to chop And there are great, cheap kid’s knives that they can use and prep with",

 "The busier I got, the fitter I got I think it’s the same in science, in the way that you need to be disciplined to take that time out, spend  minutes every other day processing what you got and what you’re doing I think a lot of the bike, I think a lot on a swim, I think a lot on the run and that’s really good, important time for me",

 "On the personal front, obviously, you know, this industry fragments a lot of families If there’s one thing I’ve learned with my children, teaching them how to cook early on in life has brought them closer to my industry So if they’re gonna follow it as a career, they know how to cook",

 "Best to start at the bottom and gradually climb up It’s much more fun, too",

 "Being assertive and somewhat really firm has to be backed up with being fair",

 "I’ve been on my arse before, but I have a lot of determination, and I’m not weak"]

def should_i_respond(user_message, user_name):
  return True
def check_in(letter_list, user_message):
  return all(letter in user_message for letter in letter_list) 
def check_four_letter_words(user_message):
  word_list = user_message.split(" ")
  print(user_message)
  for word in word_list:
    print(word)
    if len(word.lower()) == 4:         
      if check_in(["f","c","u","k"], word.lower()):
        return True
  return False
def respond(user_message, user_name):
  if check_four_letter_words(user_message):
    random.shuffle(b_list)
    bnsult = random.choice(b_list)
    return bnsult
  else:
    random.shuffle(a_list)
    ansult = random.choice(a_list)
    return ansult