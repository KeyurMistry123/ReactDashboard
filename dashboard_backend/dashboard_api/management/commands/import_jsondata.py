import json
from django.core.management.base import BaseCommand
from dashboard_api.models import Record

def parse_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

class Command(BaseCommand):
    help = 'Import data from jsondata.json into the Record model'

    def handle(self, *args, **kwargs):
        with open('data/jsondata.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            count = 0
            for item in data:
                Record.objects.create(
                    end_year=item.get('end_year', ''),
                    intensity=parse_int(item.get('intensity', None)),
                    sector=item.get('sector', ''),
                    topic=item.get('topic', ''),
                    insight=item.get('insight', ''),
                    url=item.get('url', ''),
                    region=item.get('region', ''),
                    start_year=item.get('start_year', ''),
                    impact=item.get('impact', ''),
                    added=item.get('added', ''),
                    published=item.get('published', ''),
                    country=item.get('country', ''),
                    relevance=parse_int(item.get('relevance', None)),
                    pestle=item.get('pestle', ''),
                    source=item.get('source', ''),
                    title=item.get('title', ''),
                    likelihood=parse_int(item.get('likelihood', None)),
                )
                count += 1
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} records.')) 