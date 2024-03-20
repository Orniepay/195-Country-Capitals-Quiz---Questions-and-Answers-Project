import random 

print("")
print("195 Country Capitals Quiz - Questions and Answers")

# A dictionary containing questions and answers for the quiz
quiz = {
    "question1": {
        "question": "What is the capital of Afghanistan?",
        "answer": "Kabul"
    },
    "question2": {
        "question": "What is the capital of Albania?",
        "answer": "Tirana"
    },
    "question3": {
        "question": "What is the capital of Algeria?",
        "answer": "Algiers"
    },
    "question4": {
        "question": "What is the capital of Andorra?",
        "answer": "Andorra la Vella"
    },
    "question5": {
        "question": "What is the capital of Angola?",
        "answer": "Luanda"
    },
    "question6": {
        "question": "What is the capital of Antigua and Barbuda?",
        "answer": "Saint John's"
    },
    "question7": {
        "question": "What is the capital of Argentina?",
        "answer": "Buenos Aires"
    },
    "question8": {
        "question": "What is the capital of Armenia?",
        "answer": "Yerevan"
    },
    "question9": {
        "question": "What is the capital of Australia?",
        "answer": "Canberra"
    },
    "question10": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    },
        "question11": {
        "question": "What is the capital of Azerbaijan?",
        "answer": "Baku"
    },
    "question12": {
        "question": "What is the capital of The Bahamas?",
        "answer": "Nassau"
    },
    "question13": {
        "question": "What is the capital of Bahrain?",
        "answer": "Manama"
    },
    "question14": {
        "question": "What is the capital of Bangladesh?",
        "answer": "Dhaka"
    },
    "question15": {
        "question": "What is the capital of Barbados?",
        "answer": "Bridgetown"
    },
    "question16": {
        "question": "What is the capital of Belarus?",
        "answer": "Minsk"
    },
    "question17": {
        "question": "What is the capital of Belgium?",
        "answer": "Brussels"
    },
    "question18": {
        "question": "What is the capital of Belize?",
        "answer": "Belmopan"
    },
    "question19": {
        "question": "What is the capital of Benin?",
        "answer": "Porto-Novo"
    },
    "question20": {
        "question": "What is the capital of Bhutan?",
        "answer": "Thimphu"
    },
        "question21": {
        "question": "What is the capital of Bolivia?",
        "answer": "Sucre"
    },
    "question22": {
        "question": "What is the capital of Bosnia and Herzegovina?",
        "answer": "Sarajevo"
    },
    "question23": {
        "question": "What is the capital of Botswana?",
        "answer": "Gaborone"
    },
    "question24": {
        "question": "What is the capital of Brazil?",
        "answer": "Brasília"
    },
    "question25": {
        "question": "What is the capital of Brunei?",
        "answer": "Bandar Seri Begawan"
    },
    "question26": {
        "question": "What is the capital of Bulgaria?",
        "answer": "Sofia"
    },
    "question27": {
        "question": "What is the capital of Burkina Faso?",
        "answer": "Ouagadougou"
    },
    "question28": {
        "question": "What is the capital of Burundi?",
        "answer": "Gitega"
    },
    "question29": {
        "question": "What is the capital of Cape Verde?",
        "answer": "Praia"
    },
    "question30": {
        "question": "What is the capital of Cambodia?",
        "answer": "Phnom Penh"
    },
        "question31": {
        "question": "What is the capital of Cameroon?",
        "answer": "Yaoundé"
    },
    "question32": {
        "question": "What is the capital of Canada?",
        "answer": "Ottawa"
    },
    "question33": {
        "question": "What is the capital of the Central African Republic?",
        "answer": "Bangui"
    },
    "question34": {
        "question": "What is the capital of Chad?",
        "answer": "N'Djamena"
    },
    "question35": {
        "question": "What is the capital of Chile?",
        "answer": "Santiago"
    },
    "question36": {
        "question": "What is the capital of China?",
        "answer": "Beijing"
    },
    "question37": {
        "question": "What is the capital of Colombia?",
        "answer": "Bogotá"
    },
    "question38": {
        "question": "What is the capital of the Comoros?",
        "answer": "Moroni"
    },
    "question39": {
        "question": "What is the capital of the Congo, Republic of the?",
        "answer": "Brazzaville"
    },
    "question40": {
        "question": "What is the capital of the Congo, Democratic Republic of the?",
        "answer": "Kinshasa"
    },
        "question41": {
        "question": "What is the capital of Costa Rica?",
        "answer": "San José"
    },
    "question42": {
        "question": "What is the capital of Croatia?",
        "answer": "Zagreb"
    },
    "question43": {
        "question": "What is the capital of Cuba?",
        "answer": "Havana"
    },
    "question44": {
        "question": "What is the capital of Cyprus?",
        "answer": "Nicosia"
    },
    "question45": {
        "question": "What is the capital of the Czech Republic?",
        "answer": "Prague"
    },
    "question46": {
        "question": "What is the capital of Denmark?",
        "answer": "Copenhagen"
    },
    "question47": {
        "question": "What is the capital of Djibouti?",
        "answer": "Djibouti"
    },
    "question48": {
        "question": "What is the capital of Dominica?",
        "answer": "Roseau"
    },
    "question49": {
        "question": "What is the capital of the Dominican Republic?",
        "answer": "Santo Domingo"
    },
    "question50": {
        "question": "What is the capital of East Timor (Timor-Leste)?",
        "answer": "Dili"
    },
        "question51": {
        "question": "What is the capital of Ecuador?",
        "answer": "Quito"
    },
    "question52": {
        "question": "What is the capital of Egypt?",
        "answer": "Cairo"
    },
    "question53": {
        "question": "What is the capital of El Salvador?",
        "answer": "San Salvador"
    },
    "question54": {
        "question": "What is the capital of Equatorial Guinea?",
        "answer": "Malabo"
    },
    "question55": {
        "question": "What is the capital of Eritrea?",
        "answer": "Asmara"
    },
    "question56": {
        "question": "What is the capital of Estonia?",
        "answer": "Tallinn"
    },
    "question57": {
        "question": "What is the capital of Eswatini (formerly Swaziland)?",
        "answer": "Mbabane"
    },
    "question58": {
        "question": "What is the capital of Ethiopia?",
        "answer": "Addis Ababa"
    },
    "question59": {
        "question": "What is the capital of Fiji?",
        "answer": "Suva"
    },
    "question60": {
        "question": "What is the capital of Finland?",
        "answer": "Helsinki"
    },
        "question61": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question62": {
        "question": "What is the capital of Gabon?",
        "answer": "Libreville"
    },
    "question63": {
        "question": "What is the capital of The Gambia?",
        "answer": "Banjul"
    },
    "question64": {
        "question": "What is the capital of Georgia?",
        "answer": "Tbilisi"
    },
    "question65": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question66": {
        "question": "What is the capital of Ghana?",
        "answer": "Accra"
    },
    "question67": {
        "question": "What is the capital of Greece?",
        "answer": "Athens"
    },
    "question68": {
        "question": "What is the capital of Grenada?",
        "answer": "Saint George's"
    },
    "question69": {
        "question": "What is the capital of Guatemala?",
        "answer": "Guatemala City"
    },
    "question70": {
        "question": "What is the capital of Guinea?",
        "answer": "Conakry"
    },
        "question71": {
        "question": "What is the capital of Guinea-Bissau?",
        "answer": "Bissau"
    },
    "question72": {
        "question": "What is the capital of Guyana?",
        "answer": "Georgetown"
    },
    "question73": {
        "question": "What is the capital of Haiti?",
        "answer": "Port-au-Prince"
    },
    "question74": {
        "question": "What is the capital of Honduras?",
        "answer": "Tegucigalpa"
    },
    "question75": {
        "question": "What is the capital of Hungary?",
        "answer": "Budapest"
    },
    "question76": {
        "question": "What is the capital of Iceland?",
        "answer": "Reykjavik"
    },
    "question77": {
        "question": "What is the capital of India?",
        "answer": "New Delhi"
    },
    "question78": {
        "question": "What is the capital of Indonesia?",
        "answer": "Jakarta"
    },
    "question79": {
        "question": "What is the capital of Iran?",
        "answer": "Tehran"
    },
    "question80": {
        "question": "What is the capital of Iraq?",
        "answer": "Baghdad"
    },
        "question81": {
        "question": "What is the capital of Ireland?",
        "answer": "Dublin"
    },
    "question82": {
        "question": "What is the capital of Israel?",
        "answer": "Jerusalem"
    },
    "question83": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question84": {
        "question": "What is the capital of Jamaica?",
        "answer": "Kingston"
    },
    "question85": {
        "question": "What is the capital of Japan?",
        "answer": "Tokyo"
    },
    "question86": {
        "question": "What is the capital of Jordan?",
        "answer": "Amman"
    },
    "question87": {
        "question": "What is the capital of Kazakhstan?",
        "answer": "Nur-Sultan"
    },
    "question88": {
        "question": "What is the capital of Kenya?",
        "answer": "Nairobi"
    },
    "question89": {
        "question": "What is the capital of Kiribati?",
        "answer": "South Tarawa"
    },
    "question90": {
        "question": "What is the capital of Kosovo?",
        "answer": "Pristina"
    },
        "question91": {
        "question": "What is the capital of Kuwait?",
        "answer": "Kuwait City"
    },
    "question92": {
        "question": "What is the capital of Kyrgyzstan?",
        "answer": "Bishkek"
    },
    "question93": {
        "question": "What is the capital of Laos?",
        "answer": "Vientiane"
    },
    "question94": {
        "question": "What is the capital of Latvia?",
        "answer": "Riga"
    },
    "question95": {
        "question": "What is the capital of Lebanon?",
        "answer": "Beirut"
    },
    "question96": {
        "question": "What is the capital of Lesotho?",
        "answer": "Maseru"
    },
    "question97": {
        "question": "What is the capital of Liberia?",
        "answer": "Monrovia"
    },
    "question98": {
        "question": "What is the capital of Libya?",
        "answer": "Tripoli"
    },
    "question99": {
        "question": "What is the capital of Liechtenstein?",
        "answer": "Vaduz"
    },
    "question100": {
        "question": "What is the capital of Lithuania?",
        "answer": "Vilnius"
    },
        "question101": {
        "question": "What is the capital of Luxembourg?",
        "answer": "Luxembourg"
    },
    "question102": {
        "question": "What is the capital of Madagascar?",
        "answer": "Antananarivo"
    },
    "question103": {
        "question": "What is the capital of Malawi?",
        "answer": "Lilongwe"
    },
    "question104": {
        "question": "What is the capital of Malaysia?",
        "answer": "Kuala Lumpur"
    },
    "question105": {
        "question": "What is the capital of Maldives?",
        "answer": "Malé"
    },
    "question106": {
        "question": "What is the capital of Mali?",
        "answer": "Bamako"
    },
    "question107": {
        "question": "What is the capital of Malta?",
        "answer": "Valletta"
    },
    "question108": {
        "question": "What is the capital of the Marshall Islands?",
        "answer": "Majuro"
    },
    "question109": {
        "question": "What is the capital of Mauritania?",
        "answer": "Nouakchott"
    },
    "question110": {
        "question": "What is the capital of Mauritius?",
        "answer": "Port Louis"
    },
        "question111": {
        "question": "What is the capital of Mexico?",
        "answer": "Mexico City"
    },
    "question112": {
        "question": "What is the capital of Micronesia?",
        "answer": "Palikir"
    },
    "question113": {
        "question": "What is the capital of Moldova?",
        "answer": "Chișinău"
    },
    "question114": {
        "question": "What is the capital of Monaco?",
        "answer": "Monaco"
    },
    "question115": {
        "question": "What is the capital of Mongolia?",
        "answer": "Ulaanbaatar"
    },
    "question116": {
        "question": "What is the capital of Montenegro?",
        "answer": "Podgorica"
    },
    "question117": {
        "question": "What is the capital of Morocco?",
        "answer": "Rabat"
    },
    "question118": {
        "question": "What is the capital of Mozambique?",
        "answer": "Maputo"
    },
    "question119": {
        "question": "What is the capital of Myanmar?",
        "answer": "Naypyidaw"
    },
    "question120": {
        "question": "What is the capital of Namibia?",
        "answer": "Windhoek"
    },
        "question121": {
        "question": "What is the capital of Nauru?",
        "answer": "Yaren District"
    },
    "question122": {
        "question": "What is the capital of Nepal?",
        "answer": "Kathmandu"
    },
    "question123": {
        "question": "What is the capital of the Netherlands?",
        "answer": "Amsterdam"
    },
    "question124": {
        "question": "What is the capital of New Zealand?",
        "answer": "Wellington"
    },
    "question125": {
        "question": "What is the capital of Nicaragua?",
        "answer": "Managua"
    },
    "question126": {
        "question": "What is the capital of Niger?",
        "answer": "Niamey"
    },
    "question127": {
        "question": "What is the capital of Nigeria?",
        "answer": "Abuja"
    },
    "question128": {
        "question": "What is the capital of North Korea?",
        "answer": "Pyongyang"
    },
    "question129": {
        "question": "What is the capital of North Macedonia?",
        "answer": "Skopje"
    },
    "question130": {
        "question": "What is the capital of Norway?",
        "answer": "Oslo"
    },
    "question131": {
        "question": "What is the capital of Oman?",
        "answer": "Muscat"
    },
    "question132": {
        "question": "What is the capital of Pakistan?",
        "answer": "Islamabad"
    },
    "question133": {
        "question": "What is the capital of Palau?",
        "answer": "Ngerulmud"
    },
    "question134": {
        "question": "What is the capital of Palestine?",
        "answer": "Jerusalem (East)"
    },
    "question135": {
        "question": "What is the capital of Panama?",
        "answer": "Panama City"
    },
    "question136": {
        "question": "What is the capital of Papua New Guinea?",
        "answer": "Port Moresby"
    },
    "question137": {
        "question": "What is the capital of Paraguay?",
        "answer": "Asunción"
    },
    "question138": {
        "question": "What is the capital of Peru?",
        "answer": "Lima"
    },
    "question139": {
        "question": "What is the capital of the Philippines?",
        "answer": "Manila"
    },
    "question140": {
        "question": "What is the capital of Poland?",
        "answer": "Warsaw"
    },
    "question141": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question142": {
        "question": "What is the capital of Qatar?",
        "answer": "Doha"
    },
    "question143": {
        "question": "What is the capital of Romania?",
        "answer": "Bucharest"
    },
    "question144": {
        "question": "What is the capital of Russia?",
        "answer": "Moscow"
    },
    "question145": {
        "question": "What is the capital of Rwanda?",
        "answer": "Kigali"
    },
    "question146": {
        "question": "What is the capital of Saint Kitts and Nevis?",
        "answer": "Basseterre"
    },
    "question147": {
        "question": "What is the capital of Saint Lucia?",
        "answer": "Castries"
    },
    "question148": {
        "question": "What is the capital of Saint Vincent and the Grenadines?",
        "answer": "Kingstown"
    },
    "question149": {
        "question": "What is the capital of Samoa?",
        "answer": "Apia"
    },
    "question150": {
        "question": "What is the capital of San Marino?",
        "answer": "San Marino"
    },
    "question151": {
        "question": "What is the capital of Sao Tome and Principe?",
        "answer": "São Tomé"
    },
    "question152": {
        "question": "What is the capital of Saudi Arabia?",
        "answer": "Riyadh"
    },
    "question153": {
        "question": "What is the capital of Senegal?",
        "answer": "Dakar"
    },
    "question154": {
        "question": "What is the capital of Serbia?",
        "answer": "Belgrade"
    },
    "question155": {
        "question": "What is the capital of Seychelles?",
        "answer": "Victoria"
    },
    "question156": {
        "question": "What is the capital of Sierra Leone?",
        "answer": "Freetown"
    },
    "question157": {
        "question": "What is the capital of Singapore?",
        "answer": "Singapore"
    },
    "question158": {
        "question": "What is the capital of Slovakia?",
        "answer": "Bratislava"
    },
    "question159": {
        "question": "What is the capital of Slovenia?",
        "answer": "Ljubljana"
    },
    "question160": {
        "question": "What is the capital of the Solomon Islands?",
        "answer": "Honiara"
    },
    "question161": {
        "question": "What is the capital of Somalia?",
        "answer": "Mogadishu"
    },
    "question162": {
        "question": "What is the capital of South Africa?",
        "answer": "Pretoria (executive), Bloemfontein (judicial), Cape Town (legislative)"
    },
    "question163": {
        "question": "What is the capital of South Korea?",
        "answer": "Seoul"
    },
    "question164": {
        "question": "What is the capital of South Sudan?",
        "answer": "Juba"
    },
    "question165": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question166": {
        "question": "What is the capital of Sri Lanka?",
        "answer": "Sri Jayawardenepura Kotte"
    },
    "question167": {
        "question": "What is the capital of Sudan?",
        "answer": "Khartoum"
    },
    "question168": {
        "question": "What is the capital of Suriname?",
        "answer": "Paramaribo"
    },
    "question169": {
        "question": "What is the capital of Sweden?",
        "answer": "Stockholm"
    },
    "question170": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question171": {
        "question": "What is the capital of Syria?",
        "answer": "Damascus"
    },
    "question172": {
        "question": "What is the capital of Tajikistan?",
        "answer": "Dushanbe"
    },
    "question173": {
        "question": "What is the capital of Tanzania?",
        "answer": "Dodoma"
    },
    "question174": {
        "question": "What is the capital of Thailand?",
        "answer": "Bangkok"
    },
    "question175": {
        "question": "What is the capital of Togo?",
        "answer": "Lomé"
    },
    "question176": {
        "question": "What is the capital of Tonga?",
        "answer": "Nukuʻalofa"
    },
    "question177": {
        "question": "What is the capital of Trinidad and Tobago?",
        "answer": "Port of Spain"
    },
    "question178": {
        "question": "What is the capital of Tunisia?",
        "answer": "Tunis"
    },
    "question179": {
        "question": "What is the capital of Turkey?",
        "answer": "Ankara"
    },
    "question180": {
        "question": "What is the capital of Turkmenistan?",
        "answer": "Ashgabat"
    },
    "question181": {
        "question": "What is the capital of Tuvalu?",
        "answer": "Funafuti"
    },
    "question182": {
        "question": "What is the capital of Uganda?",
        "answer": "Kampala"
    },
    "question183": {
        "question": "What is the capital of Ukraine?",
        "answer": "Kyiv"
    },
    "question184": {
        "question": "What is the capital of the United Arab Emirates?",
        "answer": "Abu Dhabi"
    },
    "question185": {
        "question": "What is the capital of the United Kingdom?",
        "answer": "London"
    },
    "question186": {
        "question": "What is the capital of the United States?",
        "answer": "Washington, D.C."
    },
    "question187": {
        "question": "What is the capital of Uruguay?",
        "answer": "Montevideo"
    },
    "question188": {
        "question": "What is the capital of Uzbekistan?",
        "answer": "Tashkent"
    },
    "question189": {
        "question": "What is the capital of Vanuatu?",
        "answer": "Port Vila"
    },
    "question190": {
        "question": "What is the capital of Vatican City?",
        "answer": "Vatican City"
    },
    "question191": {
        "question": "What is the capital of Venezuela?",
        "answer": "Caracas"
    },
    "question192": {
        "question": "What is the capital of Vietnam?",
        "answer": "Hanoi"
    },
    "question193": {
        "question": "What is the capital of Yemen?",
        "answer": "Sana'a"
    },
    "question194": {
        "question": "What is the capital of Zambia?",
        "answer": "Lusaka"
    },
    "question195": {
        "question": "What is the capital of Zimbabwe?",
        "answer": "Harare"
    }
}

score = 0

# Shuffle the quiz items for random question order
quiz_items = list(quiz.items())
random.shuffle(quiz_items)

# Iterate through each question in the quiz
for key, value in quiz_items:
    """
    Processes each question and answer in the quiz.
    - Displays the question.
    - Takes the user's answer.
    - Compares the user's answer with the correct answer.
    - Updates the score based on the correctness of the answer.
    - Displays feedback and the current score.
    """
    print("")
    print(value['question'])
    answer = input('Your Answer: ')

    if answer.lower() == value['answer'].lower():
        print("")
        print('Correct!')
        score+=1
        print('Your score is: ' + str(score))
    else:
        print("")
        print('Incorrect!')
        print('The answer is : ' + value['answer'])
        print('The score is: ' + str(score))


# Display the final score and percentage of correct answers
print("\n=================================================================")
print(f'You scored: {score} out of 195 questions correctly')
print(f'You answered: {score/195 * 100:.2f}% of your questions correctly\n')