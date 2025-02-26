
dictionary_1678 = {
	"rookie year" : 2005,
	"location" : "Davis, California, USA",
	"compete in 2019" : True,
	"competitions and locations" : "Central Valley Regional: Fresno, Ca, USA; Sacramento Reagional: Sacramento, CA, USA; Aerospace Valley Regional: Lancaster, CA, USA; Carver Division: Houston, TX, USA; Einstein Field: Houston, TX, USA.",
	"awards" : "CHAIRMAN'S AWARD, CENTRAL VALLEY REGIONAL WINNER, SACRAMENTO REGIONAL WINNER, AEROSPACE VALLEY REGIONAL WINNER",
}

dictionary_1682 = {
	"rookie year" : 2005,
	"location" : "Riverside, California, USA",
	"compete in 2019" : False,
	"competitions" : "None",
	"competitions and locations" : "None",
	"awards" : "None"
}

dictionary_1690 = {
	"rookie year" : 2005,
	"location" : "Binyamina, HaZafon, Israel",
	"competions and locations" : "ISR District Event #1: Haifa, HA 00000, Israel; ISR District Event #4: Tel Aviv-Yafo, TA 00000, Israel; FIRST Israel District Championship: Tel Aviv-Yafo, TA 00000, Israel; Darwin Division: Detroit, MI, USA; Indiana Robotics Invitational: Indianapolis, IN, USA;",
	"awards" : "None"
}

dictionary_1700 = {
	"rookie year" : 2005,
	"location" : "Palo Alto, California, USA",
	"compete in 2019" : True,
	"competitions and locations" : "San Francisco Regionals: San Francisco, CA, USA; Utah Regionals: West Valley City, Utah, USA; Turing Devision: Houston, TX, USA",
	"awards" : "None"
}

dictionary_2907 = {
	"rookie year" : 2009,
	"location" : "Auburn, Washington, USA",
	"compete in 2019" : True,
	"competitions and locations" : "PNW District Auburn Mountainview Event: Auburn, WA, USA; NW District West Valley Event: Spokane, WA, USA; PNW District Auburn Event: Auburn, WA, USA; Pacific Northwest FIRST District Championship: Tacoma, WA, USA; Roebling Division: Houston, TX, USA; Einstein Field: Houston, TX, USA; Peak Performance: Sea Tac, WA, USA;",
	"awards" : "2019 PACIFIC NORTHWEST FIRST DISTRICT CHAMPIONSHIP, 2019 ROEBLING DIVISION",
}

dictionary_3132 = {
	"rookie year" : 2010,
	"location" : "Sydney, New South Wales, Australia",
	"compete in 2019" : True,
	"competitions and locations" : "Southern Cross Regional: Sydney Olympic Park, NSW, Australia; NSouth Pacific Regional: Sydney Olympic Park, NSW, Australia; Carver Division: Houston, TX, USA; Einstein Field: Houston, TX, USA; Duel Down Under: Sydney, New South Wales, Australia;",
	"awards" : "2019 SOUTHERN CROSS REGIONAL, 2019 CARVER DIVISION",
}

teams = {
	1678 : dictionary_1678,
	1682 : dictionary_1682,
	1690 : dictionary_1690,
	1700 : dictionary_1700,
	2907 : dictionary_2907,
	3132 : dictionary_3132,
}

def team_info():
	question1 = int(input("What team would you like to look up? options: 1678, 1682, 1690, 1700, 2907, 3132"))
	question2 = input("What about the team would you like to know? options: rookie year, locations, competitions and locations, awards ")
	print(teams[question1][question2])

team_info()