"""Copy for the five service pages. Edit here, then run python3 tools/build.py.

Price ranges are typical market ranges for the Charleston area, not quotes.
Adjust them to match what the business actually charges.
"""

COST_NOTE = ("Typical ranges only, not a quote. Your exact price depends on the job and "
             "is confirmed in writing before any work starts.")

SERVICES = [
    {
        "slug": "septic-pumping",
        "name": "Septic Tank Pumping",
        "title": "Septic Tank Pumping in the SC Lowcountry",
        "desc": "Septic tank pumping in Charleston, Mount Pleasant, Summerville, Beaufort and across the SC Lowcountry. Typical cost ranges, what's included, and how often to pump.",
        "lead": "Regular pumping is the single best thing you can do for your septic system. It keeps solids out of your drain field and heads off the backups and failures that cost thousands to fix.",
        "included_title": "What's included",
        "included": [
            "Locating and uncovering the tank lid or lids",
            "Pumping out all liquid, scum and settled sludge",
            "A visual check of the tank walls, inlet and outlet baffles",
            "Cleaning the effluent filter, if your tank has one",
            "Noting any warning signs, like high water levels or damaged parts",
            "A record of the visit and a reminder when your next pumping is due",
        ],
        "signs_title": "When it's time to pump",
        "signs": [
            "It's been 3–5 years since your last pumping, or you don't know when it was",
            "Drains are slow or toilets gurgle",
            "You notice sewage odors near the tank or drain field",
            "You're buying or selling a home",
            "You're planning a big gathering or adding people to the household",
        ],
        "body": [
            ("Why pumping matters", [
                "Everything that goes down your drains ends up in the septic tank. Inside, the heavy solids sink to the bottom as sludge, grease and light material float to the top as scum, and the liquid in between flows out to the drain field. Bacteria break down some of the solids, but never all of them. Over time the sludge and scum layers grow until there is little room left for the liquid to settle.",
                "When that happens, solids start washing out of the tank and into the drain field. A drain field is built to soak up liquid, not solids. Once its gravel and soil clog, it stops draining, and the usual fix is a new drain field, often the most expensive septic repair there is. Routine pumping removes the solids before they reach that point. It costs a few hundred dollars and protects a system that can cost five figures to replace.",
            ]),
            ("How often should you pump?", [
                "Most households should pump every three to five years. The right interval for your home depends on three things: the size of the tank, how many people live in the house, and how much water and waste goes down the drains. A family of five on a 1,000-gallon tank needs pumping more often than a couple on the same tank. A garbage disposal adds solids and can shorten the interval noticeably.",
                "If you don't know when your tank was last pumped, assume it's due. We measure the sludge and scum layers during every visit and recommend a schedule based on what we actually find, not a one-size-fits-all number.",
            ]),
            ("Pumping in the Lowcountry", [
                "High water tables are a fact of life here, and they matter for pumping. When the ground is saturated after heavy rain, a storm surge or a king tide, groundwater presses up on the outside of the tank. Pumping a tank empty under those conditions can, in rare cases, push a tank out of the ground or crack it. If the ground around your tank is waterlogged, we'll talk through whether to pump now or wait a few days.",
                "We also recommend a riser on the tank lid. Many older Lowcountry tanks are buried a foot or more down, which means digging every visit. A riser brings the lid up to ground level, makes every future pumping faster and cleaner, and makes it easy to check on the tank between visits.",
            ]),
        ],
        "cost_intro": [
            "The price of pumping depends mostly on the tank size, how hard the lid is to reach, and how much sludge has built up. Tanks that haven't been pumped in many years sometimes take longer or need a second load.",
        ],
        "cost": [
            ("Standard pumping, 1,000-gallon tank", "$275 – $450"),
            ("Larger tanks, 1,250–1,500 gallons", "$350 – $600"),
            ("Locating and digging up a buried lid", "$75 – $250"),
            ("Installing a riser on the lid", "$250 – $600"),
        ],
        "cost_note": COST_NOTE,
        "faq": [
            ("How often should I pump?", "Most households should pump every 3 to 5 years. Larger families, smaller tanks and garbage disposals all shorten that interval. We'll recommend a schedule based on the sludge levels we measure."),
            ("Do I need to be home?", "Not always. As long as we can reach the tank and know where it is, we can often do the work while you're away. We'll confirm when you book."),
            ("Will it mess up my yard?", "We dig only what's needed to reach the lid and put the soil back when we're done. Installing a riser makes future pumpings quicker and cleaner."),
            ("Do septic additives replace pumping?", "No. Additives don't remove the sludge that builds up in the tank, and some can push solids into the drain field. Regular pumping is the only proven way to remove solids."),
            ("Can you pump my tank after a big storm?", "Usually, but if the ground around the tank is saturated we may suggest waiting a few days. Pumping a tank empty in very high groundwater can shift or damage it."),
        ],
    },
    {
        "slug": "septic-inspections",
        "name": "Septic Inspections",
        "title": "Septic Inspections for Home Buyers, Sellers & Owners",
        "desc": "Septic system inspections for real estate transactions and homeowners in Charleston and the SC Lowcountry. What we check, typical costs, and clear written reports.",
        "lead": "A septic system is buried and easy to overlook, but replacing one can cost more than a new roof. An inspection tells you exactly what you're dealing with before you close or before small problems grow.",
        "included_title": "What we check",
        "included": [
            "Tank condition, including cracks, leaks and corrosion",
            "Inlet and outlet baffles and the effluent filter",
            "Sludge and scum levels, and whether the tank is holding the right water level",
            "Signs of backup or surfacing wastewater over the drain field",
            "Pumps, floats and alarms, if your system has them",
            "A clear written report you can share with your agent, lender or buyer",
        ],
        "signs_title": "When to get an inspection",
        "signs": [
            "You're buying a home with a septic system",
            "You're listing your home and want to avoid surprises",
            "You've noticed odors, wet spots or slow drains",
            "You don't know the age or history of your system",
            "You're planning an addition, pool or new driveway near the system",
        ],
        "body": [
            ("Why inspections matter in a home sale", [
                "In a typical home inspection, the inspector runs the faucets and flushes the toilets. That tells you the drains work today. It doesn't tell you whether the tank is cracked, whether the baffles are gone, or whether the drain field is close to failing. A dedicated septic inspection does.",
                "For buyers, an inspection gives you leverage. If the system needs work, you can negotiate a repair or a price reduction before closing instead of discovering the problem after you move in. For sellers, an inspection before listing lets you fix problems on your own schedule and gives buyers confidence, which can keep a deal from falling apart late in the process.",
            ]),
            ("How the inspection works", [
                "We start by locating the tank and opening it. In most cases we pump the tank as part of the inspection, because a full tank hides the walls, baffles and the bottom of the tank. Once it's empty we check the structure, look for cracks or root intrusion, and confirm the inlet and outlet baffles are intact.",
                "Then we look at the rest of the system: the line from the house, the distribution box where we can reach it, and the drain field itself. We look for soggy ground, unusually green grass and other signs that wastewater is surfacing. If the system has a pump or alarm, we test it. You get a written report with what we found, photos where helpful, and any repairs we recommend, in plain language.",
            ]),
            ("Permit records", [
                "South Carolina keeps septic permit records through the SC Department of Environmental Services (SCDES). For many homes, those records show the tank size and the layout of the drain field, which helps us find everything quickly. Older homes sometimes have no records at all, and that's exactly when an inspection matters most.",
                "If records do exist, compare them with what's on the ground. Additions, new bedrooms and new structures built since the system was permitted can mean the system is now undersized for the house or that something has been built over part of the drain field. Both are worth knowing before you buy.",
            ]),
        ],
        "cost_intro": [
            "The cost depends on whether pumping is included, how easy the tank is to reach, and how complex the system is. Systems with pumps or alarms take longer to test.",
        ],
        "cost": [
            ("Visual inspection, no pumping", "$200 – $350"),
            ("Full inspection with pumping", "$450 – $750"),
            ("Locating a tank with no records", "$100 – $300"),
        ],
        "cost_note": COST_NOTE,
        "faq": [
            ("How long does an inspection take?", "Most residential inspections take two to four hours on site, depending on how easy the tank is to reach and whether we pump it."),
            ("Does the tank need to be pumped for an inspection?", "A full inspection usually includes pumping so we can see the inside of the tank and the baffles clearly. We'll explain the options when you book."),
            ("Can you work with my real estate agent's timeline?", "Yes. Let us know your closing date when you call, and we'll do our best to fit your schedule."),
            ("When will I get the report?", "We walk you through what we found on site, and the written report usually follows within one to two business days."),
            ("What happens if the inspection finds a problem?", "The report explains the problem, how serious it is and what fixing it involves. You're under no obligation to use us for the repair."),
        ],
    },
    {
        "slug": "septic-repair",
        "name": "Septic Repair",
        "title": "Septic System Repair in the SC Lowcountry",
        "desc": "Septic repair in Charleston and the SC Lowcountry: baffles, lids, pumps, lines and alarms. Honest diagnosis, typical repair costs, and a price before work starts.",
        "lead": "When something goes wrong with your septic system, you need someone who finds the real cause and fixes it right, not just a quick patch that fails again next month.",
        "included_title": "Common repairs",
        "included": [
            "Broken or missing inlet and outlet baffles",
            "Cracked or unsafe tank lids, and new risers",
            "Failed effluent or lift pumps, floats and alarms",
            "Clogged or broken lines between the house and the tank",
            "Root intrusion in lines and tanks",
            "Distribution box repair and replacement",
        ],
        "signs_title": "Signs you need a repair",
        "signs": [
            "Sewage backing up into toilets, tubs or floor drains",
            "Gurgling pipes or slow drains throughout the house",
            "A septic alarm going off",
            "Strong odors in the yard or house",
            "A sunken area or soft spot over the tank or lines",
        ],
        "body": [
            ("Diagnosis first", [
                "The same symptom can have very different causes. A slow drain might be a clog in the line from the house, a full tank, a broken baffle, or a drain field that's starting to fail. Guessing wrong wastes your money. We start every repair call by finding out what's actually wrong, then explain what we found and what it will take to fix before we start any work.",
                "Where it helps, we'll use a camera to look inside the lines, check the tank levels, and test pumps and alarms. If the problem turns out to be simple, like a clogged filter, we'll tell you so.",
            ]),
            ("Repairs that save a system", [
                "Many septic problems are much cheaper to fix than people fear. Baffles are a good example. These small fittings at the inlet and outlet of the tank keep scum and solids from flowing out to the drain field. When an outlet baffle breaks, which is common in older concrete tanks, solids start reaching the drain field. Replacing the baffle costs a few hundred dollars. Ignoring it can cost a drain field.",
                "Pumps and alarms are another common repair in the Lowcountry, where many homes on low or wet lots use a pump to move wastewater uphill or to a raised drain field. When the pump fails, the alarm sounds and the pump tank begins to fill. A quick response usually means a straightforward pump replacement.",
            ]),
            ("Preventing the next repair", [
                "Most septic repairs trace back to a handful of causes: a tank that went too long without pumping, things going down the drain that shouldn't, roots, and heavy loads over the tank or lines. After a repair, we'll tell you what likely caused the problem and what you can do to keep it from coming back.",
                "Simple habits go a long way. Keep wipes, grease, paper towels and harsh chemicals out of the drains. Fix leaky toilets and faucets, which can send hundreds of gallons a day into the system. Keep cars and trailers off the tank and drain field. And if you add an effluent filter, have it cleaned each time the tank is pumped.",
            ]),
            ("Emergencies", [
                "If sewage is backing up into your home, stop using water right away: no showers, laundry or flushing. Then call us at {{PHONE}}. Keep children and pets away from any sewage that has surfaced in the yard.",
            ]),
        ],
        "cost_intro": [
            "Repair costs vary widely with the problem. These are typical ranges for common repairs. We'll give you a firm price after we diagnose the problem.",
        ],
        "cost": [
            ("Diagnostic visit", "$150 – $300"),
            ("Baffle replacement", "$200 – $600"),
            ("Effluent filter install or replacement", "$150 – $400"),
            ("New tank lid or riser", "$250 – $800"),
            ("Pump replacement", "$800 – $2,000"),
            ("Distribution box replacement", "$600 – $1,800"),
            ("Line repair between house and tank", "$500 – $2,500"),
        ],
        "cost_note": COST_NOTE,
        "faq": [
            ("Is a backup an emergency?", "Yes. Stop using water in the house and call us at {{PHONE}} right away."),
            ("Will you tell me the cost before you start?", "Yes. We diagnose the problem, explain what we found, and give you a price before any repair work begins."),
            ("Can my system be repaired, or does it need replacing?", "Many problems can be repaired for far less than a new system. We'll give you an honest answer either way."),
            ("My septic alarm is going off. What should I do?", "Cut back on water use right away and call us. The alarm usually means the pump tank is filling because a pump or float has failed. Most pump tanks hold some reserve, but not much."),
            ("Do repairs need a permit?", "Some do. Major repairs and replacements in South Carolina can require an SCDES permit. We'll tell you if yours does and handle the paperwork."),
        ],
    },
    {
        "slug": "drain-field-repair",
        "name": "Drain Field Service",
        "title": "Drain Field Repair & Replacement",
        "desc": "Drain field diagnosis, repair and replacement for Lowcountry homes, built for high water tables and sandy soil. Signs of failure, typical costs, and how to protect yours.",
        "lead": "The drain field is where your wastewater is treated and returned to the soil. In the Lowcountry, high water tables and heavy rain make drain fields work harder, so problems need attention quickly.",
        "included_title": "What we do",
        "included": [
            "Diagnose why the drain field is failing",
            "Clear and repair distribution lines where possible",
            "Repair or replace the distribution box",
            "Drain field replacement when repair isn't an option",
            "Help with SCDES permits for replacement work",
        ],
        "signs_title": "Signs of drain field trouble",
        "signs": [
            "Soggy ground or standing water over the drain field when it hasn't rained",
            "Grass that's unusually green and lush over the lines",
            "Sewage odors in the yard",
            "Slow drains even right after the tank was pumped",
            "Backups that get worse after rain",
        ],
        "body": [
            ("How a drain field works", [
                "Liquid leaves the septic tank and flows through a pipe to the drain field, a set of trenches or chambers buried in the yard. From there it soaks slowly down through the soil. As it does, the soil and the bacteria living in it filter and treat the water before it reaches the groundwater.",
                "That treatment only works if there's enough unsaturated soil between the bottom of the trenches and the water table. That's the core challenge in the Lowcountry.",
            ]),
            ("Why Lowcountry drain fields struggle", [
                "Much of the coast sits only a few feet above the water table, and after heavy rain, tropical storms or extreme high tides, the water table can rise close to the surface. When the soil under the drain field is saturated, wastewater has nowhere to go. Drains slow down and wastewater can surface in the yard. Many systems recover once the ground dries out, but repeated saturation, combined with solids from a tank that isn't pumped often enough, wears a drain field out.",
                "Soils vary a lot across the region. Sandy soils drain quickly but give wastewater less time to be treated. Areas with heavier clay or marsh soils drain slowly. That's why many newer Lowcountry systems use raised beds, shallow placement or pumped designs, and why replacement fields often have to be designed differently from the original.",
            ]),
            ("Repair or replace?", [
                "Not every struggling drain field needs replacing. If the problem is a crushed line, a tilted distribution box or a broken outlet baffle letting solids through, a targeted repair can bring the field back. If the soil itself is clogged after years of solids reaching it, the field usually needs to be replaced, often in a new location in the yard.",
                "Replacement requires an SCDES permit. The state evaluates the site and sets the design based on the soil and water table. We'll help with the application and coordinate the process so you're not left sorting it out alone.",
            ]),
        ],
        "cost_intro": [
            "Drain field costs depend heavily on what's wrong, the size of the home, and what the soil and water table allow. A permit-required replacement on a wet lot can cost far more than a repair on a dry one.",
        ],
        "cost": [
            ("Drain field evaluation", "$250 – $500"),
            ("Line repair or distribution box replacement", "$600 – $3,000"),
            ("Conventional drain field replacement", "$5,000 – $12,000"),
            ("Raised or engineered drain field", "$10,000 – $25,000+"),
        ],
        "cost_note": COST_NOTE,
        "faq": [
            ("Why do drain fields fail?", "The most common causes are solids escaping the tank because it wasn't pumped, too much water entering the system, roots, and vehicles driving over the lines."),
            ("Can a failing drain field be saved?", "Sometimes. If it's caught early, repairs can restore it. Severely clogged or damaged fields usually need replacement."),
            ("How can I protect my drain field?", "Pump your tank on schedule, spread out water use, keep vehicles and heavy equipment off it, and send roof runoff and sump discharge away from it."),
            ("My yard is soggy after every storm. Is my drain field failing?", "Not necessarily. Many Lowcountry drain fields slow down when the water table is high and recover as it drops. If wet spots or slow drains persist after the ground dries out, it's time for an evaluation."),
            ("Can I plant a garden or build over my drain field?", "Grass is the best cover. Avoid vegetable gardens, trees, shrubs with deep roots, patios, sheds and parking over the drain field, since they can damage the lines or keep the soil from breathing."),
            ("Does replacing a drain field need a permit?", "Yes. In South Carolina a drain field replacement requires an SCDES permit, and the state sets the design based on your site. We'll help you through it."),
        ],
    },
    {
        "slug": "septic-installation",
        "name": "New System Installation",
        "title": "New & Replacement Septic System Installation",
        "desc": "New and replacement septic system installation in Charleston and the SC Lowcountry, from site evaluation and SCDES permitting to final inspection. Typical costs and timelines.",
        "lead": "Building a new home or replacing a system that's reached the end of its life? We'll guide you through the process, from site evaluation and permitting to installation and final inspection.",
        "included_title": "How it works",
        "included": [
            "A site visit to understand your property and needs",
            "Coordinating the SCDES site and soil evaluation",
            "Handling the permit application",
            "Installing the tank, lines and drain field to the permitted design",
            "Final inspection and approval before the system goes into use",
        ],
        "signs_title": "When you need a new system",
        "signs": [
            "You're building on a lot without sewer service",
            "Your current system has failed and can't be repaired",
            "You're adding bedrooms and need more capacity",
            "Your system is decades old and having repeated problems",
        ],
        "body": [
            ("The permit process in South Carolina", [
                "Every new or replacement septic system in South Carolina needs a permit from the SC Department of Environmental Services (SCDES). The process starts with an application and a site evaluation, in which the state looks at the soil, the depth to the seasonal high water table, the size of the home and the layout of the lot. That evaluation determines what kind of system the site can support and where it can go.",
                "On many Lowcountry lots, the water table is the deciding factor. Sites with deep, well-drained soil can often use a conventional gravity system. Wetter sites may need a shallow placement, a raised bed, a pumped system or an engineered design. Knowing this early helps you budget realistically, especially if you're buying land to build on.",
            ]),
            ("What installation involves", [
                "Once the permit is issued, installation is usually a matter of days. We set the tank, run the line from the house, build the drain field to the permitted design, and install any pumps, alarms and risers the design calls for. Before the system is covered, it's inspected to confirm it was built as permitted.",
                "We plan the work to protect the rest of your property as much as possible, and we'll walk you through how to care for your new system so it lasts.",
            ]),
            ("Caring for a new system", [
                "A new septic system needs very little from you, but what it does need matters. Have the tank pumped and checked within the first three to five years, then on the schedule we recommend. Keep vehicles, sheds, pools and patios off the drain field and the reserve area the permit sets aside for a future field. Plant grass over the drain field, not trees or shrubs with deep roots.",
                "If your system has a pump and alarm, learn what the alarm sounds like and where the panel is. When it goes off, cut back on water use and call us. Most pump tanks hold enough reserve for a short while, which is usually enough time to fix a failed float or pump before anything backs up.",
            ]),
            ("Buying land? Check septic first", [
                "If you're considering a lot without sewer service, find out whether it can support a septic system before you buy. A lot that needs an engineered system can add thousands to the cost of building, and some lots can't be permitted at all. We're happy to talk through what to look for.",
            ]),
        ],
        "cost_intro": [
            "Installation cost depends on the type of system the site requires, the size of the home, and site access. Permit and evaluation fees are separate and set by the state.",
        ],
        "cost": [
            ("Conventional gravity system", "$6,000 – $12,000"),
            ("Pumped or shallow-placement system", "$10,000 – $18,000"),
            ("Raised bed or engineered system", "$15,000 – $30,000+"),
            ("Tank replacement only", "$2,500 – $6,000"),
        ],
        "cost_note": COST_NOTE,
        "faq": [
            ("How long does installation take?", "Installation itself is usually a few days, but permitting and site evaluation can take several weeks. We'll give you a realistic timeline up front."),
            ("Do I need a permit?", "Yes. New and replacement septic systems in South Carolina require an SCDES permit. We'll help you through that process."),
            ("What affects the cost?", "Soil conditions, water table, lot layout, home size and the type of system required all play a role. We'll give you a clear quote after a site visit."),
            ("Can I build on a lot that needs an engineered system?", "Often, yes, but it costs more. The SCDES site evaluation will tell you what the lot can support."),
            ("How long does a septic system last?", "A well-maintained system commonly lasts 20 to 30 years or more. Regular pumping and keeping heavy loads off the drain field make the biggest difference."),
        ],
    },
]
