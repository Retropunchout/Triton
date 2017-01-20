roomdata = """
---
	"Elevator": {
	description: "The elevator door is covered in handprints. There's a crowbar lodged in the jamb. A sign flashes 'QUARANTINE ENACTED'."
	north: ,
	east: ,
	south: "Central Aft Hall",
	west: ,
	up: ,
	down: ,
	corruption: 10
	vacuum: 0
	}
---
	"Aft Central Hall": {
	description: "A cramped lobby. The smell hits you first: barbecue with rotten meat. Piles of burnt bodies."
	north: "Elevator",
	east: "Locker-Room",
	south: "Aft Airlock",
	west: "Breakroom",
	up: ,
	down: ,
	corruption: 10
	vacuum: 0
	}
---
	"Breakroom": {
	description: "A long dining room. Posters reminding engineers of their daily booster shots. A fridge is here, something red pouring out of it."
	north: ,
	east: "Central Aft Hall",
	south: ,
	west: "Toilets",
	up: ,
	down: ,
	corruption: 10
	vacuum: 0
	}
---
	"Toilets": {
	description: "A unisex bathroom, shower stalls and toilets. Corruption germinates from cisterns. On the cracked mirror, someone's written 'I've marched a million miles/seen a thousand suns set on a hundred planets/just to take a fucking dump.'"
	north: ,
	east: "Breakroom",
	south: ,
	west: ,
	up: ,
	down: ,
	corruption: 10
	vacuum: 0
	}
---
	"Locker-Room": {
	description: "Lockers hang open, empty. A half-eaten rationpack on a bench, overgrown with mold. A man halfclad in HAZMAT, killed suiting up."
	north: ,
	east: "Tool Storage",
	south: ,
	west: "Central Aft Hall",
	up: ,
	down: ,
	corruption: 10
	vacuum: 0
	}
---
	"Tool Storage": {
	description: "Shelves barricaded against the door. A woman with a slashed neck, under graffiti: 'IF YOU CAN READ THIS, FUCK YOU.'"
	north: ,
	east: ,
	south: ,
	west: "Locker-Room",
	up: ,
	down: ,
	corruption: 10
	vacuum: 0
	}
---
	"Aft Airlock": {
	description: "The airlock door fifteen feet away, broken off by force. The short corridor now a straight walk. An alarm screams."
	north: "Aft Central Hall",
	east: ,
	south: "Astern Central Hall",
	west: ,
	up: ,
	down: ,
	corruption: 10
	}
---
	"Astern Central Hall": {
	description: "Warm light flickers behind a fan. All else in shadow. Through a tinted window, the engine core glows."
	north: "Aft Airlock",
	east: "Flow Control",
	south: "Engine Core",
	west: "Atmospherics",
	up: ,
	down: ,
	corruption: 10
	vacuum: 0
	}
---
	"Flow Control": {
	description: "Down here, you're up to your ankles in motor oil, coolant, and sewage. A hundred pipes burst open. Purple vines, thick as your chest, hooked into them."
	north: "Disposals",
	east: ,
	south: ,
	west: ,
	up: ,
	down: ,
	corruption: 10
	vacuum: 0
	}
---
	"Disposals": {
	description: "A catwalk across a silo. Rubbish and corpses fall to the darkness. Below, something chews and swallows."
	north: "'Under Construction'",
	east: ,
	south: "Flow Control",
	west: ,
	up: ,
	down: ,
	corruption: 10
	vacuum: 0
	}
---
	"Under Construction": {
	description: "Unfinished floor and bare walls, warning signs all around. In the center, a pile of pulsing flesh, a meat altar. Hundreds of booster needles plugged into it, like a pincushion."
	north: ,
	east: ,
	south: "Disposals",
	west: ,
	up: ,
	down: ,
	corruption: 10
	vacuum: 0
	}
---
	"Atmospherics": {
	description: "Valves, ducts, and canisters, so tightly packed there's no room to breath. Burnt bodies lie in a circle around the fuel/air mixers. Each one closer than the last."
	north: ,
	east: ,
	south: "Astern Airlock",
	west: ,
	up: ,
	down: ,
	corruption: 10
	vacuum: 0
	}
---
	"Engine Core": {
	description: "A tall chamber surrounding a great engine. Above, the hatch hangs open. But at the pockmarked edge, the corruption regrows."
	north: "Astern Central Hall",
	east: ,
	south: "Outboard Catwalk ('Hot Zone'),
	west: ,
	up: ,
	down: ,
	corruption: 35
	vacuum: 0
	}
---
	"Astern Airlock": {
	description: "A small closet. A spacesuit hangs beside the door; two others are missing. A quarantine alarm sounds."
	north: "Atmospherics",
	east: ,
	south: "Outboard Catwalk ('Hot Zone')",
	west: ,
	up: ,
	down: ,
	corruption: 10
	vacuum: 0
	}
---
	"Outboard Catwalk ('Hot Zone')": {
	description: "You walk along the blackened catwalk, clipped to the railing. The ship's thrusters stand behind, big enough to drive a truck through. If the engines were on..."
	north: "Engine Core",
	east: "Kat's Kabin",
	south: ,
	west: "Astern Airlock",
	up: ,
	down: ,
	corruption: 10
	vacuum: 1
	}
---
	"Kat's Kabin": {
	description: "A toolshed stocked with spare wires and cutters. Disney posters line the walls. A chair sits beside a window, offering a view of the stars."
	north: "Meadow-2",
	east: ,
	south: ,
	west: "Outboard Catwalk ('Hot Zone')",
	up: ,
	down: ,
	corruption: 10
	vacuum: 1
	}
---
	"Meadow-2": {
	description: "Fields of solar panels bolted into the ship's hull. There's a dial on a control panel with a mermaid's spraypainted next to it."
	north: ,
	east: "Meadow-1",
	south: "Kat's Kabin",
	west: "Meadow-3",
	up: ,
	down: ,
	corruption: 10
	vacuum: 1
	}
---
	"Meadow-3": {
	description: "Fields of solar panels bolted into the ship's hull.There's a dial on a control panel with a crab spraypainted next to it."
	north: ,
	east: "Meadow-2",
	south: ,
	west: "Meadow-1",
	up: ,
	down: ,
	corruption: 10
	vacuum: 1
	}
---
	"Meadow-1": {
	description: "Fields of solar panels bolted into the ship's hull. There's a dial on a control panel with an octopus spraypainted next to it."
	north: ,
	east: "Meadow-3",
	south: ,
	west: "Meadow-2",
	up: ,
	down: ,
	corruption: 10
	vacuum: 1
    }
"""
