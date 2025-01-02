from typing import Any

from django.conf import settings
from django.core.management.base import BaseCommand

import helpers
from helpers.downloader import download_to_local

VENDORSTATIC_FILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.js",
    "flowbite.min.js.map": "https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.js.map",
}

STATICFILES_VENDOR_DIR = getattr(settings, "STATICFILES_VENDOR_DIR")


class Command(BaseCommand):

    def handle(self, *args, **options):

        self.stdout.write("Downloading files..")
        completed_urls = []
        for name, url in VENDORSTATIC_FILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = download_to_local(url, out_path)

            if dl_success == True:
                completed_urls.append(url)

            else:
                self.stdout.write(
                    self.style.ERROR(f"An error occurred in downloding url {url}")
                )
        if set(completed_urls) == set(VENDORSTATIC_FILES.values()):
            self.stdout.write(
                self.style.SUCCESS("All staticfiles downloaded sucessfully")
            )
        else: 
            self.stdout.write("Some static files were not downloaded")
