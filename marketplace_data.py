"""
Marketplace Data Module
Contains product listings for seeds, plants, pots, and air quality products
"""


def get_marketplace_products():
    """
    Returns list of products for the AirCare marketplace
    Each product has: name, category, price, description, benefits
    """
    products = [
        # ===== SEEDS =====
        {
            "name": "Neem Seeds (Pack of 10)",
            "category": "Seeds",
            "price": 49,
            "description": "High-quality neem seeds for growing air-purifying neem trees",
            "benefits": "Natural air purifier, pest repellent"
        },
        {
            "name": "Tulsi Seeds (Pack of 20)",
            "category": "Seeds",
            "price": 39,
            "description": "Sacred basil seeds with medicinal properties",
            "benefits": "Purifies air, mosquito repellent"
        },
        {
            "name": "Money Plant Cuttings (Set of 5)",
            "category": "Seeds",
            "price": 99,
            "description": "Ready-to-plant money plant cuttings",
            "benefits": "Removes formaldehyde, easy to grow"
        },

        # ===== LIVE PLANTS =====
        {
            "name": "Snake Plant (Sansevieria)",
            "category": "Live Plants",
            "price": 199,
            "description": "Low-maintenance air purifier, perfect for bedrooms",
            "benefits": "Converts CO2 to O2 at night, removes toxins"
        },
        {
            "name": "Areca Palm (Small)",
            "category": "Live Plants",
            "price": 299,
            "description": "NASA-recommended air purifier, adds humidity",
            "benefits": "Removes formaldehyde, xylene, toluene"
        },
        {
            "name": "Peace Lily",
            "category": "Live Plants",
            "price": 249,
            "description": "Beautiful white flowers, excellent air cleaner",
            "benefits": "Removes ammonia, benzene, formaldehyde"
        },
        {
            "name": "Spider Plant",
            "category": "Live Plants",
            "price": 149,
            "description": "Easy to grow, propagates quickly",
            "benefits": "Removes CO, formaldehyde, xylene"
        },
        {
            "name": "Rubber Plant",
            "category": "Live Plants",
            "price": 349,
            "description": "Large glossy leaves, low maintenance",
            "benefits": "Removes formaldehyde, improves air quality"
        },
        {
            "name": "Boston Fern",
            "category": "Live Plants",
            "price": 179,
            "description": "Lush green foliage, natural humidifier",
            "benefits": "Removes formaldehyde, adds moisture"
        },

        # ===== POTS & PLANTERS =====
        {
            "name": "Terracotta Pot (8 inch)",
            "category": "Pots & Planters",
            "price": 79,
            "description": "Classic clay pot with drainage hole",
            "benefits": "Breathable, prevents overwatering"
        },
        {
            "name": "Self-Watering Planter",
            "category": "Pots & Planters",
            "price": 299,
            "description": "Smart pot with water reservoir",
            "benefits": "Waters plants automatically for 7-10 days"
        },
        {
            "name": "Hanging Macrame Planter",
            "category": "Pots & Planters",
            "price": 149,
            "description": "Bohemian-style hanging planter",
            "benefits": "Saves space, decorative"
        },
        {
            "name": "Ceramic Pot Set (3 pcs)",
            "category": "Pots & Planters",
            "price": 499,
            "description": "Modern geometric design pots",
            "benefits": "Stylish, multiple sizes"
        },

        # ===== SOIL & FERTILIZERS =====
        {
            "name": "Premium Potting Mix (5 kg)",
            "category": "Soil & Fertilizers",
            "price": 199,
            "description": "Ready-to-use soil mix with compost and perlite",
            "benefits": "Good drainage, nutrient-rich"
        },
        {
            "name": "Organic Vermicompost (2 kg)",
            "category": "Soil & Fertilizers",
            "price": 149,
            "description": "100% organic earthworm compost",
            "benefits": "Natural fertilizer, improves soil"
        },
        {
            "name": "Liquid Plant Food (500ml)",
            "category": "Soil & Fertilizers",
            "price": 99,
            "description": "All-purpose liquid fertilizer",
            "benefits": "Quick absorption, balanced NPK"
        },

        # ===== AIR QUALITY PRODUCTS =====
        {
            "name": "Indoor Air Quality Monitor",
            "category": "Air Quality Products",
            "price": 2499,
            "description": "Real-time PM2.5, PM10, VOC, CO2 monitoring",
            "benefits": "Track air quality at home"
        },
        {
            "name": "HEPA Air Purifier (Small Room)",
            "category": "Air Quality Products",
            "price": 4999,
            "description": "Removes 99.97% of particles, covers 200 sq ft",
            "benefits": "Medical-grade filtration"
        },
        {
            "name": "Activated Carbon Bags (4 pack)",
            "category": "Air Quality Products",
            "price": 399,
            "description": "Natural odor absorber and air freshener",
            "benefits": "Chemical-free, reusable"
        },
        {
            "name": "Himalayan Salt Lamp",
            "category": "Air Quality Products",
            "price": 799,
            "description": "Natural air ionizer, warm glow",
            "benefits": "Reduces allergens, mood enhancer"
        },

        # ===== GARDENING TOOLS =====
        {
            "name": "Garden Tool Set (5 pieces)",
            "category": "Gardening Tools",
            "price": 449,
            "description": "Includes trowel, pruner, rake, shovel, gloves",
            "benefits": "Everything you need to start"
        },
        {
            "name": "Watering Can (2 Liter)",
            "category": "Gardening Tools",
            "price": 199,
            "description": "Ergonomic design with long spout",
            "benefits": "Easy watering, precise pour"
        },
        {
            "name": "Plant Mister Spray Bottle",
            "category": "Gardening Tools",
            "price": 79,
            "description": "Fine mist sprayer for plant leaves",
            "benefits": "Keeps leaves dust-free, adds humidity"
        },
        {
            "name": "Soil pH Tester",
            "category": "Gardening Tools",
            "price": 249,
            "description": "Digital soil moisture and pH meter",
            "benefits": "Optimize plant health"
        },
    ]

    return products


def get_product_categories():
    """Returns list of all product categories"""
    return [
        "Seeds",
        "Live Plants",
        "Pots & Planters",
        "Soil & Fertilizers",
        "Air Quality Products",
        "Gardening Tools"
    ]


def get_products_by_category(category):
    """Get products filtered by category"""
    all_products = get_marketplace_products()
    return [p for p in all_products if p['category'] == category]


def search_products(query):
    """Search products by name or description"""
    all_products = get_marketplace_products()
    query_lower = query.lower()
    return [
        p for p in all_products
        if query_lower in p['name'].lower() or query_lower in p['description'].lower()
    ]