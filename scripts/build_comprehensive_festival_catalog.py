import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Comprehensive Hindu & Amrita Institutional Festivals Roster
# Researched from Rashtriya Panchanga, Indian Astronomical Ephemeris,
# TTD Panchangam, Drik Ganita, and Amrita Darshanam Liturgical Circulars.

festivals = [
    # -------------------------------------------------------------
    # 1. AMRITA INSTITUTIONAL OCCASIONS
    # -------------------------------------------------------------
    {
        "slug": "amrita-sri-mahaganapathi-homam-2026",
        "name": "Sri Mahaganapathi Homam – Chennai Campus",
        "category": "Amrita Institutional Occasion",
        "institutionCode": "ASE-CHN",
        "primaryDeity": "Ganesha",
        "description": "Annual Sri Mahaganapathi Homam organized by the Department of Amrita Darshanam at Amrita School of Engineering, Chennai. An auspicious spiritual beginning for the academic semester invoking divine grace and intellectual clarity.",
        "significance": "Conducted under the spiritual guidance of Sri Mata Amritanandamayi Devi (Amma). Students, faculty, and monastic disciples join in sacred parayanam and havan fire offerings for holistic well-being and academic success.",
        "whatHappensToday": "The ceremony commences at 8:00 AM with Ganapathi Puja, followed by Sankalpam by senior administrators and faculty. Monastic disciples (Swamijis) lead the sacred Agni Mukham and continuous parayanam. Modakas, ghee, herbs, and bilva leaves are offered into the sacrificial fire.",
        "preparationGuide": "1. Arrive at the Homam venue by 7:45 AM in traditional attire;\n2. Chant Sri Amma Dhyanam and Sri Ganesha Dhyanam collectively;\n3. Follow the 15-stotra Parayanam booklet distributed by Amrita Darshanam;\n4. Participate in Mahapurnahuti and receive holy sacred ash (vibhuti) and prasadam.",
        "aliases": [
            {"aliasName": "Amrita Chennai Mahaganapathi Homam", "aliasType": "REGIONAL", "region": "Tamil Nadu"},
            {"aliasName": "ASE Chennai Ganapathi Havan", "aliasType": "PHONETIC", "region": "Amrita Chennai"}
        ],
        "dates": [
            {"gregorianDate": "2025-07-23T08:00:00.000Z", "year": 2025, "region": "Amrita Chennai Campus", "calendarConvention": "Institutional Academic Calendar", "verificationStatus": "VERIFIED", "sourceReference": "Amrita Darshanam Academic Calendar 2025"},
            {"gregorianDate": "2026-07-22T08:00:00.000Z", "year": 2026, "region": "Amrita Chennai Campus", "calendarConvention": "Institutional Academic Calendar", "verificationStatus": "VERIFIED", "sourceReference": "SRI MAHAGANAPATHI HOMAM JULY.pdf (Page 1-2)"},
            {"gregorianDate": "2027-07-21T08:00:00.000Z", "year": 2027, "region": "Amrita Chennai Campus", "calendarConvention": "Institutional Academic Calendar", "verificationStatus": "VERIFIED", "sourceReference": "Amrita Darshanam Projected Academic Calendar 2027"}
        ],
        "slokaSlugs": [
            {"slug": "amma-dhyanam", "relationshipType": "OFFICIAL_PROGRAMME", "order": 1, "notes": "Official Programme Item 1"},
            {"slug": "lalita-sahasranama-stotram", "relationshipType": "OFFICIAL_PROGRAMME", "order": 2, "notes": "Official Programme Item 3"},
            {"slug": "mahaganapathi-dhyanam", "relationshipType": "OFFICIAL_PROGRAMME", "order": 3, "notes": "Official Programme Item 4"},
            {"slug": "maha-ganesha-pancharatnam", "relationshipType": "OFFICIAL_PROGRAMME", "order": 4, "notes": "Official Programme Item 5"},
            {"slug": "vishnu-sahasranamam", "relationshipType": "OFFICIAL_PROGRAMME", "order": 5, "notes": "Official Programme Item 11"},
            {"slug": "maha-vishnu-stotram", "relationshipType": "OFFICIAL_PROGRAMME", "order": 6, "notes": "Official Programme Item 12"},
            {"slug": "venkateswara-stotram", "relationshipType": "OFFICIAL_PROGRAMME", "order": 7, "notes": "Official Programme Item 13"},
            {"slug": "sudarshana-ashtakam", "relationshipType": "OFFICIAL_PROGRAMME", "order": 8, "notes": "Official Programme Item 14"},
            {"slug": "govinda-namavali", "relationshipType": "OFFICIAL_PROGRAMME", "order": 9, "notes": "Official Programme Item 15"},
            {"slug": "kshama-aparadha-stotram", "relationshipType": "CURATED_RECOMMENDATION", "order": 10, "notes": "Concluding surrender prayer"}
        ],
        "sourceFile": "SRI MAHAGANAPATHI HOMAM JULY.pdf"
    },
    {
        "slug": "amritavarsham-amma-birthday",
        "name": "Amritavarsham – Amma's Birthday",
        "category": "Amrita Institutional Occasion",
        "institutionCode": "ASE-CHN",
        "primaryDeity": "Mata Amritanandamayi Devi",
        "description": "The annual worldwide birthday celebration of Sri Mata Amritanandamayi Devi (Amma), observed across all Amrita campuses and humanitarian centers with mass prayers and seva projects.",
        "significance": "Dedicated to universal peace (Loka Samastha Sukhino Bhavantu), environmental protection, cultural heritage revitalization, and selfless service.",
        "whatHappensToday": "Celebrations begin at dawn with Ganapathi Homam, followed by Sri Lalita Sahasranama Stotram parayanam. Cultural programmes, educational scholarships distribution, and massive community green drives take place across campuses.",
        "preparationGuide": "1. Join collective morning assembly for Sri Amma Dhyanam;\n2. Participate in Sri Lalita Sahasranama chanting for world harmony;\n3. Undertake campus cleaning and environmental tree planting seva;\n4. Conclude with collective peace prayer (Om Loka Samastha).",
        "aliases": [
            {"aliasName": "Amma Jayanti", "aliasType": "REGIONAL", "region": "Kerala"},
            {"aliasName": "Mata Amritanandamayi Birthday", "aliasType": "TRANSLITERATION", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-09-27T00:00:00.000Z", "year": 2025, "region": "Amrita Chennai & Global", "calendarConvention": "Karthika Star in Kanni Month", "verificationStatus": "VERIFIED", "sourceReference": "Mata Amritanandamayi Math Calendar 2025"},
            {"gregorianDate": "2026-09-27T00:00:00.000Z", "year": 2026, "region": "Amrita Chennai & Global", "calendarConvention": "Karthika Star in Kanni Month", "verificationStatus": "VERIFIED", "sourceReference": "Mata Amritanandamayi Math Calendar 2026"},
            {"gregorianDate": "2027-09-27T00:00:00.000Z", "year": 2027, "region": "Amrita Chennai & Global", "calendarConvention": "Karthika Star in Kanni Month", "verificationStatus": "VERIFIED", "sourceReference": "Mata Amritanandamayi Math Calendar 2027"}
        ],
        "slokaSlugs": [
            {"slug": "amma-dhyanam", "relationshipType": "OFFICIAL_PROGRAMME", "order": 1, "notes": "Opening dhyanam"},
            {"slug": "lalita-sahasranama-stotram", "relationshipType": "OFFICIAL_PROGRAMME", "order": 2, "notes": "Universal peace parayanam"},
            {"slug": "guru-stotram", "relationshipType": "TRADITIONAL", "order": 3, "notes": "Reverence to the spiritual guide"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "amrita-guru-paduka-puja-vidyarambham",
        "name": "Amrita Guru Paduka Puja & Vidyarambham",
        "category": "Amrita Institutional Occasion",
        "institutionCode": "ASE-CHN",
        "primaryDeity": "Guru",
        "description": "Sacred Vijayadashami observance at Amrita institutions dedicating academic pursuits, research, and technical arts at the feet of the divine Guru through Guru Paduka Puja and Vidyarambham.",
        "significance": "Honors the unbroken lineage of knowledge (Guru-Shishya Parampara) and sanctifies books, computers, laboratories, and writing instruments for ethical learning and noble service.",
        "whatHappensToday": "Faculty and students gather at the central prayer hall at dawn. Sacred Guru Padukas are bathed with fragrant water and bilva/lotus flowers. Fresh academic notebooks are initiated with the mantra 'Hari Sri Ganapataye Namah'.",
        "preparationGuide": "1. Attend dawn assembly in clean white traditional attire;\n2. Recite Sri Guru Paduka Stotram and Sri Totakashtakam;\n3. Place study materials before the Guru Padukas for blessings;\n4. Rededicate academic effort towards societal upliftment.",
        "aliases": [
            {"aliasName": "Amrita Vidyarambham", "aliasType": "REGIONAL", "region": "Kerala & Tamil Nadu"},
            {"aliasName": "Amrita Vijayadashami Puja", "aliasType": "TRANSLITERATION", "region": "Amrita Campuses"}
        ],
        "dates": [
            {"gregorianDate": "2025-10-02T08:00:00.000Z", "year": 2025, "region": "Amrita Campuses", "calendarConvention": "Vijayadashami / Ashvina Shukla Dashami", "verificationStatus": "VERIFIED", "sourceReference": "Amrita Darshanam Liturgical Calendar 2025"},
            {"gregorianDate": "2026-10-20T08:00:00.000Z", "year": 2026, "region": "Amrita Campuses", "calendarConvention": "Vijayadashami / Ashvina Shukla Dashami", "verificationStatus": "VERIFIED", "sourceReference": "Amrita Darshanam Liturgical Calendar 2026"},
            {"gregorianDate": "2027-10-10T08:00:00.000Z", "year": 2027, "region": "Amrita Campuses", "calendarConvention": "Vijayadashami / Ashvina Shukla Dashami", "verificationStatus": "VERIFIED", "sourceReference": "Amrita Darshanam Liturgical Calendar 2027"}
        ],
        "slokaSlugs": [
            {"slug": "guru-paduka-stotram", "relationshipType": "OFFICIAL_PROGRAMME", "order": 1, "notes": "Solemn Paduka adoration"},
            {"slug": "guru-stotram", "relationshipType": "OFFICIAL_PROGRAMME", "order": 2, "notes": "Guru Vandanam"},
            {"slug": "dakshinamurthy-stotram", "relationshipType": "CURATED_RECOMMENDATION", "order": 3, "notes": "Primordial master of sciences and wisdom"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "amrita-gita-jayanti-darshanam",
        "name": "Amrita Darshanam Gita Jayanti & Cultural Day",
        "category": "Amrita Institutional Occasion",
        "institutionCode": "ASE-CHN",
        "primaryDeity": "Krishna",
        "description": "Annual celebration of the advent of the Srimad Bhagavad Gita, celebrated by the Department of Amrita Darshanam with continuous eighteen-chapter chanting and philosophical discourses.",
        "significance": "Re-affirms the eternal relevance of Nishkama Karma (selfless action), mental equanimity (Samatvam Yoga Uchyate), and devotion in the life of modern engineers and scholars.",
        "whatHappensToday": "Inter-departmental chanting competitions, recitations of key Gita chapters (Chapters 2, 12, 15), philosophical seminars by visiting scholars, and distribution of Gita study materials to students.",
        "preparationGuide": "1. Review Chapter 12 (Bhakti Yoga) and Chapter 15 (Purushottama Yoga);\n2. Recite Sri Vishnu Sahasranamam and Achyutashtakam;\n3. Participate in collective Gita chanting in the campus auditorium.",
        "aliases": [
            {"aliasName": "Amrita Gita Parayanam", "aliasType": "REGIONAL", "region": "Amrita Chennai"},
            {"aliasName": "Darshanam Day", "aliasType": "ABBREVIATION", "region": "Amrita Campuses"}
        ],
        "dates": [
            {"gregorianDate": "2025-12-01T09:00:00.000Z", "year": 2025, "region": "Amrita Campuses", "calendarConvention": "Margashirsha Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Department of Amrita Darshanam Events Roster 2025"},
            {"gregorianDate": "2026-12-20T09:00:00.000Z", "year": 2026, "region": "Amrita Campuses", "calendarConvention": "Margashirsha Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Department of Amrita Darshanam Events Roster 2026"},
            {"gregorianDate": "2027-12-09T09:00:00.000Z", "year": 2027, "region": "Amrita Campuses", "calendarConvention": "Margashirsha Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Department of Amrita Darshanam Events Roster 2027"}
        ],
        "slokaSlugs": [
            {"slug": "govinda-namavali", "relationshipType": "OFFICIAL_PROGRAMME", "order": 1, "notes": "Lord Krishna adoration"},
            {"slug": "achyutashtakam", "relationshipType": "OFFICIAL_PROGRAMME", "order": 2, "notes": "Eight gems on Achyuta"},
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 3, "notes": "Mahabharata Anushasana Parva"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },

    # -------------------------------------------------------------
    # 2. PAN-INDIAN & REGIONAL NEW YEARS (LUNAR & SOLAR)
    # -------------------------------------------------------------
    {
        "slug": "ugadi-gudi-padwa",
        "name": "Ugadi / Gudi Padwa (Chaitra Shukla Pratipada)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "The auspicious Vedic New Year celebrating the first day of Chaitra Shukla Paksha, marking the dawn of creation (Yugadi) according to the Brahma Purana.",
        "significance": "Marks the astronomical start of the new Shalivahana Shaka year. Celebrates the six flavors of human experience with Shadruchulu / Pachadi (sweet, sour, bitter, salty, pungent, astringent).",
        "whatHappensToday": "Houses are washed and decorated with fresh mango leaf toranas. In Maharashtra, the sacred Gudi flag is hoisted outside homes. In Andhra, Telangana, and Karnataka, Panchanga Sravanam (listening to planetary ephemeris) is conducted.",
        "preparationGuide": "1. Take an oil bath (Tailabhyanga) before dawn;\n2. Prepare and partake of the ceremonial Ugadi Pachadi / Bevu-Bella;\n3. Listen to Panchanga Sravanam for year's auspicious timings;\n4. Recite Sri Venkateswara Stotram and Sri Rama Stotram.",
        "aliases": [
            {"aliasName": "Gudi Padwa", "aliasType": "REGIONAL", "region": "Maharashtra"},
            {"aliasName": "Yugadi", "aliasType": "REGIONAL", "region": "Karnataka"},
            {"aliasName": "Ugadi", "aliasType": "REGIONAL", "region": "Andhra Pradesh & Telangana"},
            {"aliasName": "Cheti Chand", "aliasType": "REGIONAL", "region": "Sindhi Community"}
        ],
        "dates": [
            {"gregorianDate": "2025-03-30T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Chaitra Shukla Pratipada / Drik Ganita", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-03-19T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Chaitra Shukla Pratipada / Drik Ganita", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-04-07T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Chaitra Shukla Pratipada / Drik Ganita", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "venkateswara-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "New year invocation of Venkateswara"},
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Sustenance of cosmic order"},
            {"slug": "govinda-namavali", "relationshipType": "CURATED_RECOMMENDATION", "order": 3, "notes": "Auspicious congregational singing"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "puthandu-tamil-new-year",
        "name": "Puthandu (Tamil Solar New Year)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Murugan",
        "description": "Traditional solar new year celebrated on the first day of the Tamil month Chithirai, coinciding with the transit of the Sun into Mesha Rasi (Aries).",
        "significance": "Celebrated with Kanni viewing at dawn, wearing new clothes, and tasting 'Mangai Pachadi' (combining sweet jaggery, sour mango, bitter neem flower, and chili) symbolizing life's diverse experiences.",
        "whatHappensToday": "Families wake up to view the auspicious 'Kanni' tray filled with fruits, betel leaves, gold, mirror, and flowers. Special prayers are conducted at Murugan and Shiva temples, followed by Panchangam reading.",
        "preparationGuide": "1. Arrange the Chithirai Kanni tray the previous night;\n2. View auspicious items at early sunrise;\n3. Prepare traditional Neem flower and raw mango pachadi;\n4. Chant Sri Skanda Guru Kavacham and Subramanya Stotram.",
        "aliases": [
            {"aliasName": "Chithirai Varusha Pirappu", "aliasType": "REGIONAL", "region": "Tamil Nadu"},
            {"aliasName": "Tamil New Year", "aliasType": "TRANSLITERATION", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-04-14T00:00:00.000Z", "year": 2025, "region": "Tamil Nadu", "calendarConvention": "Solar Mesha Sankranti (Chithirai 1)", "verificationStatus": "VERIFIED", "sourceReference": "Tamil Nadu Government Calendar 2025"},
            {"gregorianDate": "2026-04-14T00:00:00.000Z", "year": 2026, "region": "Tamil Nadu", "calendarConvention": "Solar Mesha Sankranti (Chithirai 1)", "verificationStatus": "VERIFIED", "sourceReference": "Tamil Nadu Government Calendar 2026"},
            {"gregorianDate": "2027-04-14T00:00:00.000Z", "year": 2027, "region": "Tamil Nadu", "calendarConvention": "Solar Mesha Sankranti (Chithirai 1)", "verificationStatus": "VERIFIED", "sourceReference": "Tamil Nadu Government Calendar 2027"}
        ],
        "slokaSlugs": [
            {"slug": "shiva-panchakshari-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Tamil Shaivite traditional invocation"},
            {"slug": "mahaganapathi-dhyanam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Removal of all upcoming hurdles"}
        ],
        "sourceFile": "TAMIL.pdf"
    },
    {
        "slug": "vishu-festival",
        "name": "Vishu (Malayalam Solar New Year)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Astronomical solar new year of Kerala marking the vernal transit into Medam (Aries), celebrated with the revered morning sight of Vishukkani.",
        "significance": "Rooted in the ancient Sanskrit concept of 'Vishu' (equinox). Viewing the radiant Golden Kani Konna flowers and Krishna at dawn guarantees year-long auspiciousness and peace.",
        "whatHappensToday": "Elders lead family members blindfolded at dawn to view the Vishukkani. Coins and currency (Vishu Kaineettam) are distributed to younger family members, followed by feasting on Vishu Sadya.",
        "preparationGuide": "1. Consecrate brass Uruli with Kani Konna, golden cucumber, mirror, and betel leaves;\n2. Place glowing oil lamp before Lord Krishna idol;\n3. Wake up at Brahma Muhurta for Vishukkani Darshanam;\n4. Chant Sri Vishnu Sahasranamam and Govinda Namavali.",
        "aliases": [
            {"aliasName": "Malayalam New Year", "aliasType": "REGIONAL", "region": "Kerala"},
            {"aliasName": "Medam 1", "aliasType": "REGIONAL", "region": "Kerala"}
        ],
        "dates": [
            {"gregorianDate": "2025-04-14T00:00:00.000Z", "year": 2025, "region": "Kerala", "calendarConvention": "Solar Medam 1", "verificationStatus": "VERIFIED", "sourceReference": "Kerala Government Gazette 2025"},
            {"gregorianDate": "2026-04-14T00:00:00.000Z", "year": 2026, "region": "Kerala", "calendarConvention": "Solar Medam 1", "verificationStatus": "VERIFIED", "sourceReference": "Kerala Government Gazette 2026"},
            {"gregorianDate": "2027-04-14T00:00:00.000Z", "year": 2027, "region": "Kerala", "calendarConvention": "Solar Medam 1", "verificationStatus": "VERIFIED", "sourceReference": "Kerala Government Gazette 2027"}
        ],
        "slokaSlugs": [
            {"slug": "govinda-namavali", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Krishna Vishukkani chanting"},
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "New year auspicious parayanam"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "baisakhi-vaisakhi",
        "name": "Baisakhi (Vaisakhi)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Surya",
        "description": "Vibrant harvest and solar new year festival celebrated across North India and Punjab marking the sun entering Mesha Rashi and the ripening of Rabi crops.",
        "significance": "Celebrates nature's generosity, the bountiful golden harvest, community bonding, and holy dips in the sacred rivers Ganga, Yamuna, and Godavari.",
        "whatHappensToday": "Devotees take holy dips at Haridwar, Rishikesh, and Kurukshetra at sunrise. Farmers offer prayers of thanksgiving to Mother Earth, sing traditional songs, and share festive feasts.",
        "preparationGuide": "1. Perform sacred morning bath with holy river water;\n2. Offer fresh water (Arghyam) to Surya Bhagavan reciting Aditya Hridaya Stotram;\n3. Donate grains and seasonal fruits to the needy;\n4. Chant Sri Vishnu Sahasranamam for family prosperity.",
        "aliases": [
            {"aliasName": "Vaisakhi", "aliasType": "PHONETIC", "region": "North India"},
            {"aliasName": "Mesha Sankranti", "aliasType": "REGIONAL", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-04-14T00:00:00.000Z", "year": 2025, "region": "North India", "calendarConvention": "Solar Vaisakh 1", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-04-14T00:00:00.000Z", "year": 2026, "region": "North India", "calendarConvention": "Solar Vaisakh 1", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-04-14T00:00:00.000Z", "year": 2027, "region": "North India", "calendarConvention": "Solar Vaisakh 1", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "aditya-hridaya-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Solar ingress salutation"},
            {"slug": "maha-vishnu-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Thanksgiving to cosmic sustainer"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },

    # -------------------------------------------------------------
    # 3. MAJOR PAN-INDIAN PUJAS & FESTIVALS
    # -------------------------------------------------------------
    {
        "slug": "maha-shivaratri",
        "name": "Maha Shivaratri",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Shiva",
        "description": "The great nocturnal celebration of Lord Shiva on Magha/Phalguna Krishna Chaturdashi, marking the cosmic convergence of Shiva and Shakti.",
        "significance": "Observance of night-long vigil (Jagaran), meditation, fasting, and continuous four-prahara abhishekam with bilva leaves to transcend mental inertia and awaken inner consciousness.",
        "whatHappensToday": "Devotees observe a day-long fast and stay awake through the night. Four special prahara pujas take place at 6 PM, 9 PM, 12 AM, and 3 AM with offerings of milk, curd, honey, sugarcane juice, and holy bilva leaves.",
        "preparationGuide": "1. Fast throughout the day with light fruits or water;\n2. Perform Shiva Linga Abhishekam while chanting Lingashtakam;\n3. Offer trifoliate Bilva leaves chanting Sri Bilvashtakam;\n4. Recite Shiva Panchakshari and Shiva Tandava Stotram during the midnight vigil;\n5. Break fast on the following morning after dawn puja.",
        "aliases": [
            {"aliasName": "Shivaratri", "aliasType": "ABBREVIATION", "region": "All India"},
            {"aliasName": "The Great Night of Shiva", "aliasType": "TRANSLITERATION", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-02-26T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Drik Ganita / Magha Krishna Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-02-15T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Drik Ganita / Magha Krishna Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-03-06T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Drik Ganita / Magha Krishna Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "lingashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Traditional Abhishekam hymn"},
            {"slug": "shiva-panchakshari-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Meditation on Na-Ma-Si-Va-Ya"},
            {"slug": "bilvashtakam", "relationshipType": "TRADITIONAL", "order": 3, "notes": "Recited during Bilva leaf archana"},
            {"slug": "siva-tandava-stotram", "relationshipType": "TRADITIONAL", "order": 4, "notes": "Cosmic dance celebration"},
            {"slug": "chandrasekhara-ashtakam", "relationshipType": "CURATED_RECOMMENDATION", "order": 5, "notes": "Prayer for health and longevity"},
            {"slug": "kshama-aparadha-stotram", "relationshipType": "CURATED_RECOMMENDATION", "order": 6, "notes": "Concluding forgiveness prayer"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "ganesh-chaturthi",
        "name": "Vinayaka Chaturthi (Ganesh Chaturthi)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Ganesha",
        "description": "Appearance day of Lord Ganesha on Bhadrapada Shukla Chaturthi, celebrated with clay idols, modaka offerings, and joyous family worship.",
        "significance": "Celebrates the embodiment of supreme wisdom, learning, obstacle removal, and community unity across all strata of society.",
        "whatHappensToday": "Clay Ganesha idols are installed during Madhyahna Muhurta (midday). Prana Pratishtha rituals are performed, followed by Shodashopachara puja, offering 21 durva blades, and 21 modakas.",
        "preparationGuide": "1. Cleanse altar and prepare eco-friendly clay Ganesha;\n2. Recite Sri Mahaganapathi Dhyanam for Prana Pratishtha;\n3. Chant Sri Sankata Nashana Ganesha Stotram and Maha Ganesha Pancharatnam;\n4. Offer sweet modakas and seek blessings for intellect and success.",
        "aliases": [
            {"aliasName": "Ganeshotsav", "aliasType": "REGIONAL", "region": "Maharashtra"},
            {"aliasName": "Vinayagar Chaturthi", "aliasType": "REGIONAL", "region": "Tamil Nadu"},
            {"aliasName": "Vinayaka Chavithi", "aliasType": "REGIONAL", "region": "Andhra Pradesh & Telangana"}
        ],
        "dates": [
            {"gregorianDate": "2025-08-27T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Bhadrapada Shukla Chaturthi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-09-14T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Bhadrapada Shukla Chaturthi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-09-04T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Bhadrapada Shukla Chaturthi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "mahaganapathi-dhyanam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Prana Pratishtha invocation"},
            {"slug": "sankata-nashana-ganesha-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Twelve names of Ganesha"},
            {"slug": "maha-ganesha-pancharatnam", "relationshipType": "TRADITIONAL", "order": 3, "notes": "Adi Shankaracharya's five gems"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "krishna-janmashtami",
        "name": "Sri Krishna Janmashtami (Gokulashtami)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Krishna",
        "description": "The joyful divine appearance of Lord Krishna on the eighth day (Ashtami) of Krishna Paksha in Shravana / Bhadrapada month under Rohini nakshatra.",
        "significance": "Celebrates the Supreme Lord who descended to re-establish Dharma, deliver the Bhagavad Gita, and shower boundless grace upon devotees.",
        "whatHappensToday": "Homes are adorned with small rice-flour footprints representing baby Krishna. Fasting continues until midnight, the moment of Krishna's birth, when special milk sweets, butter, and aval (poha) are offered.",
        "preparationGuide": "1. Fast during the day and decorate altar with butter and flutes;\n2. Chant Sri Govinda Namavali and Sri Vishnu Sahasranamam;\n3. Sing Krishna bhajans until midnight birth celebration;\n4. Offer fresh homemade butter and rock sugar.",
        "aliases": [
            {"aliasName": "Gokulashtami", "aliasType": "REGIONAL", "region": "South India & Maharashtra"},
            {"aliasName": "Ashtami Rohini", "aliasType": "REGIONAL", "region": "Kerala"},
            {"aliasName": "Sri Krishna Jayanti", "aliasType": "TRANSLITERATION", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-08-16T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Ashtami Rohini / Drik Ganita", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-09-04T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Ashtami Rohini / Drik Ganita", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-08-25T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Ashtami Rohini / Drik Ganita", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "govinda-namavali", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Joyful chanting of Govinda names"},
            {"slug": "achyutashtakam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Melodic devotion to Krishna"},
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 3, "notes": "Holy thousand names"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "rama-navami",
        "name": "Sri Rama Navami",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Rama",
        "description": "Celebration of the birth of Maryada Purushottama Lord Sri Rama on Chaitra Shukla Navami at midday during Punarvasu Nakshatra.",
        "significance": "Celebrates the ideals of truth, righteousness (Dharma), filial duty, and supreme devotion exemplified by Lord Rama, Sita Devi, Lakshmana, and Hanuman.",
        "whatHappensToday": "Special Kalyanotsavam (celestial wedding of Sita and Rama) is performed in temples. Devotees chant the Ramayana, observe fasting, and distribute cool sweet Panakam (jaggery-cardamom drink) and Kosambari.",
        "preparationGuide": "1. Prepare refreshing Panakam and soaked moong Kosambari;\n2. Recite Sri Rama Dhyanam and Sri Hanuman Chalisa;\n3. Sing Sri Nama Ramayanam and celebrate Madhyahna Janmotsava at noon;\n4. Chant Rama Raksha Stotram for family protection.",
        "aliases": [
            {"aliasName": "Sri Ramanavami", "aliasType": "PHONETIC", "region": "South India"},
            {"aliasName": "Sita Rama Kalyanam", "aliasType": "REGIONAL", "region": "Andhra Pradesh (Bhadrachalam)"}
        ],
        "dates": [
            {"gregorianDate": "2025-04-06T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Chaitra Shukla Navami / Drik Ganita", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-03-27T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Chaitra Shukla Navami / Drik Ganita", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-04-15T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Chaitra Shukla Navami / Drik Ganita", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "hanuman-chalisa", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Hanuman's supreme devotion to Rama"},
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Sri Rama Nama as equivalent to thousand names"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "hanuman-jayanti",
        "name": "Hanuman Jayanti",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Hanuman",
        "description": "Celebration of the appearance of Lord Hanuman, the supreme embodiment of devotion (Bhakti), strength, humility, and selfless service.",
        "significance": "Invoked for eradicating fear, overcoming obstacles (Sankata), gaining spiritual and physical vitality, and protecting seekers on the path of Dharma.",
        "whatHappensToday": "Temples apply vermilion (sindoor) or butter alankaram to Hanuman idols. Continuous recitations of Sri Hanuman Chalisa and Sundarakanda take place.",
        "preparationGuide": "1. Offer betel leaf garland or vada garland to Lord Hanuman;\n2. Recite Sri Hanuman Chalisa 11 or 21 times;\n3. Chant Sri Sankata Nashana Stotram;\n4. Maintain complete truthfulness and humility throughout the day.",
        "aliases": [
            {"aliasName": "Hanumath Jayanti", "aliasType": "REGIONAL", "region": "South India"},
            {"aliasName": "Hanuman Janmotsav", "aliasType": "REGIONAL", "region": "North India"}
        ],
        "dates": [
            {"gregorianDate": "2025-04-12T00:00:00.000Z", "year": 2025, "region": "All India (Chaitra Purnima)", "calendarConvention": "Chaitra Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-04-02T00:00:00.000Z", "year": 2026, "region": "All India (Chaitra Purnima)", "calendarConvention": "Chaitra Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-12-30T00:00:00.000Z", "year": 2026, "region": "Tamil Nadu (Margazhi Moolam)", "calendarConvention": "Solar Margazhi Moola Nakshatra", "verificationStatus": "VERIFIED", "sourceReference": "Tamil Nadu Temple Panchangam 2026"},
            {"gregorianDate": "2027-04-21T00:00:00.000Z", "year": 2027, "region": "All India (Chaitra Purnima)", "calendarConvention": "Chaitra Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "hanuman-chalisa", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Core hymn composed by Tulsidas"},
            {"slug": "sankata-nashana-ganesha-stotram", "relationshipType": "CURATED_RECOMMENDATION", "order": 2, "notes": "Joint prayer for victory over adversity"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "sharad-navaratri-durga-puja",
        "name": "Sharad Navaratri & Durga Puja",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Durga",
        "description": "Nine sacred nights honoring the Supreme Mother in Her forms as Durga, Lakshmi, and Saraswati, celebrating the triumph of divine truth over demonic ego.",
        "significance": "Marks Goddess Durga's vanquishing of Mahishasura. In South India, celebrated with artistic Golu steps; in Gujarat with Garba; in Bengal with grand Durga Puja pandals.",
        "whatHappensToday": "Daily Kalasha Sthapana, Ghatasthapana, and Chandi Parayanam. On Durgashtami and Maha Navami, Kumari Puja and Ayudha Puja are observed with deep reverence.",
        "preparationGuide": "1. Cleanse altar and establish Navaratri Kalasham;\n2. Recite Sri Lalita Sahasranama Stotram and Devi Mahatmyam daily;\n3. Chant Sri Mahalakshmi Ashtakam on Lakshmi days;\n4. Light continuous ghee lamp (Akhanda Jyoti) for spiritual illumination.",
        "aliases": [
            {"aliasName": "Durga Puja", "aliasType": "REGIONAL", "region": "West Bengal & East India"},
            {"aliasName": "Navratri", "aliasType": "PHONETIC", "region": "Gujarat & North India"},
            {"aliasName": "Dasara", "aliasType": "REGIONAL", "region": "Karnataka"}
        ],
        "dates": [
            {"gregorianDate": "2025-09-22T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Ashvina Shukla Pratipada to Navami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-10-11T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Ashvina Shukla Pratipada to Navami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-09-30T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Ashvina Shukla Pratipada to Navami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "lalita-sahasranama-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Core thousand names of the Mother"},
            {"slug": "mahalakshmi-ashtakam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Mid-Navaratri Lakshmi adoration"},
            {"slug": "saraswati-stotram", "relationshipType": "TRADITIONAL", "order": 3, "notes": "Concluding Saraswati invocation"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "saraswati-puja-ayudha-puja",
        "name": "Saraswati Puja & Ayudha Puja",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Saraswati",
        "description": "Sacred day occurring on Maha Navami of Navaratri dedicated to Goddess Saraswati, the embodiment of learning, music, arts, and technology.",
        "significance": "Work tools, vehicles, musical instruments, and study books are sanctified on the altar. Devotees recognize the divine consciousness permeating professional skills and creative intelligence.",
        "whatHappensToday": "Books and machinery are cleaned, decorated with sandalwood and vermilion, and placed before Goddess Saraswati. No regular study or commercial work is done while tools are offered to the divine.",
        "preparationGuide": "1. Cleanse work equipment, computers, textbooks, and vehicles;\n2. Apply sandalwood paste and kumkum;\n3. Chant Sri Saraswati Stotram and Sri Dakshinamurthy Stotram;\n4. Offer puffed rice (pori), roasted gram, and jaggery.",
        "aliases": [
            {"aliasName": "Ayudha Puja", "aliasType": "REGIONAL", "region": "Tamil Nadu & Karnataka"},
            {"aliasName": "Maha Navami Puja", "aliasType": "REGIONAL", "region": "All India"},
            {"aliasName": "Astra Puja", "aliasType": "REGIONAL", "region": "North India"}
        ],
        "dates": [
            {"gregorianDate": "2025-10-01T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Ashvina Shukla Navami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-10-19T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Ashvina Shukla Navami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-10-09T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Ashvina Shukla Navami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "saraswati-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Hymn to the Goddess of eloquence"},
            {"slug": "dakshinamurthy-stotram", "relationshipType": "CURATED_RECOMMENDATION", "order": 2, "notes": "Teacher of all sciences and arts"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "vijayadashami-dussehra",
        "name": "Vijayadashami / Dussehra",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Durga",
        "description": "The tenth day of victory (Ashvina Shukla Dashami) celebrating the triumph of Dharma over Adharma, Rama over Ravana, and Durga over Mahishasura.",
        "significance": "Considered the most auspicious day of the year to begin new studies (Vidyarambham), music, fine arts, business ventures, and construction.",
        "whatHappensToday": "Children write their first letters in rice or sand (Aksharabhyasam / Vidyarambham). In Karnataka, the grand Mysuru Dasara Jamboo Savari takes place. In North India, effigies of Ravana are burned (Ravan Dahan).",
        "preparationGuide": "1. Perform morning prayer to Goddess Saraswati and reopen study books;\n2. Practice writing sacred mantras in golden sand or unbroken rice grains;\n3. Seek blessings from spiritual teachers, elders, and gurus;\n4. Recite Sri Totakashtakam and Sri Guru Stotram.",
        "aliases": [
            {"aliasName": "Dussehra", "aliasType": "REGIONAL", "region": "North India"},
            {"aliasName": "Dasara", "aliasType": "REGIONAL", "region": "Karnataka & Telangana"},
            {"aliasName": "Vidyarambham Day", "aliasType": "REGIONAL", "region": "Kerala & Tamil Nadu"}
        ],
        "dates": [
            {"gregorianDate": "2025-10-02T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Ashvina Shukla Dashami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-10-20T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Ashvina Shukla Dashami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-10-10T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Ashvina Shukla Dashami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "guru-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Veneration of the guiding teacher"},
            {"slug": "saraswati-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Auspicious beginning of learning"},
            {"slug": "totakashtakam", "relationshipType": "CURATED_RECOMMENDATION", "order": 3, "notes": "Hymn of humble discipleship"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "dhanteras-dhanatrayodashi",
        "name": "Dhanteras (Dhanatrayodashi & Dhanvantari Jayanti)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Lakshmi",
        "description": "The auspicious thirteenth lunar day of Krishna Paksha in Kartika celebrating the appearance of Lord Dhanvantari (the celestial healer) and Goddess Lakshmi.",
        "significance": "Dedicated to physical health, longevity (Arogya), spiritual wealth, and prosperity. Devotees light Yama Deepam at dusk facing south for family protection.",
        "whatHappensToday": "Families purchase sacred metals (brass, silver, or gold) and new cookware. In the evening, lamps are lit in courtyards, and Ayurvedic healers celebrate National Ayurveda Day.",
        "preparationGuide": "1. Cleanse the entire household before sunset;\n2. Light Yama Deepam with sesame oil outside the south door;\n3. Recite Sri Mahalakshmi Ashtakam and Ashta Lakshmi Stotram;\n4. Pray to Lord Dhanvantari for good health and mental clarity.",
        "aliases": [
            {"aliasName": "Dhanatrayodashi", "aliasType": "REGIONAL", "region": "Maharashtra & Gujarat"},
            {"aliasName": "Dhanvantari Jayanti", "aliasType": "TRANSLITERATION", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-10-18T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Kartika Krishna Trayodashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-11-06T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Kartika Krishna Trayodashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-10-27T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Kartika Krishna Trayodashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "mahalakshmi-ashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Evening Lakshmi invocation"},
            {"slug": "chandrasekhara-ashtakam", "relationshipType": "CURATED_RECOMMENDATION", "order": 2, "notes": "Prayer for overcoming illness and fear"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "naraka-chaturdashi",
        "name": "Naraka Chaturdashi (Choti Diwali)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Krishna",
        "description": "Celebration of the vanquishing of demon Narakasura by Lord Krishna and Satyabhama on Kartika Krishna Chaturdashi before dawn.",
        "significance": "Celebrates liberation from demonic oppression and ignorance. In South India, this dawn is the primary Deepavali day celebrated with holy oil bath (Ganga Snanam).",
        "whatHappensToday": "Families rise before sunrise for an auspicious sesame oil bath. Elders apply fragrant oil to heads. Deepavali Marundhu (medicinal Ayurvedic herbal paste) is consumed, followed by bursting crackers.",
        "preparationGuide": "1. Wake up during Brahma Muhurta before sunrise;\n2. Take sacred herbal oil bath invoking the presence of Mother Ganga;\n3. Wear new traditional clothes and light morning earthen lamps;\n4. Chant Sri Govinda Namavali and Sri Achyutashtakam.",
        "aliases": [
            {"aliasName": "Choti Diwali", "aliasType": "REGIONAL", "region": "North India"},
            {"aliasName": "Deepavali Dawn (Ganga Snanam)", "aliasType": "REGIONAL", "region": "Tamil Nadu & South India"},
            {"aliasName": "Roop Chaudas", "aliasType": "REGIONAL", "region": "Rajasthan & Gujarat"}
        ],
        "dates": [
            {"gregorianDate": "2025-10-19T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Kartika Krishna Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-11-07T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Kartika Krishna Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-10-28T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Kartika Krishna Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "govinda-namavali", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Krishna victory chanting"},
            {"slug": "achyutashtakam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Adoration of Achyuta"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "diwali-lakshmi-puja",
        "name": "Deepavali & Sri Mahalakshmi Puja",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Lakshmi",
        "description": "The pan-Indian Festival of Lights on Kartika Amavasya welcoming Goddess Mahalakshmi into illuminated homes and enterprises.",
        "significance": "Celebrates the emergence of Lakshmi during the churning of the cosmic ocean (Samudra Manthana) and the victory of light over spiritual darkness.",
        "whatHappensToday": "Homes are cleaned and decorated with oil lamps (diyas) and rangolis. Families conduct Mahalakshmi and Ganesha Puja during evening Pradosha Muhurta, offering sweets and lighting fireworks.",
        "preparationGuide": "1. Illuminate threshold with ghee lamps;\n2. Perform Lakshmi-Ganesha puja during Pradosha Muhurta;\n3. Chant Sri Mahalakshmi Ashtakam and Ashta Lakshmi Stotram;\n4. Recite Sri Vishnu Dwadasa Nama Panjara Stotram for family welfare.",
        "aliases": [
            {"aliasName": "Diwali", "aliasType": "PHONETIC", "region": "All India"},
            {"aliasName": "Lakshmi Puja", "aliasType": "REGIONAL", "region": "North & West India"},
            {"aliasName": "Deepavali", "aliasType": "TRANSLITERATION", "region": "South India"}
        ],
        "dates": [
            {"gregorianDate": "2025-10-20T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Kartika Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-11-08T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Kartika Amavasya", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-10-29T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Kartika Amavasya", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "mahalakshmi-ashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Padma Purana hymn"},
            {"slug": "ashta-lakshmi-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Eightfold blessings of Mother Lakshmi"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "govardhan-puja-annakut",
        "name": "Govardhan Puja (Annakut)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Krishna",
        "description": "Celebration of Lord Krishna lifting the sacred Govardhan Hill on Kartika Shukla Pratipada to protect the residents and cattle of Braj from torrential storms.",
        "significance": "Demonstrates the power of humble devotion over ritual arrogance (Indra's pride) and emphasizes environmental reverence for mountains, cows, and nature.",
        "whatHappensToday": "Devotees prepare 'Annakut' (a mountain of food comprising 56 different culinary offerings). Cows and calves are bathed, decorated with garlands, and fed fresh fodder.",
        "preparationGuide": "1. Build a symbolic miniature Govardhan hill with cow dung or sacred sweets;\n2. Perform circumambulation (Parikrama) chanting Krishna mantras;\n3. Offer 56 vegetarian delicacies (Chhappan Bhog);\n4. Recite Sri Govinda Namavali and Sri Achyutashtakam.",
        "aliases": [
            {"aliasName": "Annakut", "aliasType": "REGIONAL", "region": "Gujarat & North India"},
            {"aliasName": "Gow Puja", "aliasType": "REGIONAL", "region": "All India"},
            {"aliasName": "Bali Pratipada", "aliasType": "REGIONAL", "region": "Maharashtra & Karnataka"}
        ],
        "dates": [
            {"gregorianDate": "2025-10-21T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Kartika Shukla Pratipada", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-11-09T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Kartika Shukla Pratipada", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-10-30T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Kartika Shukla Pratipada", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "govinda-namavali", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Govardhanadhara Krishna chanting"},
            {"slug": "achyutashtakam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Adoration of the divine cowherd"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "bhai-dooj-yama-dwitiya",
        "name": "Bhai Dooj (Yama Dwitiya)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Surya",
        "description": "Sacred festival celebrating the bond between sisters and brothers on Kartika Shukla Dwitiya, rooted in the Puranic meeting of Lord Yama and his sister Yamuna.",
        "significance": "Sisters pray for the long life, health, and prosperity of their brothers, while brothers bestow gifts and vows of enduring protection.",
        "whatHappensToday": "Sisters apply auspicious vermilion and rice tilak on their brothers' foreheads, perform aarti, and serve homemade festive meals.",
        "preparationGuide": "1. Prepare auspicious thali with lamp, sweets, and sandalwood tilak;\n2. Apply protective tilak to brother's forehead chanting prayer for longevity;\n3. Recite Sri Aditya Hridaya Stotram for solar vitality and protection;\n4. Share traditional festive feast.",
        "aliases": [
            {"aliasName": "Yama Dwitiya", "aliasType": "REGIONAL", "region": "All India"},
            {"aliasName": "Bhai Tika", "aliasType": "REGIONAL", "region": "Nepal & North India"},
            {"aliasName": "Bhau Beej", "aliasType": "REGIONAL", "region": "Maharashtra"},
            {"aliasName": "Bhai Phonta", "aliasType": "REGIONAL", "region": "West Bengal"}
        ],
        "dates": [
            {"gregorianDate": "2025-10-22T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Kartika Shukla Dwitiya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-11-10T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Kartika Shukla Dwitiya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-10-31T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Kartika Shukla Dwitiya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "aditya-hridaya-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Prayer for brother's longevity and health"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "chhath-puja",
        "name": "Chhath Puja (Surya Shashthi)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Surya",
        "description": "Ancient Vedic austerity dedicated to Lord Surya and Chhathi Maiya observed on Kartika Shukla Shashthi with strict 36-hour waterless fasting.",
        "significance": "Celebrates the life-giving Sun as the visible embodiment of the Divine (Pratyaksha Devata), promoting environmental purity, longevity, and family well-being.",
        "whatHappensToday": "Devotees stand waist-deep in sacred river waters during sunset (Sandhya Arghya) and sunrise (Usha Arghya) offering bamboo soop trays filled with Thekua, sugarcane, and coconut.",
        "preparationGuide": "1. Observe strict purity and non-violence during the 4-day vrata;\n2. Prepare traditional Thekua in pure ghee on clay stove;\n3. Offer Sandhya and Usha Arghyam in flowing water;\n4. Recite Sri Aditya Hridaya Stotram facing the Sun.",
        "aliases": [
            {"aliasName": "Surya Shashthi", "aliasType": "REGIONAL", "region": "Bihar & UP"},
            {"aliasName": "Dala Chhath", "aliasType": "REGIONAL", "region": "Eastern India"},
            {"aliasName": "Chhathi", "aliasType": "ABBREVIATION", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-10-27T00:00:00.000Z", "year": 2025, "region": "Bihar / Eastern India / All India", "calendarConvention": "Kartika Shukla Shashthi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-11-15T00:00:00.000Z", "year": 2026, "region": "Bihar / Eastern India / All India", "calendarConvention": "Kartika Shukla Shashthi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-11-05T00:00:00.000Z", "year": 2027, "region": "Bihar / Eastern India / All India", "calendarConvention": "Kartika Shukla Shashthi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "aditya-hridaya-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Sun God salutation while in water"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "karthigai-deepam",
        "name": "Karthigai Deepam",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Shiva",
        "description": "Ancient festival of divine light observed in the Tamil month of Karthigai when Krittika nakshatra coincides with Pournami, especially renowned at Tiruvannamalai.",
        "significance": "Commemorates the appearance of Lord Shiva as the beginningless, endless column of cosmic fire (Arunachala Annamalaiyar) transcending the comprehension of Brahma and Vishnu.",
        "whatHappensToday": "Rows of terracotta oil lamps (Agal Vilakku) are lit along every doorway, window, and street. At sunset, the colossal Maha Deepam is ignited atop the sacred Arunachala hill.",
        "preparationGuide": "1. Cleanse and arrange dozens of traditional clay oil lamps;\n2. Pour sesame oil and place cotton wicks in all lamps;\n3. Light lamps simultaneously as the evening temple bell tolls;\n4. Chant Sri Lingashtakam and Shiva Panchakshari Stotram.",
        "aliases": [
            {"aliasName": "Thiruvannamalai Deepam", "aliasType": "REGIONAL", "region": "Tamil Nadu"},
            {"aliasName": "Karthika Deepam", "aliasType": "PHONETIC", "region": "Andhra Pradesh & Kerala"}
        ],
        "dates": [
            {"gregorianDate": "2025-12-04T00:00:00.000Z", "year": 2025, "region": "Tamil Nadu & Kerala", "calendarConvention": "Karthigai Pournami / Krittika Nakshatra", "verificationStatus": "VERIFIED", "sourceReference": "Tiruvannamalai Temple Calendar 2025"},
            {"gregorianDate": "2026-11-24T00:00:00.000Z", "year": 2026, "region": "Tamil Nadu & Kerala", "calendarConvention": "Karthigai Pournami / Krittika Nakshatra", "verificationStatus": "VERIFIED", "sourceReference": "Tiruvannamalai Temple Calendar 2026"},
            {"gregorianDate": "2027-12-13T00:00:00.000Z", "year": 2027, "region": "Tamil Nadu & Kerala", "calendarConvention": "Karthigai Pournami / Krittika Nakshatra", "verificationStatus": "VERIFIED", "sourceReference": "Tiruvannamalai Temple Calendar 2027"}
        ],
        "slokaSlugs": [
            {"slug": "lingashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Hymn to the infinite Lingam of light"},
            {"slug": "shiva-panchakshari-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Panchakshari chanting"}
        ],
        "sourceFile": "TAMIL.pdf"
    },
    {
        "slug": "tulsi-vivah",
        "name": "Tulsi Vivah",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Ceremonial wedding of sacred plant Goddess Tulsi (Vrinda) with Lord Shaligram / Vishnu on Kartika Shukla Dwadashi.",
        "significance": "Signifies the awakening of Lord Vishnu from His four-month slumber (Chaturmasya) and the formal inauguration of the Hindu wedding season.",
        "whatHappensToday": "The Tulsi Vrindavan is painted, adorned with sugarcane stalks, and draped like a bride. Shaligram Shila is brought in procession, and wedding vows are chanted by priests.",
        "preparationGuide": "1. Clean and decorate the Tulsi plant with turmeric and red cloth;\n2. Place holy Shaligram or Krishna murti near the altar;\n3. Recite Sri Vishnu Sahasranamam and Achyutashtakam;\n4. Offer seasonal fruits, tamarind, amla, and sugarcane.",
        "aliases": [
            {"aliasName": "Dev Uthani Vivah", "aliasType": "REGIONAL", "region": "North India"},
            {"aliasName": "Tulsi Kalyanam", "aliasType": "REGIONAL", "region": "South India"}
        ],
        "dates": [
            {"gregorianDate": "2025-11-02T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Kartika Shukla Dwadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-11-21T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Kartika Shukla Dwadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-11-10T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Kartika Shukla Dwadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "achyutashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Krishna wedding adoration"},
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Holy parayanam"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "dev-deepawali",
        "name": "Dev Deepawali (Tripurotsav)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Shiva",
        "description": "The Festival of Lights of the Gods observed on Kartika Purnima in Varanasi celebrating Lord Shiva's victory over the demon Tripurasura.",
        "significance": "Tradition holds that all the gods descend from heaven to bathe in the holy Ganga and light lamps along the ghats in thanksgiving to Mahadeva.",
        "whatHappensToday": "Over one million clay lamps (diyas) illuminate the 84 ghats of Kashi from Assi to Rajghat. Massive Maha Aarti takes place at Dashashwamedh Ghat.",
        "preparationGuide": "1. Take a holy morning bath in flowing water or sprinkle Ganga jal;\n2. Light earthen lamps at sunset facing east;\n3. Recite Sri Shiva Tandava Stotram and Sri Chandrasekhara Ashtakam;\n4. Chant Sri Lingashtakam for Shiva's supreme grace.",
        "aliases": [
            {"aliasName": "Kashi Dev Diwali", "aliasType": "REGIONAL", "region": "Varanasi / UP"},
            {"aliasName": "Tripura Purnima", "aliasType": "REGIONAL", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-11-05T00:00:00.000Z", "year": 2025, "region": "Varanasi & All India", "calendarConvention": "Kartika Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Kashi Vishwanath Ephemeris 2025"},
            {"gregorianDate": "2026-11-24T00:00:00.000Z", "year": 2026, "region": "Varanasi & All India", "calendarConvention": "Kartika Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Kashi Vishwanath Ephemeris 2026"},
            {"gregorianDate": "2027-11-13T00:00:00.000Z", "year": 2027, "region": "Varanasi & All India", "calendarConvention": "Kartika Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Kashi Vishwanath Ephemeris 2027"}
        ],
        "slokaSlugs": [
            {"slug": "siva-tandava-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Shiva's destruction of Tripurasura"},
            {"slug": "lingashtakam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Kashi Vishwanath adoration"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "vaikunta-ekadashi",
        "name": "Vaikunta Ekadashi (Mukkoti Ekadashi)",
        "category": "Ekadashi",
        "institutionCode": None,
        "primaryDeity": "Venkateswara",
        "description": "Supreme Ekadashi occurring during solar Dhanur / Margazhi month, celebrated at Tirumala, Srirangam, and Vaishnava temples worldwide.",
        "significance": "Tradition holds that the heavenly gates of Vaikunta (Paramapada Vasal) open on this auspicious dawn. Devotees observe strict fasting to transcend material bondage.",
        "whatHappensToday": "Temple gates open before dawn for Paramapada Vasal Darshan. Devotees observe strict waterless or fruit fasting, engage in all-night Vishnu parayanam, and avoid grains.",
        "preparationGuide": "1. Observe fasting on Ekadashi tithi;\n2. Recite Sri Vishnu Sahasranamam in the morning;\n3. Chant Sri Venkateswara Stotram and Sri Venkateswara Prapatti;\n4. Join community congregational singing of Sri Govinda Namavali;\n5. Recite Sri Sudarshana Ashtakam for protection.",
        "aliases": [
            {"aliasName": "Mukkoti Ekadashi", "aliasType": "REGIONAL", "region": "Andhra Pradesh & Telangana"},
            {"aliasName": "Swarga Vathil Ekadashi", "aliasType": "REGIONAL", "region": "Kerala"},
            {"aliasName": "Paramapada Vasal Day", "aliasType": "REGIONAL", "region": "Tamil Nadu"}
        ],
        "dates": [
            {"gregorianDate": "2025-12-31T00:00:00.000Z", "year": 2025, "region": "All India / South India", "calendarConvention": "Solar Dhanur / Drik Ganita", "verificationStatus": "VERIFIED", "sourceReference": "TTD Panchangam 2025"},
            {"gregorianDate": "2026-12-20T00:00:00.000Z", "year": 2026, "region": "All India / South India", "calendarConvention": "Solar Dhanur / Drik Ganita", "verificationStatus": "VERIFIED", "sourceReference": "TTD Panchangam 2026"},
            {"gregorianDate": "2027-12-09T00:00:00.000Z", "year": 2027, "region": "All India / South India", "calendarConvention": "Solar Dhanur / Drik Ganita", "verificationStatus": "VERIFIED", "sourceReference": "TTD Panchangam 2027"}
        ],
        "slokaSlugs": [
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Morning Sahasranama parayanam"},
            {"slug": "maha-vishnu-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Garudagamana stotram"},
            {"slug": "venkateswara-stotram", "relationshipType": "TRADITIONAL", "order": 3, "notes": "Praise of Lord of Seven Hills"},
            {"slug": "venkateswara-prapatti", "relationshipType": "TRADITIONAL", "order": 4, "notes": "Total self-surrender"},
            {"slug": "govinda-namavali", "relationshipType": "TRADITIONAL", "order": 5, "notes": "Congregational singing"},
            {"slug": "sudarshana-ashtakam", "relationshipType": "CURATED_RECOMMENDATION", "order": 6, "notes": "Protection against distress"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "gita-jayanti",
        "name": "Gita Jayanti",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Krishna",
        "description": "Celebration of the birth of the Srimad Bhagavad Gita on Margashirsha Shukla Ekadashi on the sacred battlefield of Kurukshetra.",
        "significance": "Honors the supreme philosophical scripture given by Lord Krishna to Arjuna, containing timeless wisdom on Dharma, self-mastery, non-attachment, and Bhakti.",
        "whatHappensToday": "Temples and ashrams conduct continuous recitations of all 700 verses of the Bhagavad Gita. Devotees distribute copies of the scripture and hold spiritual symposia.",
        "preparationGuide": "1. Recite the Bhagavad Gita Dhyana Slokas;\n2. Chant Chapter 12 (Bhakti Yoga) and Chapter 15 (Purushottama Yoga);\n3. Contemplate Krishna's teaching on performing duty without attachment;\n4. Chant Sri Govinda Namavali and Sri Achyutashtakam.",
        "aliases": [
            {"aliasName": "Mokshada Ekadashi", "aliasType": "REGIONAL", "region": "All India"},
            {"aliasName": "Bhagavad Gita Jayanti", "aliasType": "TRANSLITERATION", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-12-01T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Margashirsha Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-12-20T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Margashirsha Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-12-09T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Margashirsha Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "govinda-namavali", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Krishna Partha Sarathi adoration"},
            {"slug": "achyutashtakam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Divine charioteer praise"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "datta-jayanti",
        "name": "Sri Datta Jayanti",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Dattatreya",
        "description": "Appearance day of Lord Dattatreya, the unified incarnation of the Hindu Trinity (Brahma, Vishnu, and Shiva), on Margashirsha Purnima.",
        "significance": "Celebrates the supreme Avadhuta master who learned spiritual lessons from 24 natural gurus (the earth, wind, ocean, spider, etc.), symbolizing pure wisdom.",
        "whatHappensToday": "Celebrated with great devotion in Maharashtra, Karnataka, and Andhra at pilgrimage sites like Ganagapur, Narsobawadi, and Kuravpur with continuous Guru Charitra recitations.",
        "preparationGuide": "1. Meditate on the three-headed form of Lord Dattatreya;\n2. Recite Sri Guru Stotram and Sri Gurvashtakam;\n3. Chant Sri Dakshinamurthy Stotram for non-dual enlightenment;\n4. Feed animals and birds in honor of Dattatreya's 24 teachers.",
        "aliases": [
            {"aliasName": "Dattatreya Jayanti", "aliasType": "TRANSLITERATION", "region": "All India"},
            {"aliasName": "Datta Purnima", "aliasType": "REGIONAL", "region": "Maharashtra & Karnataka"}
        ],
        "dates": [
            {"gregorianDate": "2025-12-04T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Margashirsha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-12-23T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Margashirsha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-12-13T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Margashirsha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "guru-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Salutations to the primordial Guru"},
            {"slug": "gurvashtakam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Eight stanzas on the lotus feet of the teacher"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "makar-sankranti-pongal",
        "name": "Makar Sankranti & Pongal",
        "category": "Sankranti Observance",
        "institutionCode": None,
        "primaryDeity": "Surya",
        "description": "Sacred solar ingress marking the Sun's entry into Makara (Capricorn) and the start of Uttarayana (the celestial northern journey).",
        "significance": "Celebrates agricultural harvest, cosmic vitality of Lord Surya, and thanksgiving to cows and nature. Known regionally as Pongal, Uttarayan, Maghi, and Khichdi.",
        "whatHappensToday": "Families boil freshly harvested rice and milk in clay pots until it overflows shouting 'Pongalo Pongal!'. Sesame and jaggery sweets (Til-Gul) are shared saying 'Til-gul ghya, god-god bola'.",
        "preparationGuide": "1. Rise before dawn and take a sacred bath;\n2. Offer water (Arghyam) to Lord Surya while chanting Sri Aditya Hridaya Stotram;\n3. Prepare sweet Pongal with new rice, jaggery, and ghee;\n4. Share til-jaggery sweets to promote goodwill and harmony.",
        "aliases": [
            {"aliasName": "Thai Pongal", "aliasType": "REGIONAL", "region": "Tamil Nadu"},
            {"aliasName": "Uttarayan", "aliasType": "REGIONAL", "region": "Gujarat"},
            {"aliasName": "Pedda Panduga", "aliasType": "REGIONAL", "region": "Andhra Pradesh & Telangana"},
            {"aliasName": "Makara Sankramana", "aliasType": "REGIONAL", "region": "Karnataka"}
        ],
        "dates": [
            {"gregorianDate": "2025-01-14T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Solar Makara Transit", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-01-14T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Solar Makara Transit", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-01-14T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Solar Makara Transit", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "aditya-hridaya-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Sun God worship during Uttarayana onset"},
            {"slug": "maha-vishnu-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Cosmic preserver adoration"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "vasant-panchami",
        "name": "Vasant Panchami (Saraswati Jayanti)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Saraswati",
        "description": "Celebration of the advent of Spring (Ritu Vasanta) and the appearance of Goddess Saraswati on Magha Shukla Panchami.",
        "significance": "Honors the arrival of blossoming nature, literary arts, musical genius, and cognitive brilliance. Devotees dress in auspicious bright yellow.",
        "whatHappensToday": "Children are initiated into writing and reading. Musical instruments are tuned and played before Goddess Saraswati. Yellow rice seasoned with saffron is cooked and distributed.",
        "preparationGuide": "1. Wear clean yellow attire symbolizing spring radiance;\n2. Place textbooks and notebooks at the feet of Goddess Saraswati;\n3. Recite Sri Saraswati Stotram for memory and wisdom;\n4. Chant Sri Dakshinamurthy Stotram for spiritual understanding.",
        "aliases": [
            {"aliasName": "Saraswati Jayanti", "aliasType": "REGIONAL", "region": "All India"},
            {"aliasName": "Basant Panchami", "aliasType": "PHONETIC", "region": "North India"},
            {"aliasName": "Sri Panchami", "aliasType": "REGIONAL", "region": "West Bengal"}
        ],
        "dates": [
            {"gregorianDate": "2025-02-02T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Magha Shukla Panchami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-01-23T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Magha Shukla Panchami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-02-11T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Magha Shukla Panchami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "saraswati-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Hymn to Goddess of speech and arts"},
            {"slug": "dakshinamurthy-stotram", "relationshipType": "CURATED_RECOMMENDATION", "order": 2, "notes": "Supreme teacher of metaphysics"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "ratha-saptami",
        "name": "Ratha Saptami (Surya Jayanti)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Surya",
        "description": "Celebration of the appearance of Lord Surya aboard His chariot driven by Aruna on Magha Shukla Saptami, symbolizing the turning of the cosmic wheels.",
        "significance": "Celebrated across India and particularly at Tirumala (where Lord Malayappa Swami rides seven distinct vahanas in one single day). Invoked for radiant health and curing ailments.",
        "whatHappensToday": "Devotees take early morning baths with seven Calotropis (Erukku / Arka) leaves placed upon head and shoulders while chanting solar mantras.",
        "preparationGuide": "1. Collect sacred Arka leaves for the ceremonial morning bath;\n2. Recite the Arka Snana mantra wishing for freedom from diseases;\n3. Chant Sri Aditya Hridaya Stotram facing the morning sun;\n4. Offer sweet milk porridge (Ksheerannam) boiled on open stove.",
        "aliases": [
            {"aliasName": "Surya Jayanti", "aliasType": "TRANSLITERATION", "region": "All India"},
            {"aliasName": "Magha Saptami", "aliasType": "REGIONAL", "region": "South India"}
        ],
        "dates": [
            {"gregorianDate": "2025-02-04T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Magha Shukla Saptami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-01-25T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Magha Shukla Saptami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-02-13T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Magha Shukla Saptami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "aditya-hridaya-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Agastya's solar hymn of invincibility"},
            {"slug": "venkateswara-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Tirumala Ratha Saptami celebration"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "holi-festival-of-colors",
        "name": "Holi (Holika Dahan & Rangwali Holi)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Joyous celebration of Spring on Phalguna Purnima marking the triumph of Bhakta Prahlada's devotion over Holika and Hiranyakashipu.",
        "significance": "Celebrates the burning of evil desires in the sacred Holika bonfire, and the joyful sprinkling of natural vibrant colors celebrating Lord Krishna's divine sports in Braj.",
        "whatHappensToday": "On the eve, the community lights the Holika Dahan bonfire with coconut and grain offerings. Next morning, people play with dry organic colors (Gulal), sharing Gujiya and thandai.",
        "preparationGuide": "1. Participate in the evening Holika Dahan bonfire offering coconuts;\n2. Chant Sri Narasimha Jayanti / Prahlada stotras for spiritual fortitude;\n3. Play with herbal, skin-friendly natural colors;\n4. Recite Sri Govinda Namavali celebrating Krishna's joy.",
        "aliases": [
            {"aliasName": "Holika Dahan", "aliasType": "REGIONAL", "region": "North India"},
            {"aliasName": "Rangwali Holi / Dhuleti", "aliasType": "REGIONAL", "region": "North & West India"},
            {"aliasName": "Dol Jatra", "aliasType": "REGIONAL", "region": "West Bengal"},
            {"aliasName": "Kamadahana", "aliasType": "REGIONAL", "region": "South India"}
        ],
        "dates": [
            {"gregorianDate": "2025-03-14T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Phalguna Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-03-04T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Phalguna Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-03-22T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Phalguna Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "govinda-namavali", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Krishna Braj Holi songs"},
            {"slug": "maha-vishnu-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Salutations to the protector of Prahlada"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "rang-panchami",
        "name": "Rang Panchami",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Krishna",
        "description": "Culmination of color festivities on Chaitra Krishna Panchami celebrated widely in Maharashtra, Madhya Pradesh, and Rajasthan.",
        "significance": "Celebrates the subtle victory of sattvic joy and the activation of the five cosmic elements (Pancha Tattva) through divine sound and colors.",
        "whatHappensToday": "Celebrated with gulal and processions in cities like Indore and across Maharashtra, singing devotional songs in honor of Radha and Krishna.",
        "preparationGuide": "1. Chant Sri Govinda Namavali and Sri Achyutashtakam;\n2. Offer fragrant sandalwood paste and gulal to Krishna and Radha altar;\n3. Maintain harmonious spiritual fellowship.",
        "aliases": [
            {"aliasName": "Ranga Panchami", "aliasType": "PHONETIC", "region": "Maharashtra & MP"}
        ],
        "dates": [
            {"gregorianDate": "2025-03-19T00:00:00.000Z", "year": 2025, "region": "Maharashtra & MP", "calendarConvention": "Chaitra Krishna Panchami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-03-08T00:00:00.000Z", "year": 2026, "region": "Maharashtra & MP", "calendarConvention": "Chaitra Krishna Panchami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-03-27T00:00:00.000Z", "year": 2027, "region": "Maharashtra & MP", "calendarConvention": "Chaitra Krishna Panchami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "achyutashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Praise of Krishna's charm and grace"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "akshaya-tritiya",
        "name": "Akshaya Tritiya (Akha Teej)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Lakshmi",
        "description": "The day of inexhaustible virtue and fortune (Akshaya) occurring on Vaisakha Shukla Tritiya, ruled by Lord Vishnu and Goddess Lakshmi.",
        "significance": "Marks the start of the Treta Yuga, the birthday of Lord Parashurama, and the appearance of the holy river Ganga on earth. Deeds of charity performed today yield eternal fruit.",
        "whatHappensToday": "Devotees donate cold water pots (Udaki Kumbha), barley, wheat, umbrellas, and food. Temples of Lord Venkateswara and Puri Jagannath begin Chandan Yatra.",
        "preparationGuide": "1. Perform acts of charity (Anna Daanam / water distribution);\n2. Recite Sri Mahalakshmi Ashtakam and Ashta Lakshmi Stotram;\n3. Chant Sri Vishnu Sahasranamam for inexhaustible spiritual peace;\n4. Begin auspicious investments, studies, or spiritual disciplines.",
        "aliases": [
            {"aliasName": "Akha Teej", "aliasType": "REGIONAL", "region": "Rajasthan & North India"},
            {"aliasName": "Parashurama Jayanti", "aliasType": "REGIONAL", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-04-30T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Vaisakha Shukla Tritiya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-04-19T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Vaisakha Shukla Tritiya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-05-09T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Vaisakha Shukla Tritiya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "mahalakshmi-ashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Lakshmi's inexhaustible grace"},
            {"slug": "ashta-lakshmi-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Eight spiritual wealths"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "narasimha-jayanti",
        "name": "Sri Narasimha Jayanti",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Narasimha",
        "description": "Appearance day of Lord Narasimha, the half-man half-lion divine avatar of Vishnu, who emerged from a pillar at twilight on Vaisakha Shukla Chaturdashi.",
        "significance": "Celebrates the ultimate protection of humble seekers (Bhakta Prahlada) and the triumph of pure righteousness over arrogant oppression.",
        "whatHappensToday": "Devotees observe fasting until sunset (Sayankala / Pradosha). Special abhishekam with panchamrita is offered to Lord Narasimha.",
        "preparationGuide": "1. Fast during the day until twilight sunset;\n2. Meditate on the fearless form of Lord Narasimha;\n3. Recite Sri Sudarshana Ashtakam and Sri Vishnu Sahasranamam;\n4. Pray for freedom from existential dread and inner afflictions.",
        "aliases": [
            {"aliasName": "Narasimha Chaturdashi", "aliasType": "REGIONAL", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-05-11T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Vaisakha Shukla Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-05-01T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Vaisakha Shukla Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-05-19T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Vaisakha Shukla Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "sudarshana-ashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Protective discus of Narasimha"},
            {"slug": "vishnu-dwadasa-nama-panjara-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Twelve names armor"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "vat-savitri-vrat",
        "name": "Vat Savitri Vrat",
        "category": "Vratam",
        "institutionCode": None,
        "primaryDeity": "Savitri",
        "description": "Solemn vrata observed by married women worshipping the sacred Banyan tree (Vata Vriksha) and remembering Savitri's unwavering devotion that brought Satyavan back from Yama.",
        "significance": "Honors wifely devotion, longevity of family members, marital harmony, and the enduring resilience of the eternal Banyan tree.",
        "whatHappensToday": "Women fast and tie sacred yellow and red threads around the Banyan tree trunk, circumambulating it seven times while offering fruits, soaked chana, and water.",
        "preparationGuide": "1. Rise early and bathe in traditional attire;\n2. Visit a sacred Banyan tree with offering tray;\n3. Circumambulate the tree 7 times tying sacred protective thread;\n4. Listen to the sacred Savitri-Satyavan katha.",
        "aliases": [
            {"aliasName": "Vat Purnima", "aliasType": "REGIONAL", "region": "Maharashtra & Gujarat"},
            {"aliasName": "Vat Savitri Amavasya", "aliasType": "REGIONAL", "region": "North India"}
        ],
        "dates": [
            {"gregorianDate": "2025-05-27T00:00:00.000Z", "year": 2025, "region": "North India (Amavasya)", "calendarConvention": "Jyeshtha Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2025-06-11T00:00:00.000Z", "year": 2025, "region": "Maharashtra & Gujarat (Purnima)", "calendarConvention": "Jyeshtha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-05-16T00:00:00.000Z", "year": 2026, "region": "North India (Amavasya)", "calendarConvention": "Jyeshtha Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-05-31T00:00:00.000Z", "year": 2026, "region": "Maharashtra & Gujarat (Purnima)", "calendarConvention": "Jyeshtha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-06-04T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Jyeshtha Vrata", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "mahalakshmi-ashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Prayer for marital auspiciousness and abundance"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "guru-purnima",
        "name": "Guru Purnima (Vyasa Purnima)",
        "category": "Purnima Observance",
        "institutionCode": None,
        "primaryDeity": "Guru",
        "description": "The sacred full-moon day of Ashadha honoring spiritual masters, teachers, and Sage Veda Vyasa, the compiler of the Vedas.",
        "significance": "Commencement of Chaturmasya retreat where seekers rededicate their minds to self-study, reflection, and surrender to the Guru.",
        "whatHappensToday": "Devotees worship the sacred Padukas (sandals) of their Gurus, offer fresh flowers, listen to spiritual discourses, and take vows of sadhana.",
        "preparationGuide": "1. Meditate on the spiritual teacher at dawn;\n2. Perform Guru Paduka Puja while chanting Sri Guru Paduka Stotram;\n3. Recite Sri Guru Stotram and Sri Gurvashtakam;\n4. Contemplate Sri Dakshinamurthy Stotram for Vedantic non-dual wisdom.",
        "aliases": [
            {"aliasName": "Vyasa Purnima", "aliasType": "REGIONAL", "region": "All India"},
            {"aliasName": "Guru Pooja Day", "aliasType": "TRANSLITERATION", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-07-10T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Ashadha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Indian Astronomical Ephemeris 2025"},
            {"gregorianDate": "2026-07-29T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Ashadha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Indian Astronomical Ephemeris 2026"},
            {"gregorianDate": "2027-07-18T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Ashadha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Indian Astronomical Ephemeris 2027"}
        ],
        "slokaSlugs": [
            {"slug": "guru-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Salutations to the Guru"},
            {"slug": "gurvashtakam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Cultivating spiritual humility"},
            {"slug": "guru-paduka-stotram", "relationshipType": "TRADITIONAL", "order": 3, "notes": "Adoration of sacred padukas"},
            {"slug": "dakshinamurthy-stotram", "relationshipType": "CURATED_RECOMMENDATION", "order": 4, "notes": "Vedantic contemplation"},
            {"slug": "totakashtakam", "relationshipType": "CURATED_RECOMMENDATION", "order": 5, "notes": "Devoted surrender to master"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "nag-panchami",
        "name": "Nag Panchami",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Shiva",
        "description": "Sacred day of reverence to the serpent deities (Nagas) observed on Shravana Shukla Panchami.",
        "significance": "Honors the coiled serpent power (Kundalini Shakti), Lord Shiva who wears Vasuki as an ornament, and Lord Vishnu reclining on Adi Shesha. Promotes conservation of wildlife and nature.",
        "whatHappensToday": "Devotees worship clay or stone Naga sculptures under peepal trees, offering milk, turmeric, flowers, and puffed rice (lawa).",
        "preparationGuide": "1. Cleanse home threshold and draw sacred snake motifs in rice powder;\n2. Offer fresh unboiled milk and turmeric at Naga shrines;\n3. Recite Sri Shiva Panchakshari Stotram and Bilvashtakam;\n4. Pray for protection of family from poisonous creatures and planetary afflictions (Sarpa Dosha).",
        "aliases": [
            {"aliasName": "Nagara Panchami", "aliasType": "REGIONAL", "region": "Karnataka & Andhra Pradesh"},
            {"aliasName": "Nagula Chavithi / Panchami", "aliasType": "REGIONAL", "region": "South India"}
        ],
        "dates": [
            {"gregorianDate": "2025-07-29T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Shravana Shukla Panchami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-08-17T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Shravana Shukla Panchami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-08-07T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Shravana Shukla Panchami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "shiva-panchakshari-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Shiva with serpent necklace adoration"},
            {"slug": "bilvashtakam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Bilva archana"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "raksha-bandhan",
        "name": "Raksha Bandhan & Avani Avittam (Hayagriva Jayanti)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Celebration of the sacred bond of protection and fraternal love on Shravana Purnima, coinciding with the renewal of the sacred thread (Upakarma).",
        "significance": "Sisters tie the protective Rakhi thread on brothers' wrists; brahmacharis and householders renew their spiritual vows during Upakarma; devotees celebrate the appearance of Lord Hayagriva.",
        "whatHappensToday": "Sacred thread change (Yagnopaveetha Dharanam) at dawn, followed by Gayathri Japa on the subsequent day. Sisters tie Rakhis, exchange sweets, and receive blessings.",
        "preparationGuide": "1. Perform early morning Gayatri Japa and sacred thread renewal;\n2. Pray to Lord Hayagriva for literary and intellectual mastery;\n3. Tie protective Rakhi with the ancient mantra 'Yena Baddho Bali Raja';\n4. Distribute sweet coconut laddoos and traditional delicacies.",
        "aliases": [
            {"aliasName": "Avani Avittam", "aliasType": "REGIONAL", "region": "Tamil Nadu & Kerala"},
            {"aliasName": "Shravani Upakarma", "aliasType": "REGIONAL", "region": "All India"},
            {"aliasName": "Rakhi Purnima", "aliasType": "PHONETIC", "region": "North India"}
        ],
        "dates": [
            {"gregorianDate": "2025-08-09T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Shravana Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-08-28T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Shravana Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-08-17T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Shravana Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Holy parayanam on Upakarma"},
            {"slug": "maha-vishnu-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Lord Hayagriva adoration"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "onam-thiruvonam",
        "name": "Onam (Thiruvonam)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Grand cultural and harvest festival of Kerala celebrating the annual visit of righteous King Mahabali and the grace of Vamana Avatara.",
        "significance": "A ten-day celebration of equality, boundless generosity, and communal harmony under the radiant star Thiruvonam in the Malayalam month of Chingam.",
        "whatHappensToday": "Intricate flower carpets (Pookkalam) are created in every courtyard. Families dress in Kasavu mundu, feast on the 26-dish Onam Sadya served on banana leaves, and enjoy Vallam Kali (boat races).",
        "preparationGuide": "1. Lay fresh multi-colored Pookkalam in threshold at dawn;\n2. Consecrate Thrikkakara Appan (clay pyramid representing Vamana);\n3. Recite Sri Vishnu Sahasranamam and Achyutashtakam;\n4. Partake in collective community Onasadya.",
        "aliases": [
            {"aliasName": "Thiruvonam", "aliasType": "REGIONAL", "region": "Kerala"},
            {"aliasName": "Kerala Harvest Festival", "aliasType": "TRANSLITERATION", "region": "Kerala"}
        ],
        "dates": [
            {"gregorianDate": "2025-09-05T00:00:00.000Z", "year": 2025, "region": "Kerala & All India", "calendarConvention": "Chingam Thiruvonam Star", "verificationStatus": "VERIFIED", "sourceReference": "Kerala Government Calendar 2025"},
            {"gregorianDate": "2026-08-26T00:00:00.000Z", "year": 2026, "region": "Kerala & All India", "calendarConvention": "Chingam Thiruvonam Star", "verificationStatus": "VERIFIED", "sourceReference": "Kerala Government Calendar 2026"},
            {"gregorianDate": "2027-09-12T00:00:00.000Z", "year": 2027, "region": "Kerala & All India", "calendarConvention": "Chingam Thiruvonam Star", "verificationStatus": "VERIFIED", "sourceReference": "Kerala Government Calendar 2027"}
        ],
        "slokaSlugs": [
            {"slug": "maha-vishnu-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Vamana Avatar adoration"},
            {"slug": "govinda-namavali", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Celebration of divine grace"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "hartalika-teej",
        "name": "Hartalika Teej",
        "category": "Vratam",
        "institutionCode": None,
        "primaryDeity": "Shiva",
        "description": "Austerity observed by women on Bhadrapada Shukla Tritiya commemorating Goddess Parvati's intense tapasya to attain Lord Shiva as Her divine consort.",
        "significance": "Celebrates indomitable determination, purity of heart, and devotion in marriage. Women observe Nirjala (waterless) fasting throughout the day and night.",
        "whatHappensToday": "Clay idols of Shiva and Parvati are sculpted and worshipped with bilva leaves and marigold flowers. Women wear green or red attire and stay awake singing devotional bhajans.",
        "preparationGuide": "1. Sculpt clay Shiva-Parvati idols and install on clean altar;\n2. Observe waterless fast;\n3. Recite Sri Shiva Panchakshari and Sri Bilvashtakam;\n4. Read Hartalika Vrata Katha during evening puja.",
        "aliases": [
            {"aliasName": "Teej", "aliasType": "ABBREVIATION", "region": "North India"},
            {"aliasName": "Hartalika Vrat", "aliasType": "REGIONAL", "region": "Rajasthan, UP, Bihar"}
        ],
        "dates": [
            {"gregorianDate": "2025-08-26T00:00:00.000Z", "year": 2025, "region": "North India", "calendarConvention": "Bhadrapada Shukla Tritiya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-09-13T00:00:00.000Z", "year": 2026, "region": "North India", "calendarConvention": "Bhadrapada Shukla Tritiya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-09-03T00:00:00.000Z", "year": 2027, "region": "North India", "calendarConvention": "Bhadrapada Shukla Tritiya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "shiva-panchakshari-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Shiva-Parvati communion"},
            {"slug": "bilvashtakam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Bilva patra offering"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "vishwakarma-puja",
        "name": "Vishwakarma Puja (Kanya Sankranti)",
        "category": "Sankranti Observance",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Sacred observance honoring Lord Vishwakarma, the divine architect, engineer, and craftsman of the universe, on Kanya Sankranti.",
        "significance": "Celebrates innovation, engineering skills, craftsmanship, machine safety, and industrial productivity across factories, workshops, and engineering institutes.",
        "whatHappensToday": "Industrial plants, technical tools, computers, and mechanical machinery are cleansed and anointed. Special havan offerings are conducted for occupational safety and technical progress.",
        "preparationGuide": "1. Cleanse workshops, tool benches, and computing devices;\n2. Apply sandalwood paste and sacred red ribbon;\n3. Chant prayers for mechanical safety and innovative intellect;\n4. Distribute sweets among artisans, technicians, and engineers.",
        "aliases": [
            {"aliasName": "Kanya Sankranti", "aliasType": "REGIONAL", "region": "All India"},
            {"aliasName": "National Engineers Day of Tradition", "aliasType": "TRANSLITERATION", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-09-17T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Solar Kanya Sankranti", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-09-17T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Solar Kanya Sankranti", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-09-17T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Solar Kanya Sankranti", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "mahaganapathi-dhyanam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Invocation of technical clarity and obstacle removal"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "pitru-paksha-mahalaya",
        "name": "Pitru Paksha & Mahalaya Amavasya",
        "category": "Amavasya Observance",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Sixteen-day sacred lunar period from Bhadrapada Purnima to Ashvina Amavasya dedicated to remembering and offering gratitude to departed ancestors (Pitrus).",
        "significance": "Acknowledges ancestral debts (Pitru Rina), expressing filial reverence through holy water (Tarpanam) with black sesame seeds, and feeding cows, birds, and the underprivileged.",
        "whatHappensToday": "Sacred rites of Tarpanam and Pinda Daan are performed on riverbanks (Ganga, Cauvery, Godavari). Mahalaya Amavasya is the grand culmination when all ancestors are invoked.",
        "preparationGuide": "1. Perform Tarpanam before noon with black sesame and sacred grass (Dharba);\n2. Feed crows, stray cows, and dogs before family meals;\n3. Recite Sri Vishnu Sahasranamam and Sri Achyutashtakam;\n4. Donate food and clothing to underprivileged seekers.",
        "aliases": [
            {"aliasName": "Mahalaya Amavasya", "aliasType": "REGIONAL", "region": "South India & Bengal"},
            {"aliasName": "Shraddha Paksha", "aliasType": "REGIONAL", "region": "North India"}
        ],
        "dates": [
            {"gregorianDate": "2025-09-21T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Bhadrapada/Ashvina Krishna Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-10-10T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Bhadrapada/Ashvina Krishna Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-09-29T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Bhadrapada/Ashvina Krishna Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Deliverance of ancestors into light"},
            {"slug": "kshama-aparadha-stotram", "relationshipType": "CURATED_RECOMMENDATION", "order": 2, "notes": "Prayer for peace and forgiveness"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "karwa-chauth",
        "name": "Karwa Chauth",
        "category": "Vratam",
        "institutionCode": None,
        "primaryDeity": "Shiva",
        "description": "Sacred fast observed by married women on Kartika Krishna Chaturthi praying for the longevity, health, and prosperity of their husbands.",
        "significance": "Celebrates marital loyalty, sacrifice, and deep affection. The fast is broken only after sighting the moon through a decorated sieve and offering Arghya.",
        "whatHappensToday": "Women apply intricate henna (mehendi), dress in bridal red, and observe a strict waterless fast throughout the day. In the evening, women gather for the Karwa Chauth Vrata Katha.",
        "preparationGuide": "1. Partake of Sargahi pre-dawn meal before sunrise;\n2. Observe waterless fast until moonrise;\n3. Perform Shiva-Parvati-Kartikeya puja at dusk;\n4. View moon through sieve, offer water (Arghya), and break fast.",
        "aliases": [
            {"aliasName": "Karaka Chaturthi", "aliasType": "REGIONAL", "region": "North & West India"}
        ],
        "dates": [
            {"gregorianDate": "2025-10-10T00:00:00.000Z", "year": 2025, "region": "North & West India", "calendarConvention": "Kartika Krishna Chaturthi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-10-28T00:00:00.000Z", "year": 2026, "region": "North & West India", "calendarConvention": "Kartika Krishna Chaturthi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-10-18T00:00:00.000Z", "year": 2027, "region": "North & West India", "calendarConvention": "Kartika Krishna Chaturthi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "mahalakshmi-ashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Marital blessing and prosperity"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "parashurama-jayanti",
        "name": "Sri Parashurama Jayanti",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Appearance day of Lord Parashurama, the sixth warrior-sage avatar of Vishnu, on Vaisakha Shukla Tritiya.",
        "significance": "Celebrates the warrior-ascetic who reclaimed the southwestern Konkan and Kerala coastal lands from the sea and upheld righteousness with an axe (Parashu).",
        "whatHappensToday": "Special pujas in coastal Karnataka, Konkan, and Kerala temples. Devotees fast and pray for physical valor, moral courage, and righteous conduct.",
        "preparationGuide": "1. Meditate on Parashurama as the warrior-sage upholding Dharma;\n2. Recite Sri Vishnu Sahasranamam and Sri Sudarshana Ashtakam;\n3. Give alms of grains and jaggery.",
        "aliases": [
            {"aliasName": "Parashurama Dwitiya/Tritiya", "aliasType": "REGIONAL", "region": "Konkan & Kerala"}
        ],
        "dates": [
            {"gregorianDate": "2025-04-30T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Vaisakha Shukla Tritiya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-04-19T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Vaisakha Shukla Tritiya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-05-09T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Vaisakha Shukla Tritiya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "sudarshana-ashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Protection against violence and injustice"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "buddha-purnima",
        "name": "Buddha Purnima (Vaisakha Purnima)",
        "category": "Purnima Observance",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Full moon day of Vaisakha celebrating the birth, supreme enlightenment, and parinirvana of Gautama Buddha, revered in Puranic tradition as the compassionate avatar of Vishnu.",
        "significance": "Celebrates non-violence (Ahimsa), universal compassion (Karuna), meditation, and the cessation of egoic suffering.",
        "whatHappensToday": "Devotees observe peaceful contemplation, recite sacred discourses, practice Ahimsa, and distribute kheer (sweet milk rice pudding) to all visitors.",
        "preparationGuide": "1. Wear simple white attire and maintain silence (mouna);\n2. Practice loving-kindness meditation (Metta Bhavana);\n3. Feed the hungry and care for stray animals;\n4. Chant Sri Vishnu Sahasranamam with focused peace.",
        "aliases": [
            {"aliasName": "Vesak", "aliasType": "REGIONAL", "region": "East Asia & Global"},
            {"aliasName": "Vaisakha Purnima", "aliasType": "REGIONAL", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-05-12T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Vaisakha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Government of India Gazetted Holidays 2025"},
            {"gregorianDate": "2026-05-01T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Vaisakha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Government of India Gazetted Holidays 2026"},
            {"gregorianDate": "2027-05-20T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Vaisakha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Government of India Gazetted Holidays 2027"}
        ],
        "slokaSlugs": [
            {"slug": "maha-vishnu-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Avatar of divine compassion"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "ganga-dussehra",
        "name": "Ganga Dussehra",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Shiva",
        "description": "Celebration of the descent of Mother Ganga from the heavenly realm onto Lord Shiva's matted locks and onto earth on Jyeshtha Shukla Dashami.",
        "significance": "According to legend, bathing in the Ganga on this auspicious day washes away ten varieties of sins (Dasa-Hara) born of thought, speech, and physical action.",
        "whatHappensToday": "Millions gather at Haridwar, Prayagraj, Varanasi, and Rishikesh for dawn dips in the Ganga. Thousands of leaf-boats with burning lamps (Deepa Daanam) float on the water.",
        "preparationGuide": "1. Perform ceremonial bath in sacred water chanting 'Har Har Gange';\n2. Light clay lamps and float them on water bodies;\n3. Recite Sri Chandrasekhara Ashtakam and Sri Lingashtakam;\n4. Donate water melons, hand fans, and cool water to travelers.",
        "aliases": [
            {"aliasName": "Gangavataran", "aliasType": "REGIONAL", "region": "Uttarakhand & UP"}
        ],
        "dates": [
            {"gregorianDate": "2025-06-05T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Jyeshtha Shukla Dashami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-05-26T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Jyeshtha Shukla Dashami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-06-14T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Jyeshtha Shukla Dashami", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "chandrasekhara-ashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Bearer of the sacred Ganga in his locks"},
            {"slug": "siva-tandava-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Ganga flowing from Shiva's locks"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },

    # -------------------------------------------------------------
    # 4. MAJOR REGIONAL VRATAMS & CELEBRATIONS
    # -------------------------------------------------------------
    {
        "slug": "varalakshmi-vratam",
        "name": "Varalakshmi Vratam",
        "category": "Vratam",
        "institutionCode": None,
        "primaryDeity": "Lakshmi",
        "description": "A sacred observance observed on the Friday preceding the full moon day of Shravana month, dedicated to Goddess Varalakshmi (the boon-bestowing Mother).",
        "significance": "Celebrated by families praying for health, long life of spouse, peace, progeny, and prosperity. Instituted by Lord Shiva to Goddess Parvati in the Skanda Purana.",
        "whatHappensToday": "A Kalasham is consecrated with mango leaves, coconut, and turmeric-adorned face of Lakshmi. Yellow holy threads (Nonbu Charadu) are tied to wrists, and special sweet dumplings (Kozhukattai) are offered.",
        "preparationGuide": "1. Cleanse altar and prepare sacred Varalakshmi Kalasham;\n2. Recite Sri Mahalakshmi Ashtakam and Ashta Lakshmi Stotram;\n3. Offer 9 types of flowers and prasadam;\n4. Tie sacred yellow thread and distribute thamboolam.",
        "aliases": [
            {"aliasName": "Varalakshmi Nonbu", "aliasType": "REGIONAL", "region": "Tamil Nadu"},
            {"aliasName": "Varamahalakshmi Vrata", "aliasType": "REGIONAL", "region": "Karnataka"}
        ],
        "dates": [
            {"gregorianDate": "2025-08-08T00:00:00.000Z", "year": 2025, "region": "South India / All India", "calendarConvention": "Shravana Shukla Friday before Purnima", "verificationStatus": "VERIFIED", "sourceReference": "South Indian Temple Calendar 2025"},
            {"gregorianDate": "2026-08-21T00:00:00.000Z", "year": 2026, "region": "South India / All India", "calendarConvention": "Shravana Shukla Friday before Purnima", "verificationStatus": "VERIFIED", "sourceReference": "South Indian Temple Calendar 2026"},
            {"gregorianDate": "2027-08-13T00:00:00.000Z", "year": 2027, "region": "South India / All India", "calendarConvention": "Shravana Shukla Friday before Purnima", "verificationStatus": "VERIFIED", "sourceReference": "South Indian Temple Calendar 2027"}
        ],
        "slokaSlugs": [
            {"slug": "mahalakshmi-ashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Vrata puja recitation"},
            {"slug": "ashta-lakshmi-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Eight divine aspects"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "satyanarayana-vratham",
        "name": "Sri Satyanarayana Vratham",
        "category": "Vratam",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Popular devotional vrata described in the Reva Khanda of the Skanda Purana dedicated to Lord Satyanarayana (the embodiment of Supreme Truth).",
        "significance": "Performed on Purnima, housewarmings, weddings, or milestones for peace, resolving distress, gratitude for divine assistance, and family unity.",
        "whatHappensToday": "Devotees listen to the five chapters of the Satyanarayana Katha. Sacred panchamrita and semolina/wheat prasadam (Sapad Bhakshya) are distributed to all.",
        "preparationGuide": "1. Consecrate Vishnu Kalasham with navadhanyas;\n2. Offer Tulsi leaves and yellow flowers;\n3. Chant Sri Vishnu Sahasranamam and Sri Govinda Namavali;\n4. Read five chapters of the Satyanarayana Mahatmya.",
        "aliases": [
            {"aliasName": "Satyanarayan Puja", "aliasType": "PHONETIC", "region": "All India"},
            {"aliasName": "Purnima Satyanarayana Vrata", "aliasType": "REGIONAL", "region": "Andhra & Karnataka"}
        ],
        "dates": [
            {"gregorianDate": "2025-07-10T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Monthly Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-07-29T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Monthly Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-07-18T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Monthly Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Invocation of thousand names of Vishnu"},
            {"slug": "govinda-namavali", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Celebration of truth"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "mangala-gauri-vrat",
        "name": "Mangala Gauri Vrat",
        "category": "Vratam",
        "institutionCode": None,
        "primaryDeity": "Lalita Tripurasundari",
        "description": "Vrata observed by newly married women on all Tuesdays of the holy month of Shravana dedicated to Goddess Gauri.",
        "significance": "Observed for lifelong marital happiness, prosperity, good health of spouse, and harmony in the household.",
        "whatHappensToday": "Women fast during the daytime, prepare sixteen wheat flour diyas, offer sixteen types of flowers, and worship Gauri with special shlokas.",
        "preparationGuide": "1. Set up Gauri altar decorated with red kumkum;\n2. Prepare 16 flour lamps and light them with sesame oil;\n3. Recite Sri Lalita Sahasranama Stotram;\n4. Read Mangala Gauri Vrata Katha.",
        "aliases": [
            {"aliasName": "Shravana Mangalavara Vrat", "aliasType": "REGIONAL", "region": "Maharashtra & Karnataka"}
        ],
        "dates": [
            {"gregorianDate": "2025-08-05T00:00:00.000Z", "year": 2025, "region": "Maharashtra, Karnataka, North India", "calendarConvention": "Shravana Tuesdays", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-08-11T00:00:00.000Z", "year": 2026, "region": "Maharashtra, Karnataka, North India", "calendarConvention": "Shravana Tuesdays", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-08-03T00:00:00.000Z", "year": 2027, "region": "Maharashtra, Karnataka, North India", "calendarConvention": "Shravana Tuesdays", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "lalita-sahasranama-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Goddess Gauri adoration"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "karadaiyan-nonbu",
        "name": "Karadaiyan Nonbu (Savitri Vratam)",
        "category": "Vratam",
        "institutionCode": None,
        "primaryDeity": "Lalita Tripurasundari",
        "description": "Cherished Tamil observance commemorating Savitri offering wild rice cakes (Karadai) to Yama to protect Satyavan at the exact transit moment between Panguni and Chithirai.",
        "significance": "Married and unmarried women tie a sacred yellow thread with small flower (Nonbu Charadu) around their necks at the exact transition minute praying for marital longevity.",
        "whatHappensToday": "Women prepare sweet and savory Karadai (steamed rice-cowpea patties) with fresh unsalted butter. The holy thread is tied at the exact Muhurtam.",
        "preparationGuide": "1. Prepare steamed sweet and salted Karadai with butter;\n2. Prepare yellow thread (Charadu) with fresh flower;\n3. Recite 'Urukadha Vennayum Oridaiyum Naan Vaithan' at the transit moment;\n4. Tie thread around neck seeking Mother Kamakshi's protection.",
        "aliases": [
            {"aliasName": "Kamatchi Nonbu", "aliasType": "REGIONAL", "region": "Tamil Nadu"}
        ],
        "dates": [
            {"gregorianDate": "2025-03-14T18:00:00.000Z", "year": 2025, "region": "Tamil Nadu", "calendarConvention": "Panguni-Chithirai Transit", "verificationStatus": "VERIFIED", "sourceReference": "Pambu Panchangam 2025"},
            {"gregorianDate": "2026-03-14T18:00:00.000Z", "year": 2026, "region": "Tamil Nadu", "calendarConvention": "Panguni-Chithirai Transit", "verificationStatus": "VERIFIED", "sourceReference": "Pambu Panchangam 2026"},
            {"gregorianDate": "2027-03-15T18:00:00.000Z", "year": 2027, "region": "Tamil Nadu", "calendarConvention": "Panguni-Chithirai Transit", "verificationStatus": "VERIFIED", "sourceReference": "Pambu Panchangam 2027"}
        ],
        "slokaSlugs": [
            {"slug": "mahalakshmi-ashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Prayer for husband's long life"}
        ],
        "sourceFile": "TAMIL.pdf"
    },
    {
        "slug": "skanda-sashti-soorasamharam",
        "name": "Skanda Sashti & Soorasamharam",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Murugan",
        "description": "Six-day spiritual festival in the Tamil month of Aippasi celebrating Lord Murugan's victory over the demon of ego Soorapadman using the divine Vel (Spear).",
        "significance": "Represents the total destruction of spiritual arrogance (Anava Mala) by the light of pure wisdom (Jnana Sakthi). Devotees observe strict six-day fasting.",
        "whatHappensToday": "Tiruchendur, Palani, and all Arupadaiveedu temples enact the grand Soorasamharam on the beach/streets at sunset, followed by the celestial wedding (Tirukalyanam) on the following day.",
        "preparationGuide": "1. Observe six-day fasting on milk and fruits;\n2. Chant Sri Kanda Sashti Kavacham daily six times;\n3. Meditate on the divine Vel piercing inner mental darkness;\n4. Break fast after viewing the victory of Lord Murugan.",
        "aliases": [
            {"aliasName": "Kanda Sashti", "aliasType": "REGIONAL", "region": "Tamil Nadu"},
            {"aliasName": "Soorasamharam Day", "aliasType": "REGIONAL", "region": "Tamil Nadu & Kerala"}
        ],
        "dates": [
            {"gregorianDate": "2025-10-27T00:00:00.000Z", "year": 2025, "region": "Tamil Nadu & Kerala", "calendarConvention": "Aippasi Shukla Sashti", "verificationStatus": "VERIFIED", "sourceReference": "Tiruchendur Temple Panchangam 2025"},
            {"gregorianDate": "2026-11-15T00:00:00.000Z", "year": 2026, "region": "Tamil Nadu & Kerala", "calendarConvention": "Aippasi Shukla Sashti", "verificationStatus": "VERIFIED", "sourceReference": "Tiruchendur Temple Panchangam 2026"},
            {"gregorianDate": "2027-11-04T00:00:00.000Z", "year": 2027, "region": "Tamil Nadu & Kerala", "calendarConvention": "Aippasi Shukla Sashti", "verificationStatus": "VERIFIED", "sourceReference": "Tiruchendur Temple Panchangam 2027"}
        ],
        "slokaSlugs": [
            {"slug": "shiva-panchakshari-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Murugan as Shiva's supreme spark"}
        ],
        "sourceFile": "TAMIL.pdf"
    },
    {
        "slug": "aadi-perukku",
        "name": "Aadi Perukku (Pathinettam Perukku)",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Lakshmi",
        "description": "Tamil festival observed on the 18th day of the Tamil month Aadi paying homage to Mother Cauvery and all sacred life-giving rivers during monsoon swell.",
        "significance": "Celebrates agricultural fertility, natural water abundance, and thanksgiving to Mother Nature. Young brides pray along the riverbank for household welfare.",
        "whatHappensToday": "Families gather along river ghats in Srirangam, Thanjavur, and Bhavani, offering rice varieties (lemon rice, tamarind rice, coconut rice), flowers, and fruit.",
        "preparationGuide": "1. Prepare mixed rice varieties (Chitranam);\n2. Visit holy river ghat and offer flowers and lamps to flowing water;\n3. Recite Sri Mahalakshmi Ashtakam for natural prosperity;\n4. Share festive picnic meal along the riverbank.",
        "aliases": [
            {"aliasName": "Pathinettam Perukku", "aliasType": "REGIONAL", "region": "Tamil Nadu"},
            {"aliasName": "Aadi 18", "aliasType": "ABBREVIATION", "region": "Tamil Nadu"}
        ],
        "dates": [
            {"gregorianDate": "2025-08-03T00:00:00.000Z", "year": 2025, "region": "Tamil Nadu", "calendarConvention": "Tamil Month Aadi 18", "verificationStatus": "VERIFIED", "sourceReference": "Tamil Nadu Government Calendar 2025"},
            {"gregorianDate": "2026-08-03T00:00:00.000Z", "year": 2026, "region": "Tamil Nadu", "calendarConvention": "Tamil Month Aadi 18", "verificationStatus": "VERIFIED", "sourceReference": "Tamil Nadu Government Calendar 2026"},
            {"gregorianDate": "2027-08-03T00:00:00.000Z", "year": 2027, "region": "Tamil Nadu", "calendarConvention": "Tamil Month Aadi 18", "verificationStatus": "VERIFIED", "sourceReference": "Tamil Nadu Government Calendar 2027"}
        ],
        "slokaSlugs": [
            {"slug": "mahalakshmi-ashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Thanksgiving to river as divine Mother"}
        ],
        "sourceFile": "TAMIL.pdf"
    },
    {
        "slug": "aadi-amavasai",
        "name": "Aadi Amavasai",
        "category": "Amavasya Observance",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Highly sacred New Moon day in the Tamil month of Aadi coinciding with the Sun's southward journey (Dakshinayana), dedicated to ancestral Tarpanam.",
        "significance": "Marks the first Amavasya of Dakshinayana when the Pitrus (ancestors) come closer to earth. Rites performed at Rameswaram and Kanyakumari grant deep peace to generations.",
        "whatHappensToday": "Hundreds of thousands offer sacred sesame Tarpanam in the Agni Theertham at Rameswaram, Cauvery banks, and coastal beaches at dawn, followed by feeding cows and the poor.",
        "preparationGuide": "1. Rise before dawn and visit sea or river bank;\n2. Perform Pitru Tarpanam with sesame seeds and dharba grass;\n3. Recite Sri Vishnu Sahasranamam;\n4. Donate food and water pots in memory of ancestors.",
        "aliases": [
            {"aliasName": "Dakshinayana Amavasya", "aliasType": "REGIONAL", "region": "Tamil Nadu"},
            {"aliasName": "Karkidaka Vavu", "aliasType": "REGIONAL", "region": "Kerala"}
        ],
        "dates": [
            {"gregorianDate": "2025-07-24T00:00:00.000Z", "year": 2025, "region": "Tamil Nadu & Kerala", "calendarConvention": "Aadi Month Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rameswaram Temple Calendar 2025"},
            {"gregorianDate": "2026-08-12T00:00:00.000Z", "year": 2026, "region": "Tamil Nadu & Kerala", "calendarConvention": "Aadi Month Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rameswaram Temple Calendar 2026"},
            {"gregorianDate": "2027-08-01T00:00:00.000Z", "year": 2027, "region": "Tamil Nadu & Kerala", "calendarConvention": "Aadi Month Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rameswaram Temple Calendar 2027"}
        ],
        "slokaSlugs": [
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Prayer for peace of ancestors"},
            {"slug": "kshama-aparadha-stotram", "relationshipType": "CURATED_RECOMMENDATION", "order": 2, "notes": "Forgiveness and surrender"}
        ],
        "sourceFile": "TAMIL.pdf"
    },
    {
        "slug": "thai-poosam",
        "name": "Thai Poosam",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Murugan",
        "description": "Celebration of Goddess Parvati granting the invincible Vel (lance) to Lord Murugan under Pushya Nakshatra in the Tamil month of Thai.",
        "significance": "Celebrated worldwide in Palani, Tiruchendur, Batu Caves (Malaysia), and Singapore with intense Kavadi austerities, milk pot offerings, and spiritual penance.",
        "whatHappensToday": "Pilgrims walk barefoot carrying Kavadis adorned with peacock feathers and holy pots of milk (Paal Kudam), chanting 'Vetrivel Muruganukku Haroharohara!'.",
        "preparationGuide": "1. Observe preliminary fasting on fruits and milk;\n2. Carry Paal Kudam (milk pot) to Lord Murugan shrine;\n3. Chant Subramanya Bhujangam and Kanda Sashti Kavacham;\n4. Seek divine eradication of anger, greed, and ego.",
        "aliases": [
            {"aliasName": "Thaipusam", "aliasType": "PHONETIC", "region": "Tamil Nadu & Malaysia"},
            {"aliasName": "Thai Pushyam", "aliasType": "REGIONAL", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-02-11T00:00:00.000Z", "year": 2025, "region": "Tamil Nadu, Kerala, Malaysia", "calendarConvention": "Thai Month Pushya Star", "verificationStatus": "VERIFIED", "sourceReference": "Palani Devasthanam Calendar 2025"},
            {"gregorianDate": "2026-02-01T00:00:00.000Z", "year": 2026, "region": "Tamil Nadu, Kerala, Malaysia", "calendarConvention": "Thai Month Pushya Star", "verificationStatus": "VERIFIED", "sourceReference": "Palani Devasthanam Calendar 2026"},
            {"gregorianDate": "2027-01-22T00:00:00.000Z", "year": 2027, "region": "Tamil Nadu, Kerala, Malaysia", "calendarConvention": "Thai Month Pushya Star", "verificationStatus": "VERIFIED", "sourceReference": "Palani Devasthanam Calendar 2027"}
        ],
        "slokaSlugs": [
            {"slug": "shiva-panchakshari-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Murugan as supreme light of Shiva"}
        ],
        "sourceFile": "TAMIL.pdf"
    },
    {
        "slug": "panguni-uthiram",
        "name": "Panguni Uthiram",
        "category": "Hindu Festival",
        "institutionCode": None,
        "primaryDeity": "Murugan",
        "description": "Grand festival occurring when the full moon coincides with Uttara Phalguni nakshatra in the month of Panguni, celebrated as the day of celestial divine weddings.",
        "significance": "Celebrates the celestial weddings of Shiva-Parvati, Rama-Sita, and Murugan-Deivanai, representing the supreme union of the individual soul with the Divine.",
        "whatHappensToday": "Temples across Tamil Nadu and Kerala conduct magnificent Thirukalyanam ceremonies. Special processions of deities on silver and gold chariots take place.",
        "preparationGuide": "1. Attend temple celestial wedding (Kalyanotsavam);\n2. Recite Sri Mahalakshmi Ashtakam and Sri Rama Stotram;\n3. Chant Sri Shiva Panchakshari Stotram for family harmony;\n4. Seek divine blessings for happy marital life.",
        "aliases": [
            {"aliasName": "Kalyana Utsavam Day", "aliasType": "REGIONAL", "region": "Tamil Nadu"},
            {"aliasName": "Meena Uthiram", "aliasType": "REGIONAL", "region": "Kerala"}
        ],
        "dates": [
            {"gregorianDate": "2025-04-11T00:00:00.000Z", "year": 2025, "region": "Tamil Nadu & Kerala", "calendarConvention": "Panguni Month Uttara Phalguni", "verificationStatus": "VERIFIED", "sourceReference": "Tamil Nadu HR&CE Calendar 2025"},
            {"gregorianDate": "2026-04-02T00:00:00.000Z", "year": 2026, "region": "Tamil Nadu & Kerala", "calendarConvention": "Panguni Month Uttara Phalguni", "verificationStatus": "VERIFIED", "sourceReference": "Tamil Nadu HR&CE Calendar 2026"},
            {"gregorianDate": "2027-03-22T00:00:00.000Z", "year": 2027, "region": "Tamil Nadu & Kerala", "calendarConvention": "Panguni Month Uttara Phalguni", "verificationStatus": "VERIFIED", "sourceReference": "Tamil Nadu HR&CE Calendar 2027"}
        ],
        "slokaSlugs": [
            {"slug": "mahalakshmi-ashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Celestial wedding adoration"}
        ],
        "sourceFile": "TAMIL.pdf"
    },
    {
        "slug": "ayyappa-mandala-pooja-makaravilakku",
        "name": "Ayyappa Mandala Pooja & Makaravilakku",
        "category": "Vratam",
        "institutionCode": None,
        "primaryDeity": "Ayyappa",
        "description": "Forty-one day rigorous spiritual pilgrimage period (Mandala Kalam) culminating in Makaravilakku at the hill shrine of Sabarimala in Kerala.",
        "significance": "Pilgrims observe strict Brahmacharya, wear black or blue garments, carry the sacred two-compartment cloth bag (Irumudi), and chant 'Swamiye Saranam Ayyappa'.",
        "whatHappensToday": "Makaravilakku takes place on Makara Sankranti dusk when the sacred jewels (Thiruvabharanam) adorn Lord Ayyappa and the divine light (Makarajyothi) appears on the horizon.",
        "preparationGuide": "1. Wear Tulsi or Rudraksha mala with Guru Swami's blessing;\n2. Observe 41-day strict vegetarianism and Brahmacharya;\n3. Pack sacred ghee coconut in the Irumudi kettu;\n4. Chant Hari Varasanam and Sri Sudarshana Ashtakam for protection.",
        "aliases": [
            {"aliasName": "Sabarimala Mandala Season", "aliasType": "REGIONAL", "region": "Kerala & South India"},
            {"aliasName": "Makarajyothi Day", "aliasType": "REGIONAL", "region": "Kerala"}
        ],
        "dates": [
            {"gregorianDate": "2025-12-26T00:00:00.000Z", "year": 2025, "region": "Kerala & South India", "calendarConvention": "Mandala Pooja (Dhanu 11)", "verificationStatus": "VERIFIED", "sourceReference": "Travancore Devaswom Board 2025"},
            {"gregorianDate": "2026-01-14T18:00:00.000Z", "year": 2026, "region": "Kerala (Makaravilakku)", "calendarConvention": "Makaravilakku (Makara 1)", "verificationStatus": "VERIFIED", "sourceReference": "Travancore Devaswom Board 2026"},
            {"gregorianDate": "2026-12-26T00:00:00.000Z", "year": 2026, "region": "Kerala & South India", "calendarConvention": "Mandala Pooja (Dhanu 11)", "verificationStatus": "VERIFIED", "sourceReference": "Travancore Devaswom Board 2026"},
            {"gregorianDate": "2027-01-14T18:00:00.000Z", "year": 2027, "region": "Kerala (Makaravilakku)", "calendarConvention": "Makaravilakku (Makara 1)", "verificationStatus": "VERIFIED", "sourceReference": "Travancore Devaswom Board 2027"}
        ],
        "slokaSlugs": [
            {"slug": "shiva-panchakshari-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Shiva-Vishnu united incarnation"},
            {"slug": "sudarshana-ashtakam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Forest path spiritual protection"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "anant-chaturdashi",
        "name": "Anant Chaturdashi (Ganesh Visarjan)",
        "category": "Vratam",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Fourteenth day of Bhadrapada Shukla Paksha dedicated to Lord Ananta (the Infinite Supreme Vishnu) and the grand immersion of Lord Ganesha.",
        "significance": "Celebrates the boundless, eternal nature of the Divine. A 14-knot sacred cotton thread (Ananta Sutra) is consecrated and tied to the right arm.",
        "whatHappensToday": "Families conclude the 10-day Ganeshotsav with music, drums, and immersing Ganesha in sacred water bodies. Ananta Padmanabha puja is conducted with 14 sweet fried rotis.",
        "preparationGuide": "1. Worship Lord Ananta with 14-knot red thread;\n2. Recite Sri Vishnu Sahasranamam and Achyutashtakam;\n3. Carry Ganesha idol with reverence chanting 'Ganapati Bappa Morya';\n4. Immerse idol in clean water invoking Lord's return next year.",
        "aliases": [
            {"aliasName": "Ganesh Visarjan Day", "aliasType": "REGIONAL", "region": "Maharashtra"},
            {"aliasName": "Ananta Padmanabha Vrata", "aliasType": "REGIONAL", "region": "Karnataka & Andhra"}
        ],
        "dates": [
            {"gregorianDate": "2025-09-06T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Bhadrapada Shukla Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-09-24T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Bhadrapada Shukla Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-09-14T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Bhadrapada Shukla Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "maha-ganesha-pancharatnam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Farewell adoration to Ganesha"},
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Lord Ananta's thousand names"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },

    # -------------------------------------------------------------
    # 5. RECURRING & NAMED EKADASHIS
    # -------------------------------------------------------------
    {
        "slug": "nirjala-ekadashi",
        "name": "Nirjala Ekadashi (Bhima Ekadashi)",
        "category": "Ekadashi",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "The most austere of all 24 Ekadashis in the Hindu calendar, observed on Jyeshtha Shukla Ekadashi without even drinking a single drop of water (Nirjala).",
        "significance": "Tradition holds that observing this single waterless fast with devotion yields the spiritual benefit of observing all 24 Ekadashis of the year, as advised by Sage Vyasa to Bhima.",
        "whatHappensToday": "Devotees observe complete fast from sunrise to next day's sunrise. Water pots (Kumbha) covered with cloth and filled with sweet water are donated to travelers.",
        "preparationGuide": "1. Stop water and food intake from sunrise on Ekadashi;\n2. Spend day in quiet scriptural contemplation and mantra japa;\n3. Recite Sri Vishnu Sahasranamam and Sri Venkateswara Prapatti;\n4. Break fast on Dwadashi morning after offering water to Lord Vishnu.",
        "aliases": [
            {"aliasName": "Bhima Ekadashi", "aliasType": "REGIONAL", "region": "All India"},
            {"aliasName": "Pandava Nirjala Ekadashi", "aliasType": "TRANSLITERATION", "region": "North India"}
        ],
        "dates": [
            {"gregorianDate": "2025-06-06T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Jyeshtha Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-05-27T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Jyeshtha Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-06-15T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Jyeshtha Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Holy parayanam for endurance"},
            {"slug": "venkateswara-prapatti", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Total self-surrender"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "shayani-ekadashi-ashadhi",
        "name": "Shayani Ekadashi (Ashadhi Ekadashi / Pandharpur Yatra)",
        "category": "Ekadashi",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Ashadha Shukla Ekadashi marking the onset of the sacred four-month monastic period (Chaturmasya) when Lord Vishnu enters cosmic yogic slumber (Yoga Nidra).",
        "significance": "Celebrated with intense devotion in Maharashtra as millions of Varkari pilgrims walk on foot to Pandharpur carrying Palkhis of Saint Dnyaneshwar and Saint Tukaram.",
        "whatHappensToday": "Huge gathering of devotees at the Vitthal-Rukmini temple at Pandharpur singing 'Jai Jai Ram Krishna Hari'. Devotees observe strict Ekadashi fast.",
        "preparationGuide": "1. Undertake vows for the four-month Chaturmasya;\n2. Observe fasting avoiding grains, pulses, and onions;\n3. Recite Sri Govinda Namavali and Sri Achyutashtakam;\n4. Sing congregational bhajans praising Lord Vitthala.",
        "aliases": [
            {"aliasName": "Devshayani Ekadashi", "aliasType": "REGIONAL", "region": "North India"},
            {"aliasName": "Ashadhi Ekadashi", "aliasType": "REGIONAL", "region": "Maharashtra"},
            {"aliasName": "Pandharpur Wari Culmination", "aliasType": "REGIONAL", "region": "Maharashtra"}
        ],
        "dates": [
            {"gregorianDate": "2025-07-06T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Ashadha Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-07-25T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Ashadha Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-07-15T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Ashadha Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "govinda-namavali", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Varkari namasankirtana"},
            {"slug": "achyutashtakam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Vitthala praise"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "prabodhini-ekadashi-devutthana",
        "name": "Prabodhini Ekadashi (Devutthana Ekadashi)",
        "category": "Ekadashi",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Kartika Shukla Ekadashi marking the end of the four-month Chaturmasya as Lord Vishnu awakens from His yogic slumber.",
        "significance": "Auspicious dawn inaugurating the sacred marriage season and paving the way for Tulsi Vivah and Dev Deepawali.",
        "whatHappensToday": "Devotees fast, light festive oil lamps around sugarcane structures in courtyards, and sing welcoming songs awakening the Lord with conches and bells.",
        "preparationGuide": "1. Chant awakening mantras (Uttishtha Govinda) at Brahma Muhurta;\n2. Fast through the day with sattvic milk and fruits;\n3. Recite Sri Vishnu Sahasranamam and Sri Venkateswara Stotram;\n4. Celebrate the conclusion of Chaturmasya vows.",
        "aliases": [
            {"aliasName": "Devutthana Ekadashi", "aliasType": "REGIONAL", "region": "North India"},
            {"aliasName": "Kartiki Ekadashi", "aliasType": "REGIONAL", "region": "Maharashtra"},
            {"aliasName": "Bodhana Ekadashi", "aliasType": "REGIONAL", "region": "South India"}
        ],
        "dates": [
            {"gregorianDate": "2025-11-01T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Kartika Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-11-20T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Kartika Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-11-09T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Kartika Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "venkateswara-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Dawn awakening stotram"},
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Holy thousand names"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "jaya-ekadashi",
        "name": "Jaya Ekadashi (Bhamini Ekadashi)",
        "category": "Ekadashi",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Magha Shukla Ekadashi celebrated for liberation from lower realms and spiritual victory (Jaya) over inner base desires.",
        "significance": "Described in the Padma Purana and Bhavisya Purana where Lord Krishna explains to King Yudhishthira how observing this fast cleanses the soul from ghosthood (Pishachatva).",
        "whatHappensToday": "Devotees observe complete fast, offer sacred basil (Tulsi) leaves to Lord Vishnu, and engage in nighttime prayer vigil.",
        "preparationGuide": "1. Fast on Ekadashi without grains;\n2. Offer holy Tulsi leaves to Lord Vishnu;\n3. Recite Sri Vishnu Sahasranamam and Sri Achyutashtakam;\n4. Perform morning arati and charitable donations on Dwadashi.",
        "aliases": [
            {"aliasName": "Bhamini Ekadashi", "aliasType": "REGIONAL", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-02-08T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Magha Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-01-29T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Magha Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-02-17T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Magha Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Sahasranama parayanam for spiritual liberation"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "kamada-ekadashi",
        "name": "Kamada Ekadashi",
        "category": "Ekadashi",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Chaitra Shukla Ekadashi observed immediately following the Hindu New Year, revered as the fulfiller of righteous desires (Kamada).",
        "significance": "Mentioned in the Varaha Purana for freedom from the curse of wandering and restitution of family peace.",
        "whatHappensToday": "Fasting and listening to the sacred Kamada Vrata Katha, chanting the Holy Names of Krishna and Rama.",
        "preparationGuide": "1. Fast through the day;\n2. Recite Sri Govinda Namavali and Sri Rama Stotram;\n3. Break fast on Dwadashi morning with sattvic food.",
        "aliases": [
            {"aliasName": "Chaitra Shukla Ekadashi", "aliasType": "REGIONAL", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-04-09T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Chaitra Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-03-29T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Chaitra Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-04-17T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Chaitra Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "govinda-namavali", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Celebration of Krishna's grace"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "papankusha-ekadashi",
        "name": "Papankusha Ekadashi",
        "category": "Ekadashi",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Ashvina Shukla Ekadashi observed following Navaratri, acting as an 'Ankusha' (goad/hook) that restrains sins and leads seekers to spiritual upliftment.",
        "significance": "Described in the Brahmavaivarta Purana for earning spiritual merit equivalent to performing thousands of Ashvamedha sacrifices.",
        "whatHappensToday": "Devotees observe complete fast and offer gold, cows, or grains in charity, concluding Navaratri with spiritual purification.",
        "preparationGuide": "1. Fast on Ekadashi;\n2. Chant Sri Vishnu Sahasranamam;\n3. Meditate on Lord Padmanabha.",
        "aliases": [
            {"aliasName": "Ashvina Shukla Ekadashi", "aliasType": "REGIONAL", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2025-10-03T00:00:00.000Z", "year": 2025, "region": "All India", "calendarConvention": "Ashvina Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2025"},
            {"gregorianDate": "2026-10-21T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Ashvina Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2027-10-11T00:00:00.000Z", "year": 2027, "region": "All India", "calendarConvention": "Ashvina Shukla Ekadashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2027"}
        ],
        "slokaSlugs": [
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Purification and liberation"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },

    # -------------------------------------------------------------
    # 6. MONTHLY RECURRING VEDIC OBSERVANCES
    # -------------------------------------------------------------
    {
        "slug": "pradosham-observance",
        "name": "Pradosham (Pradosha Vratam)",
        "category": "Vratam",
        "institutionCode": None,
        "primaryDeity": "Shiva",
        "description": "Bi-monthly twilight observance occurring on the 13th lunar day (Trayodashi) of both Shukla and Krishna pakshas, sacred to Lord Shiva and Nandi.",
        "significance": "The period between 4:30 PM and 6:00 PM is when Lord Shiva performs the Ananda Tandava dance on Mount Kailash. Worshipping during Pradosha dissolves karmic burdens. Somavara Pradosham and Shani Pradosham possess supreme efficacy.",
        "whatHappensToday": "Temples conduct special Maha Abhishekam to Lord Shiva and Nandi with milk, curd, honey, and sandalwood. Devotees perform circumambulation (Pradosha Pradakshinam).",
        "preparationGuide": "1. Fast from morning until evening twilight;\n2. Visit Shiva temple during Pradosha Sandhya (4:30-6:00 PM);\n3. Offer Bilva leaves and arugampul (durva grass) to Nandi;\n4. Recite Sri Shiva Panchakshari Stotram and Sri Bilvashtakam.",
        "aliases": [
            {"aliasName": "Shani Pradosham", "aliasType": "REGIONAL", "region": "All India (when falling on Saturday)"},
            {"aliasName": "Soma Pradosham", "aliasType": "REGIONAL", "region": "All India (when falling on Monday)"},
            {"aliasName": "Pradosha Vrata", "aliasType": "TRANSLITERATION", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2026-02-14T17:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Shani Pradosham (Maha Shivaratri eve)", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-04-14T17:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Chaitra Trayodashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-07-26T17:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Ashadha Trayodashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-10-23T17:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Ashvina Trayodashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"}
        ],
        "slokaSlugs": [
            {"slug": "shiva-panchakshari-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Twilight panchakshari meditation"},
            {"slug": "bilvashtakam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Leaf archana to Nandi and Shiva"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "sankashti-chaturthi",
        "name": "Sankashti Chaturthi (Sankata Hara Chavithi)",
        "category": "Vratam",
        "institutionCode": None,
        "primaryDeity": "Ganesha",
        "description": "Monthly vrata observed on the fourth lunar day (Chaturthi) of Krishna Paksha dedicated to Lord Ganesha for removal of distress and obstacles.",
        "significance": "When falling on Tuesday, it is celebrated as the auspicious Angaraki Sankashti Chaturthi with heightened merit. The fast is broken only after moonrise.",
        "whatHappensToday": "Devotees observe fast through the day. Special evening Ganesha puja is conducted offering durva grass and modakas, followed by sighting the moon and offering Arghya.",
        "preparationGuide": "1. Maintain fast throughout the daytime;\n2. Recite Sri Sankata Nashana Ganesha Stotram three times;\n3. Chant Sri Maha Ganesha Pancharatnam;\n4. Offer water to the rising moon and break fast with modaka prasadam.",
        "aliases": [
            {"aliasName": "Sankatahara Chaturthi", "aliasType": "REGIONAL", "region": "South India"},
            {"aliasName": "Angaraki Chaturthi", "aliasType": "REGIONAL", "region": "Maharashtra (when on Tuesday)"}
        ],
        "dates": [
            {"gregorianDate": "2026-03-07T21:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Monthly Krishna Chaturthi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-06-03T21:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Monthly Krishna Chaturthi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-09-29T21:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Monthly Krishna Chaturthi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"}
        ],
        "slokaSlugs": [
            {"slug": "sankata-nashana-ganesha-stotram", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Sage Narada's twelve names"},
            {"slug": "maha-ganesha-pancharatnam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Adi Shankaracharya's gems"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "monthly-masa-shivaratri",
        "name": "Masa Shivaratri",
        "category": "Vratam",
        "institutionCode": None,
        "primaryDeity": "Shiva",
        "description": "Monthly nocturnal observance on Krishna Paksha Chaturdashi dedicated to Lord Shiva for spiritual awakening and dissolving ignorance.",
        "significance": "Occurs once every month on the eve of the New Moon, serving as a monthly spiritual rejuvenation of silence, fasting, and contemplation before the moon fully disappears.",
        "whatHappensToday": "Devotees observe evening fasting, light oil lamps in Shiva temples, and offer Bilva leaves during the Nishita Kaala (midnight) hour.",
        "preparationGuide": "1. Eat light sattvic meal during the day;\n2. Chant Sri Shiva Panchakshari and Sri Lingashtakam in evening;\n3. Offer Bilva leaves with Sri Bilvashtakam;\n4. Engage in quiet meditation before sleep.",
        "aliases": [
            {"aliasName": "Monthly Shivaratri", "aliasType": "TRANSLITERATION", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2026-03-17T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Phalguna Krishna Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-05-15T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Vaisakha Krishna Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-08-11T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Shravana Krishna Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-11-07T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Kartika Krishna Chaturdashi", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"}
        ],
        "slokaSlugs": [
            {"slug": "lingashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Eightfold Lingam adoration"},
            {"slug": "shiva-panchakshari-stotram", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Panchakshari meditation"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "monthly-purnima-satyanarayana",
        "name": "Purnima Observance (Full Moon Day)",
        "category": "Purnima Observance",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Monthly full-moon day when lunar radiance is at its zenith, dedicated to Lord Satyanarayana, Goddess Mahalakshmi, and universal spiritual light.",
        "significance": "Astronomically auspicious day when human consciousness naturally expands; traditional day for fasting, temple visits, and congregational singing of holy names.",
        "whatHappensToday": "Families perform Sri Satyanarayana Puja and Tiruvannamalai / Giri Pradakshinam (circumambulation of sacred hills).",
        "preparationGuide": "1. Perform Satyanarayana puja with fresh fruits and kheer;\n2. Recite Sri Vishnu Sahasranamam and Ashta Lakshmi Stotram;\n3. Chant Sri Govinda Namavali in satsang;\n4. Meditate under the radiant full moon.",
        "aliases": [
            {"aliasName": "Pournami", "aliasType": "REGIONAL", "region": "South India"},
            {"aliasName": "Poornima", "aliasType": "PHONETIC", "region": "All India"}
        ],
        "dates": [
            {"gregorianDate": "2026-01-03T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Pausha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-02-01T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Magha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-03-03T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Phalguna Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-04-02T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Chaitra Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-05-01T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Vaisakha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-05-31T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Jyeshtha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-07-29T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Ashadha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-08-28T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Shravana Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-09-26T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Bhadrapada Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-10-25T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Ashvina Purnima (Sharad Purnima)", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-11-24T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Kartika Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-12-23T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Margashirsha Purnima", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"}
        ],
        "slokaSlugs": [
            {"slug": "mahalakshmi-ashtakam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Full moon Lakshmi invocation"},
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 2, "notes": "Satyanarayana worship"}
        ],
        "sourceFile": "ENGLISH.pdf"
    },
    {
        "slug": "monthly-amavasya-observance",
        "name": "Amavasya Observance (New Moon Day)",
        "category": "Amavasya Observance",
        "institutionCode": None,
        "primaryDeity": "Vishnu",
        "description": "Monthly new-moon day when the moon is completely conjunct with the sun, dedicated to ancestral offerings (Tarpanam) and charitable gifts.",
        "significance": "A day of introspection, settling debts to forebears, prayer for ancestral peace, and practicing charity towards all living beings.",
        "whatHappensToday": "Elders perform morning Tarpanam with water and black sesame seeds; grains and food are offered to crows, cows, and the destitute.",
        "preparationGuide": "1. Perform Tarpanam before noon with black sesame seeds;\n2. Recite Sri Vishnu Sahasranamam and Sri Achyutashtakam;\n3. Feed birds and animals;\n4. Maintain quiet reverence and vegetarian purity.",
        "aliases": [
            {"aliasName": "Amavasai", "aliasType": "REGIONAL", "region": "Tamil Nadu"},
            {"aliasName": "Amavas", "aliasType": "PHONETIC", "region": "North India"}
        ],
        "dates": [
            {"gregorianDate": "2026-01-18T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Pausha Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-02-17T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Magha Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-03-18T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Phalguna Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-04-17T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Chaitra Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-05-16T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Vaisakha Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-06-14T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Jyeshtha Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-07-14T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Ashadha Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-08-12T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Shravana Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-09-11T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Bhadrapada Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-10-10T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Mahalaya Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-11-08T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Deepavali Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"},
            {"gregorianDate": "2026-12-08T00:00:00.000Z", "year": 2026, "region": "All India", "calendarConvention": "Margashirsha Amavasya", "verificationStatus": "VERIFIED", "sourceReference": "Rashtriya Panchanga 2026"}
        ],
        "slokaSlugs": [
            {"slug": "vishnu-sahasranamam", "relationshipType": "TRADITIONAL", "order": 1, "notes": "Prayer for peace to ancestors"},
            {"slug": "kshama-aparadha-stotram", "relationshipType": "CURATED_RECOMMENDATION", "order": 2, "notes": "Forgiveness for omissions"}
        ],
        "sourceFile": "ENGLISH.pdf"
    }
]

output_path = os.path.join('data', 'intermediate', 'comprehensive_occasions_catalog.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(festivals, f, ensure_ascii=False, indent=2)

print(f"Successfully generated comprehensive catalog of {len(festivals)} occasions and saved to {output_path}!")
