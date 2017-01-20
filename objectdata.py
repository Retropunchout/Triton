objectdata = """
---
    !!python/object:__main__.item
    name: bandage
    description: "A Bandage, used for binding wounds"
    static: False
    wearable: False
    wieldable: False
    getable: True
    classrestr: Medic
    rarity: 1
    dmgmod: 0
    defmod: 0
    useaction: itemheal()
---
    !!python/object:__main__.item
    name: pipe
    description: "A rusty pipe"
    static: False
    wearable: False
    wieldable: True
    getable: True
    classrestr: Medic, Engineer, Marine
    rarity: 1
    dmgmod: 2
    defmod: 0
    useaction: itembash()
---
    !!python/object:__main__.item
    name: medical bench
    description: "A standard medical bench"
    static: False
    wearable: False
    wieldable: True
    getable: False
    classrestr: Medic, Engineer, Marine
    rarity: 1
    dmgmod: 2
    defmod: 0
    useaction: None
"""
