from django.test import TestCase
from quiz.models import Card

def create_cards_from_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            front_text = row[0]
            back_text = row[1]

            # Create Card instance
            card = Card(front=front_text, back=back_text)
            
            # Check if images are provided
            if len(row) > 2:
                front_image_path = row[2]
                card.front_image = ContentFile(open(front_image_path, 'rb').read(), name=front_image_path)
            
            if len(row) > 3:
                back_image_path = row[3]
                card.back_image = ContentFile(open(back_image_path, 'rb').read(), name=back_image_path)
            
            # Save the card
            card.save()