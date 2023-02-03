# this contains all of the information of the wedding
import re
from django.http import HttpResponse

class CocktailHour:
    def __init__(self, cocktail_photos, cocktail_drinks, activities, cocktail_music):
        self.cocktail_photos = cocktail_photos
        self.cocktail_drinks = cocktail_drinks
        self.activities = activities
        self.cocktail_music = cocktail_music

cocktail_photos = "Then family photos with Ana and Jacobie, followed by private photos and vows."
cocktail_drinks = "There will be a self-served bar with beer, wine, 'fake-wine', champagne, bottled water, coffee, Coke, Sprite, Diet Ginger Ale, and sparkling water"
activities = ""
cocktail_music = "Jazz and RnB classics"
cocktail_hour_info = CocktailHour(cocktail_photos, cocktail_drinks, activities,cocktail_music)



class WeddingPrep():
    def __init__(self,ana_ring, cobie_ring,rings, venue, decorations, guestbook, wedding_gifts, kitty_sitter, registry, invitations, marriage_license, guest_attire, our_attire):
        self.ana_ring = ana_ring
        self.cobie_ring = cobie_ring
        self.rings = rings
        self.venue = venue
        self.decoraitons = decorations
        self.guestbook = guestbook
        self.wedding_gifts = wedding_gifts
        self.kitty_sitter = kitty_sitter
        self.registry = registry
        self.invitations = invitations
        self.marriage_license = marriage_license
        self.guest_attire = guest_attire
        self.our_attire=our_attire


ana_ring = "Test"
cobie_ring = "Cobie's ring is: Vera Wang Three Stone Ring"
rings = ana_ring + "\n" + cobie_ring
venue = "It it located at "
decorations = "For the decorations, we will be using outside string lights and other decorations from Ana's mom."
guestbook = "The guestbook is a Vinyl record for our guests to sign"
wedding_gifts = "The weddings gifts will be put in the gift station. We will also have a card box."
kitty_sitter = "To feed the cats, we will pay Jerrod to visit every other day, then get Leye to watch them when we go on the honeymoon."
registry = "List of items with linnks"
ana_list = ""
cobie_list = ""
invitations = cobie_list + ana_list
marriage_license = "Ana's Uncle is an officiant and has a marriage license."
guest_attire = "Black and silver, semi-formal or cocktail. Please no light or bright colors."
our_attire = "Ana is wearing a white wedding dress and Jacobie will be wearing a tuxedo."

weddingprep = WeddingPrep(ana_ring,cobie_ring,rings,venue,decorations,guestbook,wedding_gifts,kitty_sitter,registry,invitations,marriage_license, guest_attire,our_attire)

class WeddingDaySchedule():
    def __init__(self, saturday_breakfast,saturday_arrival,saturday_prep,getting_ready,cocktail_time,ceremony_start,reception_start):
        self.saturday_breakfast = saturday_breakfast
        self.saturday_arrival = saturday_arrival
        self.saturday_prep= saturday_prep
        self.getting_ready=getting_ready
        self.ceremony_start=ceremony_start
        self.reception_start=reception_start
        self.cocktail_time=cocktail_time

saturday_breakfast= "Breakfast is by yourself"
saturday_arrival="Everyone should arrive before 5:00pm EST."
saturday_prep="We will put out drinks and snacks at arund 4:00pm EST"
getting_ready='Ana will start getting ready at 1:00pm EST'
ceremony_start='The ceremony starts at 6:00pm EST'
reception_start='The reception starts at 7:00pm EST'
cocktail_time = "When the guests arrive and after the ceremony."
weddingdayschedule = WeddingDaySchedule(saturday_breakfast,saturday_arrival,saturday_prep,getting_ready,cocktail_time,ceremony_start,reception_start)

class FridaySchedule():
    def __init__(self, friday_prep, friday_dinner):
        self.friday_prep = friday_prep
        self.friday_dinner = friday_dinner
friday_prep = "We will finish the last minute preping throughout the day on Friday"
friday_dinner = "Dinner will start at 6:00pm EST and will be at Boundary House"

fridayschedule = FridaySchedule(friday_prep,friday_dinner)

class Reception():
    def __init__ (self, reception_food,reception_drinks,reception_speeches,reception_activities,reception_music):
        self.reception_food = reception_food
        self.reception_drinks = reception_drinks
        self.reception_speeches = reception_speeches
        self.reception_activities = reception_activities
        self.reception_music = reception_music

reception_food='There will be steak, breadcrumb chicken breast, baked beans, cole slaw, mac n cheese, rice, baked rolls, buttered corn, and roasted veggies. '
reception_drinks="There will be a self-served bar with beer, wine, 'fake-wine', champagne, bottled water, coffee, Coke, Sprite, Diet Ginger Ale, and sparkling water"
reception_speeches="We might not do any speeches but guests are welcome to"
reception_activities="Toasts from parents"
reception_music="The music will be upbeat songs, keeping the energy flowing and people awake"
reception_list = Reception(reception_food,reception_drinks,reception_speeches,reception_activities,reception_music)




