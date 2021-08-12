import os

from .common import Common, BASE_DIR


class Test(Common):
    DEBUG = True

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ("django_nose",)
    TEST_RUNNER = "boxme_product.libs.runners.TestSuiteRunner"
    NOSE_ARGS = [
        BASE_DIR,
        "--nocapture",
        "--nologcapture",
        "--logging-clear-handlers",
    ]

    MIGRATION_MODULES = {
        "admin": None,
        "auth": None,
        "contenttypes": None,
        "sessions": None,
        "boxme_core": None,
        "boxme_countries": None,
        "boxme_jwt": None,
        "ns_addresses": None,
        "ns_fees": None,
        "ns_orders": None,
        "ns_products": None,
        "ns_purchase_orders": None,
        "ns_stores": None,
    }

    MONGODB = "178.128.23.178"
    MONGODB_NAME = f"{Common.MONGODB_NAME}_test"

    LOCAL_STATIC_DIRS = os.path.join(BASE_DIR, "storage")
