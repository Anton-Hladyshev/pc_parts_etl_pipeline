from dotenv import dotenv_values

config = dotenv_values(".env")

#URLs
AMAZON_URL = "https://www.amazon.com/s"
RAINFOREST_URL = f"https://api.rainforestapi.com/request"

#Filters

STOPWORDS = [
    "cooler", "adapter", "cable", "mount", "thermal", "paste",
    "bracket", "rgb controller", "heatsink", "extension", "holder"
]

CPU_FILTERS = {"manufacturers": ["intel", "amd", "intel®"],
               "keywords": [
    "cpu", "processor", "ryzen", "intel core", "i3", "i5", "i7", "i9",
    "xeon", "pentium", "celeron", "threadripper", "apu", "unlocked", "gen"
               ],
               "stopwords": [
                   "cooler", "cooling", "fan", "heatsink", "thermal",
    "paste", "compound", "grease", "mount", "holder", "adapter",
    "case", "bracket", "cover", "tube", "stand", "cleaner", "radiator"
               ]
               }

GPU_FILTERS = {"manufacturers": [
    "nvidia", "amd", "asus", "msi", "gigabyte", "zotac",
    "evga", "sapphire", "powercolor", "pny", "xfx", "asrock", "intel", "rx"],
               "keywords": [
    "gpu", "graphics card", "video card", "geforce", "gtx", "rtx", "radeon",
    "rx", "nvidia", "amd", "vga", "gddr6", "gddr5", "pci express"],
                "stopwords": [
    "mount", "riser", "adapter", "bracket", "support stand", "rgb kit",
    "cooling fan", "heatsink", "cable", "sticker", "extender", "case"]
}

RAM_FILTERS = {"manufacturers": [
    "corsair", "g.skill", "kingston", "crucial", "teamgroup",
    "adata", "patriot", "mushkin", "pny", "silicon power"],
               "keywords": [
    "ram", "memory", "ddr4", "ddr5", "sodimm", "dimms", "kit", "module",
    "cl16", "3200mhz", "3600mhz", "laptop memory", "desktop memory"],
                "stopwords": [
    "heatsink", "cooler", "fan", "adapter", "case", "cover",
    "decor", "lighting", "rgb kit", "thermal", "cleaner",
    "mount", "holder", "cable", "sticker"
]
}

FILTERS = {"cpu": CPU_FILTERS, "graphics_card": GPU_FILTERS, "ram": RAM_FILTERS}
