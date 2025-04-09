from django.contrib.auth import get_user_model

from metric.models import Quote, Order, OrderTracking, Budget
from product.models import Product
from team.models import TeamMember


def create_mock_data():
    user = get_user_model()
    if user.objects.filter(email="admin@example.com").exists():
        return  # Don't run if mock data already exists

    if not user.objects.filter(email="admin@example.com").exists():
        user = user.objects.create_user(email="admin@example.com", name="Admin User", password="adminpass")
        user.remember_me = True
        user.admin = True
        user.staff = True
        user.save()

        # Quotes
        Quote.objects.bulk_create([
            Quote(value=1245.50),
            Quote(value=789.70),
            Quote(value=1320.00),
            Quote(value=975.25),
            Quote(value=1432.90)
        ])

        # Orders
        Order.objects.bulk_create([
            Order(value=1500.00),
            Order(value=2000.00),
            Order(value=1800.00),
            Order(value=1700.00),
            Order(value=3500.00)
        ])

        # Budget
        Budget.objects.create(
            month="November",
            total_budget=500000.00,
            spent=450000.00
        )

        # Order Tracking
        OrderTracking.objects.bulk_create([
            OrderTracking(
                from_address="7 Avoca St, Yagoona NSW",
                to_address="14-56 Cave Rd, Strathfield NSW",
                current_status="Out for delivery",
                current_location_lat=-33.881329,
                current_location_lon=151.071156
            ),
            OrderTracking(
                from_address="120 Pitt St, Sydney NSW",
                to_address="88 George St, Parramatta NSW",
                current_status="Dispatched",
                current_location_lat=-33.8679,
                current_location_lon=151.2073
            ),
            OrderTracking(
                from_address="25 Macquarie St, Liverpool NSW",
                to_address="300 Church St, North Parramatta NSW",
                current_status="Delivered",
                current_location_lat=-33.8160,
                current_location_lon=150.9981
            ),
            OrderTracking(
                from_address="5 Elizabeth St, Melbourne VIC",
                to_address="22 Collins St, Melbourne VIC",
                current_status="In transit",
                current_location_lat=-37.814,
                current_location_lon=144.9633
            ),
            OrderTracking(
                from_address="33 Queen St, Brisbane QLD",
                to_address="99 Adelaide St, Brisbane QLD",
                current_status="Pending Pickup",
                current_location_lat=-27.4705,
                current_location_lon=153.0260
            ),
            OrderTracking(
                from_address="101 North Terrace, Adelaide SA",
                to_address="205 South Rd, Torrensville SA",
                current_status="Out for delivery",
                current_location_lat=-34.9285,
                current_location_lon=138.6007
            ),
            OrderTracking(
                from_address="456 Hunter St, Newcastle NSW",
                to_address="789 Darby St, Cooks Hill NSW",
                current_status="In transit",
                current_location_lat=-32.9267,
                current_location_lon=151.7789
            )
        ])

        Product.objects.bulk_create([
            Product(
                name="Stylish Jacket",
                description="A comfortable and stylish winter jacket.",
                price=129.99,
                variants={"colors": ["Red", "Blue", "Black"], "sizes": ["S", "M", "L"]},
                budget_info={"allocated": 150.00, "used": 129.99},
                specifications={"Material": "Polyester", "Weight": "1.2kg"},
                materials="Polyester, Cotton",
                images=["https://img.freepik.com/free-photo/still-life-rendering-jackets-display_23-2149745027.jpg", "https://img.freepik.com/free-photo/still-life-rendering-jackets-display_23-2149745039.jpg",]
            ),
            Product(
                name="Running Shoes",
                description="Lightweight shoes perfect for daily running.",
                price=89.99,
                variants={"colors": ["White", "Grey"], "sizes": ["8", "9", "10"]},
                budget_info={"allocated": 100.00, "used": 89.99},
                specifications={"Material": "Mesh", "Weight": "0.8kg"},
                materials="Mesh, Rubber",
                images=["https://img.freepik.com/free-psd/running-shoes-sneakers-transparent-background_84443-1639.jpg"]
            ),
            Product(
                name="Leather Wallet",
                description="Compact and stylish leather wallet.",
                price=49.99,
                variants={"colors": ["Brown", "Black"]},
                budget_info={"allocated": 60.00, "used": 49.99},
                specifications={"Material": "Leather", "Weight": "0.2kg"},
                materials="Genuine Leather",
                images=["https://img.freepik.com/free-psd/elegant-brown-leather-wallet-stylish-accessory-luxurious-feel_632498-34025.jpg"]
            ),
            Product(
                name="Bluetooth Headphones",
                description="Noise-cancelling over-ear headphones.",
                price=199.99,
                variants={"colors": ["Black", "Silver"]},
                budget_info={"allocated": 220.00, "used": 199.99},
                specifications={"Battery Life": "30h", "Weight": "0.5kg"},
                materials="Plastic, Metal",
                images=["https://img.freepik.com/free-photo/headphones-audio-listen_1203-7566.jpg"]
            )
        ])

        TeamMember.objects.bulk_create([
            TeamMember(name="Alice Johnson", role="Manager", email="alice@example.com", avatar_url="https://img.freepik.com/free-psd/confident-businessman-3d-model-serious-expression-professional-attire-elegant-style_191095-87673.jpg"),
            TeamMember(name="Bob Smith", role="Developer", email="bob@example.com", avatar_url="https://img.freepik.com/free-psd/3d-render-businessman-with-arms-crossed-wearing-brown-suit-gold-tie-he-looks-confident-professional_632498-32063.jpg"),
            TeamMember(name="Carol White", role="Designer", email="carol@example.com", avatar_url="https://img.freepik.com/free-psd/confident-businessman-3d-model-serious-expression-professional-attire-elegant-style_191095-87673.jpg"),
            TeamMember(name="Dave Green", role="Tester", email="dave@example.com", avatar_url="https://img.freepik.com/free-psd/confident-businessman-3d-model-serious-expression-professional-attire-elegant-style_191095-87673.jpg"),
            TeamMember(name="Eve Black", role="Product Owner", email="eve@example.com", avatar_url="https://img.freepik.com/free-psd/3d-render-businessman-with-arms-crossed-wearing-brown-suit-gold-tie-he-looks-confident-professional_632498-32063.jpg"),
            TeamMember(name="Frank Stone", role="Developer", email="frank@example.com", avatar_url="https://img.freepik.com/free-psd/3d-render-businessman-with-arms-crossed-wearing-brown-suit-gold-tie-he-looks-confident-professional_632498-32063.jpg"),
            TeamMember(name="Grace Kim", role="QA Engineer", email="grace@example.com", avatar_url="https://img.freepik.com/free-psd/confident-businessman-3d-model-serious-expression-professional-attire-elegant-style_191095-87673.jpg"),
            TeamMember(name="Henry Lee", role="DevOps", email="henry@example.com", avatar_url="https://img.freepik.com/free-psd/3d-render-businessman-with-arms-crossed-wearing-brown-suit-gold-tie-he-looks-confident-professional_632498-32063.jpg")
        ])