class Honeymoon():
    def __init__ (self, honeymoon_location, honeymoon_transportation, honeymoon_duration, honeymoon_activities):
        self.honeymoon_location=honeymoon_location
        self.honeymoon_transportation=honeymoon_transportation
        self.honeymoon_duration=honeymoon_duration
        self.honeymoon_activities=honeymoon_activities

honeymoon_location = "We will be going to the Dominican Republic at in all inclusive resort"       
honeymoon_duration = "We will bbe there for 8 days"        
honeymoon_activities = "We will relax on the beach, visit the spa, pools, shops, live enteraintment, and stuff that we usually don't do."        
honeymoon_transportation = "We will be getting there through plane"     

honeymoon_list = Honeymoon(honeymoon_location,honeymoon_transportation,honeymoon_duration,honeymoon_activities)

class Vendors():
    def __init__ (self, baker, photographer, caterer, florist):
        self.baker = baker
        self.photographer =photographer
        self.caterer = caterer
        self.florist = florist

baker = "The baker is: Spilt Milk"
photographer ="The photographer is: Ana's dad's cousin"
caterer = "The caterer is: Art Catering"
florists = ""

venodor_list = Vendors(baker,photographer,caterer,florists)


class Budget():
    def __init__ (self, vendor_budget, attire_budget, wedding_prep_budget, drinks_snacks_budget, honeymoon_budget, wedding_ring_budget):
        self.vendor_budget = vendor_budget
        self.attire_bubdget = attire_budget
        self.wedding_prep_budget = wedding_prep_budget
        self.drinks_snacks_budget=drinks_snacks_budget
        self.honeymoon_budget = honeymoon_budget
        self.wedding_ring_budget = wedding_ring_budget

photographer_budget = 0
baker_budget = 0
caterer_budget = 0
vendor_budget= caterer_budget + baker_budget + photographer_budget
attire_budget = 0
wedding_prep_budget =300
drinks_snacks_budget = 200
honeymoon_budget = 3000
wedding_ring_budget = 3000

total_budget = Budget(vendor_budget,attire_budget,wedding_prep_budget,drinks_snacks_budget,honeymoon_budget,wedding_ring_budget)

closing_statement = " \n" + "We will see you soon. Have a great day :) \n" + "\n"

wedding_ettiquette = "Guests are responsible for travel and lodging (optional). \n" +\
    "Parking will be available on the street and you may need to walk to the venue. \n" +\
        "Please keep cellphones off and put away for the entire wedding. " +\
        "We have a photographer and we don't want any cellphone photos. \n" +\
            "We will not be doing some traditional wedding activities like first dances, a dance party, a send off, etc. " +\
                 "This will be a classy evening event and we encourage you to eat, drink, and have a good time."

adddd = " \n"
addon = " \n" + "What else would you like to know? "

