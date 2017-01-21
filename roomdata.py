roomdata = """
---
    "Medical Bay": {
    description: You're standing in a standard medical bay. The lights flicker, and in the light, you see the signs of rust and neglect,
    north: "Medical Corridor A",
    east: ,
    south: ,
    west: ,
    up: ,
    down: ,
    objects: ['bandage','pipe','medical bench'],
    restriction: "",
    corruption: 10
    }
---
    "Medical Corridor A": {
    description: You are standing in the medical corridor just off the Medical Bay.,
    north: ,
    east: "Medical Corridor B",
    south: "Medical Bay",
    west: ,
    up: ,
    objects: [],
    restriction: "",
    corruption: 30
    }
---
    "Medical Corridor B": {
    description: You're standing a medical corridor, just off from the D5 Nexus.,
    north: ,
    east: "Nexus D5 - Medical",
    south: ,
    west: "Medical Corridor A",
    up: ,
    down: ,
    objects: [],
    restriction: "",
    corruption: 30
    }
---
    "Nexus D5 - Medical": {
    description: This is the Nexus point of Deck 5, it seems to be a sort of crew meeting point.,
    north: ,
    east: ,
    south: "Service Corridor C",
    west: "Medical Corridor B",
    up: ,
    down: "Nexus D4 - Engineering",
    objects: [Bandage,Pipe],
    restriction:  "",
    corruption: 10
    }
---
    "Service Corridor C": {
    description: You're standing in a Service Corridor,
    north: "Nexus D5 - Medical'",
    east: ,
    south: ,
    west: ,
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10
    }
---
    "Nexus D4 - Engineering": {
    description: "A cramped lobby. The smell hits you first: barbecue with rotten meat. Piles of burnt bodies. A sign flashes 'QUARANTINE ENACTED'",
    north: ,
    east: "Locker-Room",
    south: "Aft Airlock",
    west: "Breakroom",
    up: "Nexus - D5 'Medical'",
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 0
    }
---
    "Breakroom": {
    description: "A long dining room. Posters reminding engineers of their daily booster shots. A fridge is here, something red pouring out of it.",
    north: ,
    east: "Nexus D4 - Engineering",
    south: ,
    west: "Toilets",
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 0
    }
---
    "Toilets": {
    description: "A unisex bathroom, shower stalls and toilets. Corruption germinates from cisterns. On the cracked mirror, someone's written 'I've marched a million miles/seen a thousand suns set on a hundred planets/just to take a fucking dump.'",
    north: ,
    east: "Breakroom",
    south: ,
    west: ,
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 0
    }
---
    "Locker-Room": {
    description: "Lockers hang open, empty. A half-eaten rationpack on a bench, overgrown with mold. A man halfclad in HAZMAT, killed suiting up.",
    north: ,
    east: "Tool Storage",
    south: ,
    west: "Nexus D4 - Engineering",
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 0
    }
---
    "Tool Storage": {
    description: "Shelves barricaded against the door. A woman with a slashed neck, under graffiti: 'IF YOU CAN READ THIS, FUCK YOU.'",
    north: ,
    east: ,
    south: ,
    west: "Locker-Room",
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 0
    }
---
    "Aft Airlock": {
    description: "The airlock door fifteen feet away, broken off by force. The short corridor now a straight walk. An alarm screams.",
    north: "Aft Central Hall",
    east: ,
    south: "Astern Central Hall",
    west: ,
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10
    }
---
    "Astern Central Hall": {
    description: "Warm light flickers behind a fan. All else in shadow. Through a tinted window, the engine core glows.",
    north: "Aft Airlock",
    east: "Flow Control",
    south: "Engine Core",
    west: "Atmospherics",
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 0
    }
---
    "Flow Control": {
    description: "Down here, you're up to your ankles in motor oil, coolant, and sewage. A hundred pipes burst open. Purple vines, thick as your chest, hooked into them.",
    north: "Disposals",
    east: ,
    south: ,
    west: ,
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 0
    }
---
    "Disposals": {
    description: "A catwalk across a silo. Rubbish and corpses fall to the darkness. Below, something chews and swallows.",
    north: "'Under Construction'",
    east: ,
    south: "Flow Control",
    west: ,
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 0
    }
---
    "Under Construction": {
    description: "Unfinished floor and bare walls, warning signs all around. In the center, a pile of pulsing flesh, a meat altar. Hundreds of booster needles plugged into it, like a pincushion.",
    north: ,
    east: ,
    south: "Disposals",
    west: ,
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 0
    }
---
    "Atmospherics": {
    description: "Valves, ducts, and canisters, so tightly packed there's no room to breath. Burnt bodies lie in a circle around the fuel/air mixers. Each one closer than the last.",
    north: ,
    east: ,
    south: "Astern Airlock",
    west: ,
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 0
    }
---
    "Engine Core": {
    description: "A tall chamber surrounding a great engine. Above, the hatch hangs open. But at the pockmarked edge, the corruption regrows.",
    north: "Astern Central Hall",
    east: ,
    south: "Outboard Catwalk 'Hot Zone'",
    west: ,
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 35,
    vacuum: 0
    }
---
    "Astern Airlock": {
    description: "A small closet. A spacesuit hangs beside the door; two others are missing. A quarantine alarm sounds.",
    north: "Atmospherics",
    east: ,
    south: "Outboard Catwalk ('Hot Zone')",
    west: ,
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 0
    }
---
    "Outboard Catwalk ('Hot Zone')": {
    description: "You walk along the blackened catwalk, clipped to the railing. The ship's thrusters stand behind, big enough to drive a truck through. If the engines were on...",
    north: "Engine Core",
    east: "Kat's Kabin",
    south: ,
    west: "Astern Airlock",
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 1
    }
---
    "Kat's Kabin": {
    description: "A toolshed stocked with spare wires and cutters. Disney posters line the walls. A chair sits beside a window, offering a view of the stars.",
    north: "Meadow-2",
    east: ,
    south: ,
    west: "Outboard Catwalk ('Hot Zone')",
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 1
    }
---
    "Meadow-2": {
    description: "Fields of solar panels bolted into the ship's hull. There's a dial on a control panel with a mermaid's spraypainted next to it.",
    north: ,
    east: "Meadow-1",
    south: "Kat's Kabin",
    west: "Meadow-3",
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 1
    }
---
    "Meadow-3": {
    description: "Fields of solar panels bolted into the ship's hull.There's a dial on a control panel with a crab spraypainted next to it.",
    north: ,
    east: "Meadow-2",
    south: ,
    west: "Meadow-1",
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 1
    }
---
    "Meadow-1": {
    description: "Fields of solar panels bolted into the ship's hull. There's a dial on a control panel with an octopus spraypainted next to it.",
    north: ,
    east: "Meadow-3",
    south: ,
    west: "Meadow-2",
    up: ,
    down: ,
    restriction: "",
    objects: [Bandage,Pipe],
    corruption: 10,
    vacuum: 1
    }
"""
