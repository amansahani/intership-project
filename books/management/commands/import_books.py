import csv
from django.core.management.base import BaseCommand
from books.models import Books

class Command(BaseCommand):
    help = 'Import books from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter=";")
                for row in reader:
                    book = Books(
                        isbn=row['isbn'],
                        title=row['title'],
                        author=row['author'],
                        year = row['year'],
                        publisher=row['publisher'],
                        img_url1=row['img-url1'],
                        img_url2=row['img-url2'],
                        img_url3=row['img-url3'],
                    )
                    book.save()
            self.stdout.write(self.style.SUCCESS('Successfully imported books from CSV.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('CSV file not found.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
