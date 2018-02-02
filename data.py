## categories of words (dictionaries or associative arrays)
## TODO
## you cannot use or for strings, find another better way to combine the similar words
Date = {"aaj":[0,"day"], "kal":[1,"day"], "parson":[2,"day"], "narson":[3,"day"], "dashak":[10,"year"], 
		"tarikh":[0,0], "mahine":[0,"months"], "mahina":[0,"months"], "hafte":[0,"week"], "hafta":[0, "week"], 
		"din":[0,"day"], "divas":[0,"day"], "dino":[0,"day"], "saal":0, "varsh":0, "monday":["MO","weekday"], 
		"tuesday":["TU","weekday"], "wednesday":["WE","weekday"], "thursday":["TH","weekday"], "friday":["FR","weekday"], 
		"saturday":["SA","weekday"], "sunday":["SU","weekday"], "somvar":["MO","weekday"], "mangalvar":["TU","weekday"], 
		"budhvar":["WE","weekday"], "guruvar":["TH","weekday"], "shukravar":["FR","weekday"], "shanivar":["SA","weekday"], 
		"ravivar":["SU","weekday"], "january":[1,"month"], "february":[2,"month"], "march":[3,"month"], "april":[4,"month"], 
		"may":[5,"month"], "june":[6,"month"], "july":[7,"month"], "august":[8,"month"], "september":[9,"month"], 
		"october":[10,"month"], "november":[11,"month"], "december":[12,"month"]}

Time = {"abhi":0, "baje":0, "baj":0, "ghante":0, "ghanta":1, "ghanton":1, "subah":0, "shaam":0, "sandhya":0,
		"dopahar":0, "raat":0, "minutes":0, "minute":1, "min":1, "seconds":0, "second":1, "sec":0}

DateTime = {"baad":[1,-1], "is":[0,1], "pahle":[-1,-1], "pichle":[-1,1], "agle":[1,1], "aadhe":[0.5,1],
		    "aadha":[0.5,1], "dedh":[1.5,1], "dhaai":[2.5,1], "saade":[0.5,1]}

Numbers = {'1':[1,1], 'ek':[1,1], 'pahla':[1,1], 'pahli':[1,1], '2':[2,1], 'do':[2,1], 'doosra':[2,1],
		   '3':[3,1], 'teen':[3,1], 'teesra':[3,1], '4':[4,1], 'chaar':[4,1], 'char':[4,1], 'choutha':[4,1], '5':[5,1],
		   'paanch':[5,1], 'paanchva':[5,1], '6':[6,1], 'chhe':[6,1], 'chhata':[6,1], '7':[7,1], 'saat':[7,1], 
		   'saatva':[7,1], '8':[8,1], 'aath':[8,1], 'aathva':[8,1], '9':[9,1], 'nau':[9,1], 'nahla':[9,1], 
		   '10':[10,1], 'das':[10,1], 'dasva':[10,1], '11':[11,1], 'gyarah':[11,1], 'gyarva':[11,1], '12':[12,1], 
		   'barah':[12,1], 'barvan':[12,1], '13':[13,1], 'terah':[13,1], '14':[14,1], 'chaudah':[14,1], '15':[15,1], 
		   'pandrah':[15,1], '16':[16,1], 'solah':[16,1], '17':[17,1], 'satrah':[17,1], '18':[18,1], 
		   'atharah':[18,1], '19':[19,1], 'unnish':[19,1], '20':[20,1], 'bees':[20,1], '21':[21,1], 
		   'ikkish':[21,1], '22':[22,1], 'baaish':[22,1], '23':[23,1], 'teish':[23,1], '24':[24,1], 
		   'chaubish':[24,1], '25':[25,1], 'pachhish':[25,1], '26':[26,1], 'chhabish':[26,1], 
		   '27':[27,1], 'sattaish':[27,1], '28':[28,1], 'atthaish':[28,1], '29':[29,1], 'untish':[29,1], 
		   '30':[30,1], 'teesh':[30,1], '31':[31,1], 'ikattish':[31,1]}

Separators = {"se":0, "ke":0, "aur":0, "evam":0, "lekin":0, "par":0, "magar":0, "kintu":0, "parantu":0, 
			  "ya":0, "kyunki":0, "isliye":0}