def get_responses(message):
    p_message = message.lower()
    if re.search(r"location|venue|where is it|where is the wedding|where is it|where's the location|where's the wedding|address", p_message):
        response_text = weddingprep.venue
        return response_text + adddd + addon
    elif re.search(r"catering|dinner|what to eat|what we eat|what do we eat|menu", p_message):
        response_text = reception_list.reception_food
        return response_text + adddd + addon
            
    elif re.search(r"etiquette|rules|parking|theme|activities|first dance|phone", p_message):
        response_text = wedding_ettiquette
        return response_text + adddd + addon

    elif re.search(r"what are we doing", p_message):
        response_text = "Besides the ceremony and reception, " + reception_list.reception_activities
        return response_text + adddd + addon

    elif re.search(r"invited|invitation|bring more people|extra people|another person|invite|plus one|extra person|invite", p_message):
        response_text = "This wedding is invite only! "
        return response_text + adddd + addon


    elif re.search(r"honeymoon",p_message):
        response_text = honeymoon_list.honeymoon_location + "\n" + honeymoon_list.honeymoon_duration + "\n" + honeymoon_list.honeymoon_activities + "\n" + honeymoon_list.honeymoon_transportation
        return response_text + adddd + addon



    elif re.search(r"baker",p_message):
        response_text = venodor_list.baker
        return response_text + adddd + addon


    elif re.search(r"lodging|where to stay|where to book|airbnb|hotel|park|the area|fun things to do|gas|groceries|what to do|travel|where to go|get food",p_message):
        response_text = "Here's some information regarding options for lodging, activities in the area, parking, \n" +\
        "and everything you need to know about Ocean Isle Beach: \n" +\
            "\n" +\
            "https://www.ananewberry.com/lodging-guide"
        return response_text + adddd + addon


    elif re.search(r"donation",p_message):
        response_text = "If you would like to make a donation to our honeymoon fund, you can bring cash in a sealed envelope " +\
         "and deposit it in our Gift Station Box at the wedding. Paypal donations can be made to ana.n.talent@gmail.com"
        return response_text + adddd + addon



    elif re.search(r"cake",p_message):
        response_text = "The cake will be from Spilt Milk. It is a traditional chocolate wedding cake. We will also have an orea ice-cream groom's cake"
        return response_text + adddd + addon

    elif re.search(r"guest arrival|what time is it|when should we arrive|what time do we arrive|when should we get there|when should i arrive|when should i get there|when is it|when is the wedding|when wedding|date|time",p_message):
        resssssponse = "The latest arrival should be on Saturday, June 3rd at 5pm EST"
        response_text = resssssponse
        return response_text + adddd + addon

    elif re.search(r"drink|beverages|reception drinks|to drink", p_message):
        response_text = reception_list.reception_drinks
        return response_text + adddd + addon

    elif re.search(r"reception start|reception time|dinner time|time is reception",p_message):
        response_text = weddingdayschedule.reception_start
        return response_text + adddd + addon



    elif re.search(r"ceremony start|ceremony time|wedding time",p_message):
        response_text = weddingdayschedule.ceremony_start
        return response_text + adddd + addon

    elif re.search(r"attire|guest attire|what do we wear|dress code|what do i wear|what should i wear|what should we wear|color scheme", p_message):
        response_text = weddingprep.guest_attire
        return response_text + adddd + addon

    elif re.search(r"gift",p_message):
        response_text =  "Feel free to ship items directly to us (address below) or ship it to your home to wrap and bring it to the wedding.  \n" +\
        " \n" +\
            "124 Heritage Creek Way, Greensboro NC"
        return response_text + adddd + addon

    elif re.search(r"registry",p_message):
        response_text =  "You can checkout our registry here:  \n" +\
            " \n" +\
            "https://www.amazon.com/wedding/share/jacobieandana \n" +\
                " \n" +\
                    "Please be sure to mark “Purchased” on any item you buy, so we do not end up with repeats."
        return response_text + adddd + addon


    elif re.search(r"ring",p_message):
        response_text = weddingprep.wedding_gifts
        return response_text + adddd + addon

    elif re.search(r"budget",p_message):
        response_text = " \n" +\
            "The total vender cost is: " + str(total_budget.vendor_budget) +\
                    " \n" +\
                "The attire budget is: " + str(total_budget.attire_bubdget) +\
                    " \n" +\
                "The drinks/snacks budget is: " + str(total_budget.drinks_snacks_budget) +\
                    " \n" +\
                "The honeymoon budget is: " + str(total_budget.honeymoon_budget) +\
                    " \n" +\
                "The wedding ring budget is: " + str(total_budget.wedding_ring_budget) +\
                    " \n" +\
                "The wedding prep budget is: " + str(total_budget.wedding_prep_budget)
        return response_text + adddd + addon


    elif re.search(r"wedding photos|group photos|photo time",p_message):
        response_text = cocktail_hour_info.cocktail_photos
        return response_text + adddd + addon

    elif re.search(r"rsvp",p_message):
        response_text = "To RSVP, send a text to saying: \n" +\
            " \n" +\
            '"Hey this is (your first name and last name). \n' +\
                 'I am confirming my RSVP for (first name and last name of each person)."'
        return response_text + adddd + addon

    elif re.search(r"cocktail hour time|when is cocktail|what time is cocktail|what time cocktail",p_message):
        response_text = weddingdayschedule.cocktail_time
        return response_text + adddd + addon

    elif re.search(r"what is ana wearing|what is jacobie wearing|bride attire|bride dress|bride and groom attire|groom attire", p_message):
        response_text = weddingprep.our_attire
        return response_text + adddd + addon

    elif re.search(r"schedule", p_message):
        response_text = "5pm: Guest Arrival \n" +\
        "5pm-6pm: Outdoor Cocktail Hour\n" +\
        "6pm: Ceremony\n" +\
        "6:15pm: Ana & Jacobie IMMEDIATE family photos\n" +\
        "6:15pm: All guests return to cocktail hour\n" +\
        "7pm: Buffet dinner\n" +\
        "8pm: Cake cutting \n" +\
        "9pm-10pm: Guests may enjoy the party and exit at their leisure"
        return response_text + adddd + addon

    elif re.search(r'full schedule',p_message):
        response_text = "Here's the full schedule of everything: \n" +\
        " \n"    +\
            "Friday's schedule: \n" +\
            " \n"    +\
            fridayschedule.friday_prep + "\n" +\
            fridayschedule.friday_dinner + "\n" +\
            " \n"    +\
            "Saturday's schedule: \n" +\
            " \n"    +\
            weddingdayschedule.saturday_breakfast + "\n" +\
            weddingdayschedule.getting_ready + "\n" +\
            weddingdayschedule.saturday_prep + "\n" +\
            weddingdayschedule.saturday_arrival + "\n" +\
            weddingdayschedule.ceremony_start + "\n" +\
            cocktail_hour_info.cocktail_photos + "\n" +\
            cocktail_hour_info.cocktail_drinks + "\n" +\
            cocktail_hour_info.activities + "\n" +\
            weddingdayschedule.reception_start + "\n" +\
            reception_list.reception_food + "\n" +\
            reception_list.reception_drinks + "\n" +\
            reception_list.reception_speeches + "\n" +\
            reception_list.reception_music
        return response_text + adddd + addon

    else:
        response_text = "I'm not sure I understood... re-type a response please: "
        return response_text
